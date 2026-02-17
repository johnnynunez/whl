#!/usr/bin/env python3
"""Generate PEP 503 simple repository index for sbsa/cu130 wheels."""

import hashlib
import os
import re
from pathlib import Path

WHEELS_DIR = Path("wheels")
SBSA_DIR = Path("sbsa")
CUDA_VERSION = "cu130"
REPO_URL = "https://github.com/johnnynunez/whl/releases/download"
RELEASE_TAG = "sbsa-cu130"


def normalize_package_name(name: str) -> str:
    """Normalize package name per PEP 503 (lowercase, replace [_.-] with -)."""
    return re.sub(r"[-_.]+", "-", name).lower()


def extract_package_name(wheel_filename: str) -> str:
    """Extract raw package name from wheel filename."""
    # Wheel format: {name}-{version}(-{build})?-{python}-{abi}-{platform}.whl
    # The name part is everything before the first hyphen followed by a digit
    match = re.match(r"^(.+?)-\d", wheel_filename)
    if match:
        return match.group(1)
    raise ValueError(f"Cannot parse package name from: {wheel_filename}")


def sha256_file(filepath: Path) -> str:
    """Compute SHA256 hash of a file."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def generate_package_index(package_name: str, wheels: list[tuple[str, str]]) -> str:
    """Generate index.html content for a single package."""
    normalized = normalize_package_name(package_name)
    lines = [
        "<!DOCTYPE html>",
        "<html>",
        f"<head><title>Links for {normalized}</title></head>",
        "<body>",
        f"<h1>Links for {normalized}</h1>",
    ]
    for filename, sha256 in sorted(wheels):
        url = f"{REPO_URL}/{RELEASE_TAG}/{filename}#sha256={sha256}"
        lines.append(f'<a href="{url}">{filename}</a><br>')
    lines.append("</body>")
    lines.append("</html>")
    return "\n".join(lines)


def generate_cuda_index(package_names: list[str]) -> str:
    """Generate index.html for the CUDA version directory."""
    lines = [
        "<!DOCTYPE html>",
        "<html>",
        f"<head><title>Index of {CUDA_VERSION}</title></head>",
        "<body>",
        f"<h1>Index of {CUDA_VERSION}</h1>",
    ]
    for name in sorted(package_names):
        lines.append(f'<a href="{name}/">{name}/</a><br>')
    lines.append("</body>")
    lines.append("</html>")
    return "\n".join(lines)


def main():
    # Collect wheels by package
    packages: dict[str, list[tuple[str, str]]] = {}

    for whl_file in sorted(WHEELS_DIR.glob("*.whl")):
        filename = whl_file.name
        raw_name = extract_package_name(filename)
        normalized = normalize_package_name(raw_name)

        print(f"Processing: {filename} -> {normalized}")
        sha256 = sha256_file(whl_file)

        if normalized not in packages:
            packages[normalized] = []
        packages[normalized].append((filename, sha256))

    cuda_dir = SBSA_DIR / CUDA_VERSION

    # Create package directories and index.html files
    for normalized_name, wheels in sorted(packages.items()):
        pkg_dir = cuda_dir / normalized_name
        pkg_dir.mkdir(parents=True, exist_ok=True)

        index_content = generate_package_index(normalized_name, wheels)
        index_path = pkg_dir / "index.html"
        index_path.write_text(index_content)
        print(f"  Created: {index_path}")

    # Update cu130/index.html
    cuda_index = generate_cuda_index(list(packages.keys()))
    cuda_index_path = cuda_dir / "index.html"
    cuda_index_path.write_text(cuda_index)
    print(f"\nUpdated: {cuda_index_path}")

    # Update sbsa/index.html (keep existing CUDA versions, add new ones)
    sbsa_index_lines = [
        "<!DOCTYPE html>",
        "<html>",
        "<head><title>Index of sbsa wheels</title></head>",
        "<body>",
        "<h1>Index of sbsa wheels</h1>",
    ]
    cuda_versions = sorted(
        d.name for d in SBSA_DIR.iterdir() if d.is_dir() and d.name.startswith("cu")
    )
    for cv in cuda_versions:
        sbsa_index_lines.append(f'<a href="{cv}/">{cv}/</a><br>')
    sbsa_index_lines.append("</body>")
    sbsa_index_lines.append("</html>")
    sbsa_index_path = SBSA_DIR / "index.html"
    sbsa_index_path.write_text("\n".join(sbsa_index_lines))
    print(f"Updated: {sbsa_index_path}")

    print(f"\nTotal packages: {len(packages)}")
    print(f"Total wheels: {sum(len(w) for w in packages.values())}")
    print(f"\nRelease tag for GitHub: {RELEASE_TAG}")
    print(f"Upload wheels with: gh release create {RELEASE_TAG} wheels/*.whl")


if __name__ == "__main__":
    main()

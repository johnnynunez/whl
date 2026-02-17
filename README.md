# whl

CUDA ARM (SBSA) wheels for Spark and Thor platforms.

## Disclaimer

These are **unofficial**, community-built wheels and are **not** affiliated with or endorsed by the original package authors or NVIDIA. Use them at your own risk.

- Wheels may not follow strict PEP 440 versioning or PEP 503 repository standards.
- Version tags may be incorrect, dev-tagged, or non-standard.
- No guarantees of correctness, compatibility, or stability are provided.
- Always verify wheel integrity via the SHA256 hashes included in the index pages.

If you encounter issues, please check the upstream project before reporting here.

## Usage

```bash
pip install --extra-index-url https://johnnynunez.github.io/whl/sbsa/cu130 <package>
```

## Dependencies

```bash
wget https://developer.download.nvidia.com/compute/nvpl/25.11/local_installers/nvpl-local-repo-ubuntu2404-25.11_1.0-1_arm64.deb
sudo dpkg -i nvpl-local-repo-ubuntu2404-25.11_1.0-1_arm64.deb
sudo cp /var/nvpl-local-repo-ubuntu2404-25.11/nvpl-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install nvpl
```

```bash
wget https://developer.download.nvidia.com/compute/cudss/0.7.1/local_installers/cudss-local-repo-ubuntu2404-0.7.1_0.7.1-1_arm64.deb
sudo dpkg -i cudss-local-repo-ubuntu2404-0.7.1_0.7.1-1_arm64.deb
sudo cp /var/cudss-local-repo-ubuntu2404-0.7.1/cudss-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cudss
```

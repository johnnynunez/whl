<p align="center">
  <h1 align="center">whl</h1>
  <p align="center">
    Pre-built Python wheels for <strong>NVIDIA Grace (SBSA / aarch64)</strong> platforms<br>
    Targeting <strong>Spark</strong> and <strong>Thor</strong> systems with CUDA 13.0
  </p>
</p>

<p align="center">
  <a href="https://johnnynunez.github.io/whl/sbsa/cu130">
    <img src="https://img.shields.io/badge/index-sbsa%2Fcu130-green?style=flat-square" alt="Package Index">
  </a>
  <a href="https://github.com/johnnynunez/whl/blob/gh-pages/LICENSE">
    <img src="https://img.shields.io/github/license/johnnynunez/whl?style=flat-square" alt="License">
  </a>
</p>

---

## Quick Start

Install any package directly using pip:

```bash
pip install --extra-index-url https://johnnynunez.github.io/whl/sbsa/cu130 <package>
```

For example:

```bash
pip install --extra-index-url https://johnnynunez.github.io/whl/sbsa/cu130 torch torchvision vllm
```

## Available Packages

| Package | Version | Python | Platform |
|---------|---------|--------|----------|
| apex | 0.1 | cp312 | linux_aarch64 |
| bitsandbytes | 0.49.1 | cp312 | linux_aarch64 |
| causal-conv1d | 1.6.0 | cp312 | linux_aarch64 |
| cuda-bindings | 13.0.3 | cp312 | linux_aarch64 |
| cuda-core | 0.4.0 | cp312 | linux_aarch64 |
| diffusers | 0.36.0 | py3 | any |
| flash-attn | 3.0.0 | cp312 | linux_aarch64 |
| flash-attn-cute | 0.1.0 | py3 | any |
| flashinfer-python | 0.6.5 | py3 | any |
| flex-prefill | 0.1.0 | py3 | any |
| gsplat | 1.5.3 | cp312 | linux_aarch64 |
| hloc | 1.5 | py3 | any |
| mamba-ssm | 2.3.0 | cp312 | linux_aarch64 |
| mistral-common | 1.9.1 | py3 | any |
| nerfacc | 0.5.3 | cp312 | linux_aarch64 |
| nvidia-cudnn-frontend | 1.18.0 | cp312 | linux_aarch64 |
| nvidia-cutlass | 4.2.0.0 | py3 | any |
| onnxruntime-gpu | 1.24.1 | cp312 | linux_aarch64 |
| opencv-contrib-python | 4.13.0 | cp312 | linux_aarch64 |
| para-attn | 0.3.38 | py2.py3 | any |
| polyscope | 2.6.0 | cp312 | linux_aarch64 |
| pyceres | 2.6 | cp312 | linux_aarch64 |
| pycolmap | 3.14.0.dev0 | cp312 | linux_aarch64 |
| pycuda | 2026.1 | cp312 | linux_aarch64 |
| pycute | 4.3.5 | py3 | any |
| pytorch3d | 0.7.9 | cp312 | linux_aarch64 |
| sageattn3 | 1.0.0 | cp312 | linux_aarch64 |
| sgl-kernel | 0.3.21 | cp310+ | linux_aarch64 |
| spas-sage-attn | 0.1.0 | cp312 | linux_aarch64 |
| tinycudann | 2.0 | cp312 | linux_aarch64 |
| torch | 2.11.0 | cp312 | linux_aarch64 |
| torch-memory-saver | 0.0.9 | cp312 | linux_aarch64 |
| torchao | 0.16.0 | cp310+ | linux_aarch64 |
| torchaudio | 2.11.0 | cp312 | linux_aarch64 |
| torchcodec | 0.11.0 | cp312 | linux_aarch64 |
| torchsde | 0.2.6 | py3 | any |
| torchvision | 0.26.0 | cp312 | linux_aarch64 |
| transformer-engine | 2.13.0.dev0 | cp312 | linux_aarch64 |
| triton | 3.6.0 | cp312 | linux_aarch64 |
| vllm | 0.16.1+cu130 | cp312 | linux_aarch64 |
| xformers | 0.0.35 | cp39+ | linux_aarch64 |
| xgrammar | 0.1.31 | cp312 | linux_aarch64 |

## System Dependencies

Some packages require system-level NVIDIA libraries. Install them before using the wheels.

<details>
<summary><strong>NVPL (NVIDIA Performance Libraries)</strong></summary>

```bash
wget https://developer.download.nvidia.com/compute/nvpl/25.11/local_installers/nvpl-local-repo-ubuntu2404-25.11_1.0-1_arm64.deb
sudo dpkg -i nvpl-local-repo-ubuntu2404-25.11_1.0-1_arm64.deb
sudo cp /var/nvpl-local-repo-ubuntu2404-25.11/nvpl-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install nvpl
```

</details>

<details>
<summary><strong>cuDSS (CUDA Direct Sparse Solver)</strong></summary>

```bash
wget https://developer.download.nvidia.com/compute/cudss/0.7.1/local_installers/cudss-local-repo-ubuntu2404-0.7.1_0.7.1-1_arm64.deb
sudo dpkg -i cudss-local-repo-ubuntu2404-0.7.1_0.7.1-1_arm64.deb
sudo cp /var/cudss-local-repo-ubuntu2404-0.7.1/cudss-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cudss
```

</details>

## Disclaimer

> **These are unofficial, community-built wheels.**
> They are **not** affiliated with or endorsed by the original package authors or NVIDIA.
> Use them at your own risk.

- Wheels may not follow strict PEP 440 versioning or PEP 503 repository standards.
- Version tags may be incorrect, dev-tagged, or non-standard.
- No guarantees of correctness, compatibility, or stability are provided.
- Always verify wheel integrity via the SHA256 hashes included in the index pages.
- If you encounter issues, please check the upstream project before reporting here.

## License

[MIT](LICENSE)

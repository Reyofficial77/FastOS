# Build Instructions for FastOS (Swift)

This document describes how to build the FastOS ISO from source. Since the build process requires a native Linux environment, you must use a Debian or Ubuntu machine (or VM).

## Prerequisites

### Hardware Requirements
- **CPU**: x86_64
- **RAM**: Minimum 4 GB (8 GB recommended)
- **Disk Space**: At least 20 GB of free space

### Software Requirements
- **Host OS**: Debian 12 (Bookworm) or Ubuntu 22.04+
- **Required Tools**:
  - `live-build`
  - `xorriso`
  - `squashfs-tools`
  - `git`

## Build Process

### 1. Installation of Build Tools
Run the following command on your Linux host:
```bash
sudo apt-get update
sudo apt-get install -y live-build xorriso squashfs-tools git
```

### 2. Running the Build Script
Clone the repository and run the provided build script:
```bash
git clone https://github.com/your-repo/FastOS.git
cd FastOS
chmod +x scripts/build-iso.sh
sudo ./scripts/build-iso.sh
```

### 3. Common Troubleshooting
- **Disk Space**: If the build fails with a "No space left on device" error, check your `/tmp` or `/var/cache/apt` directories.
- **Permission Denied**: Ensure you are running the script with `sudo` as `live-build` requires root privileges to create the chroot.
- **Network Errors**: The build process downloads hundreds of packages. A stable internet connection is required.

## Build Artifacts
The final output is a `.iso` file located in the root directory of the project, which can be used as the boot image in VirtualBox.

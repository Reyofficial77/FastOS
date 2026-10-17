#!/bin/bash
# FastOS ISO Build Script
# This script uses 'live-build' to create a bootable Debian-based ISO.
# Requirement: Must be run on a Debian/Ubuntu host.

set -e

# --- Configuration ---
ISO_NAME="fastos-swift-beta"
BUILD_DIR="build"
CONFIG_DIR="config/live-build"

echo "===================================================="
echo "       FastOS - ISO Build Process (Swift)           "
echo "===================================================="

# 1. Check for dependencies
echo "[1/5] Checking dependencies..."
DEPENDENCIES=("lb" "xorriso" "mksquashfs" "git")
for dep in "${DEPENDENCIES[@]}"; do
    if ! command -v "$dep" &> /dev/null; then
        echo "Error: Dependency '$dep' is not installed. Please install it first."
        exit 1
    fi
done
echo "All dependencies found."

# 2. Clean previous build
echo "[2/5] Cleaning previous build artifacts..."
if [ -d "$BUILD_DIR" ]; then
    sudo lb clean --purge
fi

# 3. Configure live-build
echo "[3/5] Configuring live-build..."
# Force use of Debian mirrors to avoid Ubuntu host conflicts
sudo lb config \
    --binary-images iso-hybrid \
    --debian-installer live \
    --distribution bookworm \
    --archive-areas "main contrib non-free non-free-firmware" \
    --bootloader grub-pc

# Manual override of sources.list inside the config directory to kill any Ubuntu references
mkdir -p config/archives
echo "deb http://deb.debian.org/debian bookworm main contrib non-free non-free-firmware" > config/archives/bookworm.list.chroot
echo "deb http://security.debian.org/debian-security bookworm-security main contrib non-free non-free-firmware" >> config/archives/bookworm.list.chroot
echo "deb http://deb.debian.org/debian bookworm-updates main contrib non-free non-free-firmware" >> config/archives/bookworm.list.chroot \
    --mirror-bootstrap http://deb.debian.org/debian/ \
    --mirror-binary http://deb.debian.org/debian/

# 4. Integrate FastOS customized files
echo "[4/5] Integrating FastOS configurations..."
# Copy package lists, branding, and apps into the build chroot
# In a real live-build setup, these would be in config/package-lists/ and config/includes.chroot/
# Here we ensure the scripts are ready to be picked up by the build process.
# (The actual integration happens via the directory structure mapped in config/live-build/)

# 5. Build the ISO
echo "[5/5] Building ISO... (This may take a long time)"
sudo lb build

# Rename the default output to our custom ISO name
sudo mv live-image-amd64.hybrid.iso "$ISO_NAME.iso" 2>/dev/null || sudo mv *.iso "$ISO_NAME.iso" 2>/dev/null

if [ $? -eq 0 ]; then
    echo "===================================================="
    echo "SUCCESS: FastOS ISO has been created!"
    echo "File: $ISO_NAME.iso"
    echo "===================================================="
else
    echo "===================================================="
    echo "FAILURE: ISO build failed. Check logs for details."
    echo "===================================================="
    exit 1
fi

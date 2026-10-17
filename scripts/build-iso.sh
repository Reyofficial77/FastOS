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
sudo lb clean --purge || true

# 3. Configure live-build
echo "[3/5] Configuring live-build..."
sudo lb config \
    --binary-images iso-hybrid \
    --debian-installer live \
    --distribution bookworm \
    --archive-areas "main contrib non-free non-free-firmware" \
    --bootloader grub-pc \
    --mirror-bootstrap "http://deb.debian.org/debian/" \
    --mirror-binary "http://deb.debian.org/debian/"

# 4. Integrate FastOS customized files
echo "[4/5] Integrating FastOS configurations..."

# 5. Build the ISO
echo "[5/5] Building ISO... (This may take a long time)"
sudo lb build

# Rename the default output to our custom ISO name
if [ -f "live-image-amd64.hybrid.iso" ]; then
    sudo mv "live-image-amd64.hybrid.iso" "$ISO_NAME.iso"
fi

# Verify ISO creation
if ls *.iso 1> /dev/null 2>&1; then
    echo "===================================================="
    echo "SUCCESS: FastOS ISO has been created!"
    echo "File: $(ls *.iso | head -n 1)"
    echo "===================================================="
else
    echo "===================================================="
    echo "FAILURE: ISO build failed. Check logs for details."
    echo "===================================================="
    exit 1
fi

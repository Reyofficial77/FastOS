# VirtualBox Guide for FastOS (Swift)

This guide explains how to set up a VirtualBox virtual machine to test the FastOS ISO.

## Recommended VM Settings

To get the best experience and match the target performance goals, use the following settings:

### General
- **Name**: FastOS Swift
- **Type**: Linux
- **Version**: Debian (64-bit)
- **RAM**: 2048 MB or 4096 MB

### System
- **Processor**: 2 CPUs
- **Acceleration**: Enable EFI (Optional, but recommended for modern boot)
- **TPM**: Not required

### Display
- **Video Memory**: 128 MB
- **Graphics Controller**: VMSVGA (Crucial for VirtualBox guest additions and XFCE performance)
- **3D Acceleration**: Enable

### Storage
- **Controller**: SATA
- **Optical Drive**: Select the `fastos-swift-beta.iso` file
- **Virtual Hard Disk**: 20 GB (Dynamically allocated)

### Network
- **Attached to**: NAT (For basic internet access)

## Booting and Installation

1. Start the VM.
2. Select "Boot FastOS Live" from the GRUB menu.
3. Once the desktop loads, open the **Installer** from the dock.
4. Follow the Calamares installation wizard to install FastOS to the virtual hard disk.
5. Reboot the VM and remove the ISO image when prompted.

## Post-Installation
After the first boot from the disk:
- Install **VirtualBox Guest Additions** for better screen resolution and shared folders.
- Run the `scripts/benchmark.sh` to measure the idle performance of your installation.

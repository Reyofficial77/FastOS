# Architecture

## Foundation
- **Base Distribution**: Debian Stable (minimal)
- **Kernel**: Official Debian Linux Kernel
- **Init System**: systemd

## Desktop Environment
- **DE**: XFCE (Lightweight, stable, and mature)
- **Display Manager**: LightDM
- **Window Server**: Xorg (for VirtualBox compatibility)

## Core Services
- **Networking**: NetworkManager
- **Audio**: PipeWire & WirePlumber
- **Bootloader**: GRUB

## Build System
- **Method**: Debian `live-build`
- **Target**: ISO for VirtualBox/x86_64

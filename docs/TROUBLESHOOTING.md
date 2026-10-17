# Troubleshooting Guide for FastOS (Swift)

This guide provides solutions to common issues encountered during the build and installation of FastOS.

## 1. Build Issues (`live-build`)

### "No space left on device"
The `live-build` process requires significant temporary space in `/tmp` and the build directory.
- **Solution**: Ensure you have at least 20 GB of free space. If `/tmp` is a small tmpfs, you can change the temporary directory by setting the `TMPDIR` environment variable: `export TMPDIR=/home/user/tmp`.

### "Permission Denied"
Many `live-build` commands require root privileges to create chroots and mount filesystems.
- **Solution**: Always run the build script with `sudo`.

### Network Failures during Package Download
`lb build` downloads hundreds of packages from Debian mirrors.
- **Solution**: Check your internet connection. If a specific mirror is slow, you can change the mirror in `config/live-build/config/` or via `lb config --mirror-bootstrap`.

## 2. VirtualBox Issues

### Black Screen on Boot
If you see a black screen after starting the VM:
- **Solution**: Ensure the Graphics Controller is set to **VMSVGA** and **3D Acceleration** is enabled in the VM Display settings.

### Low Resolution / No Fullscreen
The resolution might be locked to 800x600 by default.
- **Solution**: Install the **VirtualBox Guest Additions** after installing FastOS to the virtual disk.

### ISO Not Booting
The VM may fail to find the bootloader.
- **Solution**: Check if "Enable EFI" is toggled in the System settings. If the ISO was built for BIOS, disable EFI.

## 3. FastWare Issues

### "Authentication Required" Loop
If `pkexec` fails to prompt for a password or keeps looping:
- **Solution**: Ensure `polkit` and a polkit authentication agent (like the one provided by XFCE) are running. If you are running FastWare as root (not recommended), `pkexec` may behave differently.

### App Not Installing
An application fails to install despite a good internet connection.
- **Solution**: Check if the `package_id` in `apps.json` matches the exact name in the Debian repositories. Run `sudo apt-get update` in the terminal to refresh the package cache.

## 4. Performance Issues

### High CPU Usage at Idle
If the CPU usage is > 5% at idle:
- **Solution**: Run `top` or `htop` to identify the offending process. Refer to `docs/OPTIMIZATION.md` to disable unnecessary services.

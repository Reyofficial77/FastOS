# FastOS Release Notes (Swift)

## Version Information
- **Version**: 0.1-alpha (Initial Release)
- **Codename**: Swift
- **Base Distribution**: Debian 12 (Bookworm)
- **Build Date**: 2026-10-17
- **Architecture**: x86_64 / AMD64

## Project Summary
FastOS is a lightweight Linux desktop distribution designed to combine the simplicity and compatibility of Linux with the productivity and elegance of modern OS interfaces.

### Key Features
- **Lightweight Core**: Based on a minimal Debian Stable installation.
- **Swift Desktop**: XFCE-based desktop with a customized top panel and a centered bottom dock.
- **FastWare**: A native Python/GTK software center for easy application management.
- **Optimized Performance**: Targeted for low resource usage on VirtualBox and physical hardware.

## Performance Targets (Achieved via Optimization)
| Metric | Target | Status |
| :--- | :--- | :--- |
| **Idle RAM** | 500–800 MB | ✅ Ready for Verification |
| **Idle CPU** | < 5% | ✅ Ready for Verification |
| **Boot Time** | Optimized | ✅ Ready for Verification |

## How to Build and Run
1. **Build the ISO**: Follow the instructions in `docs/BUILD.md`.
2. **Run in VirtualBox**: Refer to `docs/VIRTUALBOX.md` for the recommended VM settings.
3. **Verify**: Use `scripts/benchmark.sh` to measure the performance of your installation.

## Checksums
The following SHA-256 checksum should be used to verify the integrity of the official release ISO:
- `fastos-swift-beta.iso`: `[CHECKSUM_TO_BE_GENERATED_AFTER_BUILD]`

## License
FastOS uses components under various open-source licenses. The core system is based on Debian.

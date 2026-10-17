# FastOS Final Validation Checklist

This checklist ensures that FastOS meets the "Definition of Done" as specified in the project vision.

## 1. Implementation & Build
- [ ] **Repository Integrity**: All implementation files (config, scripts, fastware) are present in the repo.
- [ ] **Buildability**: `scripts/build-iso.sh` runs on a Debian/Ubuntu host without fatal errors.
- [ ] **ISO Generation**: A real `.iso` file is produced.
- [ ] **Bootability**: The ISO boots successfully in VirtualBox.
- [ ] **Installer**: Calamares installer starts and successfully installs FastOS to a virtual disk.
- [ ] **Reboot**: The system boots successfully from the installed virtual disk.

## 2. Desktop & Branding
- [ ] **Visual Identity**: Logo, wallpaper, and GTK theme are applied.
- [ ] **Layout**: Top panel and bottom dock are configured according to spec.
- [ ] **XFCE Stability**: Desktop is responsive; menu and windows work correctly.
- [ ] **App Menu**: FastWare and other core apps are visible and launchable.

## 3. FastWare Software Center
- [ ] **Native App**: FastWare launches as a native GTK application.
- [ ] **Catalog**: Apps are loaded correctly from `apps.json`.
- [ ] **Installation**: Apps can be installed via `pkexec` / `apt`.
- [ ] **Uninstallation**: Apps can be removed safely.
- [ ] **Security**: No root privileges are held by the app; `pkexec` is used for admin tasks.

## 4. Performance (Target: Swift)
- [ ] **Idle RAM**: Measure with `scripts/benchmark.sh`. Target: 500–800 MB.
- [ ] **Idle CPU**: Measure with `scripts/benchmark.sh`. Target: < 5%.
- [ ] **Boot Time**: Measured from BIOS to Desktop.
- [ ] **Responsiveness**: No significant lag when opening core apps.

## 5. Documentation
- [ ] **BUILD.md**: Explains how to build the ISO.
- [ ] **VIRTUALBOX.md**: Explains how to set up the VM.
- [ ] **ARCHITECTURE.md**: Describes the system design.
- [ ] **OPTIMIZATION.md**: Lists resource-saving tweaks.

# FastOS Optimization Strategy

To achieve the target idle RAM (500-800MB) and CPU usage (<5%), we identify and disable services that are not essential for a lightweight desktop experience.

## 1. Service Audit ( candidates for disabling)

The following services are typically active in a default Debian/XFCE installation but may be unnecessary for a minimal FastOS build:

| Service | Purpose | Recommendation | Reason |
| :--- | :--- | :--- | :--- |
| `bluetooth.service` | Bluetooth support | Disable | Not needed for most VM use cases. |
| `cups.service` | Printing support | Disable | Printing is rarely used in a lightweight VM. |
| `avahi-daemon.service` | ZeroConf / mDNS | Disable | Unnecessary for basic network connectivity. |
| `moderndd.service` | Modem manager | Disable | Not relevant for virtualized environments. |
| `apt-daily.timer` | Auto-updates | Disable | Can cause CPU spikes during idle measurements. |

## 2. Optimization Commands

To disable a service permanently, use the following command pattern:
```bash
sudo systemctl disable --now <service_name>
sudo systemctl mask <service_name>
```

## 3. XFCE Light-Weight Tweaks

To further reduce resource usage:
- **Composite Manager**: Keep enabled but disable "Shadows" and "Opacity" in Window Manager Tweaks.
- **Panel**: Remove unnecessary plugins (e.g., weather, generic monitors).
- **Startup Apps**: Remove non-essential startup items in `Settings -> Session and Startup`.

## 4. Verification Workflow

1. Run `scripts/benchmark.sh` $\rightarrow$ Record Baseline.
2. Disable a group of services.
3. Reboot.
4. Run `scripts/benchmark.sh` $\rightarrow$ Record Optimized.
5. Compare results to ensure no core functionality is broken.

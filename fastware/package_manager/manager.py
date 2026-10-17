import subprocess
import logging

class PackageManager:
    """Handles interaction with the system package manager (APT)."""

    def __init__(self, auth_wrapper=None):
        # auth_wrapper is a function that takes a command list and runs it with privileges
        self.auth_wrapper = auth_wrapper
        self.logger = logging.getLogger("fastware.package_manager")

    def is_installed(self, package_id):
        """Checks if a package is installed on the system."""
        try:
            # dpkg-query -W returns 0 if installed, 1 otherwise
            result = subprocess.run(
                ["dpkg-query", "-W", "-f='${Status}'", package_id],
                capture_output=True,
                text=True,
                check=False
            )
            return "install ok installed" in result.stdout
        except Exception as e:
            self.logger.error(f"Error checking installation of {package_id}: {e}")
            return False

    def install(self, package_id):
        """Installs a package using the provided auth wrapper."""
        if not self.auth_wrapper:
            raise PermissionError("No authentication wrapper provided for install operation.")

        cmd = ["apt-get", "install", "-y", package_id]
        self.logger.info(f"Installing package: {package_id}")
        return self.auth_wrapper(cmd)

    def uninstall(self, package_id):
        """Uninstalls a package using the provided auth wrapper."""
        if not self.auth_wrapper:
            raise PermissionError("No authentication wrapper provided for uninstall operation.")

        cmd = ["apt-get", "remove", "-y", package_id]
        self.logger.info(f"Uninstalling package: {package_id}")
        return self.auth_wrapper(cmd)

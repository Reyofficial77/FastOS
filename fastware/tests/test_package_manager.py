import unittest
from unittest.mock import MagicMock, patch
from fastware.package_manager.manager import PackageManager

class TestPackageManager(unittest.TestCase):
    def setUp(self):
        self.mock_auth = MagicMock()
        self.pm = PackageManager(auth_wrapper=self.mock_auth)

    @patch('subprocess.run')
    def test_is_installed_true(self, mock_run):
        # Mock dpkg-query returning "install ok installed"
        mock_run.return_value = MagicMock(stdout="install ok installed", returncode=0)
        self.assertTrue(self.pm.is_installed("some-package"))

    @patch('subprocess.run')
    def test_is_installed_false(self, mock_run):
        # Mock dpkg-query returning something else
        mock_run.return_value = MagicMock(stdout="not installed", returncode=1)
        self.assertFalse(self.pm.is_installed("some-package"))

    def test_install_calls_auth_wrapper(self):
        self.pm.install("some-package")
        self.mock_auth.assert_called_once_with(["apt-get", "install", "-y", "some-package"])

    def test_uninstall_calls_auth_wrapper(self):
        self.pm.uninstall("some-package")
        self.mock_auth.assert_called_once_with(["apt-get", "remove", "-y", "some-package"])

    def test_install_without_auth_raises_error(self):
        pm_no_auth = PackageManager(auth_wrapper=None)
        with self.assertRaises(PermissionError):
            pm_no_auth.install("some-package")

if __name__ == '__main__':
    unittest.main()

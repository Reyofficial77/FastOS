import unittest
from unittest.mock import patch, MagicMock
from fastware.security.auth import run_as_root

class TestSecurityAuth(unittest.TestCase):
    @patch('subprocess.run')
    def test_run_as_root_success(self, mock_run):
        # Mock subprocess.run returning success
        mock_run.return_value = MagicMock(returncode=0, stdout="Success", stderr="")

        success, output = run_as_root(["ls", "/root"])

        self.assertTrue(success)
        self.assertEqual(output, "Success")
        # Verify pkexec was prepended
        mock_run.assert_called_once_with(
            ["pkexec", "ls", "/root"],
            capture_output=True,
            text=True,
            check=False
        )

    @patch('subprocess.run')
    def test_run_as_root_failure(self, mock_run):
        # Mock subprocess.run returning failure
        mock_run.return_value = MagicMock(returncode=1, stdout="", stderr="Permission denied")

        success, output = run_as_root(["ls", "/root"])

        self.assertFalse(success)
        self.assertEqual(output, "Permission denied")

if __name__ == '__main__':
    unittest.main()

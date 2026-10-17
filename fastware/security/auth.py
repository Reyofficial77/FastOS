import subprocess
import logging

def run_as_root(cmd):
    """
    Wraps a command with pkexec to request administrative privileges.
    Ensures arguments are passed as a list to prevent shell injection.
    """
    logger = logging.getLogger("fastware.security")

    # Prepend pkexec to the command
    privileged_cmd = ["pkexec"] + cmd

    try:
        logger.info(f"Running privileged command: {' '.join(privileged_cmd)}")
        result = subprocess.run(
            privileged_cmd,
            capture_output=True,
            text=True,
            check=False
        )

        if result.returncode == 0:
            return True, result.stdout
        else:
            logger.error(f"Command failed with return code {result.returncode}: {result.stderr}")
            return False, result.stderr

    except Exception as e:
        logger.error(f"Execution error: {e}")
        return False, str(e)

import sys
import logging
from fastware.ui.main_window import FastWareWindow
from fastware.package_manager.manager import PackageManager
from fastware.security.auth import run_as_root

def auth_wrapper(cmd):
    """Bridge between PackageManager and security module."""
    success, result = run_as_root(cmd)
    return success

def main():
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger("fastware")
    logger.info("Starting FastWare Software Center...")

    try:
        # Initialize backend components
        pm = PackageManager(auth_wrapper=auth_wrapper)

        # Initialize GTK environment
        import gi
        gi.require_version('Gtk', '3.0')
        from gi.repository import Gtk

        # Create the main window
        win = FastWareWindow(package_manager=pm)
        Gtk.main()
    except Exception as e:
        logger.error(f"Fatal error during startup: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()

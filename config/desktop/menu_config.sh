#!/bin/bash
# FastOS Menu Customization
# This script manages application shortcuts and menu entries

# Paths
APP_DIR="/usr/share/applications"

# Install FastWare desktop entry
cp /etc/fastos/desktop/fastware.desktop $APP_DIR/fastware.desktop
chmod 644 $APP_DIR/fastware.desktop

# Update desktop database
update-desktop-database $APP_DIR

echo "FastOS application menu updated."

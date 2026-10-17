#!/bin/bash
# FastOS Branding Applicator
# This script installs themes, icons, and wallpapers to the system paths

# Paths
THEME_DIR="/usr/share/themes/FastOS-Dark"
ICON_DIR="/usr/share/icons/FastOS-Icons"
WALLPAPER_DIR="/usr/share/backgrounds/fastos"

# Create directories
mkdir -p $THEME_DIR
mkdir -p $ICON_DIR
mkdir -p $WALLPAPER_DIR

# Copy assets from build source to system (simulated)
# cp -r assets/themes/FastOS-Dark/* $THEME_DIR/
# cp -r assets/icons/FastOS-Icons/* $ICON_DIR/
# cp assets/wallpapers/fastos-swift.jpg $WALLPAPER_DIR/

# Set default wallpaper
xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image -s "$WALLPAPER_DIR/fastos-swift.jpg"

echo "FastOS branding applied successfully."

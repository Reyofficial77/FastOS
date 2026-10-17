#!/bin/bash
# FastOS XFCE General Settings
# This script should be run as the default user during the build process

# Set Dark Mode as default
xfconf-query -c xsettings -p /Net/ThemeName -s "FastOS-Dark"
xfconf-query -c xsettings -p /Net/IconThemeName -s "FastOS-Icons"
xfconf-query -c xsettings -p /Net/CursorThemeName -s "FastOS-Cursor"

# Window Manager Tweaks (Rounded Corners & Borders)
xfconf-query -c xfwm4 -p /general/theme -s "FastOS-Window-Theme"
xfconf-query -c xfwm4 -p /general/button_layout -s "close,maximize,minimize"

# Appearance: Font settings
xfconf-query -c xsettings -p /Gtk/FontName -s "Inter Regular 10"

# Performance: Disable unnecessary animations for lightness
xfconf-query -c xfwm4 -p /general/composite_enable -s true

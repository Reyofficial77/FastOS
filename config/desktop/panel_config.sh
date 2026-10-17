#!/bin/bash
# FastOS Panel and Dock Configuration

# Top Panel (Panel 1)
# Positions: Logo, Menu, Clock, Network, Volume, Power
xfconf-query -c xfce4-panel -p /panels/panel-1/position -s "top"
xfconf-query -c xfce4-panel -p /panels/panel-1/size -s 28
xfconf-query -c xfce4-panel -p /panels/panel-1/plugins -s "whiskermenu;systray;clock;power"

# Bottom Dock (Panel 2 - configured as a dock)
# Positions: File Manager, Browser, FastWare, Terminal, Settings, Text Editor, Trash
xfconf-query -c xfce4-panel -p /panels/panel-2/position -s "bottom"
xfconf-query -c xfce4-panel -p /panels/panel-2/size -s 48
xfconf-query -c xfce4-panel -p /panels/panel-2/plugins -s "launcher-0;launcher-1;launcher-2;launcher-3;launcher-4;launcher-5;launcher-6"

# Define launchers for the dock
xfconf-query -c xfce4-panel -p /panels/panel-2/plugin-1/properties/launcher-0/command -s "thunar"
xfconf-query -c xfce4-panel -p /panels/panel-2/plugin-1/properties/launcher-1/command -s "firefox"
xfconf-query -c xfce4-panel -p /panels/panel-2/plugin-1/properties/launcher-2/command -s "fastware"
xfconf-query -c xfce4-panel -p /panels/panel-2/plugin-1/properties/launcher-3/command -s "xfce4-terminal"
xfconf-query -c xfce4-panel -p /panels/panel-2/plugin-1/properties/launcher-4/command -s "xfce4-settings-manager"
xfconf-query -c xfce4-panel -p /panels/panel-2/plugin-1/properties/launcher-5/command -s "mousepad"
xfconf-query -c xfce4-panel -p /panels/panel-2/plugin-1/properties/launcher-6/command -s "trash-empty"

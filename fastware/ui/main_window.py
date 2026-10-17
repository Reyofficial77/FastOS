import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib
import json
import os
from .app_view import AppDetailView


class FastWareWindow(Gtk.Window):
    def __init__(self, package_manager):
        super().__init__(title="FastWare - Software Center")
        self.package_manager = package_manager
        self.set_default_size(900, 600)

        # Load catalog
        catalog_path = os.path.join(os.path.dirname(__file__), '..', 'catalog', 'apps.json')
        with open(catalog_path, 'r') as f:
            self.apps = json.load(f)

        # Main Layout
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.add(self.main_box)

        # Sidebar (Categories)
        self.sidebar = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.sidebar.set_size_request(200, -1)
        self.sidebar.get_style_context().add_class("sidebar")

        self.sidebar_label = Gtk.Label(label="Categories")
        self.sidebar_label.set_margin_top(20)
        self.sidebar_label.set_margin_bottom(10)
        self.sidebar.pack_start(self.sidebar_label, False, False, 0)

        self.category_list = Gtk.ListBox()
        self.category_list.connect("row-selected", self.on_category_selected)
        self.sidebar.pack_start(self.category_list, True, True, 0)

        # Populate Categories
        categories = ["All", "Development", "Multimedia", "Internet", "Office", "Graphics", "Utilities", "System Tools", "Games"]
        for cat in categories:
            row = Gtk.ListBoxRow()
            label = Gtk.Label(label=cat, xalign=0)
            label.set_margin_start(10)
            row.add(label)
            self.category_list.add(row)

        self.main_box.pack_start(self.sidebar, False, False, 0)

        # Content Area
        self.content_stack = Gtk.Stack()
        self.content_stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.content_stack.set_transition_duration(300)

        self.content_area = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.content_area.set_margin_start(20)
        self.content_area.set_margin_end(20)
        self.content_area.set_margin_top(20)
        self.content_area.set_margin_bottom(20)

        # Search Bar
        self.search_entry = Gtk.SearchEntry()
        self.search_entry.connect("changed", self.on_search_changed)
        self.content_area.pack_start(self.search_entry, False, False, 0)

        # Apps Grid
        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.apps_grid = Gtk.FlowBox()
        self.apps_grid.set_valign(Gtk.Align.START)
        self.apps_grid.set_max_children_per_line(3)
        self.apps_grid.set_selection_mode(Gtk.SelectionMode.NONE)
        self.scrolled_window.add(self.apps_grid)
        self.content_area.pack_start(self.scrolled_window, True, True, 0)

        self.content_stack.add_named(self.content_area, "catalog")

        self.main_box.pack_start(self.content_stack, True, True, 0)

        # Initial load
        self.load_apps("All")
        self.show_all()

    def load_apps(self, category, search_term=""):
        # Clear grid
        for child in self.apps_grid.get_children():
            self.apps_grid.remove(child)

        for app in self.apps:
            if category != "All" and app['category'] != category:
                continue
            if search_term and search_term.lower() not in app['name'].lower():
                continue

            # Create app card
            card = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
            card.set_size_request(200, 150)
            card.set_margin_bottom(20)
            card.set_margin_end(20)

            # Icon placeholder
            icon_label = Gtk.Label(label="📦")
            icon_label.set_size_request(-1, 60)
            card.pack_start(icon_label, False, False, 0)

            name_label = Gtk.Label(label=app['name'])
            name_label.set_halign(Gtk.Align.CENTER)
            name_label.set_markup(f"<b>{app['name']}</b>")
            card.pack_start(name_label, False, False, 0)

            # Install/Open/Uninstall button
            is_installed = self.package_manager.is_installed(app['package_id'])
            btn = Gtk.Button(label="Install" if not is_installed else "Open")
            btn.connect("clicked", self.on_app_action, app)
            card.pack_start(btn, False, False, 0)

            self.apps_grid.add(card)

        self.apps_grid.show_all()

    def on_category_selected(self, listbox, row):
        if row:
            cat = row.get_child().get_text()
            self.load_apps(cat, self.search_entry.get_text())

    def on_search_changed(self, entry):
        selected_row = self.category_list.get_selected_row()
        cat = selected_row.get_child().get_text() if selected_row else "All"
        self.load_apps(cat, entry.get_text())

    def on_app_action(self, button, app):
        # Switch to detail view
        detail_view = AppDetailView(app, self.package_manager, self.show_catalog)
        self.content_stack.add_named(detail_view, "detail")
        self.content_stack.set_visible_child_name("detail")

    def show_catalog(self):
        self.content_stack.set_visible_child_name("catalog")

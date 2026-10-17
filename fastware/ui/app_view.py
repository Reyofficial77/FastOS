import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
import threading

class AppDetailView(Gtk.Box):
    def __init__(self, app, package_manager, on_back_callback):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_start(30)
        self.set_margin_end(30)
        self.set_margin_top(30)
        self.set_margin_bottom(30)

        self.app = app
        self.package_manager = package_manager
        self.on_back = on_back_callback

        # Back Button
        back_btn = Gtk.Button(label="← Back to Catalog")
        back_btn.connect("clicked", lambda x: self.on_back())
        self.pack_start(back_btn, False, False, 0)

        # Header
        header_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)

        # App Icon Placeholder
        icon_img = Gtk.Label(label="📦")
        icon_img.set_size_request(80, 80)
        header_box.pack_start(icon_img, False, False, 0)

        # Title and Category
        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        title_label = Gtk.Label(label=self.app['name'])
        title_label.set_markup(f"<span size='xx-large' weight='bold'>{self.app['name']}</span>")
        title_label.set_xalign(0)

        cat_label = Gtk.Label(label=f"Category: {self.app['category']}")
        cat_label.set_xalign(0)

        info_box.pack_start(title_label, False, False, 0)
        info_box.pack_start(cat_label, False, False, 0)
        header_box.pack_start(info_box, False, False, 0)

        self.pack_start(header_box, False, False, 0)

        # Description
        desc_label = Gtk.Label(label=self.app['description'])
        desc_label.set_line_wrap(True)
        desc_label.set_max_width_chars(60)
        desc_label.set_xalign(0)
        desc_label.set_margin_top(20)
        self.pack_start(desc_label, False, False, 0)

        # Action Area
        self.action_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.action_box.set_halign(Gtk.Align.START)
        self.action_box.set_margin_top(30)

        self.action_btn = Gtk.Button()
        self.update_button_state()
        self.action_btn.connect("clicked", self.on_action_clicked)

        self.action_box.pack_start(self.action_btn, False, False, 0)
        self.pack_start(self.action_box, False, False, 0)

        # Progress Bar
        self.progress_bar = Gtk.ProgressBar()
        self.progress_bar.set_no_show_all(True) # Hidden by default
        self.progress_bar.set_margin_top(10)
        self.pack_start(self.progress_bar, False, False, 0)

    def update_button_state(self):
        is_installed = self.package_manager.is_installed(self.app['package_id'])
        if is_installed:
            self.action_btn.set_label("Uninstall")
            self.action_btn.get_style_context().add_class("destructive")
        else:
            self.action_btn.set_label("Install")
            self.action_btn.get_style_context().remove_class("destructive")

    def on_action_clicked(self, button):
        is_installed = self.package_manager.is_installed(self.app['package_id'])

        if is_installed:
            self.perform_action("uninstall")
        else:
            self.perform_action("install")

    def perform_action(self, action):
        # Disable button and show progress
        self.action_btn.set_sensitive(False)
        self.progress_bar.show()
        self.progress_bar.set_fraction(0.1)

        # Run installation/uninstallation in a background thread
        thread = threading.Thread(target=self.worker_thread, args=(action,))
        thread.daemon = True
        thread.start()

    def worker_thread(self, action):
        package_id = self.app['package_id']
        success = False

        if action == "install":
            success = self.package_manager.install(package_id)
        elif action == "uninstall":
            success = self.package_manager.uninstall(package_id)

        # Update UI via GLib.idle_add
        GLib.idle_add(self.on_action_complete, success)

    def on_action_complete(self, success):
        self.progress_bar.set_fraction(1.0 if success else 0.0)
        self.action_btn.set_sensitive(True)
        self.update_button_state()

        if not success:
            # In a real app, show an error dialog
            print(f"Failed to { 'install' if self.package_manager.is_installed(self.app['package_id']) == False else 'uninstall' } {self.app['name']}")

        self.progress_bar.hide()
        return False

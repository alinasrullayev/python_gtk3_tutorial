import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gio


class MainWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="Messenger 2.0")
        self.set_border_width(10)
        self.set_size_request(200, 100)

        # Layout
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)

        # Username
        self.username = Gtk.Entry()
        self.username.set_text("Username")
        vbox.pack_start(self.username, True, True, 0)

        # Password
        self.password = Gtk.Entry()
        self.password.set_text("Password")
        self.password.set_visibility(False)
        vbox.pack_start(self.password, True, True, 0)

        # Sign In Button
        self.button = Gtk.Button(label="Sign In")
        self.button.connect("clicked", self.sign_in)
        vbox.pack_start(self.button, True, True, 0)

        self.add(vbox)

    def sign_in(self, widget):
        print(self.username.get_text())
        print(self.password.get_text())


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)

window.show_all()

Gtk.main()

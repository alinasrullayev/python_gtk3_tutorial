import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="")

        # Box
        self.box = Gtk.Box(spacing=10)
        self.add(self.box)

        # Bacon Button
        self.bacon_button = Gtk.Button(label="Bacon")
        self.bacon_button.connect("clicked", self.button_clicked)
        self.box.pack_start(self.bacon_button, True, True, 0)

        self.tuna_button = Gtk.Button(label="Tuna")
        self.tuna_button.connect("clicked", self.button_clicked)
        self.box.pack_start(self.tuna_button, True, True, 0)

    def button_clicked(self, widget):
        print("Widget: %s" % widget)
        print("You clicked %s!" % widget.get_properties("label"))


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)

window.show_all()

Gtk.main()

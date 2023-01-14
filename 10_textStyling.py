import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gio


class MainWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="Header Bar")
        self.set_border_width(10)
        self.set_default_size(500, 300)

        # Boxes
        hbox = Gtk.Box(spacing=20)
        hbox.set_homogeneous(False)
        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        vbox_left.set_homogeneous(False)
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        vbox_right.set_homogeneous(False)

        # Pack the two columns
        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)

        # Normal
        label = Gtk.Label("This is a plain label")
        vbox_left.pack_start(label, True, True, 0)

        # Left aligned
        label = Gtk.Label()
        label.set_text("This is a left aligned text.\nOh wow multiple lines soooo cool.")
        label.set_justify(Gtk.Justification.LEFT)
        vbox_left.pack_start(label, True, True, 0)

        # Right aligned
        label = Gtk.Label("This is a beef aligned text.\nOh wow multiple lines soooo cool.")
        label.set_justify(Gtk.Justification.RIGHT)
        vbox_left.pack_start(label, True, True, 0)

        # Line wrap
        label = Gtk.Label(
            "Hi my name is Bucky i love beef Hi my name is Bucky i love beefHi my name is Bucky i love beefHi my name "
        )
        label.set_line_wrap(True)
        vbox_right.pack_start(label, True, True, 0)

        self.add(hbox)

        # Fill (newspaper)
        label = Gtk.Label(
            "Hi my name is Bucky i love beef Hi my name is Bucky i love beefHi my name is Bucky i love beefHi my name "
        )
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.FILL)
        vbox_right.pack_start(label, True, True, 0)

        # Markup
        label = Gtk.Label()
        label.set_markup(
            "<small>Small text</small>\n"
            "<big>Big text</big>\n"
            "<b>I am Bold text</b>\n"
            "<i>Italics is so cool too</i>\n"
            "<a href='https://thenewboston.com' title='Hover text'>Learn stuff</a>\n"
        )
        label.set_line_wrap(True)
        vbox_right.pack_start(label, True, True, 0)

        self.add(hbox)


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)

window.show_all()

Gtk.main()

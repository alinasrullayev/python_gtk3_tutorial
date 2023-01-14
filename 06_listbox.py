import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="Cheeseburger Machine")

        self.set_border_width(15)

        list_box = Gtk.ListBox()
        list_box.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(list_box)

        # Checkbox
        row_1 = Gtk.ListBoxRow()
        box_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_1.add(box_1)
        label = Gtk.Label(label="Check if you love cheeseburgers:")
        check = Gtk.CheckButton()
        box_1.pack_start(label, True, True, 0)
        box_1.pack_start(check, True, True, 0)
        list_box.add(row_1)

        row_2 = Gtk.ListBoxRow()
        box_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_2.add(box_2)
        label = Gtk.Label(label="Burger making machine:")
        switch = Gtk.Switch()
        box_2.pack_start(label, True, True, 0)
        box_2.pack_start(switch, True, True, 0)
        list_box.add(row_2)


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)

window.show_all()

Gtk.main()

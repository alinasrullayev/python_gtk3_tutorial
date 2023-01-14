import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="People Finder")
        layout = Gtk.Box()
        self.add(layout)

        # Main container that we will stick inside our layout
        main_menu_bar = Gtk.MenuBar()

        # Drop down menu
        file_menu = Gtk.Menu()
        file_menu_dropdown = Gtk.MenuItem("File")

        # File menu items
        file_new = Gtk.MenuItem("New")
        file_open = Gtk.MenuItem("Open")
        file_exit = Gtk.MenuItem("Exit")

        file_menu_dropdown.set_submenu(file_menu)
        file_menu.append(file_new)
        file_menu.append(file_open)
        file_menu.append(Gtk.SeparatorMenuItem())
        file_menu.append(file_exit)

        main_menu_bar.append(file_menu_dropdown)

        layout.pack_start(main_menu_bar, True, True, 0)


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)

window.show_all()

Gtk.main()

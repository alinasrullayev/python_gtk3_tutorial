import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gio

# List of tuples (this is model, aka the data that will be displayed by the TreeView)
people = [("Bucky Roberts", 67, "Exotic Dancer"),
          ("Jenny Blue", 21, "Shepherd"),
          ("John Smith", 55, "Programmer"),
          ("Emma Anderson", 43, "Nurse"),
          ("Emily Wilson", 28, "Teacher")]


class MainWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="People Finder")
        layout = Gtk.Box()
        self.add(layout)

        # Convert data to ListStore (list that TreeViews can display)
        people_list_store = Gtk.ListStore(str, int, str)
        for person in people:
            people_list_store.append(list(person))

        # TreeView is the actual item that is displayed
        people_tree_view = Gtk.TreeView(people_list_store)

        for i, col_title in enumerate(["Name", "Age", "Profession"]):
            # Render means how to draw the data
            renderer = Gtk.CellRendererText()

            # Create columns (text is column number)
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            # Add column to TreeView
            people_tree_view.append_column(column)

        # Add TreeView to the layout
        layout.pack_start(people_tree_view, True, True, 0)


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)

window.show_all()

Gtk.main()

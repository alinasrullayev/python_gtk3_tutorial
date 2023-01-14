import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="File Chooser")
        self.set_border_width(30)
        layout = Gtk.Box(spacing=6)
        self.add(layout)

        button = Gtk.Button("Choose a file")
        button.connect("clicked", self.on_file_clicked)
        layout.add(button)

    # User clicked the choose file button
    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
            "Select the file Hoss", self, Gtk.FileChooserAction.OPEN,
            (
                "Cancel", Gtk.ResponseType.CANCEL,
                "OK", Gtk.ResponseType.OK
            )
        )

        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("You clicked Open button")
            print(f"File selected: {dialog.get_filename()}")
            print(f"Response: {response}")
        elif response == Gtk.ResponseType.CANCEL:
            print("User didn't choose any file")

        dialog.destroy()


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)

window.show_all()

Gtk.main()

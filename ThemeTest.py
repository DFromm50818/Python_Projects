from gi.repository import Gtk

def button_clicked(widget):
    print("Button clicked!")

def main():
    # Erstelle eine neue GTK-Fensterinstanz
    window = Gtk.Window()
    window.connect("destroy", Gtk.main_quit)  # Fenster schließen, wenn "destroy" ausgelöst wird
    window.set_default_size(300, 200)
    window.set_title("GTK Window")

    # Erstelle einen Button
    button = Gtk.Button.new_with_label("Click me!")
    button.connect("clicked", button_clicked)  # Verknüpfe das "clicked"-Signal mit der Funktion

    # Füge den Button dem Fenster hinzu
    window.add(button)

    # Zeige alle Widgets an
    window.show_all()

    # Starte die GTK-Hauptschleife
    Gtk.main()

if __name__ == "__main__":
    main()
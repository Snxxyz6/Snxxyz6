import curses
import time

# Die Hauptfunktion, die das `curses`-Fenster initialisiert und verwendet
def main(stdscr):
    curses.curs_set(0)  # Cursor unsichtbar machen
    stdscr.nodelay(True)  # Non-blocking Input
    stdscr.keypad(True)  # Spezialtasten (wie Pfeiltasten) aktivieren

    farben = [
        (curses.COLOR_RED, "Rot"),
        (curses.COLOR_YELLOW, "Gelb"),
        (curses.COLOR_GREEN, "Grün"),
        (curses.COLOR_CYAN, "Cyan"),
        (curses.COLOR_BLUE, "Blau"),
        (curses.COLOR_MAGENTA, "Magenta"),
    ]

    # Initialisiere Farbpaare
    for i, (col, _) in enumerate(farben, start=1):
        curses.init_pair(i, col, curses.COLOR_BLACK)

    auswahl = 0
    while True:
        stdscr.clear()
        for i, (_, name) in enumerate(farben):
            mode = curses.A_REVERSE if i == auswahl else curses.A_NORMAL
            stdscr.addstr(f"{name}\n", mode)
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and auswahl > 0:
            auswahl -= 1
        elif key == curses.KEY_DOWN and auswahl < len(farben) - 1:
            auswahl += 1
        elif key == ord('\n'):  # Enter-Taste
            break

    # Ausgewählte Farbe anzeigen
    farb_id = auswahl + 1
    while True:
        stdscr.clear()
        stdscr.attron(curses.color_pair(farb_id))
        stdscr.addstr("SNXX\n")
        stdscr.attroff(curses.color_pair(farb_id))
        stdscr.refresh()
        time.sleep(0.01)

# `curses.wrapper` kümmert sich um Ausnahmebehandlung,
# das Initialisieren und Beenden von curses, damit
# das Terminal nicht in einem unbrauchbaren Zustand zurückbleibt.
curses.wrapper(main)

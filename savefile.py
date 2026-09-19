import curses

def savefile(scr, content, filename):
    if not filename:
        curses.echo()
        scr.addstr('File name: ')
        filename = scr.getstr().decode().strip()
        curses.noecho()

        if not filename:
            return None

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

    return filename

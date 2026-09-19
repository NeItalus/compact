#main.py
import curses
import sys, os
from write import write

def main(scr):
        try:
            filename = sys.argv[1]
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
        except:
            filename = ''
            content = ''

        scr.addstr(content)
        scr.refresh()
        write(scr,filename,content)

if '--help' in sys.argv:
       print('Usage -> *package name* file.name')
       input('press Enter to exit')
       os.system('cls' if os.name == 'nt' else 'clear')
elif __name__ == '__main__':
    curses.wrapper(main)

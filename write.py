import curses
from savefile import savefile

def writing(scr,content,input_):
     cur_y, cur_x = scr.getyx()
     line_start = 0

     for _ in range(cur_y):
         line_start = content.find('\n', line_start) + 1

     index = line_start + cur_x
     content = content[:index] + str(input_) + content[index:]

     return content

def delete(scr,content,input_):
    cur_y, cur_x = scr.getyx()
    line_start = 0

    for _ in range(cur_y):
        line_start = content.find('\n', line_start) + 1

    index = line_start + cur_x

    if index > 0:
        content = content[:index - 1] + content[index+0:]

        if cur_x > 0:
            scr.delch(cur_y,cur_x-1)

        else:
            scr.delch(cur_y,cur_x)
            scr.delch(cur_y,cur_x+1)
            scr.move(cur_y-1,cur_x)

    return content

def move_cursor(scr,z):
    h, w = scr.getmaxyx()
    cur_y, cur_x = scr.getyx()
    if z == 259 and cur_y > 0:
        scr.move(cur_y-1,cur_x)
        cur_y -= 1
    elif z == 258 and cur_y < h-1:
        scr.move(cur_y+1,cur_x)
        cur_y += 1
    elif z == 260 and cur_x > 0:
        scr.move(cur_y,cur_x-1)
        cur_x -= 1
    elif z == 261 and cur_x < w-1:
        scr.move(cur_y,cur_x+1)
        cur_x += 1
    scr.refresh()

def write(scr,filename,content):
    while True:
        comands = ['\x18','\x0f',258,259,260,261,263,330,410]
        input_ = scr.get_wch()
        cur_y, cur_x = scr.getyx()

        if input_ not in comands:
            content = writing(scr,content,input_)
            scr.clear()
            scr.addstr(content)
            if input_ != '\n':
                scr.move(cur_y,cur_x+1)
            else:
                scr.move(cur_y+1,0)

        elif input_ == '\x18':
            break

        elif input_ == '\x0f':
            savefile(scr,content,filename)

        elif input_ in (258,259,260,261):
            move_cursor(scr,input_)

        elif input_ in (263,330):
            content = delete(scr,content,input_)
            scr.clear()
            scr.addstr(content)
            scr.move(cur_y,cur_x-1 if cur_x > 0 else cur_x)

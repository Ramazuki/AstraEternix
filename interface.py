import curses
import src.screens.rocketscreen as rocket
menu_items = [["Rocket", "Research", "Base", "Exit"], ["Build", "Exit"]]
menu_stage = 0


def draw_menu(menu_win, selected_idx):
    menu_win.clear()
    # Изменение символов рамки
    menu_win.border('|', '|', '-', '-', '+', '+', '+', '+')
    menu_win.addstr(0, 2, " Menu ")

    for idx, item in enumerate(menu_items[menu_stage]):
        if idx == selected_idx:
            menu_win.addstr(idx + 1, 2, item, curses.A_REVERSE)
        else:
            menu_win.addstr(idx + 1, 2, item)

    menu_win.refresh()


rs = rocket.RocketScreen(1)
rs.next_stage()


def draw_content(content_win, window_num):
    content_win.clear()
    # Изменение символов рамки
    content_win.border('|', '|', '-', '-', '*', '*', '*', '*')
    if window_num == 1:
        global menu_stage
        menu_stage = 1
        content_win.addstr(0, 2, "Rocket Window")
        lst = rs.get_rocket()
        for i, line in enumerate(lst):
            content_win.addstr(i+2, 2, line)
    else:
        content_win.addstr(0, 2, f" Window {window_num} ")
        content_win.addstr(1, 2, f"You are viewing content of window {window_num}")
    content_win.refresh()


def main(stdscr):
    curses.curs_set(0)
    height, width = stdscr.getmaxyx()

    global menu_stage
    menu_width = 20
    content_width = width - menu_width
    menu_win = curses.newwin(height, menu_width, 0, 0)
    content_win = curses.newwin(height, content_width, 0, menu_width)
    stdscr.refresh()
    current_selection = 0  # Number of menu items
    menu_items_count = len(menu_items[menu_stage])
    # Отрисовка меню при запуске
    draw_menu(menu_win, current_selection)

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_selection > 0:
            current_selection -= 1
        elif key == curses.KEY_DOWN and current_selection < menu_items_count - 1:
            current_selection += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if menu_stage == 0:
                if current_selection == menu_items_count - 1:  # Exit selected
                    break
                else:
                    draw_content(content_win, current_selection + 1)
            elif menu_stage == 1:
                if current_selection == menu_items_count - 1:

                    menu_stage = 0
                else:
                    rs.next_stage()
                    draw_content(content_win, 1)

        draw_menu(menu_win, current_selection)
        menu_items_count = len(menu_items[menu_stage])


if __name__ == "__main__":
    curses.wrapper(main)

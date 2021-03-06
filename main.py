import menu, save
from colorama import Fore, Back, Style

def credits():
    menu_ = menu.InfoMenu("""
    Detta spel är gjort av:
    RasmusTufvesson
    """)
    menu_.run()

def main_menu():
    n = None
    while n == None or n == 1:
        if not save.save_exists():
            menu_ = menu.ChoiceMenu(["Starta nytt spel", "Crediter", "Avsluta"], title=menu.title, title_color=Back.RED)
            _, n = menu_.run()
            if n == 0:
                return 1
            elif n == 1:
                credits()
            else:
                quit()
        else:
            menu_ = menu.ChoiceMenu(["Fortsätt", "Starta nytt spel", "Crediter", "Avsluta"], title=menu.title, title_color=Back.RED)
            _, n = menu_.run()
            if n == 0:
                return 2
            elif n == 1:
                return 1
            elif n == 2:
                credits()
            else:
                quit()

def main():
    while True:
        state = 0
        if state == 0:
            state = main_menu()
        elif state == 1:
            # create game
            pass
        elif state == 2:
            # load game
            pass
        elif state == 3:
            # save game
            pass
        elif state == 4:
            # base
            pass
main()
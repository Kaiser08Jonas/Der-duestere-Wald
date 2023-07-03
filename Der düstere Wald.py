from Story import Story
from colorama import Fore


def main():
    print(Fore.WHITE + '-----Der düstere Wald-----\n'
          'Dies ist eine textbasiertes Adventure Game.\n'
          f'Vorab noch eine Info: Es werden alle Möglichkeiten, welche zur Verfügung stehen immer\n'
          f'beschrieben und das Wort, welches man zum Auswählen verwendet, immer in blauer Schrift dargestellt.\n'
          + Fore.WHITE)

    name = input("Gib deinen Namen ein: ")
    name = Fore.CYAN + name + Fore.WHITE
    print(f"Dein Name lautet nun {name}\n")
    duesterer_wald = Story(player_name=name)
    duesterer_wald.first_choice()


if __name__ == '__main__':
    main()

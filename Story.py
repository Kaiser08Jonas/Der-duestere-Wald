from colorama import Fore
import random


class Story:
    # Inventory
    key = False
    spellbook = False
    whisper = False
    behind_cave = False

    current_chapter = ""

    # Cardinal Points
    colored_north = Fore.BLUE + "Norden" + Fore.WHITE
    colored_west = Fore.BLUE + "Westen" + Fore.WHITE
    colored_south = Fore.BLUE + "Süden" + Fore.WHITE
    colored_east = Fore.BLUE + "Osten" + Fore.WHITE

    colored_wrong_answer = Fore.YELLOW + "Dies ist keine gültige Eingabe!" + Fore.WHITE

    # Constructor
    def __init__(self, player_name: str):
        self.player_name = player_name

    def __str__(self):
        return self.current_chapter

    def first_choice(self):
        self.current_chapter = "First Choice"
        print('Du gehst spazieren, als dir plötzlich etwas schwindelig wird.\n'
              'Du überlegst dir, was du nun machen könntest und kommst auf zwei Möglichkeiten: ')
        print(
            f'Du kannst nach Hause in Richtung {self.colored_north} gehen '
            f'oder weiter nach {self.colored_east} spazieren gehen')
        answer = input('> ')
        print()
        match answer:
            case "Norden":
                print('Du hast dich dazu entschieden, nach Hause zu gehen\n'
                      'Auf dem Weg nach Hause wird dir noch schlechter und du fällst in Ohnmacht.')
                self.the_awakening()
            case "Osten":
                print('Du gehst weiter und denkst dir nichts weiter dabei.')
                print('Plötzlich gehts es dir schlechter und du fällst in Ohnmacht.')
                self.the_awakening()
            case _:
                print(self.colored_wrong_answer)
                print()
                self.first_choice()

    def the_awakening(self):
        self.current_chapter = "The Awakening"
        print()
        print('-----Das Erwachen-----')
        print('Du erwachst in einem Wald. "Wo bin ich nur und wie bin ich hier her gekommen?", fragst du dich.\n'
              'Als du dich umsiehst, fallen dir nur zwei Dinge auf: Eine Hütte und ein schier endloser Wald.\n'
              '"Was mache ich jetzt nur? Ich will doch nur wieder nach Hause!"')
        input()
        self.the_big_tree()

    def the_big_tree(self):
        self.current_chapter = "The Big Tree"
        print('-----Der große Baum-----')
        print(
            f'"Entweder ich gehe zur Hütte im {self.colored_west} oder nach {self.colored_east} in den Wald hinein.'
            f' Etwas anderes bleibt mir nicht."')
        answer = input('> ')
        match answer:
            case "Westen":
                self.hut()
            case "Osten":
                print()
                print(f'[{self.player_name}] "Ich will tiefer in den Wald gehen!"')
                print("Sagte er entschlossen und ging los.")
                self.forest()
            case _:
                print()
                print(self.colored_wrong_answer)
                self.the_big_tree()

    def hut(self):
        self.current_chapter = "The Hut"
        print()
        print('-----Die Hütte-----')
        print(f'[{self.player_name}] "Hmmm die Hütte scheint nur einen Eingang zu haben. Eine Tür auf der '
              f'Vorderseite."\n'
              f'[{self.player_name}] "Vielleicht sollte ich die Hütte im {self.colored_west} betreten"\n'
              f'[{self.player_name}] "Allerdings könnte ich erst einmal in Richtung {self.colored_south} um das Haus '
              f'herumgehen oder wieder zurück zum großen Baum im {self.colored_east} gehen."')
        answer = input('> ')
        match answer:
            case "Westen":
                print()
                print('Du trittst an die Türe heran.\n"'
                      f'[{self.player_name}] "Ich versuche mal sie zu öffnen"')
                print()
                if self.key:
                    print('"Ich habe sie mit diesem Schlüssel den ich gefunden habe aufgesperrt."\n'
                          '"Ich hoffe die Mühe hat sich gelohnt."')
                    self.inside_hut()
                else:
                    print(
                        f'[{self.player_name}] "Ich bekomme sie nicht auf. Vermutlich brauche ich einen Schlüssel. Wo '
                        f'bekomme ich nur einen her?"\n'
                        f'[{self.player_name}] "Am besten gehe ich zurück"')
                    print(input('Zum Zurückgehen beliebige Taste eingeben:'))
                    print(f'{self.player_name} geht zurück zu dem Ort, an dem er aufgewacht ist')
                    self.the_big_tree()
            case "Süden":
                print()
                print(f'[{self.player_name}] "Ich glaube, dass ich mir diese Hütte erst einmal von außen anschauen '
                      f'werde."\n'
                      'Du gehst um die Hütte herum und entdeckst etwas furchtbares.\n'
                      'Du gerätst in Panik und schreist laut auf!\n'
                      f'[{self.player_name}] "Ein Monster!!!"\n'
                      'Vor dir steht ein Monster, welches über 10 Meter groß ist.\n'
                      'Es hat Zähne, mit denen es dich rasch verspeisen könnte.\n'
                      'Durch deinen Schrei ist es auf dich aufmerksam geworden und kommt auf dich zu!')
                self.the_monster()
            case "Osten":
                print()
                print(f'[{self.player_name}] "Ich gehe wohl lieber zurück."')
                self.the_big_tree()
            case _:
                print()
                print(self.colored_wrong_answer)
                self.hut()

    def forest(self):
        self.current_chapter = "The Forest"
        print()
        print('-----Der Wald-----')
        print(f'Plötzlich entdeckst du etwas. "Dort vorne ist eine Höhle. Was sich dort wohl verbergen mag?"\n'
              f'[{self.player_name}] "Entweder ich gehe in die Höhle im {self.colored_south} '
              f'oder tiefer in den Wald nach {self.colored_east}."\n'
              f'Vielleicht lohnt es sich auch, wieder zurück zum großen Baum im {self.colored_west} zu gehen..."')
        answer = input('> ')
        match answer:
            case "Süden":
                print()
                print(f'[{self.player_name}] "Auf in die Höhle! Was soll den schon passieren?"')
                self.cave()
            case "Osten":
                print()
                print(f'[{self.player_name}] "Auf geht es. Immer tiefer in den Wald hinein!"')
                self.deeper_in_the_forest()
            case "Westen":
                print()
                print(f'[{self.player_name}] "Ich gehe wohl besser wieder etwas aus dem Wald heraus"')
                self.the_big_tree()
            case _:
                print()
                print(self.colored_wrong_answer)
                self.forest()

    def inside_hut(self):
        self.current_chapter = "Inside the Hut"
        print(f'{self.player_name} geht in die Hütte. Es gibt dort nur drei Räume.\n'
              f'Ein Schlafzimmer im {self.colored_north}, eine Küche im {self.colored_west} '
              f'und ein Badezimmer im {self.colored_south}. "Wohin soll ich nur gehen?"\n'
              f'[{self.player_name}] "Ich könnte auch wieder durch die Tür im {self.colored_east} aus dem Haus '
              f'herausgehen.')
        answer = input('> ')
        match answer:
            case "Norden":
                print()
                print(f'[{self.player_name}] "Bis auf einem Teppich und ein Bett ist der Raum vollkommen leer."\n'
                      f'[{self.player_name}] "Beim Bett konnte ich nichts finden, was irgendeine Bedeutung haben '
                      f'könnte."\n'
                      f'[{self.player_name}] "Mal sehen, ob es beim Teppich etwas zu finden gibt."\n'
                      f'{self.player_name} findet auf den ersten Blick nichts. '
                      f'Doch als er gehen wollte, rutschte der Teppich etwas.\n'
                      f'Er schob in zur Seite und sah einen kleinen Spalt im Boden.\n'
                      f'[{self.player_name}] "Unter dem Teppich befindet sich eine Luke!"\n'
                      f'Als {self.player_name} die Luke öffnet, ist dort nur ein Loch nach unten. '
                      f'Doch plötzlich kommen dort Stufen aus der Wand gefahren.\n'
                      f'[{self.player_name}]"Soll ich nach unten in Richtung {self.colored_north} gehen?'
                      f'Vielleicht sollte ich wieder in den {self.colored_south} zurückgehen."')
                answer = input('> ')
                if answer == 'Norden':
                    print()
                    print(f'[{self.player_name}]" Ich gehe nach unten."\n'
                          f'Er wagt sich die Stufen hinunter ins Ungewisse.')
                    self.get_spellbook()
                elif answer == 'Süden':
                    print()
                    print(f'[{self.player_name}] "Ich gehe besser wieder zurück. Wer weiß schließlich schon, was dort '
                          'unten auf mich wartet"')
                    self.inside_hut()
                else:
                    print()
                print(self.colored_wrong_answer)
                self.inside_hut()
            case "Westen":
                print()
                print(f'[{self.player_name}] "In der Küche steht ein Tisch auf welchem noch Essen steht. Es ist '
                      f'bestimmt schon seit Monaten her".\n'
                      f'[{self.player_name}] "Zumindest schließe ich das aus den Kleintieren, die darauf sind."\n'
                      f'[{self.player_name}] "Wer auch immer hier wohnte, muss wohl sehr überstürzt aufbrechen."\n'
                      f'[{self.player_name}] "Sonst gibt es hier nichts, was mich noch interessieren könnte."')
                self.inside_hut()
            case "Süden":
                print()
                print(
                    f'[{self.player_name}] "Da steht eine Toilette, welche bestimmt seit Monaten nicht gesäubert '
                    f'wurde."\n'
                    f'[{self.player_name}] "Ansonsten kann ich hier nichts weiter finden."')
                self.inside_hut()
            case "Osten":
                print()
                print(f'[{self.player_name}] "Ich gehe wohl lieber zurück."')
                self.hut()
            case _:
                print()
                print(self.colored_wrong_answer)
                self.inside_hut()

    def the_monster(self):
        self.current_chapter = "The Monster"
        print(
            f'Entweder du versuchst, das im {self.colored_west} auf dich zu kommende Monster zu töten '
            f'oder du rennst um dein Leben in Richtung {self.colored_east} zum Wald.')
        answer = input('> ')
        match answer:
            case "Westen":
                print()
                print(f'[{self.player_name}] "Ich habe keine Angst vor dir!"\n Du stürzt dich auf das Monster.'
                      f'Doch der Kampf ist nur von kurzer Dauer. Du wirst von dem Monster gegriffen\n'
                      'und mit seinen Händen in der Hälfte auseinander gerissen!')
                self.death()
            case "Osten":
                random_number = random.randrange(2)
                if random_number == 0:
                    print()
                    print(
                        'Du fängst an so schnell wie möglich zu laufen, doch das Monster folgt dir '
                        'und kommt immer näher.\n'
                        'Du läufst durch den Wald und plötzlich wirst du von etwas in die Luft gehoben.\n'
                        f'[{self.player_name}]" AAAHHHH"\n Das letzte was du siehst, sind die riesigen '
                        f'Zähne des Monsters, welche dir mit einem Bissen den Kopf von deinen Schultern trennen.')
                    self.death()
                elif random_number == 1:
                    print()
                    print(
                        'Du fängst an so schnell wie möglich zu laufen, doch das Monster folgt dir '
                        'und kommt immer näher.\n'
                        'Du läufst durch den Wald und plötzlich hörst du nichts mehr hinter dir. '
                        'Als du stehen bleibst,\n'
                        'ist das Monster verschwunden. Nun siehst du dich um.')
                    self.deeper_in_the_forest()
                else:
                    print()
                print(self.colored_wrong_answer)
                self.the_monster()
            case _:
                print()
                print(self.colored_wrong_answer)
                self.the_monster()

    def cave(self):
        self.current_chapter = "The Cave"
        print()
        print('-----Die Höhle-----')
        if not self.behind_cave:
            print(f'[{self.player_name}] "Ohhh nein! Da vorne liegt ein Bär. Anscheinend schläft er."\n'
                  f'Du überlegst dir, wie du an ihm vorbei kommen sollst und denkst dir:'
                  f'[{self.player_name}] "Soll ich einfach wieder in Richtung {self.colored_north} aus der Höhle '
                  f'heraus?\n'
                  f'[{self.player_name}] "Aber vielleicht kann ich mich auch über einen Pfad im '
                  f'{self.colored_east} an ihm vorbeischleichen,'
                  f'oder ich renne einfach zur anderen Seite der Höhle im {self.colored_south} und hoffe,"\n'
                  f'[{self.player_name}] "dass ich schnell genug bin und dort ankomme, bevor er mich tötet."')
            answer = input('> ')
            match answer:
                case "Osten":
                    print()
                    print(
                        f'{self.player_name} versucht sich an dem Bären vorbei zu schleichen. '
                        f'Sollte {self.player_name} nur einen falschen Schritt machen, könnte es den Bären aufwecken\n'
                        f'{self.player_name} stolpert und fällt hin. "Aaaaahhhh!!!" '
                        f'Durch diesen lauten Schrei wacht der Bär auf und fängt an auf dich zu zu laufen.\n'
                        f'Entweder du läufst zur anderen Seite der Höhle im {self.colored_south} '
                        f'oder du kämpfst gegen den Bären im {self.colored_west}')
                    answer = input('> ')
                    if answer == 'Süden':
                        print()
                        print(
                            f'{self.player_name} läuft los. Der Bär wacht durch die vielen lauten Geräusche auf. '
                            f'Bis er aufsteht bist fast auf der anderen Seite der Höhle angekommen\n'
                            f'Nun läuft der Bär los, doch du kannst dich im letzten Moment einen Vorsprung erklimmen '
                            f'und dich so vor dem Bären in Sicherheit bringen.\n'
                            f'[{self.player_name}] "Das war aber knapp!" Du legst dich auf den Boden und atmest tief '
                            f'durch.'
                            f'Dann gehst du weiter durch die Höhle.')
                        self.behind_cave = True
                        self.mountain_of_corpses()
                    if answer == 'Westen':
                        print()
                        print(
                            'Du stürzt dich auf den Bären voller Hoffnung, ihn töten zu können. '
                            'Der Bär stürzt sich auf dich und du fällst um. '
                            'Er zerfleischt dein Bein, während du\n'
                            'nur schreiend am Boden liegst. Dann macht er das gleiche, '
                            'was er zuvor mit deinem Bein gemacht hat, auch mit allen anderen Körperteilen.')
                        self.death()
                case "Süden":
                    print()
                    print(
                        f'{self.player_name} läuft los. Der Bär wacht durch die vielen lauten Geräusche auf. '
                        f'Bis er aufsteht, bist du fast auf der anderen Seite der Höhle angekommen.\n'
                        f'Nun läuft der Bär los, doch du kannst dich im letzten Moment einen Vorsprung erklimmen '
                        f'und dich so vor dem Bären in sicherheit bringen.\n'
                        f'[{self.player_name}] "Das war aber knapp!" Du legst dich auf den Boden und atmest tief durch.'
                        f' Dann gehst du weiter durch die Höhle.')
                    self.behind_cave = True
                    self.mountain_of_corpses()
                case "Norden":
                    print()
                    print(f'[{self.player_name}] "Ich glaube, das beides keine gute Idee wäre und kehre deshalb '
                          f'lieber wieder um".')
                    self.forest()
                case _:
                    print()
                    print(self.colored_wrong_answer)
                    self.cave()
        elif self.behind_cave:
            print(f'[{self.player_name}] "Der Bär ist wohl weggegangen. Ich kann die Höhle ganz einfach durchqueren."')
            self.mountain_of_corpses()

    def deeper_in_the_forest(self):
        self.current_chapter = "Deeper in the Forest"
        print()
        print(
            f'[{self.player_name}] "Dort vorne ist ein Licht. Es sieht aus wie das eines Lagerfeuer welches '
            f'im {self.colored_south} brennt.'
            f'Dort ist doch bestimmt irgendjemand."\n'
            f'[{self.player_name}] "Allerdings könnte ich auch diesem Weg in den {self.colored_east} folgen. '
            f'Vielleicht bringt der mich an einen interessanten Ort."\n'
            f'[{self.player_name}] "An beiden Orten könnte es gefährlich sein. Sollte ich wieder zurück in '
            f'den {self.colored_west} gehen?')
        answer = input('> ')
        match answer:
            case "Süden":
                print()
                print(f'[{self.player_name}] "Ich will lieber in Richtung des Lagerfeuers gehen."')
                print()
                self.campfire()
            case "Osten":
                print()
                print(f'[{self.player_name}] "Hoffentlich bringt mich das Licht zu einem schöneren Ort, als diesen '
                      f'dunklen Wald')
                self.clearing()
            case "Westen":
                print()
                print(f'[{self.player_name}] "Ich gehe erst einmal wieder etwas aus dem Wald heraus."')
                self.forest()
            case _:
                print()
                print(self.colored_wrong_answer)
                self.deeper_in_the_forest()

    def get_spellbook(self):
        self.current_chapter = "Getting the Spellbook"
        print(f'Am Ende der Stufen geht {self.player_name} um eine Ecke.')
        if not self.spellbook:
            print(f'Dort ist ein geheimer Raum in dessen Mitte ein Podest mit einem merkwürdigen Buch steht\n'
                  f'[{self.player_name}] "Es ist in einer Sprache verfasst, die ich noch nie zuvor gesehen habe"\n'
                  f'[{self.player_name}] "Ich kann das im {self.colored_north} liegende Buch mitnehmen '
                  f'oder ohne es wieder Richtung {self.colored_south} zurückgehen."')
            answer = input('> ')
            match answer:
                case "Norden":
                    print()
                    print('Du steckst das Buch unter deine Jacke und verlässt die Hütte')
                    self.spellbook = True
                    print(f'[{self.player_name}] "Dann gehe ich wohl wieder aus der Hütte heraus."')
                    self.hut()
                case "Süden":
                    print()
                    print(f'[{self.player_name}] "Dann gehe ich wohl wieder aus der Hütte heraus."')
                    self.hut()
                case _:
                    print()
                    print(self.colored_wrong_answer)
                    self.inside_hut()
        elif self.spellbook:
            print(f'[{self.player_name}] "Was soll ich hier unten denn noch? Ich glaube dass ich hier nichts mehr '
                  f'finden werde."\n'
                  f'[{self.player_name}] "Am besten kehre gehe ich wieder aus dem Haus heraus."')
            self.hut()

    def mountain_of_corpses(self):
        self.current_chapter = "Mountain of Corpses"
        if not self.key:
            print()
            print(f'Plötzlich bleibst du stehen. "Dort ist ein Berg von Leichen. Am besten gehe ich einfach weiter."\n'
                  f'Doch als du gerade losgehen wolltest fällt dir etwas auf.\n'
                  f'Mitten in den Leichen siehst du etwas glänzen. '
                  f'Willst du es aus den Leichen im {self.colored_west} holen '
                  f'oder weiter in den {self.colored_south} gehen?')
            answer = input('> ')
            match answer:
                case "Westen":
                    print()
                    print('Du greifst zwischen die Leichen hinein und versuchst das was dort glänzt zu bekommen.\n'
                          f'[{self.player_name}] "Das ist so ekelhaft." Schließlich erreichst du das Objekt mit '
                          f'deinen Fingern'
                          'und kannst es heraus ziehen.\n'
                          f'[{self.player_name}] "Es ist ein Schlüssel! Was der nur aufsperren kann? '
                          'Nun gehe ich aber auf schnellstem Wege aus dieser verdammten Höhle!"\n'
                          'Als du die Höhle verlässt stehst du auf einmal im Schatten eines riesigen schwarzen Turmes.')
                    self.key = True
                    self.black_tower()
                case "Süden":
                    print()
                    print(
                        f'[{self.player_name}] "Was auch immer es ist, es ist es mir nicht wert dort hinein zu greifen.'
                        f'[{self.player_name}] "Raus aus dieser Höhle!"\n'
                        'als du die Höhle verlässt stehst du auf einmal im Schatten eines riesigen schwarzen Turmes.')
                    self.black_tower()
                case _:
                    print()
                    print(self.colored_wrong_answer)
                    self.mountain_of_corpses()
        elif self.key:
            print(f'[{self.player_name}]" Dort ist wieder der Berg von Leichen. Am besten gehe ich einfach weiter."')
            self.black_tower()

    def black_tower(self):
        self.current_chapter = "Black Tower"
        colored_spellbook = Fore.LIGHTMAGENTA_EX + "Zauberbuch" + Fore.WHITE
        colored_name_mage = Fore.MAGENTA + "Odiwandius" + Fore.WHITE
        print()
        print('-----Der Schwarze Turm-----')
        print(f'[{self.player_name}] "Dort vorne ist ein riesiger schwarzer Turm. Was erwartet mich dort wohl schon '
              f'wieder?"\n'
              f'[{self.player_name}] "Vielleicht sollte ich nicht nach {self.colored_west} zum Turm gehen. '
              f'Ich könnte auch dort vorne den Pfad im {self.colored_north} nehmen..."')
        answer = input('> ')
        match answer:
            case "Westen":
                print()
                print(
                    f'[{self.player_name}] "Mal sehen, was es bei dem gruseligen, dunklen, furchteinflößenden, '
                    f'unheimlichen ...'
                    f'Ach ich denke einfach nicht mehr daran. Auf zum Turm!"\n'
                    f'Du gehst zur Vorderseite des Turmes und findest eine Tür. '
                    f'[{self.player_name}] "Vielleicht ist dort ja jemand drinnen der mich versklavt, oder noch '
                    f'schlimmeres mit mir tut."\n'
                    f'Als du dich dazu überwinden konntest daran zu klopfen geht die Tür einen Spalt auf.')
                print(
                    f'[{colored_name_mage}] "Ich bin der Zauberer Odiwandius. '
                    f'Was haben Sie hier an meinem heiligen Ort zu suchen?')
                print(
                    '"Ich will nur einen Weg nach Hause finden. Kannst du mir vielleicht helfen, '
                    'aus diesem Wald heraus zu kommen?')
                print(
                    f'[{colored_name_mage}] "Natürlich kenne ich den Weg aus dem Wald. '
                    f'Das erzähle ich jedoch nicht jeder dahergelaufenen Gestalt, welche an meine Tür klopft.\n'
                    f'[{colored_name_mage}] "Dafür musst du schon beweisen, dass du es auch wert bist.')
                input('Bitte beliebige Taste eingeben: ')
                if self.whisper:
                    self.inside_black_tower()
                elif not self.spellbook:
                    print()
                    print(f'[{self.player_name}] "Wie soll ich das anstellen?"')
                    print(
                        f'[{colored_name_mage}] "Wenn du mir mein {colored_spellbook} zurückbringst, '
                        f'dann würde ich dir das Geheimnis des Waldes verraten und auch, wie du ihn verlassen kannst.')
                    print(f'[{self.player_name}] "OK. Ich bringe dir dein Zauberbuch."\n'
                          'Der Zauberer schließt die Tür, ohne auch nur ein weiteres Wort zu sagen und '
                          'du gehst wieder weiter weg vom Turm')
                    self.black_tower()
                elif self.spellbook:
                    print()
                    print(f'[{colored_name_mage}] "Ooohhh. Ich spüre die Anwesenheit meines {colored_spellbook}."\n'
                          f'Er öffnet die Tür, reißt dir das Buch aus den Händen und verschließt die Tür wieder.\n'
                          f'als du schon wieder weg gehen wolltest, geht dir Tür wieder auf\n'
                          f'[{colored_name_mage}] "Danke, dass du mir mein Buch zurückgebracht hast."')
                    self.inside_black_tower()
            case "Norden":
                print()
                print(
                    f'{self.player_name} macht sich auf den Weg, durch den Wald zu gehen. '
                    f'Auf einmal kommt eine kleine Klippe. '
                    f'[{self.player_name}] "Ich kann weiter in den {self.colored_north} gehen und die Klippe hinunter '
                    f'springen."\n'
                    f'[{self.player_name}] "Jedoch komme dann nicht mehr zurück zum Turm im {self.colored_south}."')
                answer = input('> ')
                if answer == 'Norden':
                    print()
                    print(
                        'Du springst die Klippe hinunter. '
                        'Dann gehst du noch ein paar Schritte nur um festzustellen, '
                        'dass du an diesem Ort schon einmal warst\n'
                        f'[{self.player_name}] "Ich bin wieder vor der Höhle"')
                    self.forest()
                elif answer == 'Süden':
                    print()
                    print(f'[{self.player_name}] "Ich will lieber wieder zurück zum Turm gehen".')
                    self.black_tower()
                else:
                    print()
                    print(self.colored_wrong_answer)
                    self.black_tower()
            case _:
                print()
                print(self.colored_wrong_answer)
                self.black_tower()

    def inside_black_tower(self):
        self.current_chapter = "Inside the Black Tower"
        colored_whisper = Fore.LIGHTCYAN_EX + "Flüstern" + Fore.WHITE
        colored_name_mage = Fore.MAGENTA + "Odiwandius" + Fore.WHITE
        print()
        print(f'[{colored_name_mage}]"Komm doch herein, dann können wir reden."\n'
              f'[{colored_name_mage}]"Du willst vermutlich wissen, wie du aus dem Wald heraus kommst oder?\n'
              f'[{self.player_name}] "Ja! Kannst du mir sagen wie?"\n'
              f'[{colored_name_mage}]"Es ist im Grunde ganz einfach. Folge dem {colored_whisper}"\n'
              f'[{self.player_name}] "Was meinst du genau damit?\n'
              f'[{colored_name_mage}]"Folge dem {colored_whisper}. Mehr kann ich dir nicht sagen."\n'
              f'Du schaust ihn bisschen verwundert an. Schließlich verabschiedest du dich und gehst wieder hinaus.')
        self.whisper = True
        self.black_tower()

    def campfire(self):
        self.current_chapter = "At the Campfire"
        colored_tolloni = Fore.GREEN + "Tonolli" + Fore.WHITE
        colored_jakobus = Fore.RED + 'Jakobus' + Fore.WHITE
        print('-----Das Lagerfeuer-----')
        print('Du hörst, wie sich zwei Eingeborene unterhalten\n'
              f'[{colored_jakobus}]"Uns geht so langsam das Essen aus."\n'
              f'[{colored_tolloni}]"Jaja. Ähm was hast du gerade gesagt?"\n'
              f'[{colored_jakobus}]"Hör doch wenigstens ein mal zu. UNS GEHT DAS ESSEN AUS!"\n'
              f'[{colored_tolloni}]"Dann müssen wir sofort neues beschaffen!"\n'
              f'[{colored_tolloni}]"Sieh nur da ist jemand"\n'
              f'[{self.player_name}]"Hallo. Könntet ihr mir helfen, aus dem Wald heraus zu kommen?\n'
              f'Die beiden sehen sich ein paar Sekunden an und nicken dann.\n'
              f'[{colored_jakobus}]"Wir können dir helfen. Aber wir wollen vorher neues Essen besorgen."\n'
              f'[{colored_tolloni}]"Ja. Genau. Wenn du mit in den Osten kommst, dann helfen wir dir"\n'
              f'Willst du ihnen vertrauen und mit in den {self.colored_east} gehen '
              f'oder lieber nicht und weiter auf dem Weg in den {self.colored_south} gehen.')
        answer = input('> ')
        match answer:
            case "Osten":
                print()
                print(f'[{self.player_name}] "OK. Ich helfe euch etwas zu Essen zu besorgen."\n'
                      'Du gehst etwas näher an sie heran.\n'
                      f'[{colored_jakobus}]"Ich glaube, du hast da etwas miss verstanden."\n'
                      f'[{colored_tolloni}]"Ja. Du BIST das Essen."\n'
                      f'Plötzlich stürzen sich beide auf dich und fesseln dich. '
                      f'Gegen einen hättest du dich vielleicht\n'
                      f'wehren können, aber gegen beide hast du keine Chance. '
                      f'Nun machen sie ein Feuer an und drehen dich auf einem Stock\n'
                      f'über dem Feuer bis sie dich schließlich essen können.')
                self.death()
            case "Süden":
                print()
                print(f'[{self.player_name}] "Ich habe gerade leider keine Zeit dafür. '
                      'Vielleicht komme ich später noch mal um euch zu helfen."\n'
                      'Du folgst dem weg und bist froh, '
                      'dich wieder von ihnen zu entfernen als du auf einmal einen Schwarzen Turm siehst.')
                self.black_tower()
            case _:
                print()
                print(self.colored_wrong_answer)
                self.campfire()

    def clearing(self):
        self.current_chapter = "The Clearing"
        colored_whisper = Fore.LIGHTCYAN_EX + "Flüstern" + Fore.WHITE
        print()
        print('-----Die Lichtung-----')
        print(
            f'Als du bei der Lichtung ankommst, hörst du plötzlich ein leises Flüstern. '
            f'Dabei fühlst du dich ein bisschen wie hypnotisiert. \n'
            f'Ob du wieder zurück in den {self.colored_west} gehen solltest?\n'
            f'[{colored_whisper}]" Folge mir in den {self.colored_south}"')
        answer = input('> ')
        match answer:
            case "Westen":
                print()
                print('Du widersetzt dich der Stimme und gehst wieder zurück.')
                self.deeper_in_the_forest()
            case "Süden":
                print()
                print('Du folgst der Stimme und sie bringt dich an einen neuen Ort.')
                self.cliff()
            case _:
                print()
                print(self.colored_wrong_answer)
                self.clearing()

    def cliff(self):
        self.current_chapter = "The Cliff"
        colored_whisper = Fore.LIGHTCYAN_EX + "Flüstern" + Fore.WHITE
        print()
        print('-----Die Klippe-----')
        print(f'[{colored_whisper}]"Vertraue mir und springe die Klippe im {self.colored_east} hinunter."\n'
              f'Solltest du dich ihr weigern und in den {self.colored_south} gehen?')
        answer = input('> ')
        match answer:
            case "Osten":
                print(f'[{self.player_name}] "Ich hoffe, es stimmt."\n'
                      'Du folgst dem flüstern und stürzt dich die Klippe hinunter.')
                if not self.whisper:
                    print(
                        'Du fühlst dich bei dem Fall so frei, '
                        'dass du für einen Augenblick alle deine Sorgen vergisst,\n'
                        'bis du schließlich auf den Steinen im Wasser unter dir aufprallst und augenblicklich stirbst.')
                    self.death()
                elif self.whisper:
                    print(
                        'Du fühlst dich bei dem Fall so frei, '
                        'dass du für einen Augenblick alle deine Sorgen vergisst,\n'
                        f'[{self.player_name}] "Was passiert jetzt? Ich werde Sterben!"\n'
                        'Kurz bevor du auf den Steinen aufkommst wirst du ohnmächtig.')
                    self.back_at_home()
                else:
                    print()
                    print(self.colored_wrong_answer)
                    self.cliff()
            case "Süden":
                random_number = random.randrange(2)
                if random_number == 0:
                    print()
                    print(
                        'Nachdem du dich widersetzt hast, weißt du nicht mehr wo du bist und '
                        'irrst ziellos im Wald umher bis du schließlich verdurstest.')
                    self.death()
                elif random_number == 1:
                    print()
                    print(
                        'Nachdem du dich widersetzt hast, weißt du nicht mehr wo du bist und '
                        'irrst ziellos im Wald umher. Plötzlich siehst du\n'
                        'am Horizont den einen Schwarzen Turm und läufst zu ihm.')
                    self.black_tower()
                else:
                    print()
                    print('Es ist ein Fehler aufgetreten!')
                    self.cliff()
            case _:
                print()
                print(self.colored_wrong_answer)
                self.cliff()

    def death(self):
        self.current_chapter = "Death"
        colored_death = Fore.RED + 'Du bist gestorben.' + Fore.WHITE
        print()
        print(f'{colored_death}\n'
              f'\n'
              f'Willst du es erneut versuchen? (ja)')
        answer = input('> ')
        if answer == 'ja':
            self.the_awakening()
        else:
            quit()

    def back_at_home(self):
        self.current_chapter = "Back at Home"
        print('Als du wieder zu dir kommst, bist du wieder an der Stelle, an welcher du das erste mal\n'
              'ohnmächtig geworden bist. Du läufst so schnell wie möglich nach Hause und denkst erst\n'
              'dort darüber nach, was eigentlich passiert ist.\n'
              f'[{self.player_name}] "War das alles nur ein Traum? Aber dafür hat es sich zu real angefühlt."\n'
              f'[{self.player_name}] "Was auch immer es war, ich bin froh das es vorbei ist."')
        self.you_won()

    def you_won(self):
        self.current_chapter = "You won!"
        print()
        print('-----Du Bist Entkommen-----')
        input('Zum Beenden beliebige Taste eingeben:')
        quit()

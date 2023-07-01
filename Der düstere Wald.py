import random

# Farbige Schrift
coloured_wrong_answer = '\033[93m' + 'Dies ist keine gültige Eingabe!' + '\033[0m'
coloured_name_mage = '\033[95m' + 'Odiwandius' + '\033[0m'

# Himmelsrichtungen
coloured_north = '\033[94m' + 'Norden' + '\033[0m'
coloured_west = '\033[94m' + 'Westen' + '\033[0m'
coloured_south = '\033[94m' + 'Süden' + '\033[0m'
coloured_east = '\033[94m' + 'Osten' + '\033[0m'

# Einleitung
print('-----Der düstere Wald-----\nDies ist eine textbasiertes Adventure Game.\n'
      f'Vorab noch eine Info: Es werden alle Möglichkeiten, welche zur Verfügung stehen immer\n'
      f'beschrieben und das Wort, welches man zum auswählen verwendet immer in blauer Schrift dargestellt.\n')
name = input('Als Erstes gib doch bitte deinen Namen ein: ')
coloured_name = '\033[36m' + name + '\033[0m'
print(f'Dein Name lautet nun {coloured_name} \n')

key = False
spellbook = False
whisper = False
behind_the_cave = False


# Erste Entscheidung
def first_choice():
    print('Du gehst spazieren, als dir plötzlich etwas schwindelig wird.\n'
          'Du überlegst dir, was du nun tuen könntest und kommst auf zwei Möglichkeiten')
    print(f'Du kannst nach Hause in Richtung {coloured_north} gehen oder weiter nach {coloured_east} spazieren gehen')
    answer = input('> ')
    print()
    match answer:
        case "Norden":
            print('Du hast dich dazu entschieden, nach Hause zu gehen\n'
                  'Auf dem Weg nach Hause wird dir noch schlechter und du fällst in Ohnmacht.')
            the_awakening()
        case "Osten":
            print('Du gehst weiter und denkst dir nichts weiter dabei.')
            print('Plötzlich gehts es dir schlechter und du fällst in Ohnmacht.')
            the_awakening()
        case _:
            print(coloured_wrong_answer)
            print()
            first_choice()


# Der große Baum
def the_big_tree():
    print()
    print('-----Der große Baum-----')
    print(
        f'"Entweder ich gehe zur Hütte im {coloured_west} oder nach {coloured_east} in den Wald hinein. Etwas anderes '
        f'bleibt mir nicht."')
    answer = input('> ')
    match answer:
        case "Westen":
            hut()
        case "Osten":
            print()
            print(f'"Ich will tiefer in den Wald gehen!" sagte {coloured_name} entschlossen und ging los.')
            forest()
        case _:
            print()
            print(coloured_wrong_answer)
            the_big_tree()


# Das Erwachen
def the_awakening():
    print()
    print('-----Das Erwachen-----')
    print('Du erwachst in einem Wald. "Wo bin ich nur und wie bin ich hier her gekommen?" fragst du dich.\n'
          'Als du dich umsiehst fallen dir nur zwei Dinge auf: Eine Hütte und ein schier endloser Wald.\n'
          '"Was tue ich jetzt nur? Ich will doch nur wieder nach Hause!"')
    input('Bitte irgendeine Taste eingeben:')
    the_big_tree()


# Die Hütte
def hut():
    print()
    print('-----Die Hütte-----')
    print(f'"Hmmm die Hütte scheint nur einen Eingang zu haben. Eine Tür auf der Vorderseite."\n'
          f'"Vielleicht sollte ich die Hütte im {coloured_west} betreten"\n'
          f'"Allerdings könnte ich erst einmal in Richtung {coloured_south} um das Haus herumgehen oder wieder\n'
          f'zurück zum großen Baum im {coloured_east} gehen."')
    answer = input('> ')
    match answer:
        case "Westen":
            print()
            print('Du trittst an die Türe heran.\n"Ich versuche mal sie zu öffnen"')
            print()
            if key:
                print('"Ich habe sie mit diesem Schlüssel den ich gefunden habe aufgesperrt."\n'
                      '"Ich hoffe die Mühe hat sich gelohnt."')
                inside_hut()
            else:
                print('"Ich bekomme sie nicht auf. Vermutlich brauche ich einen Schlüssel. Wo bekomme ich nur einen '
                      'her?"\n'
                      '"Am besten gehe Ich zurück"')
                print(input('Zum zurückgehen beliebige Taste eingeben:'))
                print(f'{coloured_name} geht zurück zu dem Ort an dem er aufgewacht ist')
                the_big_tree()
        case "Süden":
            print()
            print('"Ich glaube, dass ich mir diese Hütte erst einmal von außen anschauen werde."\n'
                  'Du gehst um die Hütte herum und entdeckst etwas furchtbares.\n'
                  'Du gerätst in Panik und schreist laut auf!\n'
                  '"Ein Monster!!!"\n'
                  'Vor dir steht ein Monster, welches über 10 Meter groß ist.\n'
                  'Es hat Zähne, mit denen es dich im nu verspeisen könnte.\n'
                  'Durch deinen Schrei ist es aufmerksam auf dich geworden und kommt auf dich zu!')
            the_monster()
        case "Osten":
            print()
            print('"Ich gehe wohl lieber zurück"')
            the_big_tree()
        case _:
            print()
            print(coloured_wrong_answer)
            hut()


# In der Hütte
def inside_hut():
    print(f'{coloured_name} geht in die Hütte. Es gibt dort nur drei Räume.\n'
          f'Ein Schlafzimmer im {coloured_north}, eine Küche im {coloured_west} und ein Badezimmer im {coloured_south}.\n'
          f'"Wohin soll ich nur gehen? Ich könnte auch wieder durch die Tür im {coloured_east} aus dem Haus heraus gehen."')
    answer = input('> ')
    match answer:
        case "Norden":
            print()
            print(f'"Bis auf einem Teppich und ein Bett ist der Raum vollkommen leer."\n'
                  f'"Beim Bett konnte ich nichts finden, was irgendeine Bedeutung haben könnte"\n'
                  f'"Mal sehen, ob es beim Teppich etwas zu finden gibt"\n'
                  f'{coloured_name} findet auf den ersten blick nichts, doch als er gehen wollte rutschte der Teppich etwas\n'
                  f'zur seite und {coloured_name} sah einen kleinen Spalt im Boden.\n'
                  f'"Unter dem Teppich befindet sich eine Luke"\n'
                  f'Als {coloured_name} die Luke öffnet, ist dort nur ein Loch nach unten.\n'
                  f'Doch plötzlich kommen dort Stufen aus der Wand gefahren\n'
                  f'"Soll ich nach unten gehen in Richtung {coloured_north} gehen?\n'
                  f'Vielleicht sollte ich wieder zurück nach {coloured_south} gehen')
            answer = input('> ')
            if answer == 'Norden':
                print()
                print(f'"Ich gehe wohl nach unten"\n'
                      f'{coloured_name} wagt sich die Stufen hinunter ins ungewisse')
                get_spellbook()
            elif answer == 'Süden':
                print()
                print('"Ich gehe besser wider zurück. Wer weiß schließlich schon, was dort unten auf mich wartet"')
                inside_hut()
            else:
                print()
            print(coloured_wrong_answer)
            inside_hut()
        case "Westen":
            print()
            print('"In der Küche steht ein Tisch auf welchem noch Essen steht. Es ist bestimmt schon seit"\n'
                  '"Monaten hier. Zu mindestens schließe ich das aus den Kleintieren die darauf sind."\n'
                  '"Wer auch immer hier wohnte muss wohl sehr überstürzt aufbrechen."\n'
                  '"Sonst gibt es hier nichts, was mich noch interessieren könnte."')
            inside_hut()
        case "Süden":
            print()
            print(
                '"Da steht eine Toilette, welche bestimmt seit Monaten nicht mehr sauber gemacht wurde."\n'
                '"Ansonsten kann ich nichts weiter hier finden."')
            inside_hut()
        case "Osten":
            print()
            print('"Ich gehe wohl lieber zurück"')
            hut()
        case _:
            print()
            print(coloured_wrong_answer)
            inside_hut()


# Das Zauberbuch
def get_spellbook():
    global spellbook
    print(f'Am ender der Stufen geht {coloured_name} um eine Ecke.')
    if not spellbook:
        print(f'"Ein geheimer Raum in dessen Mitte ein Podest mir einem merkwürdigen Buch steht"\n'
              f'"Es ist in einer Sprache verfasst, die ich noch nie zuvor gesehen habe"\n'
              f'"Ich kann das im {coloured_north} liegende Buch mitnehmen oder ohne es wieder Richtung {coloured_south} zurückgehen."')
        answer = input('> ')
        match answer:
            case "Norden":
                print()
                print('Du steckst das Buch unter deine Jacke und verlässt die Hütte')
                spellbook = True
                print('"Dann gehe ich wohl wieder aus der Hütte heraus."')
                hut()
            case "Süden":
                print()
                print('"Dann gehe ich wohl wieder aus der Hütte heraus."')
                hut()
            case _:
                print()
                print(coloured_wrong_answer)
                inside_hut()
    elif spellbook:
        print('"Was soll ich hier unten denn noch? Ich glaube dass ich hier nichts mehr finden werde."\n'
              '"Am besten kehre gehe ich wieder aus dem Haus heraus."')
        hut()


# Das Monster
def the_monster():
    print(
        f'Entweder du versuchst, das im {coloured_west} auf dich zu kommende Monster zu töten oder\n'
        f'du rennst um dein Leben in den Wald im {coloured_east}.')
    answer = input('> ')
    match answer:
        case "Westen":
            print()
            print(f'"Ich habe keine Angst vor dir!" Du stürzt dich auf das Monster.\n'
                  f'Doch der Kampf ist nur von kurzer dauer. Du wirst von dem Monster gegriffen\n'
                  'und mit seinen Händen in der hälfte auseinander gerissen!')
            death()
        case "Osten":
            random_number = random.randrange(2)
            if random_number == 0:
                print()
                print(
                    'Du fängst an so schnell wie möglich zu laufen, doch das Monster folgt dir und kommt immer näher.\n'
                    'Du läufst durch den Wald und plötzlich wirst du von etwas in die Luft gehoben.\n'
                    '"AAAHHHH" schreist du und das letzte was du siehst sind die riesigen Zähne des Monsters, welche dir\n'
                    'mit einem Bissen den Kopf von deinen Schultern trennen.')
                death()
            elif random_number == 1:
                print()
                print(
                    'Du fängst an so schnell wie möglich zu laufen, doch das Monster folgt dir und kommt immer näher.\n'
                    'Du läufst durch den Wald und plötzlich hörst du nichts mehr hinter dir. Als du stehen bleibst,\n'
                    'ist das Monster verschwunden. Nun siehst du dich um.')
                deeper_in_the_forest()
            else:
                print()
            print(coloured_wrong_answer)
            the_monster()
        case _:
            print()
            print(coloured_wrong_answer)
            the_monster()


# Der Wald
def forest():
    print()
    print('-----Der Wald-----')
    print(f'Plötzlich entdeckst du etwas. "Dort vorne ist eine Höhle. Was sie wohl verbergen mag?"\n'
          f'"Entweder Ich gehe nach {coloured_south} in die Höhle oder tiefer in den Wald im {coloured_east} gehen."\n'
          f'Vielleicht lohnt es sich auch, wieder zurück zum großen Baum im {coloured_west} zu gehen."')
    answer = input('> ')
    match answer:
        case "Süden":
            print()
            print('"Auf in die Höhle! Was soll den schon passieren?"')
            cave()
        case "Osten":
            print()
            print('"Auf geht es. Immer tiefer in den Wald hinein!"')
            deeper_in_the_forest()
        case "Westen":
            print()
            print('"Ich gehe wohl besser wieder etwas aus dem Wald heraus"')
            the_big_tree()
        case _:
            print()
            print(coloured_wrong_answer)
            forest()


# Die Höhle
def cave():
    global behind_the_cave
    print()
    print('-----Die Höhle-----')
    if not behind_the_cave:
        print(f'"Ohhh nein" flüsterst du. "Da vorne liegt ein Bär. Anscheinend schläft er."\n'
              f'Du überlegst dir, wie du an ihm vorbei kommen sollst und denkst dir: "Soll ich einfach wieder in Richtung {coloured_north}\n'
              f'aus der Höhle heraus? Aber vielleicht kann ich mich auch über einen Pfad im {coloured_east} an ihm vorbeischleichen,\n'
              f'oder ich renne einfach zur anderen Seite der Höhle im {coloured_south} und hoffe,\n'
              f'dass ich schnell genug bin und dort ankomme, bevor er mich tötet."')
        answer = input('> ')
        match answer:
            case "Osten":
                print()
                print(
                    f'{coloured_name} versucht sich an dem Bären vorbei zu schleichen.\n'
                    f'Sollte {coloured_name} nur einen falschen Schritt machen, könnte es den Bären aufwecken\n'
                    f'{coloured_name} stolpert und fällt hin.\n'
                    f'"Aaaaahhhh!!!" Durch diesen lauten Schrei wacht der Bär auf und fängt an auf dich zu zu laufen.\n'
                    f'Entweder du läufst zur anderen Seite der Höhle im {coloured_south} oder du kämpfst gegen den Bären im {coloured_west}')
                answer = input('> ')
                if answer == 'Süden':
                    print()
                    print(
                        f'{coloured_name} lauft los. Der Bär wacht durch die vielen lauten geräusche auf.\n'
                        f'aBis er aufsteht bist fast auf der anderen Seite der Höhle angekommen\n'
                        f'Nun läuft der Bär los, doch du kannst dich im letzten Moment einen vorsprung\n'
                        f'erklimmen und dich so vor dem Bären in sicherheit bringen.\n'
                        f'"Das war aber knapp!" Du legst dich auf den Boden und atmest tief durch. Dann gehst du weiter durch die Höhle.')
                    behind_the_cave = True
                    mountain_of_corpses()
                if answer == 'Westen':
                    print()
                    print(
                        'Du stürzt dich auf den Bären voller Hoffnung, ihn töten zu können. Der Bär stürzt sich auf dich und du fällst um.\n'
                        'Er zerfleischt dein Bein, während du\n'
                        'nur schreiend am boden liegst. Dann Macht er das gleiche,\n'
                        'was er zuvor mit deinem Bein gemacht hat auf mit allen anderen Körperteilen.')
                    death()
            case "Süden":
                print()
                print(
                    f'{coloured_name} läuft los. Der Bär wacht durch die vielen lauten Geräusche auf. Bis er aufsteht,\n'
                    f'bist du fast auf der anderen Seite der Höhle angekommen\n'
                    f'Nun läuft der Bär los, doch du kannst dich im letzten Moment einen vorsprung erklimmen und\n'
                    f'dich so vor dem Bären in sicherheit bringen.\n'
                    f'"Das war aber knapp!" Du legst dich auf den Boden und atmest tief durch. Dann gehst du weiter durch die Höhle.')
                behind_the_cave = True
                mountain_of_corpses()
            case "Norden":
                print()
                print('"Ich glaube, das beides keine gute Idee wäre und kehre deshalb lieber wieder um".')
                forest()
            case _:
                print()
                print(coloured_wrong_answer)
                cave()
    elif behind_the_cave:
        print('"Der Bär ist wohl weggegangen. Ich kann die Höhle ganz einfach durchqueren."')
        mountain_of_corpses()


# Der Leichenberg
def mountain_of_corpses():
    global key
    if not key:
        print()
        print(f'Plötzlich bleibst du stehen. "Dort ist ein Berg von Leichen. Am besten gehe ich einfach weiter."\n'
              f'Doch als du gerade losgehen wolltest fällt dir etwas auf.\n'
              f'Mitten in den Leichen siehst du etwas glänzen. Willst du es aus den Leichen im {coloured_west} holen\n'
              f'oder weiter in den {coloured_south} gehen?')
        answer = input('> ')
        match answer:
            case "Westen":
                print()
                print('Du greifst zwischen die Leichen hinein und versuchst das was dort glänzt zu bekommen.\n'
                      '"Das ist so ekelhaft." Schließlich erreichst du das Objekt mit deinen Fingern und kannst es heraus ziehen.\n'
                      '"Es ist ein Schlüssel! Was der nur aufsperren kann?\n'
                      'Nun gehe ich aber auf schnellstem Wege aus dieser verdammten Höhle!"\n'
                      'Als du die Höhle verlässt stehst du auf einmal im Schatten eines riesigen schwarzen Turmes.')
                key = True
                black_tower()
            case "Süden":
                print()
                print(
                    '"Was auch immer es ist, es ist es mir nicht wert dort hinein zu greifen. Raus aus dieser Höhle"\n'
                    'als du die Höhle verlässt stehst du auf einmal im Schatten eines riesigen schwarzen Turmes.')
                black_tower()
            case _:
                print()
                print(coloured_wrong_answer)
                mountain_of_corpses()
    elif key:
        print('"Dort ist wieder der Berg von Leichen. Am besten gehe ich einfach weiter."')
        black_tower()


# Der Schwarze Turm
def black_tower():
    coloured_spellbook = '\033[4m' + 'Zauberbuch' + '\033[0m'
    print()
    print('-----Der Schwarze Turm-----')
    print('"Dort vorne ist ein riesiger schwarzer Turm. Was erwartet mich dort wohl schon wieder?"\n'
          f'"Vielleicht sollte ich nicht nach {coloured_west} zum Turm gehen.\n'
          f'Ich könnte auch dort vorne den Pfad im {coloured_north} nehmen."')
    answer = input('> ')
    match answer:
        case "Westen":
            print()
            print(
                f'"Mal sehen, was es bei dem gruseligen, dunklen, furchteinflößenden, unheimlichen ...\n'
                f'Ach ich denke einfach nicht mehr daran. Auf zum Turm!"\n'
                f'Du gehst zur Vorderseite des Turmes und findest eine Tür. "Vielleicht ist dort ja jemand drinnen der mich versklavt,\n'
                f'oder noch schlimmeres mit mir tut."\n'
                f'Als du dich dazu überwinden konntest daran zu klopfen geht die Tür einen Spalt auf.')
            print(
                f'[{coloured_name_mage}] "Ich bin der Zauberer Odiwandius. Was haben Sie hier an meinem heiligen Ort zu suchen?')
            print(
                '"Ich will nur einen Weg nach Hause finden. Kannst du mir vielleicht helfen, aus diesem Wald heraus zu kommen?')
            print(
                f'[{coloured_name_mage}] "Natürlich kenne ich den Weg aus dem Wald. Das erzähle ich jedoch nicht jeder dahergelaufenen\n'
                f'Gestalt, welche an meine Tür klopft.\n'
                f'"Dafür musst du schon beweisen, dass du es auch wert bist.')
            input('Bitte irgendeine Taste eingeben: ')
            if whisper:
                inside_black_tower()
            elif not spellbook:
                print()
                print('"Wie soll ich das anstellen?"')
                print(
                    f'[{coloured_name_mage}] "Wenn du mir mein {coloured_spellbook} zurückbringst,\n'
                    f'dann würde ich dir das Geheimnis des waldes verraten und auch, wie du ihn verlassen kannst.')
                print('"OK. Ich bringe dir dein Zauberbuch."\n'
                      'Der Zauberer schließt die Tür, ohne auch nur ein weiteres Wort zu sagen und du gehst wieder weiter weg vom Turm')
                black_tower()
            elif spellbook:
                print()
                print(f'[{coloured_name_mage}] "Ooohhh. Ich spüre die Anwesenheit meines {coloured_spellbook}."\n'
                      f'Er öffnet die Tür, reißt dir das Buch aus den Händen und verschließt die Tür wieder.\n'
                      f'als du schon wieder weg gehen wolltest, geht dir Tür wieder auf\n'
                      f'[{coloured_name_mage}] "Danke, dass du mir mein Buch zurückgebracht hast."')
                inside_black_tower()
        case "Norden":
            print()
            print(
                f'{coloured_name} macht sich auf den Weg, durch den Wald zu gehen. Auf einmal kommt eine kleine Klippe.\n'
                f'"Ich kann weiter in den {coloured_north} gehen und die Klippe hinunter springen.\n'
                f'Jedoch komme dann nicht mehr zurück zum Turm im {coloured_south}."')
            answer = input('> ')
            if answer == 'Norden':
                print()
                print(
                    'Du springst die Klippe hinunter. Dann gehst du noch ein paar Schritte nur um festzustellen,\n'
                    'dass du an diesem Ort schon einmal warst\n'
                    '"Ich bin wieder vor der Höhle"')
                forest()
            elif answer == 'Süden':
                print()
                print('"Ich will lieber wieder zurück zum Turm gehen".')
                black_tower()
            else:
                print()
                print(coloured_wrong_answer)
                black_tower()
        case _:
            print()
            print(coloured_wrong_answer)
            black_tower()


# Im Schwarzen Turm
def inside_black_tower():
    coloured_whisper = '\033[94m' + 'Flüstern' + '\033[0m'
    print()
    print(f'[{coloured_name_mage}]"Komm doch herein, dann können wir reden."\n'
          f'[{coloured_name_mage}]"Du willst vermutlich wissen, wie du aus dem Wald heraus kommst oder?\n'
          f'"Ja! Kannst du mir sagen wie?"\n'
          f'[{coloured_name_mage}]"Es ist im Grunde ganz einfach. Folge dem {coloured_whisper}"\n'
          f'"Was meinst du genau damit?\n'
          f'[{coloured_name_mage}]"Folge dem {coloured_whisper}. Mehr kann ich dir nicht sagen."\n'
          f'Du schaust ihn bisschen verwundert an. Schließlich verabschiedest du dich un gehst wieder hinaus.')
    global whisper
    whisper = True
    black_tower()


# Noch tiefer in den Wald
def deeper_in_the_forest():
    print()
    print(
        f'"Dort vorne ist ein Licht. Es sieht aus wie das eines Lagerfeuer welches im {coloured_south} brennt.\n'
        f'Dort ist doch bestimmt irgend jemand."\n'
        f'"Allerdings könnte ich auch diesem Weg in den {coloured_east} folgen. Vielleicht bringt der mich an einen interessanten Ort."\n'
        f'"An beiden Orten könnte es gefährlich sein. Sollte ich wieder zurück in den {coloured_west} gehen?')
    answer = input('> ')
    match answer:
        case "Süden":
            print()
            print('"Ich will lieber in Richtung des Lagerfeuers gehen."')
            print()
            campfire()
        case "Osten":
            print()
            print('"Hoffentlich bringt mich das Licht zu einem schöneren Ort, als diesen dunklen Wald')
            clearing()
        case "Westen":
            print()
            print('"Ich gehe erst einmal wieder etwas aus dem Wald heraus."')
            forest()
        case _:
            print()
            print(coloured_wrong_answer)
            deeper_in_the_forest()


# Das Lagerfeuer
def campfire():
    coloured_tolloni = '\033[36m' + 'Tonolli' + '\033[0m'
    coloured_jakobus = '\033[36m' + 'Jakobus' + '\033[0m'
    print('-----Das Lagerfeuer-----')
    print('Du hörst, wie sich zwei eingeborene unterhalten\n'
          f'[{coloured_jakobus}]"Uns geht so langsam das Essen aus."\n'
          f'[{coloured_tolloni}]"Jaja. Ähm was hast du gerade gesagt?"\n'
          f'[{coloured_jakobus}]"Hör doch wenigstens ein mal zu. UNS GEHT DAS ESSEN AUS!"\n'
          f'[{coloured_tolloni}]"Dann müssen wir sofort neues beschaffen!"\n'
          f'[{coloured_tolloni}]"Sieh nur da ist jemand"\n'
          f'"Hallo. Könntet ihr mir helfen, aus dem Wald heraus zu kommen?\n'
          f'Die beiden sehen sich ein paar Sekunden an und nicken dann.\n'
          f'[{coloured_jakobus}]"Wir können dir helfen. Aber wir wollen vorher neues Essen besorgen."\n'
          f'[{coloured_tolloni}]"Ja. Genau. Wenn du mit in den Osten kommst, dann helfen wir dir"\n'
          f'Willst du ihnen vertrauen und mit in den {coloured_east} gehen oder lieber nicht und\n'
          f'weiter auf dem Weg in den {coloured_south} gehen.')
    answer = input('> ')
    match answer:
        case "Osten":
            print()
            print('"OK. Ich helfe euch etwas zu Essen zu besorgen."\n'
                  'Du gehst etwas näher an sie heran.\n'
                  f'[{coloured_jakobus}]"Ich glaube, du hast da etwas miss verstanden."\n'
                  f'[{coloured_tolloni}]"Ja. Du BIST das Essen."\n'
                  f'Plötzlich stürzen sich beide auf dich und fesseln dich. Gegen einen hättest du dich vielleicht\n'
                  f'wehren können, aber gegen beide hast du keine Chance. Nun machen sie ein Feuer an und drehen dich auf einem Stock\n'
                  f'über dem Feuer bis sie dich schließlich essen können.')
            death()
        case "Süden":
            print()
            print('"Ich habe gerade leider keine Zeit dafür. Vielleicht komme ich später noch mal um euch zu helfen."\n'
                  'Du folgst dem weg und bist froh, dich wieder von ihnen zu entfernen als du auf einmal einen Schwarzen Turm siehst.')
            black_tower()
        case _:
            print()
            print(coloured_wrong_answer)
            campfire()


# Die Lichtung
def clearing():
    coloured_name_whisper = '\033[33m' + 'Flüstern' + '\033[0m'
    print()
    print('-----Die Lichtung-----')
    print(
        f'Als du bei der Lichtung ankommst, hörst du plötzlich ein leises Flüstern. Dabei fühlst du dich ein bisschen wie hypnotisiert. \n'
        f'Ob du wieder zurück in den {coloured_west} gehen solltest?\n'
        f'[{coloured_name_whisper}]"Folge mir in den {coloured_south}"')
    answer = input('> ')
    match answer:
        case "Westen":
            print()
            print('Du widersetzt dich der Stimme und gehst wieder zurück.')
            deeper_in_the_forest()
        case "Süden":
            print()
            print('Du folgst der Stimme und sie bringt dich an einen neuen Ort.')
            cliff()
        case _:
            print()
            print(coloured_wrong_answer)
            clearing()


def cliff():
    global whisper
    coloured_name_whisper = '\033[33m' + 'Flüstern' + '\033[0m'
    print()
    print('-----Die Klippe-----')
    print(f'[{coloured_name_whisper}]"Vertraue mir und springe die Klippe im {coloured_east} hinunter."\n'
          f'Solltest du dich ihr weigern und in den {coloured_south} gehen?')
    answer = input('> ')
    match answer:
        case "Osten":
            print('"Ich hoffe, es stimmt."\n'
                  'Du folgst dem flüstern und stürzt dich die Klippe hinunter.')
            if not whisper:
                print('Du fühlst dich bei dem Fall so frei, dass du für einen Augenblick alle deine Sorgen vergisst,\n'
                      'bis du schließlich auf den Steinen im Wasser unter dir aufprallst und augenblicklich stirbst.')
                death()
            elif whisper:
                print('Du fühlst dich bei dem Fall so frei, dass du für einen Augenblick alle deine Sorgen vergisst,\n'
                      '"Was passiert jetzt? Ich werde Sterben!" Kurz bevor du auf den Steinen aufkommst wirst du ohnmächtig.')
                back_at_home()
            else:
                print()
                print(coloured_wrong_answer)
                cliff()
        case "Süden":
            random_number = random.randrange(2)
            if random_number == 0:
                print()
                print(
                    'Nachdem du dich widersetzt hast, weißt du nicht mehr wo du bist und\n'
                    'irrst ziellos im Wald umher bis du schließlich verdurstest.')
                death()
            elif random_number == 1:
                print()
                print(
                    'Nachdem du dich widersetzt hast, weißt du nicht mehr wo du bist und irrst ziellos im Wald umher. Plötzlich siehst du\n'
                    'am Horizont den einen Schwarzen Turm und läufst zu ihm.')
                black_tower()
            else:
                print()
                print('Es ist ein Fehler aufgetreten!')
                cliff()
        case _:
            print()
            print(coloured_wrong_answer)
            cliff()


# Der Tod
def death():
    coloured_death = '\033[91m' + 'Du bist gestorben.' + '\033[0m'
    print()
    print(f'{coloured_death}\n'
          f'\n'
          f'Willst du es erneut versuchen? (ja)')
    answer = input('> ')
    if answer == 'ja':
        the_awakening()
    else:
        quit()


# wieder zu Hause
def back_at_home():
    print('"Als du wieder zu dir kommst, bist du wieder an der Stelle, an welcher du das erste mal\n'
          'ohnmächtig geworden bist. Du läufst so schnell wie möglich nach Hause und denkst erst\n'
          'dort darüber nach, was eigentlich passiert ist.\n'
          '"War das alles nur ein Traum? Aber dafür hat es sich zu real angefühlt."\n'
          '"Was auch immer es war, ich bin froh das es vorbei ist".')
    you_win()


def you_win():
    print()
    print('-----Du Bist Entkommen-----')
    input('Zum Beenden irgendeine Taste drücken:')
    quit()


def main():
    first_choice()


if __name__ == '__main__':
    main()

import random

# Farbige Schrift
coloured_wrong_answer = '\033[93m' + 'Dies ist keine gültige Eingabe.' + '\033[0m'
coloured_further = '\033[94m' + 'weiter' + '\033[0m'
coloured_hut = '\033[94m' + 'Hütte' + '\033[0m'
coloured_forest = '\033[94m' + 'tiefer in den Wald' + '\033[0m'
coloured_explore_forest = '\033[94m' + 'den Wald erkunden' + '\033[0m'
coloured_yes = '\033[94m' + 'Ja' + '\033[0m'
coloured_no = '\033[94m' + 'Nein' + '\033[0m'
coloured_kill = '\033[94m' + 'töten' + '\033[0m'
coloured_run = '\033[94m' + 'läufst' + '\033[0m'
coloured_cave = '\033[94m' + 'Höhle' + '\033[0m'
coloured_back = '\033[94m' + 'zurückgehen' + '\033[0m'
coloured_name_mage = '\033[95m' + 'Odiwandius' + '\033[0m'

# Himmelsrichtungen
coloured_north = '\033[94m' + 'Norden' + '\033[0m'
coloured_west = '\033[94m' + 'Westen' + '\033[0m'
coloured_south = '\033[94m' + 'Süden' + '\033[0m'
coloured_east = '\033[94m' + 'Osten' + '\033[0m'

# Einleitung
print('-----Der düstere Wald-----\nDies ist eine textbasiertes Adventure Game\n'
      f'Vorab noch eine Info: Es werden alle Möglichkeiten, welche zur Verfügung stehen immer\n'
      f'beschrieben und das Wort, welches man zum auswählen verwendet immer in blauer Schrift dargestellt.\n'
      f'Ansonsten viel Spaß\n'
      f'')
name = input('Als erstes gib doch bitte deinen Namen ein: ')
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
    if answer == 'Norden':
        print('Du hast dich dazu entschieden, nach Hause zu gehen\n'
              'Auf dem Weg nach Hause wird dir noch schlechter und du fällst in Ohnmacht.')
        the_awakening()
    elif answer == 'Osten':
        print('Du gehst weiter und denkst dir nichts weiter dabei.')
        print('Plötzlich gehts es dir schlechter und du fällst in Ohnmacht.')
        the_awakening()
    else:
        print(coloured_wrong_answer)
        print()
        first_choice()


# Der große Baum
def the_big_tree():
    print()
    print('-----Der große Baum-----')
    print(f'"Entweder ich gehe zur Hütte im {coloured_west} oder nach {coloured_east} in den Wald hinein. Etwas anderes bleibt mir nicht."')
    answer = input('> ')
    if answer == 'Westen':
        hut()
    elif answer == 'Osten':
        print()
        print(f'"Ich will tiefer in den Wald gehen!" sagte {coloured_name} entschlossen und ging los.')
        forest()
    else:
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
    input('Bitte irgend eine Taste eingeben:')
    the_big_tree()


# Die Hütte
def hut():
    coloured_enter = '\033[94m' + 'versuchen hinein' + '\033[0m'
    coloured_look_from_outside = '\033[94m' + 'außen anschauen' + '\033[0m'
    print()
    print('-----Die Hütte-----')
    print(f'"Hmmm die Hütte scheint nur einen Eingang zu haben. Eine Tür auf der Vorderseite."\n'
          f'"Vielleicht sollte ich {coloured_enter} zu gehen?"\n'
          f'"Allerdings könnte ich sie mir erst einmal von {coloured_look_from_outside} oder wieder\n'
          f'zurück zum großen Baum im {coloured_east} gehen."')
    answer = input('> ')
    if answer == 'versuchen hinein':
        print()
        print('Du trittst an die Türe heran.\n"Ich versuche mal sie zu öffnen"')
        print()
        if key:
            print('"Ich habe sie mit diesem Schlüssel den ich gefunden habe aufgesperrt."\n'
                  '"Ich hoffe die Mühe hat sich gelohnt."')
            inside_hut()
        else:
            print('"Ich bekomme sie nicht auf. Vermutlich brauche ich einen Schlüssel. Wo bekomme ich nur einen her?"\n'
                  '"Am besten gehe Ich zurück"')
            print(input('Zum zurückgehen beliebige Taste eingeben:'))
            print(f'{coloured_name} geht zurück zu dem Ort an dem er aufgewacht ist')
            the_big_tree()
    elif answer == 'außen anschauen':
        print()
        print('"Ich glaube, dass ich mir diese Hütte erst einmal von außen anschauen werde."\n'
              'Du gehst um die Hütte herum und entdeckst etwas furchtbares.\n'
              'Du gerätst in Panik und schreist laut auf!\n'
              '"Ein Monster!!!"\n'
              'Vor dir steht ein Monster, welches über 10 Meter groß ist.\n'
              'Es hat Zähne, mit denen es dich im nu verspeisen könnte.\n'
              'Durch deinen Schrei ist es aufmerksam auf dich geworden und kommt auf dich zu!')
        the_monster()
    elif answer == 'Osten':
        print()
        print('"Ich gehe wohl lieber zurück"')
        the_big_tree()
    else:
        print()
        print(coloured_wrong_answer)
        hut()


# In der Hütte
def inside_hut():
    coloured_bedroom = '\033[94m' + 'Schlafzimmer' + '\033[0m'
    coloured_kitchen = '\033[94m' + 'Küche' + '\033[0m'
    coloured_bathroom = '\033[94m' + 'Badezimmer' + '\033[0m'
    print(f'{coloured_name} geht in die Hütte. Es gibt dort nur drei Räume.\n'
          f'Ein {coloured_bedroom}, eine {coloured_kitchen} und ein {coloured_bathroom}. "Wohin soll ich nur gehen?"\n'
          f'"Ich könnte auch {coloured_back}')
    answer = input('> ')
    if answer == 'Schlafzimmer':
        print()
        print(f'"Bis auf einem Teppich und ein Bett ist der Raum vollkommen leer."\n'
              f'"Beim Bett konnte ich nichts finden, was irgend eine Bedeutung haben könnte"\n'
              f'"Mal sehen, ob es beim Teppich etwas zu finden gibt"\n'
              f'{coloured_name} findet auf den ersten blick nichts, doch als er gehen wollte rutschte der Teppich etwas\n'
              f'zur seite und {coloured_name} sah einen kleinen Spalt im Boden.\n'
              f'"Unter dem Teppich befindet sich eine Luke"\n'
              f'Als {coloured_name} die Luke öffnet, ist dort nur ein Loch nach unten. Doch plötzlich kommen dort Stufen aus der Wand gefahren\n'
              f'"Soll ich nach unten gehen?" ({coloured_yes} oder {coloured_back})')
        answer = input('> ')
        if answer == 'Ja':
            print()
            print(f'"Ich gehe wohl nach unten"\n'
                  f'{coloured_name} wagt sich die Stufen hinunter ins ungewisse')
            get_spellbook()
        elif answer == 'zurückgehen':
            print()
            print('"Ich gehe besser wider zurück. Wer weiß schließlich schon, was dort unten auf mich wartet"')
            inside_hut()
        else:
            print()
        print(coloured_wrong_answer)
        inside_hut()
    elif answer == 'Küche':
        print()
        print('"In der Küche steht ein Tisch auf welchem noch Essen steht. Es ist bestimmt schon seit"\n'
              '"Monaten hier. Zu mindestens schließe ich das aus den Kleintieren die darauf sind."\n'
              '"Wer auch immer hier wohnte muss wohl sehr überstürzt aufbrechen."\n'
              '"Sonst gibt es hier nichts, was mich noch interessieren könnte."')
        inside_hut()
    elif answer == 'Badezimmer':
        print()
        print(
            '"Da steht eine Toilette, welche bestimmt seit Monaten nicht mehr sauber gemacht wurde."\n''"Ansonsten kann ich nichts weiter hier finden."')
        inside_hut()
    elif answer == 'zurückgehen':
        print()
        print('"Ich gehe wohl lieber zurück"')
        hut()
    else:
        print()
        print(coloured_wrong_answer)
        inside_hut()


# Das Zauberbuch
def get_spellbook():
    global spellbook
    coloured_take_along = '\033[94m' + 'mitnehmen' + '\033[0m'
    coloured_leave_there = '\033[94m' + 'dalassen' + '\033[0m'
    print(f'Am ender der Stufen geht {coloured_name} um eine Ecke.')
    if not spellbook:
        print(f'"Ein geheimer Raum in dessen Mitte ein Podest mir einem merkwürdigen Buch steht"\n'
              f'"Es ist in einer Sprache verfasst, die ich noch nie zuvor gesehen habe"\n'
              f'"Ich kann es {coloured_take_along} oder {coloured_leave_there}."')
        answer = input('> ')
        if answer == 'mitnehmen':
            print()
            print('Du steckst das Buch unter deine Jacke und verlässt die Hütte')
            spellbook = True
            print('"Dann gehe ich wohl besser wieder aus der Hütte heraus."')
            hut()
        elif answer == 'dalassen':
            print()
            print('"Dann gehe ich wohl besser wieder aus der Hütte heraus."')
            hut()
        else:
            print()
            print(coloured_wrong_answer)
            inside_hut()
    elif spellbook:
        print('"Was soll ich hier unten denn noch? Ich glaube dass ich hier nichts mehr finden werde."\n'
              '"Am besten kehre gehe ich wieder aus dem Haus heraus."')
        hut()


# Das Monster
def the_monster():
    print(f'Entweder du versuchst es zu {coloured_kill} oder du {coloured_run} um dein Leben')
    answer = input('> ')
    if answer == 'töten':
        print()
        print(f'"Ich habe keine Angst vor dir!" Du stürzt dich auf das Monster.\n'
              f'Doch der Kampf ist nur von kurzer dauer. Du wirst von dem Monster gegriffen\n'
              'und mit seinen Händen in der hälfte auseinander gerissen!')
        death()
    elif answer == 'läufst':
        random_number = random.randrange(2)
        if random_number == 0:
            print()
            print('Du fängst an so schnell wie möglich zu laufen, doch das Monster folgt dir und kommt immer näher.\n'
                  'Du läufst durch den Wald und plötzlich wirst du von etwas in die Luft gehoben.\n'
                  '"AAAHHHH" schreist du und das letzte was du siehst sind die riesigen Zähne des Monsters, welche dir\n'
                  'mit einem Bissen den Kopf von deinen Schultern trennen.')
            death()
        elif random_number == 1:
            print()
            print('Du fängst an so schnell wie möglich zu laufen, doch das Monster folgt dir und kommt immer näher.\n'
                  'Du läufst durch den Wald und plötzlich hörst du nichts mehr hinter dir. Als du stehen bleibst,\n'
                  'ist das Monster verschwunden. Nun siehst du dich um.')
            deeper_in_the_forest()
        else:
            print()
        print(coloured_wrong_answer)
        the_monster()
    else:
        print()
        print(coloured_wrong_answer)
        the_monster()


# Der Wald
def forest():
    print()
    print('-----Der Wald-----')
    print(f'Plötzlich entdeckst du etwas. "Dort vorne ist eine Höhle. Was sie wohl verbergen mag?"\n'
          f'"Entweder Ich gehe in die Nach {coloured_south} in die Höhle oder tiefer in den Wald im {coloured_east} gehen."\n'
          f'Vielleicht lohnt es sich auch, wieder zurück zum großen Baum im {coloured_west} zu gehen."')
    answer = input('> ')
    if answer == 'Süden':
        print()
        print('"Auf in die Höhle! Was soll den schon passieren?"')
        cave()
    elif answer == 'Osten':
        print()
        print('"Auf geht es. Immer tiefer in den Wald hinein!"')
        deeper_in_the_forest()
    elif answer == 'Westen':
        print()
        print('"Ich gehe wohl besser wieder etwas aus dem Wald heraus"')
        the_big_tree()
    else:
        print()
        print(coloured_wrong_answer)
        forest()


# Die Höhle
def cave():
    global behind_the_cave
    coloured_sneak = '\033[94m' + 'vorbei schleichen' + '\033[0m'
    coloured_runs = '\033[94m' + 'laufe' + '\033[0m'
    coloured_running = '\033[94m' + 'laufen' + '\033[0m'
    print()
    print('-----Die Höhle-----')
    if not behind_the_cave:
        print(f'"Ohhh nein" flüsterst du. "Da vorne liegt ein Bär. Anscheinend schläft er."\n'
              f'Du überlegst dir, wie du an ihm vorbei kommen sollst und denkst dir: "Soll ich einfach wieder in richtung {coloured_north} aus der Höhle heraus?\n'
              f'Aber vielleicht kann ich mich auch an ihm {coloured_sneak}, oder ich {coloured_runs} einfach zur anderen seite der Höhle und hoffe,\n'
              f'dass ich schnell genug bin und dort ankomme, bevor er mich tötet."')
        answer = input('> ')
        if answer == 'vorbei schleichen':
            print()
            print(
                f'{coloured_name} versucht sich an dem Bären vorbei zu schleichen. Sollte {coloured_name} nur einen falschen schritt machen, könnte es den Bären aufwecken\n'
                f'{coloured_name} stolpert und fällt hin. "Aaaaahhhh!!!" Durch diesen lauten Schrei wacht der Bär auf und fängt an auf dich zu zu laufen. ({coloured_running} oder {coloured_kill})')
            answer = input('> ')
            if answer == 'laufen':
                print()
                print(
                    f'{coloured_name} lauft los. Der Bär wacht durch die vielen lauten geräusche auf. Bis er aufsteht bist fast auf der anderen Seite der Höhle angekommen\n'
                    f'Nun läuft der Bär los, doch du kannst dich im letzten Moment einen vorsprung erklimmen und dich so vor dem Bären in sicherheit bringen.\n'
                    f'"Das war aber knapp!" Du legst dich auf den Boden und atmest tief durch. Dann gehst du weiter durch die Höhle.')
                behind_the_cave = True
                mountain_of_corpses()
            if answer == 'töten':
                print()
                print(
                    'Du stürzt dich auf den Bären voller Hoffnung, ihn töten zu können. Der Bär stürzt sich auf dich und du fällst um. Er zerfleischt dein Bein, während du\n'
                    'nur schreiend am boden liegst. Dann Macht er das gleiche, was er zuvor mit deinem Bein gemacht hat auf mit allen anderen Körperteilen.')
                death()
        elif answer == 'laufe':
            print()
            print(
                f'{coloured_name} lauft los. Der Bär wacht durch die vielen lauten geräusche auf. Bis er aufsteht bist fast auf der anderen Seite der Höhle angekommen\n'
                f'Nun läuft der Bär los, doch du kannst dich im letzten Moment einen vorsprung erklimmen und dich so vor dem Bären in sicherheit bringen.\n'
                f'"Das war aber knapp!" Du legst dich auf den Boden und atmest tief durch. Dann gehst du weiter durch die Höhle.')
            behind_the_cave = True
            mountain_of_corpses()
        elif answer == 'Norden':
            print()
            print('"Ich glaube, das beides keine gute Idee wäre und kehre deshalb lieber wieder um".')
            forest()
        else:
            print()
            print(coloured_wrong_answer)
            cave()
    elif behind_the_cave:
        print('"Der Bär ist wohl weg gegangen. Ich kann die Höhle ganz einfach durchqueren."')
        mountain_of_corpses()


# Der Leichenberg
def mountain_of_corpses():
    global key
    if not key:
        print()
        print(f'Plötzlich bleibst du stehen. "Dort ist ein Berg von Leichen. Am besten gehe ich einfach weiter."\n'
              f'Doch als du gerade los gehen wolltest fällt dir etwas auf.\n'
              f'Mitten in den Leichen siehst du etwas glänzen. Willst du es holen? {coloured_yes} oder {coloured_no}')
        answer = input('> ')
        if answer == 'Ja':
            print()
            print('Du greifst zwischen die Leichen hinein und versuchst das was dort glänzt zu bekommen.\n'
                  '"Das ist so ekelhaft." Schließlich erreichst du das Objekt mit deinen Fingern und kannst es heraus ziehen.\n'
                  '"Es ist ein Schlüssel! Was der nur aufsperren kann? Nun gehe ich aber auf schnellstem Wege aus dieser scheiß Höhle!"\n'
                  'als du die Höhle verlässt stehst du auf einmal im Schatten eines riesigen schwarzen Turmes.')
            key = True
            black_tower()
        elif answer == 'Nein':
            print()
            print('"Was auch immer es ist, es ist es mir nicht wert dort hinein zu greifen. Raus aus dieser Höhle"\n'
                  'als du die Höhle verlässt stehst du auf einmal im Schatten eines riesigen schwarzen Turmes.')
            black_tower()
        else:
            print()
            print(coloured_wrong_answer)
            mountain_of_corpses()
    elif key:
        print('"Dort ist wieder der Berg von Leichen. Am besten gehe ich einfach weiter."')
        black_tower()


# Der Schwarze Turm
def black_tower():
    coloured_jump = '\033[94m' + 'springen' + '\033[0m'
    coloured_spellbook = '\033[4m' + 'Zauberbuch' + '\033[0m'
    print()
    print('-----Der Schwarze Turm-----')
    print('"Dort vorne ist ein riesiger schwarzer Turm. Was erwartet mich dort wohl schon wieder?"\n'
          f'"Vielleicht sollte ich nicht nach {coloured_west} zum Turm gehen. Ich könnte auch dort vorne den Pfad im {coloured_north} nehmen."')
    answer = input('> ')
    if answer == 'Westen':
        print()
        print(
            f'"Mal sehen, was es bei dem gruseligen, dunklen, furchteinflößenden, unheimlichen ... Ach ich denke einfach nicht mehr daran. Auf zum Turm!"\n'
            f'Du gehst zur Vorderseite des Turmes und findest eine Tür. "Vielleicht ist dort ja jemand drinnen der mich versklavt, oder noch schlimmeres mit mir tut."\n'
            f'Als du dich dazu überwinden konntest daran zu klopfen geht die Tür einen Spalt auf.')
        print(
            f'[{coloured_name_mage}] "Ich bin der Zauberer Odiwandius. Was haben Sie hier an meinem heiligen Ort zu suchen?')
        print(
            '"Ich will nur einen Weg nach Hause finden. Kannst du mir vielleicht helfen, aus diesem Wald heraus zu kommen?')
        print(
            f'[{coloured_name_mage}] "Natürlich kenne ich den Weg aus dem Wald. Das erzähle ich jedoch nicht jeder dahergelaufenen Gestalt, welche an meine Tür klopft.\n'
            f'"Dafür musst du schon beweisen, dass du es auch wert bist.')
        input('Bitte irgend eine Taste eingeben: ')
        if whisper:
            inside_black_tower()
        elif not spellbook:
            print()
            print('"Wie soll ich das anstellen?"')
            print(
                f'[{coloured_name_mage}] "Wenn du mir mein {coloured_spellbook} zurückbringst, dann würde ich dir das Geheimnis des waldes verraten und auch, wie du ihn verlassen kannst.')
            print('"OK. Ich bringe dir dein Zauberbuch."\n'
                  'Der Zauberer schließt die Tür, ohne auch nur ein weiteres Wort zu sagen und du gehst wieder weiter weg vom Turm')
            black_tower()
        elif spellbook:
            print()
            print(f'[{coloured_name_mage}] "Ooohhh. Ich spüre die Anwesenheit meines {coloured_spellbook}."\n'
                  f'Er öffnet die Tür, reißt dir das Buch aus den Händen und verschließt die Tür wieder.\n'
                  f'als du schon wieder weg gehen wolltest, geht dir Tür wieder auf\n'
                  f'[{coloured_name_mage}] "Danke dass du mir mein Buch zurück gebracht hast."')
            inside_black_tower()
    elif answer == 'Norden':
        print()
        print(
            f'{coloured_name} macht sich auf den Weg, durch den Wald zu gehen. Auf einmal kommt eine kleine Klippe. "Ich kann dort hinunter {coloured_jump},\n'
            f'aber ich komme dann nicht mehr {coloured_back}."')
        answer = input('> ')
        if answer == 'springen':
            print()
            print(
                'Du springst die Klippe hinunter. Dann gehst du noch ein paar schritte nur um festzustellen, dass du an diesem Ort schon einmal warst\n'
                '"Ich binn wieder vor der Höhle"')
            forest()
        elif answer == 'zurück':
            print()
            print('"Ich will lieber wieder zurück zum Turm gehen".')
            black_tower()
        else:
            print()
            print(coloured_wrong_answer)
            black_tower()
    else:
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
          f'[{coloured_name_mage}]"Es ist im grunde ganz einfach. Folge dem {coloured_whisper}"\n'
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
        f'"Dort vorne ist ein Licht. Es sieht aus wie das eines Lagerfeuer welches im {coloured_south} brennt. Dort ist doch bestimmt irgend jemand."\n'
        f'"Allerdings könnte ich auch diesem Weg in den {coloured_east} folgen. Vielleicht bringt der mich an einen interessanten Ort."\n'
        f'"An beiden Orten könnte es gefährlich sein. Sollte ich wieder zurück in den {coloured_west} gehen?')
    answer = input('> ')
    if answer == 'Süden':
        print()
        print('"Ich will lieber in Richtung des Lagerfeuers gehen."')
        print()
        campfire()
    elif answer == 'Osten':
        print()
        print('"Hoffentlich bringt mich das Licht zu einem schöneren Ort, als diesen dunklen Wald')
        clearing()
    elif answer == 'Westen':
        print()
        print('"Ich gehe erst einmal wieder etwas aus dem Wald heraus."')
        forest()
    else:
        print()
        print(coloured_wrong_answer)
        deeper_in_the_forest()


# Das Lagerfeuer
def campfire():
    coloured_tolloni = '\033[36m' + 'Tonolli' + '\033[0m'
    coloured_jakobus = '\033[36m' + 'Jakobus' + '\033[0m'
    coloured_trust = '\033[94m' + 'vertrauen' + '\033[0m'
    coloured_not = '\033[94m' + 'nicht' + '\033[0m'
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
          f'[{coloured_tolloni}]"Ja. Genau. Wenn du mit kommst, dann helfen wir dir"\n'
          f'Willst du ihnen {coloured_trust} oder lieber {coloured_not} und weiter auf dem Weg gehen.')
    answer = input('> ')
    if answer == 'vertrauen':
        print()
        print('"OK. Ich helfe euch etwas zu Essen zu besorgen."\n'
              'Du gehst etwas näher an sie heran.\n'
              f'[{coloured_jakobus}]"Ich glaube, du hast da etwas miss verstanden."\n'
              f'[{coloured_tolloni}]"Ja. Du BIST das Essen."\n'
              f'Plötzlich stürzen sich beide auf dich und fesseln dich. Gegen einen hättest du dich vielleicht\n'
              f'wehren können, aber gegen beide hast du keine Chance. Nun machen sie ein Feuer an und drehen dich auf einem Stock\n'
              f'über dem Feuer bis sie dich schließlich essen können.')
        death()
    elif answer == 'nicht':
        print()
        print('"Ich habe gerade leider keine Zeit dafür. Vielleicht komme ich später noch mal um euch zu helfen."\n'
              'Du folgst dem weg und bist froh, dich wieder von ihnen zu entfernen als du auf einmal einen Schwarzen Turm siehst.')
        black_tower()
    else:
        print()
        print(coloured_wrong_answer)
        campfire()


# Die Lichtung
def clearing():
    coloured_name_whisper = '\033[33m' + 'Flüstern' + '\033[0m'
    print()
    print('-----Die Lichtung-----')
    print(
        f'Als du bei der Lichtung ankommst hörst du plötzlich ein leises Flüstern. Dabei fühlst du dich ein bisschen wie hypnotisiert. \n'
        f'Ob du wieder zurück in den {coloured_west} gehen solltest?\n'
        f'[{coloured_name_whisper}]"Folge mir in den {coloured_south}"')
    answer = input('> ')
    if answer == 'Westen':
        print()
        print('Du widersetzt dich der Stimme und gehst wieder zurück.')
        deeper_in_the_forest()
    elif answer == 'Süden':
        print()
        print('Du folgst der Stimme und sie bringt dich an einen neuen Ort.')
        cliff()
    else:
        print()
        print(coloured_wrong_answer)
        clearing()


def cliff():
    global whisper
    coloured_name_whisper = '\033[33m' + 'Flüstern' + '\033[0m'
    coloured_jump = '\033[94m' + 'spring' + '\033[0m'
    coloured_oppose = '\033[94m' + 'widersetzen' + '\033[0m'
    print()
    print('-----Die Klippe-----')
    print(f'[{coloured_name_whisper}]"Vertraue mir und {coloured_jump}."\n'
          f'Solltest du dich ihr {coloured_oppose}?')
    answer = input('> ')
    if answer == 'spring':
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
    elif answer == 'widersetzen':
        random_number = random.randrange(2)
        if random_number == 0:
            print()
            print(
                'Nachdem du dich widersetzt hast weist du nicht mehr wo du bist und irrst ziellos im Wald umher bis du schließlich verdurstest.')
            death()
        elif random_number == 1:
            print()
            print(
                'Nachdem du dich widersetzt hast weist du nicht mehr wo du bist und irrst ziellos im Wald umher. Plötzlich siehst du\n'
                'am horizont den einen Schwarzen Turm und läufst zu ihm.')
            black_tower()
        else:
            print()
            print('Es ist ein Fehler aufgetreten')
            cliff()
    else:
        print()
        print(coloured_wrong_answer)
        cliff()


# Der Tod
def death():
    coloured_death = '\033[91m' + 'Du bist gestorben.' + '\033[0m'
    print()
    print(f'{coloured_death}\n'
          f'\n'
          f'willst du es erneut versuchen? (ja)')
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

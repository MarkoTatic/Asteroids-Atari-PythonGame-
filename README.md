# Asteroids-Atari-Python-Game-
University project [Faculty of Technical Sciences, Novi Sad]

Python
Interpreterski jezik, visoke apstrakcije i opšte namene.
Koristi se CPython implementacija – piton kod se kompajlira a potom izvršava u virtuelnoj mašini.
Nema deklarisanja varijabli, one su dinamički alocirane.
Hip (garbage collection) je automatski.
Snažno tipiziran jezik (strongly typed), konverzija iz tipa u tip nije automatska.
Razlikuje mala i velika slova.
Objektno orijentisan, sve je objekat.
Nema karaktera za kraj naredbe, ne stavlja se ‘;’ na kraju naredbe.
Blokovi naredbi se definišu nazubljivanjem.

PyQt
Biblioteka koja uvezuje Qt razvojni okvir, koji podržvava više platformi, uključujući Windows, OS X, Linux, iOS i Android.
Qt je pisan u C++ jeziku, isto kao i Piton interpreter, što omogućuje njegovo direktrno korišćenje ili korišćenje putem biblioteka koje ga enkapsuliraju u piton jezik. Na sličan način se i druge C/C++ biblioteke mogu koristiti u piton aplikacijama.

Asteroids
Je igra koja je pisana u python programskom jeziku uz upotrebu PyQt biblioteke.
Igrica u svom pocetnom prozoru ima ima tri dugmeta koja su ‘New Game’, ‘About game’ i ‘Exit’ koja otvaraju novi prozor za obabir vrste igre, osnovne informacije I napustanje igre respektivno.
Posteoje cetiri rezima igre ‘Singleplayer’, ‘Multiplayer’, ‘Tournament’ i ‘Network’.
Rezim sigleplayer je samostalna igra, odnosno jedan igrac igra sve dok ne izgubi sve zivote.
Multiplayer je igra u dvoje I igra se dok oba igraca ne ostanu na 0 zivota I pobednik je onaj koji je unistio najvise asteroida.
Tournament rezim se igra u cetvoro, tj. dva polufinala I jedno finale, u finale ulaze igraci iz polufinala sa vecim osvojenim brojem bodova, u slucaju neresenog rezultata prolazi dalje igrac koji je duze izdrzao u igri.
Network je igra u cetvoro na 2 racunara na principu svako za sebe I igra se dok poslednji ne ostane bez zivota.
Povecanjem nivoa igre povecava se I broj asteroida I njihova brzina.
Igrac je ogranice na 10 metkova u okviru, tj. ne moze ispaljivati nove metkove dok stari ne napuste teren.
Postoje 3 velicine asteroida I unistavanjem se stvaraju dva manja asteroida.

# u Server.py sam dodao promenljivu level koja krece od 1 i na osnovu koje se generisu asteroidi u 
# game_scene.py

# treba da se obezbedi da se stalno proverava koji je ostalo asteroida u polju i kad dodje do nule
# da se poveca Server.level i da se ponovo pozove f-ja za generisanje asteroida, i da se ubrzava brzina kretanja asteroida + rakete

#RESENO# ako se izgubi u single player modu, treba da na klik exit dugmeta igrica kroz ugasi da ne ostane aktivna ~~~ stavljeno da thread bude daemon da bi se i on ugasio kada i main

# prenos Server.py preko neta, to se moramo naci da bi mogli da testiramo

#RESENO# pnije dobro odradjeno zatvaranje programa nakon kraja igre (samo se sakrije prozor)~~~ stavljeno da thread bude daemon da bi se i on ugasio kada i main

# takmicenje
# skriveni bonus
# treba napraviti da asteroidi idu veliki, srednji, mali i logika da se manji asteroidi stvore na mestu gde je unisten stari
# da asteroidi idu nekom konstantnom putanjom, da svaki klijent fakticki zna kuda idu asteroidi a ne da mora i to preko mreze da se salje(mada ovo mozemo srediti samo za mod preko mreze, a single i multiplayer da ostanu isti)
# napraviti da ima 4 * slike raketa pa za svakog playera druga boja i srediti skor da se pamti odvojeno
# broj metkova ograniciti na 20-30 da moze svaki igrac maximalno da ima ispaljeno u jednom trenutku (imam resenje za ovo iskucano pusujem sutra)
# treba srediti kretanje u multiplayeru, ima neki bugg da li sa queue ili sa metodama keyPresedEvent i keyReleasedEvent
# fixati velicine rakete, asteroida i metka, idalje se nekad desava da asteroid prodje kroz raketu a da je ne unisti i da metak prodje kroz asteroid a da ga ne unisti

# RAD

# Andrej:
    # dodacu labelu koja pokazu koji je trenutno level
    # i da se poveca nivo i broj asteroida za jedan

# Marko M
    # poradicu na bojama raketa za svakog igraca posebna
    # i velicini asteroida veliki/srednji/mali, radio sam nesto ali cim se tipa unisti veliki svi postaju srednji, tako sigurno ne treba xD
    
    # da bi znali konstantnu kretnju asteroida morali bi onda njihovu logiku kretanja da menjamo jer smo napravili 
    #   random kretnju, tako da videti ako moze da se salje tako ako ne onda menjamo

# Tatic:
    # ograniciti da svaki igrac moze da ima max 30 metkova u jednom trenutku aktivnih +
    # dodacu ono za dodatnu silu sto ima kao da bude da se pokupi zivot +
    # pokusacu na kopiji nekoj malo server-client da vidim kako funckionise
    # fixati kretanje space_shuttlova u multiplayeru
Marcin Szadkowski, 250091
#------------
Python >= 3.7
Sly >= .-4
python3-venv
#------------

Kompilacja:
$ make
zostaje stworzone środowisko wirtualne, a w nim poprzez poetry zainstalowane zależności
Następnie:
$ source .venv/bin/activate

#-------------
Uruchomienie:
$ python3 kompilator.py <nazwa pliku wejściowego> <nazwa pliku wyjściowego>


#-------------
Opis plików:
W pakiecie AST znajdują się klasy tworzące drzewo AST
w pakiecie compiler znajdują się pozostałe klasy odpowiedzialne za produkcję kodu wynikowego
plik kompilator.py jest głównym plikiem wykonywalnym
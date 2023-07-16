# ELECTION SCRAPER

Třetí projekt pro Engeto Python Akademii

## Popis projektu

Závěrečný projekt prověří tvé znalosti nejenom z posledních lekcí, ale z celého kurzu. Tvým úkolem bude vytvořit scraper výsledků voleb z roku 2017, který vytáhne data přímo z webu.

Napiš takový skript, který vybere jakýkoliv územní celek z tohoto odkazu: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ např. X u Benešov odkazuje sem: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101. Z tohoto odkazu chcete vyscrapovat výsledky hlasování pro všechny obce (resp. pomocí X ve sloupci Výběr okrsku).

## Použíté knihovny

Knihovny, které jsou potřeba pro funkci programu jsou obsažené v souboru requirements.txt. Z tohoto souboru se instalují za pomocí příkazu v příkazovém řádku: 
$ pip install -r requirements.txt 

## Spuštění projektu

Hlavní soubor projektu projekt_3.py se spouští z příkazového řádku a požaduje dva argumenty (odkaz uzemního celku ke scrapování a druhý název výstupního souboru CSV) a název hlavního souboru projektu viz níže.

obecny  příklad:
python projekt_3.py "odkaz_uzemniho_celku" "nazev_vystupni_soubor"

příklad pro Cheb:
python projekt_3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=5&xnumnuts=4101" "cheb.csv"

Výsledkem je .csv který obsahuje výsledky voleb pro danou oblast.
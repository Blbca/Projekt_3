'''

projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Petr Novák
email: peternovaksson@seznam.cz
discord: Goodchilde#1716

'''

import requests
import bs4
import sys
import csv 
 
def data(link):
    """Tato funkce vrací ve třídě BS HTML adresu ze zadaného argumentu."""
    odp_serveru = requests.get(link)
    html = bs4.BeautifulSoup(odp_serveru.text, "html.parser")
    print("Stále pracuji", link)
    return html
    
def obec_cislo() -> list:
    """Tato funkce vrací list čísel obcí v hledaném okresu"""
    cislo_obce= []
    vyhl_cisel = url_adresa.find_all("td", "cislo")
    for v in vyhl_cisel:
        cislo_obce.append(v.text)
    return cislo_obce

def obec_nazev() -> list:
    """Tato funkce vrací list obcí v hledaném okresu"""
    obce = []
    vyhl_obci = url_adresa.find_all("td", "overflow_name")
    for v in vyhl_obci:
        obce.append(v.text)
    return obce

def obec_odkaz() -> list:
    """Tato funkce vrací URL adresu, která je potřebná pro získání detailů o 
    jednotlivých obcí hledaném okresu"""
    odkaz = []
    detail_obce = url_adresa.find_all("td", "cislo", "href")
    for d in detail_obce:
        d = d.a["href"]
        odkaz.append(f"https://volby.cz/pls/ps2017nss/{d}")
    return odkaz

def obec_strany() -> list:
    """Tato funkce vrací list stran, které kandidují v dané obci"""
    strany = []
    mesto= obec_odkaz()
    odkaz = requests.get(mesto[0])
    odkaz_obce = bs4.BeautifulSoup(odkaz.text, "html.parser")
    strana = odkaz_obce.find_all("td", "overflow_name")
    for s in strana:
        strany.append(s.text)
    return strany

def registorvany() -> list:
    """Tato funkce ukladá do proměné celkový počet voličů, kteří jsou v jednotlivých
    obcích registrovaní voliči."""
    odkaz = obec_odkaz()
    registorovany_volic = []
    for o in odkaz:
        odkaz_html = requests.get(o)
        obec = bs4.BeautifulSoup(odkaz_html.text, "html.parser")
        registrovany = obec.find_all("td", headers="sa2")
        for r in registrovany:
            r = r.text
            registorovany_volic.append(r.replace('\xa0', ' '))
    return  registorovany_volic 

def zucastneny() -> list:
    """Tato funkce ukladá do proměné celkový počet voličů, kteří jsou v jednotlivých
    obcích zůčastnění voliči."""
    odkaz = obec_odkaz()
    zucasteny_volic = []
    for o in odkaz:
        odkaz_html = requests.get(o)
        obec = bs4.BeautifulSoup(odkaz_html.text, "html.parser")    
        zucastneny = obec.find_all("td", headers="sa3")
        for z in zucastneny:
            z = z.text
            zucasteny_volic.append(z.replace('\xa0', ' '))
    return zucasteny_volic
    
def platny() -> list:
    """Tato funkce ukladá do proměné celkový počet voličů, kteří jsou v jednotlivých
    obcích platní voliči."""
    odkaz = obec_odkaz()
    platny_volic = []
    for o in odkaz:
        odkaz_html = requests.get(o)
        obec = bs4.BeautifulSoup(odkaz_html.text, "html.parser")     
        platny = obec.find_all("td", headers="sa6")
        for p in platny:
            p = p.text
            platny_volic.append(p.replace('\xa0', ' '))
    return platny_volic    

def strany_hlasy() -> list:
    """Tato funkce vrací list, který udáva zisk politických stran
    pro každou obec."""
    odkaz = obec_odkaz()
    hlasy = []
    for o in odkaz:
        list = []
        obec = data(o)
        hlas = obec.find_all("td", "cislo", headers=["t1sb3", "t2sb3"])
        for h in hlas:
            list.append(h.text)
        hlasy.append(list)
    return hlasy

def pomocna_fce() -> list:
    """Tato funkce slouží pro vytvoření 'list listů', kde jsou sloučeny hledané informmace
    jako číslo obce, název obce, registrovaní voliči, zúčastnění voliči, platní voliči a
    procentuální výsledky kandidujících stran."""
    slouceni = []
    cislo = obec_cislo()
    obec = obec_nazev()
    registorovaný_volic = registorvany()
    zucasteny_volic = zucastneny()
    platny_volic = platny()
    hlasy_celk = strany_hlasy()
    zip_1 = zip(cislo, obec, registorovaný_volic, zucasteny_volic, platny_volic )
    pomocny_list = []
    for c, o, r, z, p in zip_1:
        pomocny_list.append([c, o, r, z, p])
    zip_2 = zip(pomocny_list, hlasy_celk)
    for pl, pr in zip_2:
        slouceni.append(pl + pr)
    return slouceni

def election2017(link, soubor) -> None:
    """Tato funkce vytváří finální CSV soubor s daty."""
    try:
        nadpisy = ['Číslo obce', 'Název obce', 'Voliči v seznamu', 'Vydané obálky', 'Platné hlasy']
        hlavni_data = pomocna_fce()
        strany = obec_strany()
        print("Data jsou uložena v:", soubor)
        for s in strany:
            nadpisy.append(s)
        with open(soubor, 'w', newline='') as f:
            f_writer = csv.writer(f)
            f_writer.writerow(nadpisy)
            f_writer.writerows(hlavni_data)
        print("Konec souboru:", sys.argv[0])
    except IndexError:
        print("Došlo k chybě")
        quit()

if __name__ == '__main__' and len(sys.argv) == 3:
    url_adresa = data(sys.argv[1]) 
    adresa = sys.argv[1]
    nazev_souboru = sys.argv[2]
    election2017(adresa, nazev_souboru)
else:
    print('Zadal jste špatný počet argumentů.')
    quit()    

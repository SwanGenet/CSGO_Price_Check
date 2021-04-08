from tkinter import *
import requests
import json

import requests
import json 
from tkinter import *


def print_price(arme,skin,nom):

    tab_qualite = ['Factory%20New','Minimal%20Wear','Field-Tested','Well-Worn','Battle-Scarred']

    print('\n====================')
    print(nom + ' - ' + skin)
    print('====================\n')

    i = 0
    while i < len(tab_qualite) :

        result = requests.get('https://steamcommunity.com/market/priceoverview/?country=FR&currency=1&appid=730&market_hash_name='+ arme +'%20%7C%20'+ skin +'%20%28'+ tab_qualite[i] +'%29')
        dico_result = result.json()

        if 'lowest_price' not in dico_result.keys():
            print("Qualité non disponible.")

        else :
            if i == 0:
                print('Prix FN : ' + dico_result['lowest_price'])
            elif i == 1:
                print('Prix MW : ' + dico_result['lowest_price'])
            elif i == 2:
                print('Prix FT : ' + dico_result['lowest_price'])
            elif i == 3:
                print('Prix WW : ' + dico_result['lowest_price'])
            else:
                print('Prix BS : ' + dico_result['lowest_price'])

        i += 1

def arme_link_name(arme):
    # Pistols
    if 'cz' in arme.lower():
        arme = 'CZ75-Auto'
    if 'eagle' in arme.lower():
        arme = 'Desert%20Eagle'
    if 'dual' in arme.lower():
        arme = 'Dual%20Berettas'
    if 'five' in arme.lower():
        arme = 'Five-SeveN'
    if 'glock' in arme.lower():
        arme = 'Glock-18'
    if '2000' in arme.lower():
        arme = 'P2000'
    if '250' in arme.lower():
        arme = 'P250'
    if 'r8' in arme.lower():
        arme = 'R8%20Revolver'
    if 'tec' in arme.lower():
        arme = 'Tec-9'
    if 'usp' in arme.lower():
        arme = 'USP-S'
    
    # Riffles
    if 'ak' in arme.lower():
        arme = 'AK-47'
    if 'aug' in arme.lower():
        arme = 'AUG'
    if 'awp' in arme.lower():
        arme = 'AWP'
    if 'famas' in arme.lower():
        arme = 'FAMAS'
    if 'g3' in arme.lower():
        arme = 'G3SG1'
    if 'galil' in arme.lower():
        arme = 'Galil%20AR'
    if 'a1' in arme.lower():
        arme = 'M4A1-S'
    if 'a4' in arme.lower():
        arme = 'M4A4'
    if 'scar' in arme.lower():
        arme = 'SCAR-20'
    if 'sg' in arme.lower():
        arme = 'SG-553'
    if 'ssg' in arme.lower():
        arme = 'SSG%2008'
        
    # PMs
    if 'mac' in arme.lower():
        arme = 'MAC-10'
    if 'mp5' in arme.lower():
        arme = 'MP5-SD'
    if 'mp7' in arme.lower():
        arme = 'MP7'
    if 'mp9' in arme.lower():
        arme = 'MP9'
    if 'pp' in arme.lower():
        arme = 'PP-Bizon'
    if 'p90' in arme.lower():
        arme = 'P90'
    if 'ump' in arme.lower():
        arme = 'UMP-45'
        
    # Heavy
    if 'mag' in arme.lower():
        arme = 'MAG-7'
    if 'nova' in arme.lower():
        arme = 'Nova'
    if 'sawed' in arme.lower():
        arme = 'Sawed-Off'
    if 'xm' in arme.lower():
        arme = 'XM1014'
    if 'm249' in arme.lower():
        arme = 'M249'
    if 'negev' in arme.lower():
        arme = 'Negev' 
        
    return arme
    
def nom_arme(arme):
    if '%20' in arme_link_name(arme):
        nom = arme.replace('%20',' ')
    else : 
        nom = arme
    return nom


#-------------------------------------------------------------#



window = Tk()
l1 = Label(window,text="Title")


arme = input("Arme : ")
skin = input("Skin : ")

arme = arme_link_name(arme)

print_price(arme,skin,nom_arme(arme))

# Attention, case sensitive pour le skin : Redline is ok - redline is not.
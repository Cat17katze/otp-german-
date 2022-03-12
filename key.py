#!usr/bin/env python3

import os
from time import sleep

debug= 1
if debug:
	print('Imports abgeschlossen')

def encrypt(filename):
	to_encrypt = open(filename, "rb").read()
	size = len(to_encrypt)
	key = os.urandom(size)
	with open(filename + ".key", "wb") as key_out:
		key_out.write(key)
	encrypted = bytes(a ^ b for(a, b) in zip(to_encrypt, key))
	with open(filename, "wb") as encrypted_out:
		encrypted_out.write(encrypted)
		
def decrypt(filename, key):
	file = open(filename, "rb").read()
	key = open(key, "rb").read()
	decrypted = bytes(a ^ b for (a , b)in zip(file, key))
	with open("d_" + filename, "wb") as decrypted_out:
		decrypted_out.write(decrypted)

mode = "h"
while True:	
	try:
		while True:
			if mode ==1:
				filename= input("Die Datei muss sich im gleichen Ordner befinden\n\nFilename: ")
				try:
					encrypt(filename)
				except FileNotFoundError:
					print("Fehler: Datei nicht gefunden")
			elif mode ==2:
				filename= input("Die Datei muss sich im gleichen Ordner befinden\n\nFilename: ")
				key = input("Schlüsseldatei muss sich im gleichen Ordner befinden\n\nKeydatei: ")
				try:
					decrypt(filename,key)
				except FileNotFoundError:
					print("Fehler: Datei nicht gefunden")
			elif mode == 99:
				exit("Auf Wiedersehen")
			elif mode == "1":
				filename= input("Die Datei muss sich im gleichen Ordner befinden\n\nFilename: ")
				try:
					encrypt(filename)
				except FileNotFoundError:
					print("Fehler: Datei nicht gefunden oder ungültiger Dateiname")
			elif mode =="2":
				filename= input("Die Datei muss sich im gleichen Ordner befinden\n\nFilename: ")
				key = input("Schlüsseldatei muss sich im gleichen Ordner befinden\n\nKeydatei: ")
				try:
					decrypt(filename,key)
				except FileNotFoundError:
					print("Fehler: Datei nicht gefunden oder ungültiger Dateiname")
			elif mode == "99":
				exit("Auf Wiedersehen")
			elif mode =="exit":
				exit("Auf Wiedersehen")
			elif mode =="h":
				print("Das Programm ver/entschlüsselt Dateien oder Nachrichten.\nEs wird empfohlen das Programm im Terminal zu benutzen, da zum Beispielhelp VS-Code den Dateizugriff blockiert.\nBei der Eingabe von Dateinamen bitte die Endung  wie z.B *.jpeg , *.txt nicht vergessen.")
			elif mode == "help":
				print("Das Programm ver/entschlüsselt Dateien oder Nachrichten.\nEs wird empfohlen das Programm im Terminal zu benutzen, da zum Beispielhelp VS-Code den Dateizugriff blockiert.\nBei der Eingabe von Dateinamen bitte die Endung  wie z.B *.jpeg , *.txt nicht vergessen.")
			else:
				print("Ungültige Eingabe\n\n")
			sleep(2)
			print("\n\n\nDecrypt-Encrypt\nby Leon Pätzol3d\n\nHauptmenü")
			print("Auswahlmöglichkeiten:\n\n\n-1- Dateien verschlüsseln\n-2- Dateien entschlüsseln\n-h-\n       -Hilfe aufrufen (empfohlen, bei erster Benutzung des Programms)\n-help-\n-exit- Das Programm verlassen (strg + c) ist deaktiviert\n")
			mode = input("Ihre Auswahl: ")
	except KeyboardInterrupt:
		print("Exit nur mit der Eingabe im Menü von -exit- mgl.")
		sleep(3)
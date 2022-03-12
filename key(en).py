#!usr/bin/env python3

import os
from time import sleep

debug= 0
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
				filename= input("The file has to be in the same folder as the programm\"\n\nFilename: ")
				try:
					encrypt(filename)
				except FileNotFoundError:
					print("Error: File not found or invalid filename")
			elif mode ==2:
				filename= input("The file has to be in the same folder as the programm\"\n\nFilename: ")
				key = input("The key file has to be in the same folder as the programm\n\nKeydatei: ")
				try:
					decrypt(filename,key)
				except FileNotFoundError:
					print("Error: File not found or invalid filename")
			elif mode == 99:
				exit("Have a nice day!")
			elif mode == "1":
				filename= input("The file has to be in the same folder as the programm\"\n\nFilename: ")
				try:
					encrypt(filename)
				except FileNotFoundError:
					print("Error: File not found or invalid filename")
			elif mode =="2":
				filename= input("The file has to be in the same folder as the programm\"\n\nFilename: ")
				key = input("The key file has to be in the same folder as the programm\n\nKeydatei: ")
				try:
					decrypt(filename,key)
				except FileNotFoundError:
					print("Error: File not found or invalid filename")
			elif mode == "99":
				exit("Have a nice day!")
			elif mode =="exit":
				exit("Have a nice day!")
			elif mode =="h":
				print("The program de/ encrypt files with the OTP algorithm. Please use this programm in a native terminal or as a .exe version because specific development environments like visual code block the file acces, the acess to files is important. When you type file names, please don't forget file endings like .jpeg or .txt. ")
			elif mode == "help":
				print("The program de/ encrypt files with the OTP algorithm. Please use this programm in a native terminal or as a .exe version because specific development environments like visual code block the file acces, the acess to files is important. When you type file names, please don't forget file endings like .jpeg or .txt. ")
			else:
				print("Ungültige Eingabe\n\n")
			sleep(2)
			print("\n\n\nDecrypt-Encrypt\nby Leon Pätzol3d\n\nHauptmenü")
			print("Possible Choices\n\n\n-1- Encrypt files\n-2- Decrypt files\n-h- Show help(recommend, if you use this programm the first time)\n-help-\n-exit- Exit the programm (ctrl + c is disabled)\n")
			mode = input("You choice: ")
	except KeyboardInterrupt:
		print("You can't exit this programm with ctrl + c.")
		sleep(3)
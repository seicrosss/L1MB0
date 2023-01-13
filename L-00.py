import os
import subprocess
from signal import SIGTERM
from subprocess import Popen
import sys
import webbrowser
import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import wmi


velocidad=175
volumen=0.9
name = "limbo"
name1="L1MB0"
usu="seicros"
no="Funcion en desarrollo"
star=True

listener = sr.Recognizer()#Escuchar
listener.energy_threshold=100
listener.dynamic_energy_threshold=True
#Hablar
engine=pyttsx3.init()
voice_id = 'spanish-latin-am'
engine.setProperty("voice",voice_id)

rate=engine.getProperty("rate")
engine.setProperty("rate",velocidad)

volume = engine.getProperty('volume')
engine.setProperty('volume', volumen)

#Star
def reposo():
	print("*"+name1+" en reposo")
	freposo()

def freposo():
	with sr.Microphone() as source:
		try:

			listener.adjust_for_ambient_noise(source)
			audio = listener.listen(source)
			temp = listener.recognize_google(audio, language="es-MX")
			temp = temp.lower()
			if name in temp:
				hablar("Activa, "+usu)
				com()
		except:
			freposo()

#input y output
def escuchar():
	try:
		with sr.Microphone() as source:
			print("*"+name1+" escuchando")
			listener.adjust_for_ambient_noise(source)
			audio=listener.listen(source)
			text=listener.recognize_google(audio,language="es-MX")
			text = text.lower()

	except:
		print("-No detecto tu voz,"+usu)
		pass
	return text

def hablar(text):
	print("*"+name1+"...")
	engine.say(text)
	engine.runAndWait()
	print("'"+text+"'")

#Comandos
def cont():
	hablar("Te puedo ayudar en algo mas? "+usu)
	text=escuchar()
	if "yes" in text:
		hablar("Dime,"+usu)
		com()

def com():
	text=escuchar()

	if name in text:
		print("Indicador")
		text = text.replace(name + " ", "")
		print(text)

	if "ejcuta" in text:
		ejecuta(text)

	elif "busca" in text:
		busca()

	elif "hora" in text:
		hora()

	elif "reproduce" in text:
		reproduce(text)

	elif "pausa" in text or "despausa" in text:
		pausa_volumen()

	elif"volumen" in text:
		if "subir" in text or "aumenta" in text:
			subir_volumen()
		elif"bajar"in text or "reduce" in text:
			bajar_volumen()

	elif "muestrame" in text:
		muestrame(text)

	elif "nada" in text:
		hablar("Volviendo a reposo, " + usu)
		return

	elif "cierra"in text:
		cierre(text)

	elif "apaga"in text or "apagado" in text:
		apagado()


	cont()

#Comandos
#Desarrollo
def ejecuta(text):
	hablar(no)

def busca(text):
	bus = text.replace("busca" + "", "")
	print("*Realizando busquedad.")
	webbrowser.open("https://www.google.com/search?client=opera-gx&q=" + bus)
	hablar("Aqui estan los resultado de " + bus + " ," + usu)

def hora():
	hora = datetime.datetime.now().strftime('%I:%M %p')
	hablar("Son las " + hora + ", " + usu)
	print("*Reloj: " + hora)

def reproduce(text):
	music = text.replace("reproduce" + "", "")
	hablar("Reproduciendo ")
	pywhatkit.playonyt(music)

#Desarrollo
def pausa_volumen():
	hablar(no)

#Desarrollo
def subir_volumen():
	hablar(no)

#Desarrollo
def bajar_volumen():
	hablar(no)

#Desarrollo
def muestrame(text):
	muestra = text.replace("muestrame" + "", "")
	if "bonito" in muestra:
		hablar(no)

def apagado():
	hablar("Apagando el ordenador")
	subprocess.run("shutdown -s")

def cierre(text):
	text = text.replace("cierra" + "", "")
	c = wmi.WMI()
	text = text + ".exec"
	hablar("Buscando")
	for process in c.Win32_Process():
		print(process.ProcessId, process.Name)
		if process.Name in text:
			hablar("Ejecutando cerrado de " + text +","+ usu)
			print("*Cerrando",process.ProcessId, process.Name)
			os.kill(process.ProcessId,SIGTERM)
			return
	hablar("no logre encontrar "+text+" entre procesos")

hablar("Iniciada y entrando en reposo")
reposo()


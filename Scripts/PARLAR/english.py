# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
fitxer = open('C:\\xampp\\htdocs\\nao\\data\\ip.txt')
l = fitxer.readline()
ip = l.encode('ascii','replsce')

tts = ALProxy("ALTextToSpeech", ip , 9559)
tts.say(" ")
tts.setLanguage("English")
tts.say("Hello, my name is NAO. I live in the Pla de l'estany high school")
tts.setLanguage("Spanish")
# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
#LECTOR DE IP
fitxer_ip = open('C:\\xampp\\htdocs\\nao\\data\\ip.txt')
l = fitxer_ip.readline()
ls = l.encode('ascii','replsce')

#LECTOR DE TEXT
fitxer_text = open('C:\\xampp\\htdocs\\nao\\data\\stext.txt')
descod_text = fitxer_text.readline()
text = descod_text.encode('ascii','replsce')

tts = ALProxy("ALTextToSpeech",ls, 9559)

	
strtxt = text.encode('ascii','replsce')
tts.say(strtxt)
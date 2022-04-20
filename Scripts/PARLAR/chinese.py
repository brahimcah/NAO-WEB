# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
fitxer = open('C:\\xampp\\htdocs\\nao\\data\\ip.txt')
l = fitxer.readline()
ls = l.encode('ascii','replsce')

tts = ALProxy("ALTextToSpeech", ls , 9559)
tts.say(" ")
tts.setLanguage("Chinese")
tts.say("你好我的名字是NAO")
tts.say("我住在平湖學院")
tts.setLanguage("Spanish")
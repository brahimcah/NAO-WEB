# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
fitxer = open('C:\\xampp\\htdocs\\nao\\data\\ip.txt')
l = fitxer.readline()
ls = l.encode('ascii','replsce')

tts = ALProxy("ALTextToSpeech", ls , 9559)
tts.say(" ")
tts.setLanguage("Japanese")
tts.say("こんにちは、NAOです")
tts.say("私はプラデレスタニー高校に住んでいます")
tts.setLanguage("Spanish")
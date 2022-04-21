#!/usr/bin/env python

from naoqi import *
import time
import socket

ip = "172.16.251.37"
port = 9559

broker = ALBroker("pythonBroker","0.0.0.0", 0, ip, port)
motion = ALProxy("ALMotion", ip, port)
memory = ALProxy("ALMemory", ip, port)
basicawareness = ALProxy("ALBasicAwareness", ip, port)
barcode = ALProxy("ALBarcodeReader", ip, port)
tts = ALProxy("ALTextToSpeech", ip, port)
aas = ALProxy("ALAnimatedSpeech", ip, port)
memory = ALProxy("ALMemory", ip, port)
leds = ALProxy("ALLeds", ip, port)

def compruebaCabeza(ip, port):
 motion = ALProxy("ALMotion", ip, port)
 names = "Head"
 useSensors = False
 commandAngles = motion.getAngles(names, useSensors)
 print ("Command angles: ")
 print (str(commandAngles))
 print ("")
 return commandAngles

def mueveCabeza(ip, port, objetive):
 motion = ALProxy("ALMotion", ip, port)
 motion.setStiffnesses("Head", 1.0) 
 
 names = "HeadYaw"
 angles = objetive[0]
 fractionMaxSpeed = 0.1
 motion.setAngles(names,angles,fractionMaxSpeed)
 names = "HeadPitch"
 angles = objetive[1]
 fractionMaxSpeed = 0.1
 motion.setAngles(names,angles,fractionMaxSpeed)

def manejaEstimulos(ip, port, cad):
 basicawareness = ALProxy("ALBasicAwareness", ip, port)
 basicawareness.setStimulusDetectionEnabled("People", cad)
 basicawareness.setStimulusDetectionEnabled("Movement", cad)
 basicawareness.setStimulusDetectionEnabled("Touch", cad)
 basicawareness.setStimulusDetectionEnabled("Sound", cad)

class misocket:

    def __init__(self):
        self.sock = socket.socket()

    def conecta(self, host, port):
        self.sock.connect((host, port))

    def escucha(self, host, port):
        self.sock.bind((host, port))
        self.sock.listen(10)
        print ("Ahora escucha")

    def envia(self,msg):
        msg ="ID: " + msg + " FIN"
        self.sock.sendall(msg)

    def recibe(self):
        conn, addr = self.sock.accept()
        print ("Conexion establecido con ", addr)
        self.msg = conn.recv(1024)
        return True

    def dameMensaje(self):
       return self.msg

    def cierra(self):
        print ("Cerrando conexion...")
        self.sock.close()

    class myEventHandler(ALModule):

        def myCallback(self, key, value, msg):
            print (key, value, msg)
            if(value):
                memory.post.insertData("cadena", value)
                cad = str(value)
                aux = cad.split("'",3)
                aux = aux[1]
                print (aux)
                listavacia.append(aux)
                print (listavacia)
                n = len(listavacia)
                print (n)

                OldID = listavacia[n-2]
                print (OldID)
                CurrentID = listavacia[n-1]
                print (CurrentID)

                if(CurrentID != OldID):
                    print ("Es diferente")
                    msg = "Bienvenido" + CurrentID
                    habla(msg, ip, port)
                    NaoSocket = misocket()
                    NaoSocket.conecta("localhost", 9998)
                    NaoSocket.envia(aux)
                    NaoSocket.cierra()

                else:
                    print ("No es diferente")


            else:
                memory.post.insertData("nombre", "")

                def habla(msg, ip, port):
                    tts = ALProxy("ALTextToSpeech", ip, port)
                    id = tts.post.say(msg)
                    return id

                if __name__ == "__main__":
                    manejaEstimulos(ip, port, False)
                    #objetivo = [0.0, 0.51]
                    objetivo = [-0.0031099319458007812, 0.09199810028076172]
                    mueveCabeza(ip, port, objetivo)
                    time.sleep(2)
                    listavacia = []
                    listavacia.append("Nada")
                    n = 0
                    NaoSocketServer = misocket()
                    NaoSocket = misocket()
                    NaoSocketServer.escucha("localhost", 9999)
                    calculado = compruebaCabeza(ip, port)
                    error = [objetivo[0] - calculado[0], objetivo[1] - calculado[1]]

                    print ('Errores: ')
            
            print (str(error))
            print ('')

            handlerModule = myEventHandler("handlerModule")
            while True:
                id = memory.post.subscribeToEvent("BarcodeReader/BarcodeDetected","handlerModule", "myCallback")
            bol = NaoSocketServer.recibe()
            if(bol == True):
                memory.stop(id)
                frases = NaoSocketServer.dameMensaje()
                frases = frases[2:len(frases)]

                frases = frases.split("/")
                print (frases)
                iteracion = 0
                for iteracion in range(0,len(frases)):
                    #aas.say(str(frases[iteracion]))
                    tts.say(str(frases[iteracion]))
                    iteracion = iteracion + 1

            memory.post.insertData("cadena", '')

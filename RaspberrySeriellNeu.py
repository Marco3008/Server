import socket
import serial
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(5, GPIO.OUT)

se = serial.Serial('/dev/ttyAMA0', 9600) 
se.open()
time.sleep(5) 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.2.124'
port = 8008
s.bind((host, port))
s.listen(5)
c = None

while True:                                             #Verbinden mit Client
    if c is None:
        print ('[Waiting for connection...]')
        c, addr = s.accept()
        print ('Got connection from', addr)
    else:
        while True:
            Temperatur = input("Temperatur: ")                  #se.readline()
            c.send(bytes(Temperatur, "utf8"))                                                 
            Luftfeuchtigkeit = input("Luftfeuchtigkeit: ")  
            c.send(bytes(Luftfeuchtigkeit, "utf8"))
            PHWert = input("PH-Wert: ")           
            #print(Temperatur)
            #print(PH-Wert)
            #print(Luftfeuchtigkeit)
            c.send(bytes(PHWert, "utf8"))
            a = str(c.recv(1024), "utf8")
            print(a)
            if a is "EIN" :
               GPIO.output(5, GPIO.HIGH)
               print("geht")
            else:
                if a is "AUS" :
                   GPIO.output(5, GPIO.LOW)
            
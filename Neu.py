import socket
import serial
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(5, GPIO.OUT)

se = serial.Serial('/dev/ttyACM0', 9600)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.2.132'
port = 8008
s.bind((host, port))
s.listen(5)
c = None

while True:                                             
    if c is None:
        print ('[Waiting for connection...]')
        c, addr = s.accept()
        print ('Got connection from', addr)
        se.close()
        se.open()
        #print(str(se.readline(),"utf8"))
    else:
        while True:
            Strom = str(se.readline(),"utf8")
            c.send(bytes(Strom, "utf8"))
            print(Strom)
            
            Temperatur = str(se.readline(),"utf8")
            c.send(bytes(Temperatur, "utf8"))
            print(Temperatur)
            
            Luftfeuchtigkeit = str(se.readline(),"utf8")
            c.send(bytes(Luftfeuchtigkeit, "utf8"))
            print(Luftfeuchtigkeit)
            
            
            
            
            a = str(c.recv(1024), "utf8")
            print(a)
            if int(a) == 1:
                print("EIN")
                GPIO.output(5, GPIO.HIGH)
               
            else:
                if int(a) == 0 :
                    print("AUS")
                    GPIO.output(5, GPIO.LOW)


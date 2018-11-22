import socket
import serial
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(5, GPIO.OUT)

se = serial.Serial('/dev/ttyACM1', 9600)

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
        time.sleep(5) 
    else:
        while True:
            Strom = se.readline() #input("Strom: ")   
            print(Strom)
            Strom1 = str(float(Strom))
            c.send(bytes(Strom1, "utf8"))   
            Temperatur = se.readline()  #input("Temperatur: ")                  #se.readline()
            print(Temperatur)
            Temperatur1 = str(float(Temperatur))
            c.send(bytes(Temperatur1, "utf8"))  
            Luftfeuchtigkeit = se.readline() #input("Luftfeuchtigkeit: ")
            print(Luftfeuchtigkeit)
            Luftfeuchtigkeit1 = str(float(Luftfeuchtigkeit))
            c.send(bytes(Luftfeuchtigkeit1, "utf8"))
            a = str(c.recv(1024), "utf8")
            print(a)
            if int(a) == 1:
                print("EIN")
                GPIO.output(5, GPIO.HIGH)
               
            else:
                if int(a) == 0 :
                    print("AUS")
                    GPIO.output(5, GPIO.LOW)

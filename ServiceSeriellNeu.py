#!/usr/bin/python

import socket
minTemp = (int(str(input("Minimale Temperatur: "))))
#minTemp = (int(str(f1)))
maxLuft = (int(str(input("maximale Luftfeuchtigkeit: "))))
#maxLuft = (int(str(j1)))
maxPH = (int(str(input("Maximaler PH-Wert: "))))
#maxPH = (int(str(k1)))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.2.132'
port = 8008
s.connect((host, port))
print ('Connected to', host)
while True:
    a = str(s.recv(1024), "utf8")
    print ("Aktuelle Temperatur: ", a)
    b = (float(str(a)))
    if b > minTemp:
        g = str(s.recv(1024), "utf8")
        d = (float(str(g)))
        print("Aktueller PH-Wert: ",d)
        if d < maxLuft:
            v = str(s.recv(1024), "utf8")
            w = (float(str(v)))
            print("Aktuelle Luftfeuchtigkeit: ")
            if w < maxPH :
                e = "EIN"
                print(e)
                s.send(bytes(e, "utf8"))
            else:
                h = "AUS"
                print(h)
                s.send(bytes(h, "utf8"))
        else:
            str(s.recv(1024), "utf8")
            f = "AUS"
            print(f)
            s.send(bytes(f, "utf8"))
    else:    
        str(s.recv(1024), "utf8")
        g = "AUS"
        print(g)
        s.send(bytes(g, "utf8"))
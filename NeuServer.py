import socket

maxStrom = (int(str(input("Maximaler Strom: "))))
minTemp = (int(str(input("Minimale Temperatur: "))))
maxLuft = (int(str(input("maximale Luftfeuchtigkeit: "))))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.43.177.25'
port = 8008
s.connect((host, port))
print ('Connected to', host)

while True:

    a = float(str(s.recv(1024),"utf8"))
    if a < maxStrom:
        b = float(str(s.recv(1024),"utf8"))
        if b > minTemp:
            c = float(str(s.recv(1024),"utf8"))
            if c < maxLuft:
                s.send(bytes(1, "utf8"))
            else:
                s.send(bytes(0, "utf8"))
        else:
            str(s.recv(1024), "utf8")
            s.send(bytes(0, "utf8"))
    else:
        str(s.recv(1024), "utf8")
        str(s.recv(1024), "utf8")
        s.send(bytes(0, "utf8"))
                
   

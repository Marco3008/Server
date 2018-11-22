import socket



maxStrom = 0 #(int(str(input("Maximaler Strom: "))))

minTemp = 10 #(int(str(input("Minimale Temperatur: "))))

maxLuft = 80 #(int(str(input("maximale Luftfeuchtigkeit: "))))



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.2.132'

port = 8008

s.connect((host, port))

print ('Connected to', host)



while True:



    a = float(str(s.recv(1024),"utf8"))

    if a > maxStrom:

        b = float(str(s.recv(1024),"utf8"))

        if b > minTemp:

            c = float(str(s.recv(1024),"utf8"))

            if c < maxLuft:

                s.send(bytes(str(1), "utf8"))

            else:

                s.send(bytes(str(0), "utf8"))

        else:

            str(s.recv(1024), "utf8")

            s.send(bytes(str(0), "utf8"))

    else:

        str(s.recv(1024), "utf8")

        str(s.recv(1024), "utf8")

        s.send(bytes(str(0), "utf8"))

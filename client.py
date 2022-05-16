
import socket
 
# user input
#name = input('enter your username : ')    
#bytesToSend1 = str.encode(name)

IP = input('iNGRESA EL IP : ')   
serverAddrPort = (IP, 3000)
bufferSize = 1024


# connecting to hosts
UDPClientSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM) 
#try:
while(True):
        funcion = input("Ingrese funcion ")
        minimo = input("ingrese valor minimo ")
        maximo = input("ingrese valor maximo ")
        bytesToSend1 = str.encode(funcion)
        # sending username by encoding it
        #UDPClientSocket.sendto(bytesToSend1, serverAddrPort) 
        # sending password by encoding it
        UDPClientSocket.sendto(bytesToSend1, serverAddrPort) 
        if funcion == "FIN":
            break
        
        bytesToSend2 = str.encode(minimo)
        UDPClientSocket.sendto(bytesToSend2, serverAddrPort)

        bytesToSend3 = str.encode(maximo)
        UDPClientSocket.sendto(bytesToSend3, serverAddrPort)

        msgFromServer = UDPClientSocket.recvfrom(bufferSize) 
        msg = "Respuesta: {}".format(msgFromServer[0].decode()) 
        print(msg)

        msgFromServer = UDPClientSocket.recvfrom(bufferSize) 
        msg = "Cantidad de divisiones: {}".format(msgFromServer[0].decode()) 
        print(msg)
#except:
   # print("algo salió mal")
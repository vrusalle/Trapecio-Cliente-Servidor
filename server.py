from ast import Break
import socket
from integralTrap import HallarInt
  
hostname = socket.gethostname()
localIP = socket.gethostbyname(hostname)
#localIP = "127.0.0.1"
localPort = 3000
bufferSize = 1024
print(localIP)
UDPServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("Servidor listo-")
 
 
while(True):
   # receiving name from client
   funcion, addr1 = UDPServerSocket.recvfrom(bufferSize) 
 
   funcion = funcion.decode() 
   if funcion == "FIN":
      break

   minimo, addr1 = UDPServerSocket.recvfrom(bufferSize) 
   minimo = minimo.decode()

   maximo, addr1 = UDPServerSocket.recvfrom(bufferSize) 
   maximo = maximo.decode() 

   resultado, div = HallarInt(funcion, minimo, maximo)
   #print(funcion)
   msg = resultado

   bytesToSend = str.encode(msg)
      # sending encoded status of name and pwd
   UDPServerSocket.sendto(bytesToSend, addr1)

   msg = div

   bytesToSend = str.encode(msg)
      # sending encoded status of name and pwd
   UDPServerSocket.sendto(bytesToSend, addr1) 
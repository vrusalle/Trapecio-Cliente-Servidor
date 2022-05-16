# Trapecio-Cliente-Servidor
Cliente/Servidor UDP en Python para realizar integrales usando el método del trapecio

Existe una conexion UDP entre client.py y server.py.
Cuando client.py envía la información a server.py, este llama al archivo integralTrap.py para realizar las operaciones del trapecio, cuando termina retorna el resultado y la cantidad de divisiones al server.py para que este se las envíe a client.py

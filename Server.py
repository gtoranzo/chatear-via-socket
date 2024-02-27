import socket

# Crea un socket
s = socket.socket()

# La IP del servidor y el puerto a utilizar
s.bind(("localhost", 60))

# Clientes permitidos
s.listen(1)
print("Server corriendo")

# Funcion que espera que un cliente se conecte
# para iniciar la conexion
sc, addr = s.accept()

while True:
    # Espera hasta que reciba datos
    recibido = sc.recv(1024)

    # Imprime los datos recibidos
    print("Received:", recibido)

    # Para terminar la conexion por peticion del cliente
    if recibido == "quit":
        break


# Termina conexion del servidor
s.close()
# Termina conexion del socket con el cliente
sc.close()
print("Conexión terminada")

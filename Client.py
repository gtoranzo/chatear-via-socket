import socket

# Crea un socket
s = socket.socket()

# Se conecta al servidor y elige el puerto a utilizar
s.connect(("localhost", 60))

while True:
    # Escribe el mensaje para enviar
    #     mensaje = raw_input("> ")
    mensaje = input("> ")

    # Envia el mensaje
    s.send(mensaje)

    # Cierra la conexion por peticion
    if mensaje == "quit":
        break

# Cierra el socket
s.close()
print("Conexión terminada")

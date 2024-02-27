# chatear-via-socket

#### Servidor y Cliente en Python con Medidas de Seguridad

**Funcion:** Crea un servidor y un usuario que se conecta a traves de un socket en donde se pueden enviar mensajes, archivos, imagenes y documentos.

**Denegacion de Servicio:** Si usted manda datos infinitos como

```python
while True:
   socket.send(data)
```

Usted **derribara el servidor** para proteger nuestro servidor debemos **limitar** la conexion acceptada se puede realizar de diferentes maneras.

- Limitar el tamaño de los bytes recibidos
- Restrigir el exceso de conexiones
- Bloquear conexiones por direccion IP

**Excepcion no Atrapada:** Su servidor puede tener un error de codigo que puede **derribar el servidor** como una excepcion que no es atrapada es importante que todas las excepciones sean atrapadas.

**Ejemplo:**

```python
int division = 0/0
```

Por realizar esta division en su servidor cerrara de manera inmediatamente y mostrara el siguiente error

```python
ZeroDivisionError: division by zero
```

**Inyeccion de Datos:** Cuando el cliente inyecta datos de manera fraudulenta para recibir datos que estan restingidos como **contraseñas**.

**Ejemplo:**

```python
socket.send(0)
```

Usted manda un `0` no recibira ningun dato si cambia el valor de el mensaje a un `1 ` recibira datos restringidos como una `contraseña`

**Actividad Sospechosa:** Debemos tener un algoritmo que detecte la actividad sospechosa para impedir cualquier accion maliciosa por parte de personas malitencionadas.

**Pasos**

- Documentar la actividad del usuario
- Almacenar el documento en una base de datos
- Analizar la actividad del usuario

Con estos datos podemos diseñar un **cortafuegos** para impedir las actividades maliciosas.

**Ejemplo:**

```python
socket.send(0x52)
```

Al verificar este mensaje recibido por un cliente se puede señalar que es diferente al que tendriamos que recibir esto es porque es una conexion fraudulenta al documentar estas acciones podemos crear un algoritmo de **cortafuegos** para rechazar estas conexiones.

**Recuperacion de Cuenta:** Una persona puede obtener nuestras credenciales como **usuario** y **contraseña** por diversas maneras intentara bloquear al propetario de la cuenta para no permitirle el ingreso para impedir esta accion podemos usar.

- **Verificacion por SMS:** Para que este proceso de recuperacion sea seguro debemos darle proridad a los numeros telefonicos mas antiguos registrados.

- **Verificacion por Ubicacion:** Podemos utilizar la ubicacion del usuario para poder comprobar el legitimo dueño del propietario de la cuenta.

- **Pregunta Secreta:** Este metodo es subestimado y lo consideran anticuado no deben olvidar que este metodo de verificacion implementado es confiable.

**No Permitir la Entrada de Robots:** Un robot como **Sophia** de **Microsoft** puede entrar a nuestro servidor o un programa informatico como un **bot** puede hacer **spam** en nuestro sitio para evitar esto podemos utilizar.

- **Captcha:** Es una prueba de la capacidad de una máquina para exhibir un comportamiento inteligente similar al de un ser humano puede ser implementado en sonido o imagen.

- **Deteccion de Errores:** Una persona se equivoca en determinadas acciones cuando realizan peticiones con un patron perfecto puede ser considerado un robot.

- **Duracion de una Sesion:** Una persona para `escribir` un mensaje se demora aproximamente `5 segundos` y para enviarlo se demora `8 segundos` aproximadamente cuando las peticiones se manda un tiempo imposible para un **humano** puede ser considerado un robot.

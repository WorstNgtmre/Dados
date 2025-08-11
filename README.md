# **Lanzador de Dados en Python**

Este proyecto contiene dos versiones de un lanzador de dados, una para la terminal y otra con una interfaz gráfica de usuario (GUI). Ambas permiten simular tiradas de dados con un formato común en juegos de rol, como 2d6+3.

## **Contenido del Proyecto**

* **Terminal.py**: Una aplicación de línea de comandos que solicita al usuario la tirada de dados y muestra el resultado en la terminal.  
* **UI.py**: Una aplicación con una interfaz gráfica de usuario, construida con la librería customtkinter, que permite seleccionar la cantidad de dados, el número de caras y un bonificador.

## **Características**

### **Terminal.py**

* Simulación de tiradas de dados con el formato XdY.  
* Soporte para bonificadores positivos y negativos (XdY+Z o XdY-Z).  
* Muestra el valor de cada dado individual, el total de la tirada y el resultado final con el bonificador aplicado.

### **UI.py**

* Interfaz gráfica de usuario para una interacción más sencilla.  
* Campos para la cantidad de dados y el bonificador.  
* Menú desplegable para elegir el número de caras (4, 6, 8, 10, 12, 20, 100).  
* Opción para activar/desactivar el uso del bonificador.  
* Botón para lanzar los dados y mostrar los resultados en un cuadro de texto.  
* Manejo de errores para entradas inválidas.

## **Requisitos**

### **Terminal.py**

* Python 3.x  
* No se necesitan librerías adicionales.

### **UI.py**

* Python 3.x  
* Librería customtkinter. Puedes instalarla con el siguiente comando:  
  pip install customtkinter

## **Cómo Usar**

### **Terminal.py**

1. Abre una terminal o símbolo del sistema.  
2. Navega hasta el directorio donde se encuentra el archivo.  
3. Ejecuta el script con el siguiente comando:  
   python Terminal.py

4. Introduce tu tirada de dados en el formato XdY, XdY+Z o XdY-Z. Por ejemplo:  
   * 2d6 (dos dados de 6 caras)  
   * 1d20+5 (un dado de 20 caras con un bonificador de 5\)  
   * 3d8-2 (tres dados de 8 caras con un bonificador de \-2)  
5. Escribe s para salir.

### **UI.py**

1. Asegúrate de tener instalada la librería customtkinter.  
2. Navega hasta el directorio del archivo y ejecuta el script:  
   python UI.py

3. Usa la interfaz para configurar tu tirada de dados y haz clic en "¡Lanzar\!".

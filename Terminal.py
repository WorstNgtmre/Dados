import random

tirada = input("Introduce la tirada de dados (Ej: 2d4+3, 1d20-1) o 's' para terminar: ")

while tirada != 's': 
    try:
        trozos = tirada.split("d")
        cant = int(trozos[0])
        if len(trozos) > 2:
            raise SyntaxError
        try:
            trozos2 = trozos[1].split("+")
            caras = int(trozos2[0])
            bonificador = int(trozos2[1])
            signo = "+"
        except:
            try:
                trozos2 = trozos[1].split("-")
                caras = int(trozos2[0])
                bonificador = int(trozos2[1])
                signo = "-"
            except:
                caras = int(trozos[1])
                bonificador = 0
                signo = ""

        valores = []         
        for dado in range(cant):
            valores.append(random.randint(1,caras))
            print(f"Dado {dado +1}: {valores[dado]}")
        
        total = 0
        for valor in valores:
            total += valor
        print(f"Valor total sin bonificadores: {total}")

        if signo == "+":
            resultado = total + bonificador
        elif signo == "-":
            resultado = total - bonificador
        else:
            resultado = total

        print(f"Resultado total con bonificadores: {resultado}")

    except:
        print("Introduce el formato correcto (Ej: 2d4+3, 1d20-1)")
        
    tirada = input("Introduce la tirada de dados (Ej: 2d4+3, 1d20-1) o 's' para terminar: ")

   


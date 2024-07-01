#taller de automtriz necsita, registrar vehiculo,listar autos registrados,imprimir por marca, salir
import os
os.system("cls")

menu_con_numeros = """Menu principal
1.registrar vehiculo
2.listar ordenes
3.imprimir ordenes
4.salir
"""

matriz=[

]
marcas=["Chevrolet","ford","toyota"]

def registrar_auto():
    try:
            opc=input("""¿Que marca de auto desea ingresar
1.toyota
2.ford
3.Chevrolet
""")
            if opc == "1":
                marca="toyota"
            elif opc == "2":
                marca="ford"
            elif opc == "3":
                marca="chevrolet"
            año_fabr=int(input("ingrese el año de fabricacion(ejemplo: 2000)\n"))
            if año_fabr>999 and año_fabr<10000:
                pass
            else:
                return 0
            km=int(input("ingrese el kilometraje del vehiculo(ejemplo: 648)\n"))
            est=int(input("ingrese el costo estimado de reparacion en clp\n"))
            if est>99999:
                pass
            else:
                input("ingrese un valor mas alto")
                return 0
            servicio= est*0.08
            matriz.append([marca,año_fabr,km,est,int(servicio),int(est+servicio)])
    except:
        input("error al registrar un vehiculo")
        return 0

def generarReporte(a=0):
    try:
            #definicion para crear un reporte en la variable texto
            texto = """
        ╔════╦════════════╦════════════╦═══════════════╦═════════════════╦═══════════╦════════════════╗
        ║    ║            ║            ║               ║                 ║           ║                ║
        ║ n° ║   marca    ║ Año fabric.║ Kilometraje   ║ Precio estimado ║ Servicio  ║ precio total   ║
        ║    ║            ║            ║               ║                 ║           ║                ║
        ╚════╩════════════╩════════════╩═══════════════╩═════════════════╩═══════════╩════════════════╝

        """
            if a == 0:
                for i in range (len(matriz)):
                    texto += f"{i+1:4d}" #agrega un id
                    texto += f"{"":2s}"
                    texto += f"{matriz[i][0]:13s}"#agrega el contenido de el primer elemento 
                    texto += f"{matriz[i][1]:13d}"#agrega el contenido de el segundo elemento
                    texto += f"{matriz[i][2]:16d}"#agrega el contenido de el tercer elemento
                    texto += f"{matriz[i][3]:18d}"#agrega el contenido de el cuarto elemento
                    texto += f"{matriz[i][4]:12d}"#agrega el contenido de el quinto elemento
                    texto += f"{matriz[i][5]:17d}"#agrega el contenido de el sexto elemento
                    texto += f"\n"
                return texto
            
            elif a != 0:
                for i in range (len(matriz)):
                    if matriz[i][0]== a: # este if filtra los elementos que tengan el valor de a
                        texto += f"{i+1:5d}" #agrega un id
                        texto += f"{"":1d}"
                        texto += f"{matriz[i][0]:13s}"#agrega el contenido de el primer elemento 
                        texto += f"{matriz[i][1]:13d}"#agrega el contenido de el segundo elemento
                        texto += f"{matriz[i][2]:16d}"#agrega el contenido de el tercer elemento
                        texto += f"{matriz[i][3]:18d}"#agrega el contenido de el cuarto elemento
                        texto += f"{matriz[i][4]:12d}"#agrega el contenido de el quinto elemento
                        texto += f"{matriz[i][5]:17d}"#agrega el contenido de el sexto elemento
                        texto += f"\n"
                return texto
    except:
        input("exepcion")
def imprimir_orden():
    try:
            opc = int(input("""Que orden quiere imprimir
1. todas
2. chevrolet
3. ford
4. toyota
        """))
            if opc == 1:
                reporte=generarReporte(0)
                with open ("orden.txt","w",encoding='utf-8') as archivo:
                    archivo.write(reporte)
            elif opc == 2:
                reporte=generarReporte("chevrolet")
                with open ("orden.txt","w",encoding='utf-8') as archivo:
                    archivo.write(reporte)
            elif opc == 3:
                reporte=generarReporte("ford")
                with open ("orden.txt","w",encoding='utf-8') as archivo:
                    archivo.write(reporte)
            elif opc == 4:
                reporte=generarReporte("toyota")
                with open ("orden.txt","w",encoding='utf-8') as archivo:
                    archivo.write(reporte)
    except:
        input("excepcion al imprimir")

while True:
    os.system("cls")
    print(menu_con_numeros)
    opc = input("Ingrese la opcion: ")
    if opc == "1":
        regist=registrar_auto()
        if regist==0:
            input("ingrese los datos correctamente")
        else:
            input("se a registrado de forma correcta")
    elif opc == "2":
        print(generarReporte())
        input("\npresione enter para continuar")
    elif opc == "3":
        imprimir_orden()
        input("\npresione enter para continuar")
    elif opc == "4":
        input("gracias por usar el programa")
        break
    else:
        input("ingrese una opcion valida")


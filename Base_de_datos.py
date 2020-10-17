from __future__ import print_function
from PIL import Image
def compra():
    print("Escriba 1 si quiere entrar a la pagina de compra del Model S: ")
    print("Escriba 2 si quiere entrar a la pagina de compra del Model X: ")
    print("Escriba 3 si quiere entrar a la pagina de compra del Model 3: ")
    preferencia_cliente = int(input())
    if(preferencia_cliente == 1):
        print(compramodels())
    if(preferencia_cliente == 2):
        print(compramodelx())
    if(preferencia_cliente == 3):
        print(compramodel3())


def datos_pago():
    datos_comprador = []
    nombre = str(input("Inserte nombre completo: "))
    nombre_mayusculas = nombre.upper()
    datos_comprador.append([nombre_mayusculas])
    tarjeta = str(input("Inserte su tipo de tarjeta (Debito o Credito): "))
    tajeta_mayusculas = tarjeta.upper()
    datos_comprador.append([tajeta_mayusculas])
    digitos = int(input("Inserte los 16 digitos de su tarjeta: "))
    datos_comprador.append([digitos])
    fecha = (input("Inserte la fecha de vencimiento en este formato ( 00/00 ): "))
    datos_comprador.append([fecha])
    datos_seguridad = int(input("Inserte los 4 digitos de seguridad: "))
    datos_comprador.append([datos_seguridad])
    while True:
        print()
        print("Su información es correcta?")
        print("1. Nombre completo: ", datos_comprador[0])
        print("2. Tipo de tarjeta: ", datos_comprador[1])
        print("3. 16 digitos de la tarjeta: ", datos_comprador[2])
        print("4. Fecha de vencimiento: ", datos_comprador[3])
        print("5. Numero de seguridad: ", datos_comprador[4])
        print()
        información = int(input("Escriba '1' =info. correcta, '2' =info. incorrecta: "))
        if (información == 1):
            print()
            print("Dirijase a la siguiente pagina para finalizar")
            print()
            print("https://www.tesla.com/es_mx")
            break
        if (información == 2):
            modificacion = int(input("Inserte el numero de dato que quiere modificar: "))
            modificacion -= 1
            correccion = input("Inserte la correcion del dato: ")
            if(modificacion == 0 or modificacion == 1):
                correccion = correccion.upper()
            datos_comprador[modificacion] = correccion
            
    return print(datos_comprador)


def organigrama():
    final = []

    numero = int(input("Inserte el numero de perfiles que registrara: "))
    q = 0
    w = 0
    acumulador = 0
    number = 2
    while acumulador < numero:
        a = str(input("Inserte nombre completo: "))
        b = int(input("Edad: "))
        c = str(input("Sexo: "))
        d = str(input("Estado civil: "))
        e = str(input("Inserte cargo en la empresa: "))
        f = str(input("Nacionalidad: "))
        g = int(input("Numero de Contacto: "))
        print()
        if(number <= numero):
            print("Inserte la informacion del perfil número", number)

        persona = [a, b, c, d, e, f, g]
        final.insert([q][w], persona)
        acumulador = acumulador + 1
        number += 1
    print(final)
    m = 1
    s = 0
    g = 1
    while m <= numero:

        print("Escriba", g, "si usted quiere la informacion de", final[s][0])
        s += 1
        g += 1
        m += 1
    p = 1
    k = int(input())
    h = 0
    f = 0
    while True:
        if(k == p):
            print("Nombre: ", final[h][f])
            f += 1
            print("Edad: ", final[h][f])
            f += 1
            print("Sexo: ", final[h][f])
            f += 1
            print("Estado civil: ", final[h][f])
            f += 1
            print("Cargo en la empresa: ", final[h][f])
            f += 1
            print("Nacionalidad: ", final[h][f])
            f += 1
            print("Numero de contacto: ", final[h][f])
            break
        else:
            p += 1
            h += 1


def compramodels():
    im = Image.open("s.jpeg")
    box = (500,300,2400,1500)
    area_recortada = im.crop(box)
    area_recortada.show()
    a = open("models.txt", "r")

    print(a.read())

    a.close()

    costofinal = 0

    costobase = str(input("Inserte la versión que desea adquirir: "))

    if(costobase == "plaid" or costobase == "Plaid"):
        costofinal += 3099900
    elif(costobase == "performance" or costobase == "Performance"):
        costofinal += 2123900
    elif(costobase == "Long Range Plus" or costobase == "Long range plus"):
        costofinal += 1823900
    costocolor = str(input("Inserte color, Blanco|Negro|Gris|Azul|Rojo: "))
    if(costocolor == "Blanco" or costocolor == "blanco"):
        costofinal += 0
    elif(costocolor != "Blanco"):
        costofinal += 32500
    print("Inserte '1' si usted quiere los rines Tempest de 19")
    print("Inserte '2' si quiere agregar Sonic Carbon Twin Turbine de 21")
    costorines = int(input())

    if(costorines == 1):
        costofinal += 0
    elif (costorines == 2):
        costofinal += 97000

    costointeriores = str(input("Inserte color interior negro blanco beige: "))

    if(costocolor == "Negro" or costocolor == "negro"):
        costofinal += 0
    elif(costocolor != "Negro"):
        costofinal += 32400
    print("Inserte 'si', si usted quiere agregar el servicio de autopilot: ")
    print("Inserte 'no', si usted no lo quiere agregar: ")
    autopilot = str(input())

    if(costocolor == "si" or costocolor == "Si"):
        costofinal += 177200
    elif(costocolor != "No" or costocolor != "no"):
        costofinal += 0
    print("El costo final de su vehiculo sera de: ", costofinal)
    print()
    print("Inserte '1' si usted quiere adquirir el vehiculo")
    print("inserte '2' si no quiere realizar la compra")
    p = int(input())
    if(p == 1):
        return print(datospago())
    elif(p != 1):
        return print("Gracias por usar el modelo personalizado de TESLA")


def compramodelx():
    im = Image.open("x.jpeg")
    box = (500,200,2400,1400)
    area_recortada = im.crop(box)
    area_recortada.show()
    b = open("modelx.txt", "r")

    print(b.read())

    b.close()

    costofinal = 0

    costobase = str(input("Inserte la versión que desea adquirir: "))
    if(costobase == "Long Range Plus" or costobase == "Long range plus"):
        costofinal += 1998900
    elif(costobase == "performance" or costobase == "Performance"):
        costofinal += 2298900
    costocolor = str(input("Inserte color |Blanco|Negro|Gris|Azul|Rojo: "))

    if(costocolor == "Blanco" or costocolor == "blanco"):
        costofinal += 0
    elif(costocolor != "Blanco"):
        costofinal += 32400
    print("Inserte '1' si usted quiere los rines Silver de 20:")
    print ("Inserte '2' si usted quiere los rines negro onyx de 22:")
    costorines = int(input())

    if(costorines == 1):
        costofinal += 0
    elif (costorines == 2):
        costofinal += 119000
    costoasientos = int(input("Ingrese numero de asientos que desea /5/6/7: "))
    if(costoasientos == 5):
        costofinal += 0
    if(costoasientos == 6):
        costofinal += 140000
    if(costoasientos == 7):
        costofinal += 76000

    costointeriores = str(input("Inserte color interior /negro/blanco/beige:"))

    if(costocolor == "Negro" or costocolor == "negro"):
        costofinal += 0
    elif(costocolor != "Negro"):
        costofinal += 32400
    print("Inserte 'si', si quiere agregar el servicio de autopilot")
    print("Inserte'no', si usted no lo quiere agregar: ")
    autopilot = str(input())

    if(costocolor == "si" or costocolor == "Si"):
        costofinal += 177200
    elif(costocolor != "No" or costocolor != "no"):
        costofinal += 0
    print("El costo final de su vehiculo sera de: ", costofinal)
    print()
    print("Inserte '1' si usted quiere adquirir el vehiculo")
    print("Inserte '2' si no quiere realizar la compra")
    p = int(input())
    if(p == 1):
        return print(datospago())
    elif(p != 1):
        return print("Gracias por usar el modelo personalizado de TESLA")


def compramodel3():
    im = Image.open("3.jpg")
    box = (350,300,1550,1000)
    area_recortada = im.crop(box)
    area_recortada.show()
    c = open("model3.txt", "r")

    print(c.read())

    c.close()

    costofinal = 0


    costofinal = 0

    costob = str(input("Inserte la versión que desea adquirir: "))
    costobase = costob.lower()
    if(costobase == "autonomia estandar plus"):
        costofinal += 1049900
    elif(costobase == "Autonomía Mayor" or costobase == "autonomía mayor"):
        costofinal += 1249900
    elif(costobase == "Performance" or costobase == "performance"):
        costofinal += 1349900
    costocolor = str(input("Inserte el color,Blanco,Negro,Gris,Azul o Rojo: "))

    if(costocolor == "Blanco" or costocolor == "blanco"):
        costofinal += 0
    elif(costocolor != "Blanco"):
        costofinal += 21600
    costointeriores = str(input("Inserte color interiores,negro o blanco: "))

    if(costocolor == "Negro" or costocolor == "negro"):
        costofinal += 0
    elif(costocolor != "Negro"):
        costofinal += 21600
    print("Inserte 'si', si usted quiere agregar el servicio de autopilot: ")
    print("Inserte 'no', si usted no lo quiere agregar: ")
    autopilot = str(input())
    if(costocolor == "si" or costocolor == "Si"):
        costofinal += 177200
    elif(costocolor != "No" or costocolor != "no"):
        costofinal += 0
    print("El costo final de su vehiculo sera de: ", costofinal)
    print()
    print("Inserte '1' si usted quiere proceder con la compra")
    print("Inserte '2' si no quiere realizar la compra")
    p = int(input())
    if(p == 1):
        return print(datospago())
    elif(p != 1):
        return print("Gracias por usar el modelo personalizado de TESLA")
print("Escriba 1 si quiere adquirir un vehiculo Tesla: ")
print("Escriba 2 si quiere entrar a la base de perfiles de la empresa: ")
a = int(input())
if(a == 1):
    print(compra())
elif(a == 2):
    print(organigrama())
    




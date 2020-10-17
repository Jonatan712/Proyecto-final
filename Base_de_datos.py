"""
Proyecto Final
Simulador de Base de datos.
El programa inicialmente tiene dos opciones de funcionamiento,
la primera es para la adquisición de un vehiculo TESLA y la segunda
es para crear una base de perfiles de los empleados de la empresa.
"""
'''biblioteca'''
from __future__ import print_function
from PIL import Image
'''
La función de estas librerias son abrir imagenes en ciertas parte
del codigo, esto de una manera simple; estas se abren cuando ingreso
a comprar algun modelo TESLA.
'''

'''================== funciones ========================='''


def compra():
    '''
    Al aplicar esta función, se piden valores numericos para conocer el
    vehiculo que    desea adquirir, y devuelve la funcion que corresponde
    al modelo que selecciono.
    '''
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
    '''
    Al usar esta función se solicitan diferentes datos de pago para poder
    adquirir el auto que el usuario selecciono, esta entra al final de cada
    personalización del vehiculo elegido.
    '''
    datos_comprador = []
    nombre = str(input("Inserte nombre completo: "))
    nombre_mayusculas = nombre.upper()
    datos_comprador.append([nombre_mayusculas])
    tarjeta = str(input("Inserte su tipo de tarjeta (Debito o Credito): "))
    tajeta_mayusculas = tarjeta.upper()
    datos_comprador.append([tajeta_mayusculas])
    digitos = int(input("Inserte los 16 digitos de su tarjeta: "))
    datos_comprador.append([digitos])
    fecha = (input("Inserte fecha de vencimiento en este formato ( 00/00 ): "))
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
        print("Escriba '1' si la informacion es correcta")
        print("Escriba '2' si la informacion es incorrecta")
        información = int(input())
        if (información == 1):
            print()
            print("Dirijase a la siguiente pagina para finalizar")
            print()
            print("https://www.tesla.com/es_mx")
            break
        if (información == 2):
            modificacion = int(input("Inserte el numero de dato erroneo: "))
            modificacion -= 1
            correccion = input("Inserte la correcion del dato: ")
            if(modificacion == 0 or modificacion == 1):
                correccion = correccion.upper()
            datos_comprador[modificacion] = correccion
    return print(datos_comprador)


def organigrama():
    '''
    Esta es la función que hace posible la produccion de un organigrama,
    primero solicita los perfiles a agregar, llenas los perfiles, y al final
    tienes la opcion de obtener el perfil de cualquier persona.
    '''
    perfiles = []

    numero = int(input("Inserte el numero de perfiles que registrara: "))
    primer_valor_matriz = 0
    segundo_valor_matriz = 0
    acumulador = 0
    number = 2
    while acumulador < numero:
        nombre = str(input("Inserte nombre completo: "))
        edad = int(input("Edad: "))
        sexo = str(input("Sexo: "))
        est_civ = str(input("Estado civil: "))
        cargo = str(input("Inserte cargo en la empresa: "))
        nacio = str(input("Nacionalidad: "))
        numero = int(input("Numero de Contacto: "))
        print()
        if(number <= numero):
            print("Inserte la informacion del perfil número", number)

        persona = [nombre, edad, sexo, est_civ, cargo, nacio, numero]
        perfiles.insert([primer_valor_matriz][segundo_valor_matriz], persona)
        acumulador = acumulador + 1
        number += 1
    print(perfiles)
    contador = 1
    val_mat = 0
    acum_dato = 1
    texto = ("si usted quiere la información de")
    while contador <= numero:
        print("Escriba", acum_dato, texto, perfiles[val_mat][0])
        val_mat += 1
        acum_dato += 1
        contador += 1
    contador = 1
    perfil_solicitado = int(input())
    uno_val_mat = 0
    seg_val_mat = 0
    while True:
        if(perfil_solicitado == contador):
            print("Nombre: ", perfiles[uno_val_mat][seg_val_mat])
            seg_val_mat += 1
            print("Edad: ", perfiles[uno_val_mat][seg_val_mat])
            seg_val_mat += 1
            print("Sexo: ", perfiles[uno_val_mat][seg_val_mat])
            seg_val_mat += 1
            print("Estado civil: ", perfiles[uno_val_mat][seg_val_mat])
            seg_val_mat += 1
            print("Cargo en la empresa: ", perfiles[uno_val_mat][seg_val_mat])
            seg_val_mat += 1
            print("Nacionalidad: ", perfiles[uno_val_mat][seg_val_mat])
            seg_val_mat += 1
            print("Numero de contacto: ", perfiles[uno_val_mat][seg_val_mat])
            break
        else:
            contador += 1
            uno_val_mat += 1


def compramodels():
    '''
    El objetivo de esta función es el poder tener un servio personalizado
    al adquirir un vehiculo (Tesla model S), además de que al incio coloca
    la imagen del vehiculo. La personalización cubre datos como el color,
    versión,etc.
    '''
    imagen = Image.open("s.jpeg")
    box = (500, 300, 2400, 1500)
    area_recortada = imagen.crop(box)
    area_recortada.show()
    imprimir_texto = open("models.txt", "r")

    print(imprimir_texto.read())

    imprimir_texto.close()

    costo_final = 0

    costo_base = str(input("Inserte la versión que desea adquirir: "))
    costo_base_mayusculas = costo_base.upper()
    if(costo_base_mayusculas == "PLAID"):
        costo_final += 3099900
    elif(costo_base_mayusculas == "PERFORMANCE"):
        costo_final += 2123900
    elif(costo_base_mayusculas == "LONG RANGE PLUS"):
        costo_final += 1823900
    costo_color = str(input("Inserte color, Blanco|Negro|Gris|Azul|Rojo: "))
    costo_color_mayusculas = costo_color.upper()
    if(costo_color_mayusculas == "BLANCO"):
        costo_final += 0
    elif(costo_color_mayusculas != "BLANCO"):
        costo_final += 32500
    print('''Inserte '1' si usted quiere los rines Tempest de 19"''')
    print('''Inserte '2' si quiere agregar Sonic Carbon Twin Turbine de 21"''')
    costorines = int(input())
    if(costorines == 1):
        costo_final += 0
    elif (costorines == 2):
        costo_final += 97000

    costo_interiores = str(input("Inserte interior |Negro|Blanco|Beige|: "))
    costo_interiores_mayusculas = costo_interiores.upper()
    if(costo_interiores_mayusculas == "NEGRO"):
        costo_final += 0
    elif(costo_interiores_mayusculas != "NEGRO"):
        costo_final += 32400
    print("Inserte 'si', si usted quiere agregar el servicio de autopilot: ")
    print("Inserte 'no', si usted no lo quiere agregar: ")
    autopilot = str(input())
    autopilot_mayusculas = autopilot.upper()
    if(autopilot_mayusculas == "SI"):
        costo_final += 177200
    elif(autopilot_mayusculas == "NO"):
        costo_final += 0
    print("El costo final de su vehiculo sera de: ", costo_final)
    print()
    print("Inserte '1' si usted quiere adquirir el vehiculo")
    print("inserte '2' si no quiere realizar la compra")
    sugerencia = int(input())
    if(sugerencia == 1):
        return print(datos_pago())
    elif(sugerencia != 1):
        return print("Gracias por usar el modelo personalizado de TESLA")


def compramodelx():
    '''
    El objetivo de esta función es el poder tener un servio personalizado
    al adquirir un vehiculo (Tesla model X), además de que al incio coloca
    la imagen del vehiculo. La personalización cubre datos como el color,
    versión,etc.
    '''
    imagen = Image.open("x.jpeg")
    box = (500, 200, 2400, 1400)
    area_recortada = imagen.crop(box)
    area_recortada.show()
    texto = open("modelx.txt", "r")

    print(texto.read())

    texto.close()

    costo_final = 0

    costo_base = str(input("Inserte la versión que desea adquirir: "))
    costo_base_mayusculas = costo_base.upper
    if(costo_base_mayusculas == "LONG RANGE PLUS"):
        costo_final += 1998900
    elif(costo_base_mayusculas == "PERFORMANCE"):
        costo_final += 2298900
    costo_color = str(input("Inserte color |Blanco|Negro|Gris|Azul|Rojo: "))
    costo_color_mayusculas = costo_color.upper()
    if(costo_color_mayusculas == "BLANCO"):
        costo_final += 0
    elif(costo_color_mayusculas != "BLANCO"):
        costo_final += 32400
    print("Inserte '1' si usted quiere los rines Silver de 20:")
    print ("Inserte '2' si usted quiere los rines negro onyx de 22:")
    costo_rines = int(input())
    if(costorines == 1):
        costo_final += 0
    elif (costorines == 2):
        costo_final += 119000
    costo_asientos = int(input("Ingrese numero de asientos /5/6/7: "))
    if(costo_asientos == 5):
        costo_final += 0
    if(costo_asientos == 6):
        costo_final += 140000
    if(costo_asientos == 7):
        costo_final += 76000

    costo_interiores = str(input("Inserte interior |Negro|Blanco|Beige|:"))
    costo_interiores_mayusculas = costo_interiores.upper
    if(costo_interiores_mayusculas == "NEGRO"):
        costo_final += 0
    elif(costo_interiores_mayusculas != "NEGRO"):
        costo_final += 32400
    print("Inserte 'si', si quiere agregar el servicio de autopilot")
    print("Inserte'no', si usted no lo quiere agregar: ")
    autopilot = str(input())
    autopilot_mayusculas = autopilot.upper
    if(autopilot_mayusculas == "SI"):
        costo_final += 177200
    elif(autopilot_mayusculas == "NO"):
        costo_final += 0
    print("El costo final de su vehiculo sera de: ", costo_final)
    print()
    print("Inserte '1' si usted quiere adquirir el vehiculo")
    print("Inserte '2' si no quiere realizar la compra")
    sugerencia = int(input())
    if(sugerencia == 1):
        return print(datos_pago())
    elif(sugerencia != 1):
        return print("Gracias por usar el modelo personalizado de TESLA")


def compramodel3():
    '''
    El objetivo de esta función es el poder tener un servio personalizado
    al adquirir un vehiculo (Tesla model 3), además de que al incio
    coloca la imagen del vehiculo. La personalización cubre datos como
    el color, versión,etc.
    '''
    im = Image.open("3.jpg")
    box = (350, 300, 1550, 1000)
    area_recortada = im.crop(box)
    area_recortada.show()
    texto = open("model3.txt", "r")

    print(texto.read())

    texto.close()

    costo_final = 0
    costo_base = str(input("Inserte la versión que desea adquirir: "))
    costo_base_mayusculas = costo_base.upper()
    if(costo_base_mayusculas == "AUTONOMIA ESTANDAR PLUS"):
        costo_final += 1049900
    elif(costo_base_mayusculas == "AUTONOMIA MAYOR"):
        costo_final += 1249900
    elif(costo_base_mayusculas == "PERFORMANCE" or costobase == "performance"):
        costo_final += 1349900
    costo_color = str(input("Inserte color |Blanco|Negro|Gris|Azul|Rojo: "))
    costo_color_mayusculas = costo_color.upper()
    if(costo_color_mayusculas == "BLANCO"):
        costo_final += 0
    elif(costo_color_mayusculas != "BLANCO"):
        costo_final += 21600
    costo_interiores = str(input("Inserte color interiores |Negro|Blanco|: "))
    costo_interiores_mayusculas = costo_interiores.upper()
    if(costo_interiores_mayusculas == "NEGRO"):
        costo_final += 0
    elif(costo_interiores_mayusculas != "NEGRO"):
        costo_final += 21600
    print("Inserte 'si', si usted quiere agregar el servicio de autopilot: ")
    print("Inserte 'no', si usted no lo quiere agregar: ")
    autopilot = str(input())
    autopilot_mayusculas = autopilot.upper()
    if(autopilot_mayusculas == "SI"):
        costo_final += 177200
    elif(autopilot_mayusculas == "NO"):
        costo_final += 0
    print("El costo final de su vehiculo sera de: ", costo_final)
    print()
    print("Inserte '1' si usted quiere proceder con la compra")
    print("Inserte '2' si no quiere realizar la compra")
    sugerencia = int(input())
    if(sugerencia == 1):
        return print(datos_pago())
    elif(sugerencia != 1):
        return print("Gracias por usar el modelo personalizado de TESLA")
'''
========  parte principal del programa =========
Esta es la parte inicial del codigo, en base a estas dos condiciones
se puede accesar a cualquier parte del codigo, esto depende de lo que
busque el usuario o empleado.
'''

print("Escriba 1 si quiere adquirir un vehiculo Tesla: ")
print("Escriba 2 si quiere entrar a la base de perfiles de la empresa: ")
direccion_usuario = int(input())
if(direccion_usuario == 1):
    print(compra())
elif(direccion_usuario == 2):
    print(organigrama())

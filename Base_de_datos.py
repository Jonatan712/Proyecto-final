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

'''================== funciones ==================='''


def revisar_cadena(texto_inicio, texto_error):
    '''
    Esta función tiene como objetivo revisar que los datos
    introducidos por el usuario conrrespondan a una cadena
    de texto. La función recibe como parametro los textos
    que le aparecen al usuario y esta devuelve un valor
    de cadena, si no es una cadena vuelve a correr el ciclo
    hasta obtener strings.
    '''
    while True:
        cadena = input(texto_inicio)
        try:
            cadena = int(cadena)
            print(texto_error)
        except (ValueError):
            cadena = str(cadena)
            return cadena
            break


def revisar_enteros(texto_inicio, texto_error):
    '''
    Esta función tiene como objetivo revisar que los datos
    introducidos por el usuario conrrespondan a valores
    numericos. La función recibe como parametro los textos
    que le aparecen al usuario y esta devuelve un valor
    numerico, si no es un "int" vuelve a correr el ciclo
    hasta obtener numeros enteros.
    '''
    while True:
        try:
            valor = int(input(texto_inicio))
            return valor
            break
        except (ValueError):
            print(texto_error)


def organigrama(numero):
    '''
    Esta es la función que hace posible la produccion de un organigrama,
    primero solicita los perfiles a agregar, llenas los perfiles, y al final
    tienes la opcion de obtener el perfil de cualquier persona.

    '''
    perfiles = []
    primer_valor_matriz = 0
    segundo_valor_matriz = 0
    acumulador = 0
    number = 2
    while acumulador < numero:
        texto_inicio = "Inserte nombre completo: "
        texto_error = "Error: Debe de insertar su nombre:"
        nombre = revisar_cadena(texto_inicio, texto_error)
        texto_inicio = "Inserte su edad: "
        texto_error = "Error: Debe de insertar un valor numerico"
        edad = revisar_enteros(texto_inicio, texto_error)
        texto_inicio = "Inserte sexo: "
        texto_error = "Error: Debe de insertar su sexo"
        sexo = revisar_cadena(texto_inicio, texto_error)
        texto_inicio = "Estado civil: "
        texto_error = "Error: Debe de insertar su estado civil"
        est_civ = revisar_cadena(texto_inicio, texto_error)
        texto_inicio = "Inserte cargo en la empresa: "
        texto_error = "Error: Debe de insertar su cargo en la empresa"
        cargo = revisar_cadena(texto_inicio, texto_error)
        texto_inicio = "Inserte su nacionalidad: "
        texto_error = "Error: Debe de insertar su nacionalidad"
        nacio = revisar_cadena(texto_inicio, texto_error)
        texto_inicio = "Inserte su numero de contacto: "
        texto_error = "Error: Debe de insertar un valor numerico"
        numeroo = revisar_enteros(texto_inicio, texto_error)
        acumulador += 1
        if(number <= numero):
            print("Inserte la informacion del perfil número", number)

        persona = [nombre, edad, sexo, est_civ, cargo, nacio, numeroo]
        perfiles.append(persona)
        number += 1
    return perfiles


def compra(preferencia_cliente):
    '''
    Al aplicar esta función se obtiene el str del modelo
    elegido por el usuario, esta recibe un valor entero y
    la compara con una serie ifs para que al obtener el
    nombre del modelo sea este el return de la función,
    AL obtener el return de esta funcion, este se compara
    con otros modelos y luego se dirije a la funcion de compra
    del modelo elegido.
    '''
    primer_modelo = "models"
    segundo_modelo = "modelx"
    tercer_modelo = "model3"
    opcion_cliente = ""
    if(preferencia_cliente == 1):
        opcion_cliente = primer_modelo
    elif(preferencia_cliente == 2):
        opcion_cliente = segundo_modelo
    elif(preferencia_cliente == 3):
        opcion_cliente = tercer_modelo
    return(opcion_cliente)


def datos_pago(nombre_mayus, tajeta_mayus, digitos, fecha, datos_seguridad):
    '''
    Esta función recibe 5 datos, estos sirven para crear un perfil
    de compra, recibe datos del usuario para continuar con la
    adquisicion del usuario; esta función entra al finalizar la
    personalizacion de algun modelo de TESLA.
    '''
    datos_comprador = []
    datos_comprador.append([nombre_mayus])
    datos_comprador.append([tajeta_mayus])
    datos_comprador.append([digitos])
    datos_comprador.append([fecha])
    datos_comprador.append([datos_seguridad])
    return datos_comprador


def confirmacion_datos(datos_comprador):
    '''
    Esta funcion recibe como parametro el resultado de la función
    pasada (datos_pago), el objetivo de esta función es imprimir
    la información brindada por el usuario y preguntar si es
    correcta, si no lo es, se puede cambiar cualquier dato, la
    función devuelve un perfil correcto de datos del usuario.
    '''
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
        frase_final = "Para finalizar dirijase a: https://www.tesla.com/es_mx"
        if (información == 1):
            print()
            return frase_final
            break
        if (información == 2):
            modificacion = int(input("Inserte el numero de dato erroneo: "))
            modificacion -= 1
            correccion = input("Inserte la correcion del dato: ")
            if(modificacion == 0 or modificacion == 1):
                correccion = correccion.upper()
            datos_comprador[modificacion] = correccion


def compramodels(c_b_m, c_c_m, cr, c_i_m, a_m):
    '''
    El objetivo de esta función es el poder tener un servio personalizado
    al adquirir un vehiculo (Tesla model S), además de que al incio coloca
    la imagen del vehiculo. La personalización cubre datos como el color,
    versión,etc. y los introduce en una serie de ifs, todo esto para
    obtener un precio final del vehiculo seleccionado.
    '''
    costo_final = 0
    if(c_b_m == "PLAID"):
        costo_final += 3099900
    elif(c_b_m == "PERFORMANCE"):
        costo_final += 2123900
    elif(c_b_m == "LONG RANGE PLUS"):
        costo_final += 1823900
    if(c_c_m == "BLANCO"):
        costo_final += 0
    elif(c_c_m != "BLANCO"):
        costo_final += 32500
    if(cr == 1):
        costo_final += 0
    elif (cr == 2):
        costo_final += 97000
    if(c_i_m == "NEGRO"):
        costo_final += 0
    elif(c_i_m != "NEGRO"):
        costo_final += 32400
    if(a_m == "SI"):
        costo_final += 177200
    elif(a_m == "NO"):
        costo_final += 0
    return costo_final


def compramodelx(c_b_m, c_c_m, c_r, c_a, c_i_m, a_m):
    '''
    El objetivo de esta función es el poder tener un servio personalizado
    al adquirir un vehiculo (Tesla model X), además de que al incio coloca
    la imagen del vehiculo. La personalización cubre datos como el color,
    versión,etc. y los introduce en una serie de ifs, todo esto para
    obtener un precio final del vehiculo seleccionado.
    '''
    costo_final = 0
    if(c_b_m == "LONG RANGE PLUS"):
        costo_final += 1998900
    elif(c_b_m == "PERFORMANCE"):
        costo_final += 2298900
    if(c_c_m == "BLANCO"):
        costo_final += 0
    elif(c_c_m != "BLANCO"):
        costo_final += 32400
    if(c_r == 1):
        costo_final += 0
    elif (c_r == 2):
        costo_final += 119000
    if(c_a == 5):
        costo_final += 0
    elif(c_a == 6):
        costo_final += 140000
    elif(c_a == 7):
        costo_final += 76000
    if(c_i_m == "NEGRO"):
        costo_final += 0
    elif(c_i_m != "NEGRO"):
        costo_final += 32400
    if(a_m == "SI"):
        costo_final += 177200
    elif(a_m == "NO"):
        costo_final += 0
    return costo_final


def compramodel3(c_b_m, c_c_m, c_i_m, a_m):
    '''
    El objetivo de esta función es el poder tener un servio personalizado
    al adquirir un vehiculo (Tesla model 3), además de que al incio coloca
    la imagen del vehiculo. La personalización cubre datos como el color,
    versión,etc. y los introduce en una serie de ifs, todo esto para
    obtener un precio final del vehiculo seleccionado.
    '''
    costo_final = 0
    if(c_b_m == "AUTONOMIA ESTANDAR PLUS"):
        costo_final += 1049900
    elif(c_b_m == "AUTONOMIA MAYOR"):
        costo_final += 1249900
    elif(c_b_m == "PERFORMANCE" or costobase == "performance"):
        costo_final += 1349900
    if(c_c_m == "BLANCO"):
        costo_final += 0
    elif(c_c_m != "BLANCO"):
        costo_final += 21600
    if(c_i_m == "NEGRO"):
        costo_final += 0
    elif(c_i_m != "NEGRO"):
        costo_final += 21600
    if(a_m == "SI"):
        costo_final += 177200
    elif(a_m == "NO"):
        costo_final += 0
    return costo_final
'''
========  parte principal del programa =========
Esta es la parte inicial del codigo, en base a estas dos condiciones
se puede accesar a cualquier parte del codigo, esto depende de lo que
busque el usuario o empleado. A lo largo del codigo cada dato contiene
un ciclo while, cuya función es obligar al usuario a introducir la
información en el formato correcto.
'''
print("Escriba 1 si quiere entrar a la base de perfiles de la empresa: ")
print("Escriba 2 si quiere adquirir un vehiculo Tesla: ")
while True:
    direccion_usuario = input()
    if (direccion_usuario == "1" or direccion_usuario == "2"):
        direccion_usuario = int(direccion_usuario)
        break
    else:
        print("Debe de ser valor '1' o '2'")
if(direccion_usuario == 1):
    while True:
        try:
            numero = int(input("Inserte numero de perfiles que registrara: "))
            break
        except (ValueError):
            print("Error: Debe de insertar un valor numerico")
    perfiles = (organigrama(numero))
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
    uno_val_mat = 0
    seg_val_mat = 0
    while True:
        try:
            perfil_solicitado = int(input())
            break
        except (ValueError):
            print("Error: Debe de insertar un valor numerico")
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
                print("Cargo en empresa: ", perfiles[uno_val_mat][seg_val_mat])
                seg_val_mat += 1
                print("Nacionalidad: ", perfiles[uno_val_mat][seg_val_mat])
                seg_val_mat += 1
                print("Numero contacto: ", perfiles[uno_val_mat][seg_val_mat])
                break
        else:
                contador += 1
                uno_val_mat += 1

elif(direccion_usuario == 2):
    print("Escriba 1 si quiere entrar a la pagina de compra del Model S: ")
    print("Escriba 2 si quiere entrar a la pagina de compra del Model X: ")
    print("Escriba 3 si quiere entrar a la pagina de compra del Model 3: ")
    while True:
        try:
            preferencia_cliente = int(input())
            break
        except (ValueError):
            print("Error: Debe de insertar un valor numerico")
    modelo = (compra(preferencia_cliente))
    if(modelo == "models"):
        imagen = Image.open("s.jpeg")
        box = (500, 300, 2400, 1500)
        area_recortada = imagen.crop(box)
        area_recortada.show()
        imprimir_texto = open("models.txt", "r")
        print(imprimir_texto.read())
        imprimir_texto.close()
        while True:
            version = input("Inserte la versión deseada: ")
            v_m = version.upper()
            a_p = "PLAID"
            a_pe = "PERFORMANCE"
            a_lrp = "LONG RANGE PLUS"
            if (v_m == a_p or v_m == a_pe or v_m == a_lrp):
                costo_base_mayusculas = v_m
                break
            else:
                print("Error: Debe de insertar el nombre de la versión:")
        print()
        while True:
            color = input("Inserte el color |BLANCO|NEGRO|GRIS|: ")
            c_m = color.upper()
            if (c_m == "BLANCO" or c_m == "NEGRO" or c_m == "GRIS"):
                costo_color_mayusculas = c_m
                break
            else:
                print("Error: Debe de insertar el color deseado:")
        print()
        print('''Inserte '1' si usted quiere los rines Tempest de 19"''')
        print('''Inserte '2' si quiere rines Twin Turbine de 21"''')
        while True:
            costorines = input()
            if (costorines == "1" or costorines == "2"):
                costorines = int(costorines)
                break
            else:
                print("Debe de ser valor '1' o '2'")
        print()
        while True:
            color_int = input("Inserte color interior |BLANCO|BEIGE|NEGRO|: ")
            ci_m = color_int.upper()
            if (ci_m == "BLANCO" or ci_m == "BEIGE" or ci_m == "NEGRO"):
                costo_interiores_mayusculas = ci_m
                break
            else:
                print("Error: Debe de insertar el color deseado:")
        print()
        print("Inserte 'si', si usted quiere el servicio de autopilot: ")
        print("Inserte 'no', si usted no lo quiere agregar: ")
        while True:
            autopilot = input()
            at = autopilot.upper()
            if (at == "SI" or at == "NO"):
                autopilot_mayusculas = at
                break
            else:
                print("Debe de ser la palabra 'si' o 'no'")
        a_cbm = costo_base_mayusculas
        a_ccm = costo_color_mayusculas
        a_cr = costorines
        a_cim = costo_interiores_mayusculas
        a_am = autopilot_mayusculas
        models = (compramodels(a_cbm, a_ccm, a_cr, a_cim, a_am))
        print()
        print("El costo final de su vehiculo sera de: ", models)
    if(modelo == "modelx"):
        imagen = Image.open("x.jpeg")
        box = (500, 200, 2400, 1400)
        area_recortada = imagen.crop(box)
        area_recortada.show()
        texto = open("modelx.txt", "r")
        print(texto.read())
        texto.close()
        while True:
            version = input("Inserte la versión que desea adquirir: ")
            v_m = version.upper()
            if (v_m == "LONG RANGE PLUS" or v_m == "PERFORMANCE"):
                costo_base_mayusculas = v_m
                break
            else:
                print("Error: Debe de insertar el nombre de la versión:")
        print()
        while True:
            color = input("Inserte el color |BLANCO|NEGRO|GRIS|: ")
            c_m = color.upper()
            if (c_m == "BLANCO" or c_m == "NEGRO" or c_m == "GRIS"):
                costo_color_mayusculas = c_m
                break
            else:
                print("Error: Debe de insertar el color deseado:")
        print()
        print('''Inserte '1' si usted quiere los rines Silver de 20"''')
        print('''Inserte '2' si usted quiere los rines negro onyx de 22"''')
        while True:
            costorines = input()
            if (costorines == "1" or costorines == "2"):
                costo_rines = int(costorines)
                break
            else:
                print("Debe de ser valor '1' o '2'")
        print()
        while True:
            asientos = input("Ingrese numero de asientos /5/6/7: ")
            if (asientos == "5" or asientos == "6" or asientos == "7"):
                costo_asientos = int(asientos)
                break
            else:
                print("Debe de ser valor '5','6' o '7'")
        print()
        while True:
            color_int = input("Inserte color interior |NEGRO|BLANCO|BEIGE|: ")
            ci_m = color_int.upper()
            if (ci_m == "BLANCO" or ci_m == "BEIGE" or ci_m == "NEGRO"):
                costo_interiores_mayusculas = ci_m
                break
            else:
                print("Error: Debe de insertar el color deseado:")
        print()
        print("Inserte 'si', si usted quiere el servicio de autopilot: ")
        print("Inserte 'no', si usted no lo quiere agregar: ")
        while True:
            autopilot = input()
            at = autopilot.upper()
            if (at == "SI" or at == "NO"):
                autopilot_mayusculas = at
                break
            else:
                print("Debe de ser la palabra 'si' o 'no'")
        a_cbm = costo_base_mayusculas
        a_ccm = costo_color_mayusculas
        a_cr = costo_rines
        a_ca = costo_asientos
        a_cim = costo_interiores_mayusculas
        a_am = autopilot_mayusculas
        modelx = (compramodelx(a_cbm, a_ccm, a_cr, a_ca, a_cim, a_am))
        print("El costo final de su vehiculo sera de: ", modelx)
    if(modelo == "model3"):
        im = Image.open("3.jpg")
        box = (350, 300, 1550, 1000)
        area_recortada = im.crop(box)
        area_recortada.show()
        texto = open("model3.txt", "r")
        print(texto.read())
        texto.close()
        while True:
            version = input("Inserte la versión deseada: ")
            v_m = version.upper()
            abrv_aep = "AUTONOMIA ESTANDAR PLUS"
            abrv_am = "AUTONOMIA MAYOR"
            abrv_p = "PERFORMANCE"
            if (v_m == abrv_aep or v_m == abrv_am or v_m == abrv_p):
                costo_base_mayusculas = v_m
                break
            else:
                print("Error: Debe de insertar el nombre de la versión:")
        print()
        while True:
            color = input("Inserte el color |BLANCO|NEGRO|AZUL|: ")
            c_m = color.upper()
            if (c_m == "BLANCO" or c_m == "NEGRO" or c_m == "AZUL"):
                costo_color_mayusculas = c_m
                break
            else:
                print("Error: Debe de insertar el color deseado:")
        print()
        while True:
            color_int = input("Inserte color del interior |BLANCO|NEGRO|: ")
            ci_m = color_int.upper()
            if (ci_m == "BLANCO" or ci_m == "NEGRO"):
                costo_interiores_mayusculas = ci_m
                break
            else:
                print("Error: Debe de insertar el color deseado:")
        print()
        print("Inserte 'si', si usted quiere el servicio de autopilot: ")
        print("Inserte 'no', si usted no lo quiere agregar: ")
        while True:
            autopilot = input()
            at = autopilot.upper()
            if (at == "SI" or at == "NO"):
                autopilot_mayusculas = at
                break
            else:
                print("Debe de ser la palabra 'si' o 'no'")
        abrv1 = costo_base_mayusculas
        abrv2 = costo_color_mayusculas
        abrv3 = costo_interiores_mayusculas
        abrv4 = autopilot_mayusculas
        model3 = (compramodel3(abrv1, abrv2, abrv3, abrv4))
        print("El costo final de su vehiculo sera de: ", model3)
    print()
    print("Inserte '1' si usted quiere proceder con la compra")
    print("Inserte '2' si no quiere realizar la compra")
    while True:
        try:
            sugerencia = int(input())
            break
        except (ValueError):
            print("Error: Debe de insertar un valor numerico")
    if(sugerencia == 1):
        texto_inicio = "Inserte nombre completo: "
        texto_error = "Error: Debe de insertar su nombre:"
        nombre = revisar_cadena(texto_inicio, texto_error)
        nombre_mayusculas = nombre.upper()
        while True:
            tarjeta = input("Inserte su tipo de tarjeta (Debito o Credito): ")
            t_m = tarjeta.upper()
            if (t_m == "DEBITO" or t_m == "CREDITO"):
                tajeta_mayusculas = t_m
                break
            else:
                print("Error: Debe de insertar 'debito' o 'credito':")
        texto_inicio = "Inserte los 16 digitos de su tarjeta: "
        texto_error = "Error: Debe de insertar valores numericos"
        digitos = revisar_enteros(texto_inicio, texto_error)
        fecha = (input("Inserte fecha de vencimiento ( 00/00 ): "))
        while True:
            try:
                datos_seguridad = int(input("Ingrese 4 digitos de seguridad:"))
                datos_seguridad = str(datos_seguridad)
                if(len(datos_seguridad) == 4):
                    atos_seguridad = int(datos_seguridad)
                    break
                else:
                    print("Error: Debe de insertar 4 valores numericos")
            except (ValueError):
                print("Error: Debe de insertar 4 valores numericos")
        abrev1 = nombre_mayusculas
        abrev2 = tajeta_mayusculas
        abrev3 = datos_seguridad
        datos_comprador = (datos_pago(abrev1, abrev2, digitos, fecha, abrev3))
        confirmacion = (confirmacion_datos(datos_comprador))
        print(confirmacion)
    elif(sugerencia != 1):
        print("Gracias por usar el modelo personalizado de TESLA")

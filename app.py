print('''
**********************************************
*     VALOR A PAGAR DE PRODUCTOS COMPRADOS   *
**********************************************
      ''')
valor_unitario_manzanas = 1000
valor_unitario_peras = 1500
valor_unitario_bananos = 2000

'''
    FUNCIÓN PARA REUTILIZAR
'''

def evaluar_valor(variable,fruta):
    nueva_variable = variable
    while nueva_variable < 0:
        print('Digite un número igual o superior a 0')
        nueva_variable = int(input(f'Ingresa cantidad de {fruta} :'))
    return nueva_variable

'''
    SECUENCIA DE FRUTAS
'''
lista_frutas_disponibles = ['manzana','pera','banano']

fruta_ingresada = input('Digitar el nombre de la fruta que deseas comprar: ')

'''
    OPERADOR DE PERTENENCIA
'''
while fruta_ingresada not in lista_frutas_disponibles:
    print('¡¡¡ALERTA!!! No tenemos la fruta ingresada en inventario')
    fruta_ingresada = input('Digitar de nuevo el nombre de la fruta que deseas comprar: ')

cant_manz = 0
cant_peras = 0
cant_bananos = 0

'''
    CONDICIONAL IF
'''

if fruta_ingresada == 'manzana':

    cant_manz = int(input("Ingresa cantidad de manzanas: "))
    cant_manz = evaluar_valor(cant_manz,'manzana')

elif fruta_ingresada == 'pera':

    cant_peras = int(input("Ingresa cantidad de peras: "))
    cant_peras = evaluar_valor(cant_peras,'peras')

elif fruta_ingresada == 'banano':

    cant_bananos = int(input("Ingresa cantidad de bananos: "))
    cant_bananos = evaluar_valor(cant_bananos,'bananos')
'''
    TODO: CONCATENAR
'''
valor_total_a_pagar = valor_unitario_manzanas*cant_manz + \
                      valor_unitario_peras*cant_peras + \
                      valor_unitario_bananos*cant_bananos
print(f'''
******************************************************
*             EL VALOR TOTAL A PAGAR ES DE:          *
*                      ${valor_total_a_pagar}  
******************************************************
      ''')

# sentencias de control if, elif
from app.service.te.te import Te, set_nombre, get_nombre

te_1 = Te()
te_2 = Te()

te_1 = set_nombre("te_negro")
te_2 = set_nombre("te_verde")

def tipo_data():
    type_data_te_1 = type(te_1)
    type_data_te_2 = type(te_2)

    print(f'Valor de te_1: {te_1}, Tipo de dato: {type_data_te_1}, Valor de te_2: {te_2}, tipo de dato: {type_data_te_2}')

    if type_data_te_1 == type_data_te_2:
        print('Ambos objetos son del mismo tipo')
    else:
        print('Los objetos no son del mismo tipo')

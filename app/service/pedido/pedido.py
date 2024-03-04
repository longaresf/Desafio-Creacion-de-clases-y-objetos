from app.service.te.te import Te, tiempo_recomendación, precio_formato

def crear_pedido():
    print('Para pedido, favor contestar las siguientes preguntas:')
    tipo_te = int(input("¿Qué tipo de té quieres?\nFavor presiona 1 para Té Negro, 2 para Té Verde ó 3 para Agua de hierbas "))
    formato_te = int(input("¿Tipo de formato?\n1 para formato de 300gr o 2 para formato de 500gr "))
    Cantidad_te = int(input("¿Cuánta cantidad de té quieres?\n Favor escribe un monto "))

    monto_total = precio_formato(formato_te)[0] * Cantidad_te

    print(f'''  Usted eligió {tiempo_recomendación(tipo_te)[2]}, en formato de {precio_formato(formato_te)[1]}gr,
                el precio a pagar es CLP {precio_formato(formato_te)[0]},
                tiene un tiempo de preparación de {tiempo_recomendación(tipo_te)[0]},
                se recomienda {tiempo_recomendación(tipo_te)[1]},
                el monto total a pagar es  CLP {monto_total}".
                Todos los té tienen un tiempo de duración de 1 año o 365 días''')

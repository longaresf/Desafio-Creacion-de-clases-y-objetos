class Te():
    sabor = ['té negro', 'té verde', 'Infusión de hierbas']
    formatos = ['300', '500']
    Precios = [3000, 5000]
    tiempo = ['3 minutos', '5 minutos', '6 minutos']
    recomendacion = {'té negro': 'al desayuno', 'té verde': 'al medio día', 'Infusión de hierbas': 'al atardecer'}

def set_nombre(nombre:str):
    return nombre

def get_nombre(self):
    return self.nombre

@staticmethod
def tiempo_recomendación(tipo_te:int):
    if tipo_te == 1:    # Té Negro
        return Te.tiempo[0], Te.recomendacion[Te.sabor[0]], Te.sabor[0]
    elif tipo_te == 2:   # Té Verde
        return Te.tiempo[1], Te.recomendacion[Te.sabor[1]], Te.sabor[1]
    else:               # Infusión de Hierbas
        return Te.tiempo[2], Te.recomendacion[Te.sabor[2]], Te.sabor[2]

@staticmethod
def precio_formato(formato_te:int):
    if formato_te == 1:    # Bolsa de 300gr
        return Te.Precios[0], Te.formatos[0]
    else:                   # Bolsa de 500gr
        return Te.Precios[1], Te.formatos[1]
    
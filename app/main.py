from app.service.pedido.pedido import crear_pedido
from app.service.instancias.instancias import tipo_data
from app.service.te.te import Te, tiempo_recomendación, precio_formato, get_nombre, set_nombre

def app():
    crear_pedido()
    tipo_data()
    
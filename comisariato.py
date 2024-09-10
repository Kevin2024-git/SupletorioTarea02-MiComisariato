# Variables globales
productos = []  # Lista para almacenar productos
usuarios = []   # Lista para almacenar usuarios

# Función principal para mostrar el menú
def menu_principal():
    print("\n--- Sistema de Ventas Mi Comisariato ---")
    print("1. Gestión de Productos")
    print("2. Gestión de Usuarios")
    print("3. Generar Factura de Venta")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion  # Devuelve la opción seleccionada

# Función para gestionar productos
def gestionar_productos():
    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Añadir Producto")
        print("2. Listar Productos")
        print("3. Eliminar Producto")
        print("4. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            producto = crear_producto()
            if producto:
                productos.append(producto)
                print(f"Producto '{producto['nombre']}' añadido con éxito.")
        elif opcion == '2':
            listar_productos()
        elif opcion == '3':
            eliminar_producto()
        elif opcion == '4':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Función para crear un producto
def crear_producto():
    nombre = input("Ingrese el nombre del producto: ")
    try:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad en stock: "))
    except ValueError:
        print("Error: Precio o cantidad no válidos.")
        return None
    return {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}

# Función para listar productos
def listar_productos():
    if not productos:
        print("No hay productos registrados.")
    else:
        print("\n--- Lista de Productos ---")
        for i, producto in enumerate(productos):
            print(f"{i + 1}. {producto['nombre']} - Precio: ${producto['precio']} - Cantidad: {producto['cantidad']}")

# Función para eliminar un producto
def eliminar_producto():
    listar_productos()
    if not productos:
        return
    try:
        producto_index = int(input("Seleccione el número del producto a eliminar: ")) - 1
        if 0 <= producto_index < len(productos):
            eliminado = productos.pop(producto_index)
            print(f"Producto '{eliminado['nombre']}' eliminado con éxito.")
        else:
            print("Producto no válido.")
    except ValueError:
        print("Entrada no válida.")

# Función para gestionar usuarios
def gestionar_usuarios():
    while True:
        print("\n--- Gestión de Usuarios ---")
        print("1. Registrar Usuario")
        print("2. Listar Usuarios")
        print("3. Editar Usuario")
        print("4. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            usuario = crear_usuario()
            if usuario:
                usuarios.append(usuario)
                print(f"Usuario '{usuario['nombre']}' registrado con éxito.")
        elif opcion == '2':
            listar_usuarios()
        elif opcion == '3':
            editar_usuario()
        elif opcion == '4':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Función para crear un usuario
def crear_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    cedula = input("Ingrese la cédula del usuario: ")
    if len(cedula) != 10 or not cedula.isdigit():
        print("Cédula no válida.")
        return None
    return {'nombre': nombre, 'cedula': cedula}

# Función para listar usuarios
def listar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        print("\n--- Lista de Usuarios ---")
        for i, usuario in enumerate(usuarios):
            print(f"{i + 1}. {usuario['nombre']} - Cédula: {usuario['cedula']}")

# Función para editar un usuario
def editar_usuario():
    listar_usuarios()
    if not usuarios:
        return
    try:
        usuario_index = int(input("Seleccione el número del usuario a editar: ")) - 1
        if 0 <= usuario_index < len(usuarios):
            usuario = usuarios[usuario_index]
            nuevo_nombre = input(f"Ingrese el nuevo nombre (actual: {usuario['nombre']}): ")
            nueva_cedula = input(f"Ingrese la nueva cédula (actual: {usuario['cedula']}): ")
            if len(nueva_cedula) == 10 and nueva_cedula.isdigit():
                usuarios[usuario_index] = {'nombre': nuevo_nombre, 'cedula': nueva_cedula}
                print("Usuario actualizado con éxito.")
            else:
                print("Cédula no válida.")
        else:
            print("Usuario no válido.")
    except ValueError:
        print("Entrada no válida.")

# Función para generar factura
def generar_factura():
    if not productos:
        print("No hay productos disponibles para la venta.")
        return
    if not usuarios:
        print("No hay usuarios registrados para crear una factura.")
        return

    usuario = seleccionar_usuario()
    if not usuario:
        print("Usuario no válido.")
        return

    total, factura = crear_factura()

    print("\n--- Factura de Venta ---")
    print(f"Cliente: {usuario['nombre']} - Cédula: {usuario['cedula']}")
    for item in factura:
        print(f"{item['producto']} - Cantidad: {item['cantidad']} - Subtotal: ${item['subtotal']:.2f}")
    print(f"Total a pagar: ${total:.2f}")

# Función para seleccionar un usuario
def seleccionar_usuario():
    listar_usuarios()
    try:
        usuario_index = int(input("Seleccione el número del usuario para la factura: ")) - 1
        return usuarios[usuario_index] if 0 <= usuario_index < len(usuarios) else None
    except ValueError:
        return None

# Función para crear factura
def crear_factura():
    total = 0
    factura = []

    while True:
        listar_productos()
        try:
            producto_index = int(input("Seleccione el número del producto a comprar (0 para finalizar): ")) - 1
            if producto_index == -1:
                break
            if 0 <= producto_index < len(productos):
                producto = productos[producto_index]
                cantidad = int(input(f"Ingrese la cantidad de '{producto['nombre']}' a comprar: "))
                if cantidad > producto['cantidad']:
                    print(f"No hay suficiente stock. Disponible: {producto['cantidad']}")
                    continue
                producto['cantidad'] -= cantidad
                subtotal = cantidad * producto['precio']
                total += subtotal
                factura.append({'producto': producto['nombre'], 'cantidad': cantidad, 'subtotal': subtotal})
                print(f"{cantidad} unidades de '{producto['nombre']}' añadidas a la factura.")
            else:
                print("Producto no válido.")
        except ValueError:
            print("Entrada no válida.")
    
    return total, factura

# Ejecutar el menú principal
while True:
    opcion = menu_principal()
    if opcion == '1':
        gestionar_productos()
    elif opcion == '2':
        gestionar_usuarios()
    elif opcion == '3':
        generar_factura()
    elif opcion == '4':
        print("Gracias por usar el sistema de ventas.")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")

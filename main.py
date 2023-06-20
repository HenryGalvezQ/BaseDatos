import mysql.connector

# Datos de conexión a la base de datos
host = 'localhost'
port = 3306
user = 'root'
password = 'root'
database = 'control_stock_libreria'

# Función para establecer la conexión a la base de datos
def establecer_conexion():
    try:
        conexion = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
         # La conexión se realizó con éxito
        print("Conexión exitosa a la base de datos.")
        return conexion
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None

# Función para cerrar la conexión a la base de datos
def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada.")

# Función para insertar registros en la tabla GZZ_ESTADO_REGISTRO
def insertar_estado_registro(conexion, codigo, descripcion, estado_registro):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO GZZ_ESTADO_REGISTRO (EstRegCod, EstRegDes, EstRegEstReg) VALUES (%s, %s, %s)"
        valores = (codigo, descripcion, estado_registro)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla GZZ_ESTADO_REGISTRO.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla GZZ_ESTADO_REGISTRO:", error)

# Función para seleccionar todos los registros de la tabla GZZ_ESTADO_REGISTRO
def seleccionar_estado_registro(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM GZZ_ESTADO_REGISTRO")
        registros = cursor.fetchall()
        print("Registros en la tabla GZZ_ESTADO_REGISTRO:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla GZZ_ESTADO_REGISTRO:", error)

# Función para insertar registros en la tabla GZZ_ZONA
def insertar_zona(conexion, codigo, descripcion):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO GZZ_ZONA (ZonCod, ZonDes) VALUES (%s, %s)"
        valores = (codigo, descripcion)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla GZZ_ZONA.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla GZZ_ZONA:", error)

# Función para seleccionar todos los registros de la tabla GZZ_ZONA
def seleccionar_zona(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM GZZ_ZONA")
        registros = cursor.fetchall()
        print("Registros en la tabla GZZ_ZONA:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla GZZ_ZONA:", error)

# Función para insertar registros en la tabla GZZ_MARCA
def insertar_marca(conexion, codigo, nombre, estado_registro):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO GZZ_MARCA (MarCod, MarNom, MarEstReg) VALUES (%s, %s, %s)"
        valores = (codigo, nombre, estado_registro)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla GZZ_MARCA.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla GZZ_MARCA:", error)

# Función para seleccionar todos los registros de la tabla GZZ_MARCA
def seleccionar_MARCA(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM GZZ_MARCA")
        registros = cursor.fetchall()
        print("Registros en la tabla GZZ_MARCA:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla GZZ_MARCA:", error)

# Función para insertar registros en la tabla GZZ_UNIDAD_MEDIDA
def insertar_unidad_medida(conexion, codigo, nombre, estado_registro):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO GZZ_UNIDAD_MEDIDA (UniMedCod, UniMedNom, EstRegCod) VALUES (%s, %s, %s)"
        valores = (codigo, nombre, estado_registro)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla GZZ_UNIDAD_MEDIDA.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla GZZ_UNIDAD_MEDIDA:", error)

# Función para seleccionar todos los registros de la tabla GZZ_UNIDAD_MEDIDA
def seleccionar_unidad_medida(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM GZZ_UNIDAD_MEDIDA")
        registros = cursor.fetchall()
        print("Registros en la tabla GZZ_UNIDAD_MEDIDA:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla GZZ_UNIDAD_MEDIDA:", error)

# Función para insertar registros en la tabla GZZ_EMPLEADO
def insertar_empleado(conexion, codigo, nombre, estado_registro):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO GZZ_EMPLEADO (VenCod, VenNom, EstRegCod) VALUES (%s, %s, %s)"
        valores = (codigo, nombre, estado_registro)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla GZZ_EMPLEADO.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla GZZ_EMPLEADO:", error)

# Función para seleccionar todos los registros de la tabla GZZ_EMPLEADO
def seleccionar_empleado(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM GZZ_EMPLEADO")
        registros = cursor.fetchall()
        print("Registros en la tabla GZZ_EMPLEADO:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla GZZ_EMPLEADO:", error)

# Función para insertar registros en la tabla L1M_CLIENTE
def insertar_cliente(conexion, codigo, nombre, fecha_inscripcion, direccion, zona, estado_registro):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO L1M_CLIENTE (CliCod, CliNom, CliFecInsAño, CliDir, CliZon, CliEstReg) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (codigo, nombre, fecha_inscripcion['año'], direccion, zona, estado_registro)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla L1M_CLIENTE.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla L1M_CLIENTE:", error)

# Función para actualizar registros en la tabla L1M_CLIENTE
def actualizar_cliente(conexion, codigo, nombre, direccion):
    try:
        cursor = conexion.cursor()
        sql = "UPDATE L1M_CLIENTE SET CliNom = %s, CliDir = %s WHERE CliCod = %s"
        valores = (nombre, direccion, codigo)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro actualizado correctamente en la tabla L1M_CLIENTE.")
    except mysql.connector.Error as error:
        print("Error al actualizar registro en la tabla L1M_CLIENTE:", error)

# Función para eliminar un registro de la tabla L1M_CLIENTE
def eliminar_cliente(conexion, codigo):
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM L1M_CLIENTE WHERE CliCod = %s"
        valor = (codigo,)
        cursor.execute(sql, valor)
        conexion.commit()
        print("Registro eliminado correctamente de la tabla L1M_CLIENTE.")
    except mysql.connector.Error as error:
        print("Error al eliminar registro de la tabla L1M_CLIENTE:", error)

# Función para seleccionar todos los registros de la tabla L1M_CLIENTE
def seleccionar_clientes(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM L1M_CLIENTE")
        registros = cursor.fetchall()
        print("Registros en la tabla L1M_CLIENTE:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla L1M_CLIENTE:", error)

# Función para insertar registros en la tabla L1M_PROVEEDOR
def insertar_proveedor(conexion, codigo, nombre, anio_inscripcion, mes_inscripcion, dia_inscripcion, direccion, zona, estado_registro):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO L1M_PROVEEDOR (ProCod, ProNom, ProFecInsProAño, ProFecInsProMes, ProFecInsProDia, ProDir, ProZon, ProEstReg) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (codigo, nombre, anio_inscripcion, mes_inscripcion, dia_inscripcion, direccion, zona, estado_registro)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla L1M_PROVEEDOR.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla L1M_PROVEEDOR:", error)

# Función para actualizar un registro en la tabla L1M_PROVEEDOR
def actualizar_proveedor(conexion, codigo, nombre, anio_inscripcion, mes_inscripcion, dia_inscripcion, direccion, zona, estado_registro):
    try:
        cursor = conexion.cursor()
        sql = "UPDATE L1M_PROVEEDOR SET ProNom = %s, ProFecInsProAño = %s, ProFecInsProMes = %s, ProFecInsProDia = %s, ProDir = %s, ProZon = %s, ProEstReg = %s WHERE ProCod = %s"
        valores = (nombre, anio_inscripcion, mes_inscripcion, dia_inscripcion, direccion, zona, estado_registro, codigo)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro actualizado correctamente en la tabla L1M_PROVEEDOR.")
    except mysql.connector.Error as error:
        print("Error al actualizar registro en la tabla L1M_PROVEEDOR:", error)

# Función para eliminar un registro en la tabla L1M_PROVEEDOR
def eliminar_proveedor(conexion, codigo):
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM L1M_PROVEEDOR WHERE ProCod = %s"
        valor = (codigo,)
        cursor.execute(sql, valor)
        conexion.commit()
        print("Registro eliminado correctamente de la tabla L1M_PROVEEDOR.")
    except mysql.connector.Error as error:
        print("Error al eliminar registro de la tabla L1M_PROVEEDOR:", error)

# Función para seleccionar y mostrar los registros de la tabla L1M_PROVEEDOR
def seleccionar_proveedor(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM L1M_PROVEEDOR")
        registros = cursor.fetchall()
        print("Registros en la tabla L1M_PROVEEDOR:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla L1M_PROVEEDOR:", error)

# Función para insertar registros en la tabla L1M_ARTICULO
def insertar_articulo(conexion, codigo, nombre, cantidad, descripcion, estado_registro, marca, unidad_medida):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO L1M_ARTICULO (ArtCod, ArtNom, ArtCan, ArtDes, ArtEstReg, ArtMar, UniMedCod) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (codigo, nombre, cantidad, descripcion, estado_registro, marca, unidad_medida)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla L1M_ARTICULO.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla L1M_ARTICULO:", error)

# Función para actualizar registros en la tabla L1M_ARTICULO
def actualizar_articulo(conexion, codigo, nueva_cantidad):
    try:
        cursor = conexion.cursor()
        sql = "UPDATE L1M_ARTICULO SET ArtCan = %s WHERE ArtCod = %s"
        valores = (nueva_cantidad, codigo)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro actualizado correctamente en la tabla L1M_ARTICULO.")
    except mysql.connector.Error as error:
        print("Error al actualizar registro en la tabla L1M_ARTICULO:", error)

# Función para eliminar registros de la tabla L1M_ARTICULO
def eliminar_articulo(conexion, codigo):
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM L1M_ARTICULO WHERE ArtCod = %s"
        valores = (codigo,)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro eliminado correctamente de la tabla L1M_ARTICULO.")
    except mysql.connector.Error as error:
        print("Error al eliminar registro de la tabla L1M_ARTICULO:", error)

# Función para seleccionar todos los registros de la tabla L1M_ARTICULO
def seleccionar_articulos(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM L1M_ARTICULO")
        registros = cursor.fetchall()
        print("Registros en la tabla L1M_ARTICULO:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla L1M_ARTICULO:", error)

# Función para insertar registros en la tabla L1T_STOCK_ENTRADA_CAB
def insertar_stock_entrada_cab(conexion, codigo, fecha_ins_ano, fecha_ins_mes, fecha_ins_dia, proveedor, estado_registro, vendedor):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO L1T_STOCK_ENTRADA_CAB (StoEntCabCod, StoEntCabFecInsAño, StoEntCabFecInsMes, StoEntCabFecInsDia, StoEntCabPro, StoEntCanEstReg, VenCod) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (codigo, fecha_ins_ano, fecha_ins_mes, fecha_ins_dia, proveedor, estado_registro, vendedor)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla L1T_STOCK_ENTRADA_CAB.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla L1T_STOCK_ENTRADA_CAB:", error)

# Función para actualizar registros en la tabla L1T_STOCK_ENTRADA_CAB
def actualizar_stock_entrada_cab(conexion, codigo, nuevo_estado_registro, nuevo_proveedor):
    try:
        cursor = conexion.cursor()
        sql = "UPDATE L1T_STOCK_ENTRADA_CAB SET StoEntCanEstReg = %s, StoEntCabPro = %s WHERE StoEntCabCod = %s"
        valores = (nuevo_estado_registro, nuevo_proveedor, codigo)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro actualizado correctamente")
    except mysql.connector.Error as error:
        print("Error al actualizar registro en la tabla L1T_STOCK_ENTRADA_CAB:", error)


# Función para eliminar registros de la tabla L1T_STOCK_ENTRADA_CAB
def eliminar_stock_entrada_cab(conexion, codigo):
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM L1T_STOCK_ENTRADA_CAB WHERE StoEntCabCod = %s"
        valor = (codigo,)
        cursor.execute(sql, valor)
        conexion.commit()
        print("Registro eliminado correctamente de la tabla L1T_STOCK_ENTRADA_CAB.")
    except mysql.connector.Error as error:
        print("Error al eliminar registro de la tabla L1T_STOCK_ENTRADA_CAB:", error)

# Función para seleccionar todos los registros de la tabla L1T_STOCK_ENTRADA_CAB
def seleccionar_stock_entrada_cab(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM L1T_STOCK_ENTRADA_CAB")
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla L1T_STOCK_ENTRADA_CAB:", error)

# Función para insertar registros en la tabla L1T_STOCK_ENTRADA_DET
def insertar_stock_entrada_det(conexion, secuencia, cantidad, cabecera_codigo, articulo_codigo, cabecera_estado_registro):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO L1T_STOCK_ENTRADA_DET (StoEntCabSec, StoEntDetCan, StoEntCabCod, StoEntDetArt, StoEntCabEstReg) VALUES (%s, %s, %s, %s, %s)"
        valores = (secuencia, cantidad, cabecera_codigo, articulo_codigo, cabecera_estado_registro)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla L1T_STOCK_ENTRADA_DET.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla L1T_STOCK_ENTRADA_DET:", error)

# Función para actualizar registros en la tabla L1T_STOCK_ENTRADA_DET
def actualizar_stock_entrada_det(conexion, sec, cantidad):
    try:
        cursor = conexion.cursor()
        sql = "UPDATE L1T_STOCK_ENTRADA_DET SET StoEntDetCan = %s WHERE StoEntCabSec = %s"
        cursor.execute(sql, (cantidad, sec))
        conexion.commit()
        print("Registro actualizado exitosamente.")
    except mysql.connector.Error as error:
        print("Error al actualizar el registro en L1T_STOCK_ENTRADA_DET:", error)

# Función para eliminar registros en la tabla L1T_STOCK_ENTRADA_DET
def eliminar_stock_entrada_det(conexion, secuencia):
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM L1T_STOCK_ENTRADA_DET WHERE StoEntCabSec = %s"
        valores = (secuencia,)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro eliminado correctamente de la tabla L1T_STOCK_ENTRADA_DET.")
    except mysql.connector.Error as error:
        print("Error al eliminar registro de la tabla L1T_STOCK_ENTRADA_DET:", error)

# Función para seleccionar todos los registros de la tabla L1T_STOCK_ENTRADA_DET
def seleccionar_stock_entrada_det(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM L1T_STOCK_ENTRADA_DET")
        registros = cursor.fetchall()
        print("Registros en la tabla L1T_STOCK_ENTRADA_DET:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al eliminar registro de la tabla L1T_STOCK_ENTRADA_DET:", error)

# Función para insertar registros en la tabla L1T_STOCK_SALIDA_CAB
def insertar_stock_salida_cab(conexion, codigo, fecha_ins_ano, fecha_ins_mes, fecha_ins_dia, cliente, estado_registro):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO L1T_STOCK_SALIDA_CAB (StoSalCabCod, StosalCabFecInsStoAño, StosalCabFecInsStoMes, StosalCabFecInsStoDia, StoSalCabCli, StoSalCabEstReg) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (codigo, fecha_ins_ano, fecha_ins_mes, fecha_ins_dia, cliente, estado_registro)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla L1T_STOCK_SALIDA_CAB.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla L1T_STOCK_SALIDA_CAB:", error)

# Función para actualizar registros en la tabla L1T_STOCK_SALIDA_CAB
def actualizar_stock_salida_cab(conexion, codigo, nuevo_estado_registro, nuevo_cliente):
    try:
        cursor = conexion.cursor()
        sql = "UPDATE L1T_STOCK_SALIDA_CAB SET StoSalCabEstReg = %s, StoSalCabCli = %s WHERE StoSalCabCod = %s"
        valores = (nuevo_estado_registro, nuevo_cliente, codigo)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro actualizado correctamente")
    except mysql.connector.Error as error:
        print("Error al actualizar registro en la tabla L1T_STOCK_SALIDA_CAB:", error)


# Función para eliminar registros de la tabla L1T_STOCK_SALIDA_CAB
def eliminar_stock_salida_cab(conexion, codigo):
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM L1T_STOCK_SALIDA_CAB WHERE StoSalCabCod = %s"
        valor = (codigo,)
        cursor.execute(sql, valor)
        conexion.commit()
        print("Registro eliminado correctamente de la tabla L1T_STOCK_SALIDA_CAB.")
    except mysql.connector.Error as error:
        print("Error al eliminar registro de la tabla L1T_STOCK_SALIDA_CAB:", error)

# Función para seleccionar todos los registros de la tabla L1T_STOCK_SALIDA_CAB
def seleccionar_stock_salida_cab(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM L1T_STOCK_SALIDA_CAB")
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla L1T_STOCK_SALIDA_CAB:", error)

# Función para insertar registros en la tabla L1T_STOCK_SALIDA_DET
def insertar_stock_salida_det(conexion, secuencia, cantidad, cabecera_codigo, articulo_codigo, cabecera_estado_registro):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO L1T_STOCK_SALIDA_DET (StoSalDetSec, StoSalDetCan, StoSalCabCod, StoSalDetArt, StoSalCabEstReg) VALUES (%s, %s, %s, %s, %s)"
        valores = (secuencia, cantidad, cabecera_codigo, articulo_codigo, cabecera_estado_registro)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla L1T_STOCK_SALIDA_DET.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla L1T_STOCK_SALIDA_DET:", error)

# Función para actualizar registros en la tabla L1T_STOCK_SALIDA_DET
def actualizar_stock_salida_det(conexion, sec, cantidad):
    try:
        cursor = conexion.cursor()
        sql = "UPDATE L1T_STOCK_SALIDA_DET SET StoSalDetCan = %s WHERE StoSalDetSec = %s"
        cursor.execute(sql, (cantidad, sec))
        conexion.commit()
        print("Registro actualizado exitosamente.")
    except mysql.connector.Error as error:
        print("Error al actualizar el registro en L1T_STOCK_SALIDA_DET:", error)

# Función para eliminar registros en la tabla L1T_STOCK_SALIDA_DET
def eliminar_stock_salida_det(conexion, secuencia):
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM L1T_STOCK_SALIDA_DET WHERE StoSalDetSec = %s"
        valores = (secuencia,)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro eliminado correctamente de la tabla L1T_STOCK_SALIDA_DET.")
    except mysql.connector.Error as error:
        print("Error al eliminar registro de la tabla L1T_STOCK_SALIDA_DET:", error)

# Función para seleccionar todos los registros de la tabla L1T_STOCK_SALIDA_DET
def seleccionar_stock_salida_det(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM L1T_STOCK_SALIDA_DET")
        registros = cursor.fetchall()
        print("Registros en la tabla L1T_STOCK_SALIDA_DET:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al eliminar registro de la tabla L1T_STOCK_SALIDA_DET:", error)

# Establecer la conexión a la base de datos
conexion = establecer_conexion()

if conexion is not None:
       
    # Insertar registros en la tabla GZZ_ESTADO_REGISTRO
    insertar_estado_registro(conexion, 'A', 'Activo', 'A')
    insertar_estado_registro(conexion, 'I', 'Inactivo', 'A')

    # Seleccionar registros de la tabla GZZ_ESTADO_REGISTRO
    seleccionar_estado_registro(conexion)

    # Insertar registros en la tabla GZZ_ZONA
    insertar_zona(conexion, 1, 'Zona 1')
    insertar_zona(conexion, 2, 'Zona 2')

    # Seleccionar registros de la tabla GZZ_ZONA
    seleccionar_zona(conexion)

    # Insertar registros en la tabla GZZ_MARCA
    insertar_marca(conexion, 1, 'Faber', 'A')
    insertar_marca(conexion, 2, 'Layconsa', 'A')

    # Seleccionar registros de la tabla GZZ_MARCA
    seleccionar_MARCA(conexion)

    # Insertar registros en la tabla GZZ_UNIDAD_MEDIDA
    insertar_unidad_medida(conexion, 1, 'unidades', 'A')
    insertar_unidad_medida(conexion, 2, 'metros', 'A')

    # Seleccionar registros de la tabla GZZ_UNIDAD_MEDIDA
    seleccionar_unidad_medida(conexion)

    # Insertar registros en la tabla GZZ_EMPLEADO
    insertar_empleado(conexion, 1, 'Henry Galvez', 'A')
    insertar_empleado(conexion, 2, 'Esteven Calcina', 'A')

    # Seleccionar registros de la tabla GZZ_EMPLEADO
    seleccionar_empleado(conexion)
  
    # Insertar un nuevo cliente
    insertar_cliente(conexion, 1, "Cliente 1", {"año": 2023, "mes": 6, "dia": 20}, "Calle 1", 1, 'A')
    insertar_cliente(conexion, 2, "Cliente 2", {"año": 2022, "mes": 4, "dia": 19}, "Calle 2", 2, 'A')
    insertar_cliente(conexion, 3, "Cliente 3", {"año": 2021, "mes": 3, "dia": 18}, "Calle 3", 1, 'A')

    # Actualizar un cliente existente
    actualizar_cliente(conexion, 1, "Cliente 4", "Nueva Dirección")

    # Eliminar un cliente existente
    eliminar_cliente(conexion, 3)

    # Seleccionar todos los clientes
    seleccionar_clientes(conexion)

    # Insertar un proveedor
    insertar_proveedor(conexion, 1, "Proveedor 1", 2023, 6, 20, "Dirección 1", 2, 'A')
    insertar_proveedor(conexion, 2, "Proveedor 2", 2022, 5, 19, "Dirección 2", 1, 'A')
    insertar_proveedor(conexion, 3, "Proveedor 3", 2021, 4, 18, "Dirección 3", 2, 'A')

    # Actualizar un proveedor existente
    actualizar_proveedor(conexion, 1, "Proveedor 1 Actualizado", 2024, 5, 19, "Nueva Dirección 1", 2, 'A')

    # Eliminar un cliente existente
    eliminar_proveedor(conexion, 2)

    # Seleccionar todos los proveedores
    seleccionar_proveedor(conexion)

    # Insertar un nuevo artículo
    insertar_articulo(conexion, 1, "Cuaderno", 10, "Cuaderno cuadriculado", 'A', 1, 1)
    insertar_articulo(conexion, 2, "Cinta", 6, "Cinta roja", 'A', 2, 2)
    insertar_articulo(conexion, 3, "Goma", 5, "Goma mediana", 'A', 1, 1)

    # Actualizar la cantidad de un artículo
    actualizar_articulo(conexion, 1, 15)

    # Eliminar un artículo
    eliminar_articulo(conexion, 3)

    # Seleccionar todos los artículos
    seleccionar_articulos(conexion)


    #Insertar un nuevo registro cabecera entrada
    insertar_stock_entrada_cab(conexion, 1, 2023, 6, 20, 1, 'A', 2)
    insertar_stock_entrada_cab(conexion, 2, 2022, 5, 19, 1, 'A', 1)
    insertar_stock_entrada_cab(conexion, 3, 2021, 4, 18, 3, 'A', 1)

    #Actualizar un registro existente
    actualizar_stock_entrada_cab(conexion, 1, 'A', 3)

    #Eliminar un registro existente
    eliminar_stock_entrada_cab(conexion, 2)

    #Seleccionar todos los registros de la tabla
    seleccionar_stock_entrada_cab(conexion) 


    #Insertar un registro en L1T_STOCK_ENTRADA_DET
    insertar_stock_entrada_det(conexion, 1, 10, 1, 2, 'A')
    insertar_stock_entrada_det(conexion, 2, 6, 3, 1, 'A')
    insertar_stock_entrada_det(conexion, 3, 11, 3, 2, 'A')

    #Actualizar el campo StoEntDetCan del registro con StoEntCabSec igual a 1
    actualizar_stock_entrada_det(conexion, 1, 15)

    #Eliminar el registro con StoEntCabSec igual a 3
    eliminar_stock_entrada_det(conexion, 3)

    #Seleccionar todos los registros de L1T_STOCK_ENTRADA_DET
    seleccionar_stock_entrada_det(conexion)

    #Insertar un nuevo registro cabecera salida
    insertar_stock_salida_cab(conexion, 1, 2023, 6, 20, 1, 'A')
    insertar_stock_salida_cab(conexion, 2, 2022, 5, 19, 1, 'A')
    insertar_stock_salida_cab(conexion, 3, 2021, 4, 18, 2, 'A')

    #Actualizar un registro existente
    actualizar_stock_salida_cab(conexion, 1, 'A', 2)

    #Eliminar un registro existente
    eliminar_stock_salida_cab(conexion, 2)

    #Seleccionar todos los registros de la tabla
    seleccionar_stock_salida_cab(conexion) 

    #Insertar un registro en L1T_STOCK_SALIDA_DET
    insertar_stock_salida_det(conexion, 1, 10, 1, 2, 'A')
    insertar_stock_salida_det(conexion, 2, 6, 3, 1, 'A')
    insertar_stock_salida_det(conexion, 3, 11, 3, 2, 'A')

    #Actualizar el campo StoSalDetCan del registro con StoSalCabSec igual a 1
    actualizar_stock_salida_det(conexion, 1, 15)

    #Eliminar el registro con StoSalCabSec igual a 3
    eliminar_stock_salida_det(conexion, 3)

    #Seleccionar todos los registros de L1T_STOCK_SALIDA_DET
    seleccionar_stock_salida_det(conexion)

cerrar_conexion(conexion)

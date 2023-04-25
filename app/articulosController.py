from bd import obtener_conexion


def insertar(id, title, body, author, create_date):
    conexion = obtener_conexion()

    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO articles(id, title, body, author, create_date) VALUES (%s, %s, %s, %s, %s)",
                       (id, title, body, author, create_date))

        conexion.commit()
        conexion.close()


def listar():
    conexion = obtener_conexion()
    articulos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM articles")
        articulos = cursor.fetchall()
    conexion.close()

    return articulos


def ListarArticulo(id):
    conexion = obtener_conexion()
    articulo = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM articles WHERE id = %s", (id,))
        articulo = cursor.fetchone()
    conexion.close()
    return articulo


def eliminarArticulo(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM articles WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def actualizarArticulo(id, title, body, author):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE articles SET title = %s, body = %s, author = %s WHERE id = %s",
                       (title, body, author, id))
    conexion.commit()
    conexion.close()


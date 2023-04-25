

import pymysql


def obtener_conexion():
    return pymysql.connect(host='localhost', user='root', password='Autonoma@2023', db='articulos')


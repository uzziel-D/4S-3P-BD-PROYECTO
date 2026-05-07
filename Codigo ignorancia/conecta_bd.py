#Se importa la libreria necesaria
import pymysql

##Procedimiento para conectar y extraer informacion de la BD
def recupera_categoria():
	##Se crea un objeto de coneccion a la BD
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
	##Se crea un cursor para ejecutar consultas a la base de datos
	cursor = conn.cursor()
	##Se utiliza el cursor para ejecutar la consulta sobre la tabla de categorias
	cursor.execute('select descripcion from categoria')
	##Se crea una lista para contener las categorias extraidas de la base de datos
	categorias = cursor.fetchall()
	##cerrar la base de datos
	conn.close()
	#print(categorias)
	return categorias

def recupera_preguntas(cat):
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
	cursor = conn.cursor()
	# Se arma la primera parte de la consulta SQL seleccionando todos los datos necesarios de la tabla pregunta.
	# Aquí se obtienen el id de la pregunta, el texto, las 4 opciones, la respuesta correcta y la categoría.
	consulta='select b.id_pregunta,b.pregunta,b.opcion_1,b.opcion_2,b.opcion_3,b.opcion_4,b.correcto,b.id_categoria '
	# Se agrega la parte FROM indicando las tablas que se van a usar.
	# La tabla categoria se renombra como "a" y pregunta como "b" para escribir menos y hacer más fácil la consulta.
	consulta=consulta+' from categoria a, pregunta b'
	# Se agrega la condición para relacionar ambas tablas.
	# Se busca la categoría usando la descripción que el usuario seleccionó, y después compara el id_categoria de ambas tablas para traer solamente las preguntas que pertenecen a esa categoría.
	consulta=consulta+' where a.descripcion="'+cat+'" and b.id_categoria=a.id_categoria '
	cursor.execute(consulta)
	preguntas = cursor.fetchall()
	conn.close()
	return preguntas

def recupera_usuarios():
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('select id_usuario, nombre from usuario')
	usuarios = cursor.fetchall()
	conn.close()
	return usuarios

def tabla_usuarios():
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('select id_usuario, nombre from usuario')
	usuarios = cursor.fetchall()
	conn.close()
	return usuarios

def inserta_usuario(nombre):
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('insert into usuario (nombre) values (%s)',(nombre,))
	conn.commit()
	conn.close()
	
def recupera_usuario_categoria():
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('select a.id_usuario, a.id_categoria, a.puntos from usuario_categoria a')
	usuario_categoria = cursor.fetchall()
	conn.close()
	return usuario_categoria

def actualiza_puntos_usuario(id_usuario, id_categoria, puntos):
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute("CALL sp_actualiza_usuario_categoria(%s, %s, %s)", (id_usuario, id_categoria, puntos))
	conn.commit()
	conn.close()

def inserta_usuario(nombre):
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('insert into usuario (nombre) values (%s)',(nombre,))
	conn.commit()
	conn.close()

def tabla_categoria():
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('select id_categoria, descripcion from categoria')
	cats = cursor.fetchall()
	conn.close()
	return cats

def inserta_categoria(descripcion):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
    cursor = conn.cursor()
    cursor.execute('insert into categoria (descripcion) values (%s)',(descripcion,))
    conn.commit()
    conn.close()

def modif_usuario(ac, nombre):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
    cursor = conn.cursor()
    cursor.execute('UPDATE usuario SET nombre=%s WHERE id_usuario=%s',(nombre, ac))
    conn.commit()
    conn.close()

def borra_categoria(ab):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('delete from categoria where Id_categoria=%s', (ab))
	conn.commit()
	conn.close()

def selec_categoria(ab):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('SELECT id_categoria, descripcion FROM categoria WHERE id_categoria = %s', (ab,))
	dato=cursor.fetchone()
	return dato

def modif_categoria(ab, descripcion):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
    cursor = conn.cursor()
    cursor.execute('UPDATE categoria SET descripcion=%s WHERE id_categoria=%s',(descripcion, ab))
    conn.commit()
    conn.close()

def tabla_pregunta(id):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('select id_pregunta,pregunta,opcion_1,opcion_2,opcion_3,opcion_4,correcto from pregunta where id_categoria=%s', (id))
	preguntas = cursor.fetchall()
	conn.close()
	return preguntas


def selec_pregunta(ab):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('select id_categoria,pregunta,opcion_1,opcion_2,opcion_3,opcion_4,correcto,id_categoria from pregunta where id_pregunta=%s',(ab))
	dato=cursor.fetchone()
	return dato


def modif_pregunta(ab,datos):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('update pregunta set pregunta=%s,opcion_1=%s,opcion_2=%s,opcion_3=%s,opcion_4=%s,correcto=%s where Id_pregunta=%s',
    (datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],ab))
	conn.commit()

def borra_pregunta(ab):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('delete from pregunta where Id_pregunta=%s', (ab))
	conn.commit()

def inserta_pregunta(datos,id):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('insert into pregunta (pregunta,opcion_1,opcion_2,opcion_3,opcion_4,correcto,id_categoria) values(%s,%s,%s,%s,%s,%s,%s)', (datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],id))
	conn.commit()
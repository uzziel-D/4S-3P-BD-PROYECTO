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

	#se recuperan los valores del usuario 
def recupera_usuarios():
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('select id_usuario, nombre from usuario')
	usuarios = cursor.fetchall()
	conn.close()
	return usuarios
	#obtiene la tabla de usuarios
def tabla_usuarios():
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('select id_usuario, nombre from usuario')
	usuarios = cursor.fetchall()
	conn.close()
	return usuarios
	#inserta usuarios y su nombre
def inserta_usuario(nombre):
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
	cursor = conn.cursor()
	#Se inserta un nuevo usuario en la bd, recibe el nombre desde una variable y se manda usando el %s para evitar problemas de seguridad o error en el formato 
	cursor.execute('insert into usuario (nombre) values (%s)',(nombre,))
	conn.commit()
	conn.close()
	#recupera los valores deseados de la tabla de usuario_categoria
#funcion para recuperar la tabla de usuariocategoria
def recupera_usuario_categoria():
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
	cursor = conn.cursor()
	#Consulta todos los registros de la tabla usuario_categoria
	#Sirve para relacionar usuarios con categorias y guarda los puntos obtenidos por cada.
	#La letra "a" es el alias que usamos para escribir menos codigo.
	cursor.execute('select a.id_usuario, a.id_categoria, a.puntos from usuario_categoria a')
	usuario_categoria = cursor.fetchall()
	conn.close()
	return usuario_categoria
	#funcion para actualizar los puntos del usuario
def actualiza_puntos_usuario(id_usuario, id_categoria, puntos):
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
	cursor = conn.cursor()
	#Ejecuta un procedimiento almacenado de MySQL
	#Este procedimiento actualiza los puntos de un usuario dependiendo de la categoria jugada.
	#Se mandan tres datos: usuario, categoria y puntos
	cursor.execute("CALL sp_actualiza_usuario_categoria(%s, %s, %s)", (id_usuario, id_categoria, puntos))
	conn.commit()
	conn.close()

#funcion para robtener la tabla de categoria
def tabla_categoria():
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('select id_categoria, descripcion from categoria')
	cats = cursor.fetchall()
	conn.close()
	return cats
#funcion para insertar categoria
def inserta_categoria(descripcion):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
    cursor = conn.cursor()
	#inserta una nueva categoria de la bd
	#la descripcion normalmente es el nombre visible que aparecera en el juego o catalogo
    cursor.execute('insert into categoria (descripcion) values (%s)',(descripcion,))
    conn.commit()
    conn.close()
#funcion para modificar el usuario
def modif_usuario(ac, nombre):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
    cursor = conn.cursor()
	#Se modifica el nombre de algun usuario existente.
	#recibe el nuevo nombre, despues el id del mismo y se actualiza.
    cursor.execute('UPDATE usuario SET nombre=%s WHERE id_usuario=%s',(nombre, ac))
    conn.commit()
    conn.close()
#funcion para borrar categoria
def borra_categoria(ab):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	#borra una categoria usando el id, el "ab" es el identificador de la categoria que se selecciono.
	cursor.execute('delete from categoria where Id_categoria=%s', (ab))
	conn.commit()
	conn.close()
#funcion para seleccionar la categoria
def selec_categoria(ab):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	#busca categoria especificamente usando el id correspondiente.
	#se recupera el id y su descripcion para poder mostrarlos o editarlos despues de la interfaz
	cursor.execute('SELECT id_categoria, descripcion FROM categoria WHERE id_categoria = %s', (ab,))
	dato=cursor.fetchone()
	return dato
#funcion para modificar categoria
def modif_categoria(ab, descripcion):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
    cursor = conn.cursor()
	#actualiza la descripcion de una categoria, manda el nuevo texto primero y despues el id de la categoria que sera modificada
    cursor.execute('UPDATE categoria SET descripcion=%s WHERE id_categoria=%s',(descripcion, ab))
    conn.commit()
    conn.close()
#funcion para recuperar la tabla de preguntas
def tabla_pregunta(id):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	#toma todas las preguntas que pertenecen a una categoria
	#tambien trae las 4 opciones y la respuesta correcta para mostrarlas dentro del juego
	cursor.execute('select id_pregunta,pregunta,opcion_1,opcion_2,opcion_3,opcion_4,correcto from pregunta where id_categoria=%s', (id))
	preguntas = cursor.fetchall()
	conn.close()
	return preguntas

#funcion para seleccionar la pregunta
def selec_pregunta(ab):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	#busca preguntas especificas usando su id
	#se recuperan todos los datos que sean necesarios para cargarla en los cuadros de texto y que se pueda editar
	cursor.execute('select id_categoria,pregunta,opcion_1,opcion_2,opcion_3,opcion_4,correcto,id_categoria from pregunta where id_pregunta=%s',(ab))
	dato=cursor.fetchone()
	return dato

#funcion para modificar la pregunta
def modif_pregunta(ab,datos):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	#actualiza una pregunta que ya existe
	#tambien modifica sus opciones de respuesta y la respuesta correcta
	#los datos vienen guardados dentro de una tupla llamada "datos"
	#cada posicion representa una parte diferente de la pregunta
	cursor.execute('update pregunta set pregunta=%s,opcion_1=%s,opcion_2=%s,opcion_3=%s,opcion_4=%s,correcto=%s where Id_pregunta=%s',
    (datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],ab))
	conn.commit()
#funcion para borrar la pregunta
def borra_pregunta(ab):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	#borra una pregunta de la bd usando el id de la pregunta seleccionada
	cursor.execute('delete from pregunta where Id_pregunta=%s', (ab))
	conn.commit()
#funcion para insertar preguntas
def inserta_pregunta(datos,id):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	#agrega una nueva pregunta junto con sus opciones, la respuesta correcta y la categoria a la que pertenece
	#los datos de la pregunta se almacenan en una tupla
	cursor.execute('insert into pregunta (pregunta,opcion_1,opcion_2,opcion_3,opcion_4,correcto,id_categoria) values(%s,%s,%s,%s,%s,%s,%s)', (datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],id))
	conn.commit()
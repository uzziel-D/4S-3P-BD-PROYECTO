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
	consulta='select b.id_pregunta,b.pregunta,b.opcion_1,b.opcion_2,b.opcion_3,b.opcion_4,b.correcto,b.id_categoria '
	consulta=consulta+' from categoria a, pregunta b'
	consulta=consulta+' where a.descripcion="'+cat+'" and b.id_categoria=a.id_categoria '
	cursor.execute(consulta)
	preguntas = cursor.fetchall()
	conn.close()
	return preguntas

def tabla_categoria(id):
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('select id_categoria,pregunta,opcion_1,opcion:2,opcion3,opcion4,correcto,id_categoria from pregunta where id_categoria=%s',(id))
	cats= cursor.fetchall()
	conn.close()
	return cats

def inserta_categoria(datos,id):
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('inserta into pregunta (pregunta,opcion_1,opcion_2,opcion_3,opcion_4,correcto,id_categoria) values(%s,%s,%s,%s,%s,%s,%s)', 
	    (datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],id))
	conn.commit()
	conn.close()

def borra_categoria(ab):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('delete from categoria where Id_categoria=%s' (ab))
	conn.commit()
	conn.close()

def selec_categoria(ab):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('select id_categoria,pregunta,opcion_1,opcion_2,opcion_3,opcion_4,correcto,id_categoria from pregunta where id_categoria=%s',(id))
	dato=cursor.fetchone()
	return dato

def modif_categoria(ab,datos):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('update pregunta set pregunta=%s,opcion_1=%s,opcion_2=%s,opcion_3=%s,opcion_4=%s,correcto=%s where Id_pregunta=%s',
	(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],ab))
	conn.commit()
	conn.close()

def tabla_pregunta(id):
	conn = pymysql.connect(host='localhost',user='root',passwd='', db='ignorancia')
	cursor = conn.cursor()
	cursor.execute('select id_categoria,pregunta,opcion_1,opcion_2,opcion_3,opcion_4,correcto,id_categoria from pregunta where id_categoria=%s',(id))
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
	cursor.execute('inserta into pregunta (pregunta,opcion_1,opcion_2,opcion_3,opcion_4,correcto,id_categoria) values(%s,%s,%s,%s,%s,%s,%s)', (datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],id))
	conn.commit()
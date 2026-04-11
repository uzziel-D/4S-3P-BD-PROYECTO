import pymysql


def recupera_categoria():
    conn = pymysql.connect(host='localhost', user ='root', passwd="", db='ignorancia')
    cursor = conn.cursor()
    cursor.execute('select descripcion from categoria')
    categorias = cursor.fetchall()
    conn.close
    return categorias

def recupera_preguntas (cat):
    conn = pymysql.connect(host='localhost', user ='root', passwd='', db='ignorancia')
    cursor = conn.cursor()
    consulta='select b.id_pregunta,b.pregunta,b.opcion_1,b.opcion_2,b.opcion_3,b.opcion_4,b.correcto,b.id_pregunta '
    consulta=consulta+'from categoria a, pregunta b '
    consulta=consulta+' where a.descripcion="'+cat+'" and b.id_categoria=a.id_categoria '
    cursor.execute(consulta)
    preguntas= cursor.fetchall()
    conn.close()
    return preguntas    
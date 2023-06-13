"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """   
    pelicula={"nombre":nombre,"genero":genero,"duracion":duracion,"anio":anio,"clasificacion":clasificacion,"hora":hora,"dia":dia} 
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    return pelicula

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    pelicula_encontrada=None
    
    if nombre_pelicula.lower()==p1['nombre'].lower():
        pelicula_encontrada=p1
    elif nombre_pelicula.lower()==p2['nombre'].lower():
         pelicula_encontrada=p2
    elif nombre_pelicula.lower()==p3['nombre'].lower():
         pelicula_encontrada=p3
    elif nombre_pelicula.lower()==p4['nombre'].lower():
         pelicula_encontrada=p4
    elif nombre_pelicula.lower()==p5['nombre'].lower():
         pelicula_encontrada=p5
    return pelicula_encontrada
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    if(p1["duracion"]>p2["duracion"] or p1["duracion"]>p3["duracion"] or p1["duracion"]>p4["duracion"] or p1["duracion"]>p5["duracion"]):
        return p1
    elif(p2["duracion"]>p3["duracion"] or p2["duracion"]>p4["duracion"] or p2["duracion"]>p5["duracion"]):
        return p2
    elif(p3["duracion"]>p4["duracion"]or p3["duracion"]>p5["duracion"]):
        return p3
    elif (p4["duracion"]>p5["duracion"]):
        return p4
    else:
        return p5
    
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
   

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    duracion=(p1['duracion']+p2['duracion']+p3['duracion']+p4['duracion']+p5['duracion'])/5
    horas=int(duracion//60)
    minutos=int(round(duracion%60))

    if minutos<10:
        minutos_str='0'+str(minutos)
    else:
        minutos_str=str(minutos)
    
    if horas<10:
        horas_str='0'+str(horas)
    else:
        horas_str=str(horas)
           
    return horas_str+':'+minutos_str

    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    if(p1["anio"]>anio and p2["anio"]>anio and p3["anio"]>anio and p4["anio"]>anio and p5["anio"]>anio):
        return p1["nombre"],",",p2["nombre"],p3["nombre"],"y",p4["nombre"],"y",p5["nombre"]
    elif(p1["anio"]>anio and p2["anio"]>anio and p3["anio"]>anio and p4["anio"]>anio ):
        return p1["nombre"],",",p2["nombre"],p3["nombre"],"y",p4["nombre"]
    elif(p1["anio"]>anio and p2["anio"]>anio and p3["anio"]>anio ):
        return p1["nombre"],",",p2["nombre"],p3["nombre"]
    elif(p1["anio"]>anio and p2["anio"]>anio ):
        return p1["nombre"],",",p2["nombre"]
    elif(p1["anio"]>anio):
        return p1["nombre"]
    
    if(p2["anio"]>anio and p3["anio"]>anio and p4["anio"]>anio and p5["anio"]>anio ):
        return p2["nombre"],p3["nombre"],"y",p4["nombre"],"y",p5["nombre"]
    elif(p2["anio"]>anio and p3["anio"]>anio and p4["anio"]>anio  ):
        return p2["nombre"],p3["nombre"],"y",p4["nombre"]
    elif(p2["anio"]>anio and p3["anio"]>anio  ):
        return p2["nombre"],p3["nombre"]
    elif(p2["anio"]>anio ):
        return p2["nombre"]
    
    if( p3["anio"]>anio and p4["anio"]>anio and p5["anio"]>anio ):
        return p3["nombre"],"y",p4["nombre"],"y",p5["nombre"]
    elif( p3["anio"]>anio and p4["anio"]>anio  ):
        return p3["nombre"],"y",p4["nombre"]
    elif( p3["anio"]>anio  ):
        return p3["nombre"]
    
    if(p4["anio"]>anio and p5["anio"]>anio ):
        return p4["nombre"],"y",p5["nombre"]
    else:
        return p4["nombre"]
    

    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    Num_peliculas_18_mas=0
    
    if p1['clasificacion']=='18+':
        Num_peliculas_18_mas+=1
    if p2['clasificacion']=='18+':
        Num_peliculas_18_mas+=1
    if p3['clasificacion']=='18+':
        Num_peliculas_18_mas+=1
    if p4['clasificacion']=='18+':
        Num_peliculas_18_mas+=1
    if p5['clasificacion']=='18+':
        Num_peliculas_18_mas+=1
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    return Num_peliculas_18_mas
def hora_final(HI:int,duracion:int)->int:
    hi=HI//100
    mi=HI%100
    mf=(mi+duracion)%60
    hf=(mi+duracion)//60+hi
    HF=hf*100+mf
    return HF

def horarios_no_se_cruzan(nueva_hora: int, nuevo_dia: str,duracion:int,peli2:dict)->bool:
    reprogramar=False
    
    hora_final1=hora_final(nueva_hora,duracion)
    hora_final2=hora_final(peli2['hora'],peli2['duracion'])
    if nuevo_dia==peli2['dia']:
        if nueva_hora<peli2['hora']:
            if hora_final1<peli2['hora']:
                reprogramar=True
        elif nueva_hora>peli2['hora']:
            if hora_final2<nueva_hora:
                reprogramar=True
    else:
        reprogramar=True
    
    return reprogramar

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    puede_reagendar=False
    if peli==p1:
        puede_reagendar=horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p2) and horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p3) and horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p4) and horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p5)
    elif peli==p2:
        puede_reagendar=horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p1) and horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p3) and horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p4) and horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p5)
    elif peli==p3:
        puede_reagendar=horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p1) and horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p2) and horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p4) and horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p5)
    elif peli==p4:
        puede_reagendar=horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p1) and horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p2) and horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p3) and horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p5)
    elif peli==p5:
        puede_reagendar=horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p1) and horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p2) and horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p3) and horarios_no_se_cruzan(nueva_hora,nuevo_dia,peli['duracion'], p4)
    
    if control_horario:
        if peli['genero'].find('Documental')!=-1 and nueva_hora>=2200:
            puede_reagendar=False
        if peli['genero'].find('Drama')!=-1 and nuevo_dia=='viernes':
            puede_reagendar=False
        if (nuevo_dia!='domingo' and nuevo_dia!='sábado') and (nueva_hora>=2300 or nueva_hora<=600):
            puede_reagendar=False
    
    if puede_reagendar==True:
        peli['dia']=nuevo_dia
        peli['hora']=nueva_hora
        
            
    
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    return puede_reagendar
    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    invitar=True
    if peli['clasificacion']=='Todos':
        clasificacion_int=0
    else:
        clasificacion_str=peli['clasificacion']
        if len(clasificacion_str)==3:
            clasificacion_int=int(clasificacion_str[:2])
        else:
            clasificacion_int=int(clasificacion_str[:1])
    
    if edad_invitado<15 and peli['genero'].find('Terror')!=-1:
        invitar=False
    elif edad_invitado<=10 and peli['genero'].find('Familiar')==-1:
        invitar=False
    elif edad_invitado<clasificacion_int and not autorizacion_padres:
        invitar=False
               
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    return invitar

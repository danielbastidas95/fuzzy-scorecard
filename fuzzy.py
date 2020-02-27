import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import csv

#Inicializate iniciatives
data_inic = [['Iniciativa', 'Valor'], 
            ['Disminuir los pasivos a corto plazo', 0], 
            ['Aumentar los ingresos', 0],
            ['Crear cultura basada en la experiencia', 0],
            ['Alcanzar los tiempos promedio de instalacion y reparacion requeridos', 0],
            ['Garantizar los niveles de calidad establecidos en la prestacion de los servicios TIC', 0],
            ['Generar nuevas oportunidades de negocio', 0],
            ['Crear una cultura de planeacion estrategica en la empresa', 0],
            ['Establecer acciones, metodos y procedimientos de control y seguimiento a la gestion incluyendo...', 0],
            ['Implementar el Sistema de Gestion de la Calidad en la empresa', 0],
            ['Atender oportunamente los asuntos legales que surjan respecto a las actividades de la organizacion', 0],
            ['Crear una cultura de optimizacion del uso de los recurso de la empresa', 0],
            ['Garantizar la eficiencia y la eficacia en los subprocesos compras y almacen', 0],
            ['Garantizar que exista una informacion documental veraz y oportuna en la empresa.', 0],
            ['Realizar una gestion eficiente de cartera', 0],
            ['Exceder las expectativas del cliente', 0],
            ['Desarrolar una cultura de comunicacion e informacion que facilite el alcance de los objetivos...', 0],
            ['Mejorar las capacidades, conocimientos y entrenamiento de los colaboradores', 0],
            ['Mejorar la Cultura y Clima Organizacional', 0],
            ['Integrar efectivamente la infraestructura tecnologica en la empresa', 0]]

#Inicializate objectives
data = [['Objetivo', 'Valor'], 
        ['Objetivo 1', 0], 
        ['Objetivo 2', 0],
        ['Objetivo 3', 0],
        ['Objetivo 4', 0],
        ['Objetivo 5', 0],
        ['Objetivo 6', 0],
        ['Objetivo 7', 0]]

def calculate_obj1(value_ini_11, value_ini_12):

    #OBJETIVO 1: GARANTIZAR LA SOSTENEBILIDAD ECONOMICA DE LA ORGANIZACION
    # Generate universe variables
    #   El rango de las iniciativas estrategicas es [0,110]
    #   El rango del objetivo de salida es [0,110]
    # Inic1 = Disminuir los pasivos a corto plazo
    # Inic2 = Incrementar los ingresos

    # New Antecedent/Consequent objects hold universe variables and membership
    # functions
    Inic1 = ctrl.Antecedent(np.arange(0, 110, 1), 'Disminuir los pasivos...')
    Inic2 = ctrl.Antecedent(np.arange(0, 110, 1), 'Incrementar los ingresos')
    Obj1 = ctrl.Consequent(np.arange(0, 110, 1), 'Objetivo 1')

    # Generate fuzzy membership functions
    Inic1['Dmayor'] = fuzz.trapmf(Inic1.universe, [-1, 0, 20, 29])
    Inic1['Dmenor'] = fuzz.trimf(Inic1.universe, [12, 40, 46])
    Inic1['Fmenor'] = fuzz.trimf(Inic1.universe, [36, 60, 75])
    Inic1['Fmayor'] = fuzz.trapmf(Inic1.universe, [73, 80, 110, 120])

    Inic2['Dmayor'] = fuzz.trapmf(Inic2.universe, [-1, 0, 20, 33])
    Inic2['Dmenor'] = fuzz.trimf(Inic2.universe, [32, 40, 56])
    Inic2['Fmenor'] = fuzz.trimf(Inic2.universe, [55, 60, 79])
    Inic2['Fmayor'] = fuzz.trapmf(Inic2.universe, [77, 80, 110, 120])

    Obj1['Dmayor'] = fuzz.trapmf(Obj1.universe, [-1, 0, 20, 40])
    Obj1['Dmenor'] = fuzz.trimf(Obj1.universe, [20, 40, 60])
    Obj1['Fmenor'] = fuzz.trimf(Obj1.universe, [40, 60, 80])
    Obj1['Fmayor'] = fuzz.trapmf(Obj1.universe, [60, 80, 110, 120])

    # generate rules
    rule1 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Dmayor'], Obj1['Dmayor'])
    rule2 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Dmayor'], Obj1['Dmayor'])
    rule3 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Dmayor'], Obj1['Dmenor'])
    rule4 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Dmayor'], Obj1['Dmenor'])
    rule5 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Dmenor'], Obj1['Dmayor'])
    rule6 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Dmenor'], Obj1['Dmenor'])
    rule7 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Dmenor'], Obj1['Dmenor'])
    rule8 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Dmenor'], Obj1['Fmenor'])
    rule9 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Fmenor'], Obj1['Dmenor'])
    rule10 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Fmenor'], Obj1['Dmenor'])
    rule11 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Fmenor'], Obj1['Fmenor'])
    rule12 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Fmenor'], Obj1['Fmayor'])
    rule13 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Fmayor'], Obj1['Dmenor'])
    rule14 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Fmayor'], Obj1['Fmenor'])
    rule15 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Fmayor'], Obj1['Fmayor'])
    rule16 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Fmayor'], Obj1['Fmayor'])

    #create system control and simulation
    solving_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16])
    solving = ctrl.ControlSystemSimulation(solving_ctrl)

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    solving.input['Disminuir los pasivos...'] = value_ini_11
    solving.input['Incrementar los ingresos'] = value_ini_12
    # Crunch the numbers
    solving.compute()

    #value objetivo 1
    Obj1_result = solving.output['Objetivo 1']

     #update data
    n = 1
    m = 1

    with open('static/data/datamain.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[n] = ['Objetivo', row['Valor']]
            n=n+1
             
    data[1][1] = Obj1_result
 
    with open('static/data/datamain.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data)

    with open('static/data/data-inic.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_inic[m] = [data_inic[m][0], row['Valor']]
            m=m+1

    
    data_inic[1][1] = value_ini_11
    
    data_inic[2][1] = value_ini_12

    with open('static/data/data-inic.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data_inic)  

    csvFile.close()

def calculate_obj2(value_ini_21, value_ini_22, value_ini_23):

    #OBJETIVO 2: Crear experiencias gratamente memorables para posicionar la marca EMTEL en el corazón de los clientes
    # Generate universe variables
    #   El rango de las iniciativas estrategicas es [0,110]
    #   El rango del objetivo de salida es [0,110]
    # Inic1 = Crear cultura basada en la experiencia
    # Inic2 = Alcanzar los tiempos promedio de instalacion y reparación requeridos
    # Inic3 = Garantizar los niveles de calidad establecidos en la prestación de los servicios TIC

    # New Antecedent/Consequent objects hold universe variables and membership
    # functions
    Inic1 = ctrl.Antecedent(np.arange(0, 110, 1), 'Inic1')
    Inic2 = ctrl.Antecedent(np.arange(0, 110, 1), 'Inic2')
    Inic3 = ctrl.Antecedent(np.arange(0, 110, 1), 'Inic3')
    Obj2 = ctrl.Consequent(np.arange(0, 110, 1), 'Objetivo 2')

    # Generate fuzzy membership functions
    Inic1['Dmayor'] = fuzz.trapmf(Inic1.universe, [-1, 0, 20, 30])
    Inic1['Dmenor'] = fuzz.trimf(Inic1.universe, [29, 40, 55])
    Inic1['Fmenor'] = fuzz.trimf(Inic1.universe, [48, 60, 78])
    Inic1['Fmayor'] = fuzz.trapmf(Inic1.universe, [76, 80, 110, 120])

    Inic2['Dmayor'] = fuzz.trapmf(Inic2.universe, [-1, 0, 20, 31])
    Inic2['Dmenor'] = fuzz.trimf(Inic2.universe, [30, 40, 58])
    Inic2['Fmenor'] = fuzz.trimf(Inic2.universe, [36, 60, 73])
    Inic2['Fmayor'] = fuzz.trapmf(Inic2.universe, [71, 80, 110, 120])

    Inic3['Dmayor'] = fuzz.trapmf(Inic3.universe, [-1, 0, 20, 27])
    Inic3['Dmenor'] = fuzz.trimf(Inic3.universe, [26, 40, 55])
    Inic3['Fmenor'] = fuzz.trimf(Inic3.universe, [44, 60, 77])
    Inic3['Fmayor'] = fuzz.trapmf(Inic3.universe, [72, 80, 110, 120])

    Obj2['Dmayor'] = fuzz.trapmf(Obj2.universe, [-1, 0, 20, 40])
    Obj2['Dmenor'] = fuzz.trimf(Obj2.universe, [20, 40, 60])
    Obj2['Fmenor'] = fuzz.trimf(Obj2.universe, [40, 60, 80])
    Obj2['Fmayor'] = fuzz.trapmf(Obj2.universe, [60, 80, 110, 120])

    #generate rules membreship
    rule1 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Dmayor'] & Inic3["Dmayor"], Obj2['Dmayor'])
    rule2 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Dmenor'] & Inic3["Dmayor"], Obj2['Dmayor'])
    rule3 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Fmenor'] & Inic3["Dmayor"], Obj2['Dmayor'])
    rule4 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Fmayor'] & Inic3["Dmayor"], Obj2['Dmenor'])
    rule5 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Dmayor'] & Inic3["Dmenor"], Obj2['Dmayor'])
    rule6 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Dmenor'] & Inic3["Dmenor"], Obj2['Dmayor'])
    rule7 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Fmenor'] & Inic3["Dmenor"], Obj2['Dmenor'])
    rule8 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Fmayor'] & Inic3["Dmenor"], Obj2['Dmenor'])
    rule9 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Dmayor'] & Inic3["Fmenor"], Obj2['Dmayor'])
    rule10 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Dmenor'] & Inic3["Fmenor"], Obj2['Dmenor'])
    rule11 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Fmenor'] & Inic3["Fmenor"], Obj2['Dmenor'])
    rule12 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Fmayor'] & Inic3["Fmenor"], Obj2['Dmenor'])
    rule13 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Dmayor'] & Inic3["Fmayor"], Obj2['Dmenor'])
    rule14 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Dmenor'] & Inic3["Fmayor"], Obj2['Dmenor'])
    rule15 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Fmenor'] & Inic3["Fmayor"], Obj2['Fmenor'])
    rule16 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Fmayor'] & Inic3["Fmayor"], Obj2['Fmenor'])

    rule17 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Dmayor'] & Inic3["Dmayor"], Obj2['Dmayor'])
    rule18 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Dmenor'] & Inic3["Dmayor"], Obj2['Dmayor'])
    rule19 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Fmenor'] & Inic3["Dmayor"], Obj2['Dmenor'])
    rule20 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Fmayor'] & Inic3["Dmayor"], Obj2['Dmenor'])
    rule21 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Dmayor'] & Inic3["Dmenor"], Obj2['Dmayor'])
    rule22 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Dmenor'] & Inic3["Dmenor"], Obj2['Dmenor'])
    rule23 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Fmenor'] & Inic3["Dmenor"], Obj2['Dmenor'])
    rule24 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Fmayor'] & Inic3["Dmenor"], Obj2['Dmenor'])
    rule25 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Dmayor'] & Inic3["Fmenor"], Obj2['Dmayor'])
    rule26 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Dmenor'] & Inic3["Fmenor"], Obj2['Dmenor'])
    rule27 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Fmenor'] & Inic3["Fmenor"], Obj2['Dmenor'])
    rule28 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Fmayor'] & Inic3["Fmenor"], Obj2['Dmenor'])
    rule29 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Dmayor'] & Inic3["Fmayor"], Obj2['Dmenor'])
    rule30 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Dmenor'] & Inic3["Fmayor"], Obj2['Fmenor'])
    rule31 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Fmenor'] & Inic3["Fmayor"], Obj2['Fmenor'])
    rule32 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Fmayor'] & Inic3["Fmayor"], Obj2['Fmenor'])

    rule33 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Dmayor'] & Inic3["Dmayor"], Obj2['Dmayor'])
    rule34 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Dmenor'] & Inic3["Dmayor"], Obj2['Dmenor'])
    rule35 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Fmenor'] & Inic3["Dmayor"], Obj2['Dmenor'])
    rule36 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Fmayor'] & Inic3["Dmayor"], Obj2['Fmenor'])
    rule37 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Dmayor'] & Inic3["Dmenor"], Obj2['Dmayor'])
    rule38 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Dmenor'] & Inic3["Dmenor"], Obj2['Dmenor'])
    rule39 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Fmenor'] & Inic3["Dmenor"], Obj2['Fmenor'])
    rule40 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Fmayor'] & Inic3["Dmenor"], Obj2['Fmenor'])
    rule41 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Dmayor'] & Inic3["Fmenor"], Obj2['Dmenor'])
    rule42 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Dmenor'] & Inic3["Fmenor"], Obj2['Fmenor'])
    rule43 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Fmenor'] & Inic3["Fmenor"], Obj2['Fmenor'])
    rule44 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Fmayor'] & Inic3["Fmenor"], Obj2['Fmenor'])
    rule45 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Dmayor'] & Inic3["Fmayor"], Obj2['Dmenor'])
    rule46 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Dmenor'] & Inic3["Fmayor"], Obj2['Fmenor'])
    rule47 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Fmenor'] & Inic3["Fmayor"], Obj2['Fmenor'])
    rule48 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Fmayor'] & Inic3["Fmayor"], Obj2['Fmayor'])

    rule49 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Dmayor'] & Inic3["Dmayor"], Obj2['Dmayor'])
    rule50 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Dmenor'] & Inic3["Dmayor"], Obj2['Dmenor'])
    rule51 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Fmenor'] & Inic3["Dmayor"], Obj2['Fmenor'])
    rule52 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Fmayor'] & Inic3["Dmayor"], Obj2['Fmenor'])
    rule53 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Dmayor'] & Inic3["Dmenor"], Obj2['Dmenor'])
    rule54 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Dmenor'] & Inic3["Dmenor"], Obj2['Dmenor'])
    rule55 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Fmenor'] & Inic3["Dmenor"], Obj2['Fmenor'])
    rule56 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Fmayor'] & Inic3["Dmenor"], Obj2['Fmenor'])
    rule57 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Dmayor'] & Inic3["Fmenor"], Obj2['Dmenor'])
    rule58 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Dmenor'] & Inic3["Fmenor"], Obj2['Fmenor'])
    rule59 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Fmenor'] & Inic3["Fmenor"], Obj2['Fmenor'])
    rule60 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Fmayor'] & Inic3["Fmenor"], Obj2['Fmayor'])
    rule61 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Dmayor'] & Inic3["Fmayor"], Obj2['Fmenor'])
    rule62 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Dmenor'] & Inic3["Fmayor"], Obj2['Fmenor'])
    rule63 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Fmenor'] & Inic3["Fmayor"], Obj2['Fmayor'])
    rule64 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Fmayor'] & Inic3["Fmayor"], Obj2['Fmayor'])

    #create system control and simulation
    solving_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32, rule33, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50, rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60, rule61, rule62, rule63, rule64])
    solving = ctrl.ControlSystemSimulation(solving_ctrl)

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    solving.input['Inic1'] = value_ini_21
    solving.input['Inic2'] = value_ini_22
    solving.input['Inic3'] = value_ini_23
    # Crunch the numbers
    solving.compute()

    #value objetivo 2
    Obj2_result = solving.output['Objetivo 2']

    #update data
    n = 1
    m = 1

    with open('static/data/datamain.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[n] = ['Objetivo', row['Valor']]
            n=n+1
     
    #update table 
    data[2][1] = Obj2_result
    
    with open('static/data/datamain.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data)

    with open('static/data/data-inic.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_inic[m] = [data_inic[m][0], row['Valor']]
            m=m+1
  
    data_inic[3][1] = value_ini_21
    data_inic[4][1] = value_ini_22
    data_inic[5][1] = value_ini_23

    with open('static/data/data-inic.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data_inic)

    csvFile.close()

def calculate_obj3(value_ini_31):
    #OBJETIVO 3: INCURSIONAR EN NUEVAS OPORTUNIDADES DE NEGOCIO
    # Generate universe variables
    #   El rango de las iniciativas estrategicas es [0,110]
    #   El rango del objetivo de salida es [0,110]
    # Inic1 = Generar nuevas oportunidades de negocio

    # New Antecedent/Consequent objects hold universe variables and membership
    # functions
    Inic1 = ctrl.Antecedent(np.arange(0, 110, 1), 'Inic1')
    Obj3 = ctrl.Consequent(np.arange(0, 110, 1), 'Objetivo 3')

    # Generate fuzzy membership functions
    Inic1['Dmayor'] = fuzz.trapmf(Inic1.universe, [-1, 0, 20, 26])
    Inic1['Dmenor'] = fuzz.trimf(Inic1.universe, [21, 40, 57])
    Inic1['Fmenor'] = fuzz.trimf(Inic1.universe, [55, 60, 79])
    Inic1['Fmayor'] = fuzz.trapmf(Inic1.universe, [72, 80, 110, 120])

    Obj3['Dmayor'] = fuzz.trapmf(Obj3.universe, [-1, 0, 20, 40])
    Obj3['Dmenor'] = fuzz.trimf(Obj3.universe, [20, 40, 60])
    Obj3['Fmenor'] = fuzz.trimf(Obj3.universe, [40, 60, 80])
    Obj3['Fmayor'] = fuzz.trapmf(Obj3.universe, [60, 80, 110, 120])

    #generate rules membreship
    rule1 = ctrl.Rule(Inic1['Dmayor'], Obj3['Dmayor'])
    rule2 = ctrl.Rule(Inic1['Dmenor'], Obj3['Dmenor'])
    rule3 = ctrl.Rule(Inic1['Fmenor'], Obj3['Fmenor'])
    rule4 = ctrl.Rule(Inic1['Fmayor'], Obj3['Fmayor'])

    #create system control and simulation
    solving_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
    solving = ctrl.ControlSystemSimulation(solving_ctrl)

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    solving.input['Inic1'] = value_ini_31
    # Crunch the numbers
    solving.compute()

    #value objetivo 3
    Obj3_result = solving.output['Objetivo 3']

    #update data
    n = 1
    m = 1

    with open('static/data/datamain.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[n] = ['Objetivo', row['Valor']]
            n=n+1
     
    #update table obj
    data[3][1] = Obj3_result
    
    with open('static/data/datamain.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data)

    #update table inic
    with open('static/data/data-inic.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_inic[m] = [data_inic[m][0], row['Valor']]
            m=m+1
  
    data_inic[6][1] = value_ini_31


    with open('static/data/data-inic.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data_inic)

    csvFile.close()

    return Obj3_result

def calculate_sub1(value_ini_41, value_ini_42, value_ini_43):
    #OBJETIVO 4: OPTAR POR LA EXCELENCIA OPERACIONAL
    # Sub1 = subsistema de salida G. de la calidad y G de la estratégica
    # Generate universe variables
    #   El rango de las iniciativas estrategicas es [0,100]
    #   El rango del subsistema de salida es [0,100]

    # Sub1 = subsistema de salida G. de la calidad y G de la estratégica
    # Inic1 = Crear una cultura de planeación estratégica en la empresa
    # Inic2 = Establecer acciones, metodos y procedimientos de control y seguimiento a la gestión incluyendo 
    #         gestión de riesgo y seguimiento establecer mecanismos para la prevención y evaluación.
    # Inic3 = Implementar el Sistema de Gestión de la Calidad en la empresa

    # New Antecedent/Consequent objects hold universe variables and membership
    # functions
    Inic1 = ctrl.Antecedent(np.arange(0, 110, 1), 'Iniciativa 1')
    Inic2 = ctrl.Antecedent(np.arange(0, 110, 1), 'Iniciativa 2')
    Inic3 = ctrl.Antecedent(np.arange(0, 110, 1), 'Iniciativa 3')
    G_estrategica = ctrl.Consequent(np.arange(0, 110, 1), 'Gestion estrategica')
    G_calidad = ctrl.Consequent(np.arange(0, 110, 1), 'Gestion calidad')

    G_estrategica_ant = ctrl.Antecedent(np.arange(0, 110, 1), 'Gestion estrategica antecedente')
    G_calidad_ant = ctrl.Antecedent(np.arange(0, 110, 1), 'Gestion calidad antecedente')

    Sub1 = ctrl.Consequent(np.arange(0, 110, 1), 'subsistema 1')

    # Generate fuzzy membership functions
    Inic1['Dmayor'] = fuzz.trapmf(Inic1.universe, [-1, 0, 20, 31])
    Inic1['Dmenor'] = fuzz.trimf(Inic1.universe, [29, 40, 48])
    Inic1['Fmenor'] = fuzz.trimf(Inic1.universe, [47, 60, 76])
    Inic1['Fmayor'] = fuzz.trapmf(Inic1.universe, [63, 80, 110, 120])

    Inic2['Dmayor'] = fuzz.trapmf(Inic2.universe, [-1, 0, 20, 34])
    Inic2['Dmenor'] = fuzz.trimf(Inic2.universe, [33, 40, 55])
    Inic2['Fmenor'] = fuzz.trimf(Inic2.universe, [48, 60, 88])
    Inic2['Fmayor'] = fuzz.trapmf(Inic2.universe, [77, 80, 110, 120])

    Inic3['Dmayor'] = fuzz.trapmf(Inic3.universe, [-1, 0, 20, 31])
    Inic3['Dmenor'] = fuzz.trimf(Inic3.universe, [26, 40, 61])
    Inic3['Fmenor'] = fuzz.trimf(Inic3.universe, [56, 60, 77])
    Inic3['Fmayor'] = fuzz.trapmf(Inic3.universe, [75, 80, 110, 120])

    G_estrategica['Dmayor'] = fuzz.trapmf(G_estrategica.universe, [-1, 0, 20, 40])
    G_estrategica['Dmenor'] = fuzz.trimf(G_estrategica.universe, [20, 40, 60])
    G_estrategica['Fmenor'] = fuzz.trimf(G_estrategica.universe, [40, 60, 80])
    G_estrategica['Fmayor'] = fuzz.trapmf(G_estrategica.universe, [60, 80, 110, 120])

    G_estrategica_ant['Dmayor'] = fuzz.trapmf(G_estrategica_ant.universe, [-1, 0, 20, 40])
    G_estrategica_ant['Dmenor'] = fuzz.trimf(G_estrategica_ant.universe, [20, 40, 60])
    G_estrategica_ant['Fmenor'] = fuzz.trimf(G_estrategica_ant.universe, [40, 60, 80])
    G_estrategica_ant['Fmayor'] = fuzz.trapmf(G_estrategica_ant.universe, [60, 80, 110, 120])

    G_calidad['Dmayor'] = fuzz.trapmf(G_calidad.universe, [-1, 0, 20, 40])
    G_calidad['Dmenor'] = fuzz.trimf(G_calidad.universe, [20, 40, 60])
    G_calidad['Fmenor'] = fuzz.trimf(G_calidad.universe, [40, 60, 80])
    G_calidad['Fmayor'] = fuzz.trapmf(G_calidad.universe, [60, 80, 110, 120])

    G_calidad_ant['Dmayor'] = fuzz.trapmf(G_calidad_ant.universe, [-1, 0, 20, 40])
    G_calidad_ant['Dmenor'] = fuzz.trimf(G_calidad_ant.universe, [20, 40, 60])
    G_calidad_ant['Fmenor'] = fuzz.trimf(G_calidad_ant.universe, [40, 60, 80])
    G_calidad_ant['Fmayor'] = fuzz.trapmf(G_calidad_ant.universe, [60, 80, 110, 120])

    Sub1['Dmayor'] = fuzz.trapmf(Sub1.universe, [-1, 0, 20, 40])
    Sub1['Dmenor'] = fuzz.trimf(Sub1.universe, [20, 40, 60])
    Sub1['Fmenor'] = fuzz.trimf(Sub1.universe, [40, 60, 80])
    Sub1['Fmayor'] = fuzz.trapmf(Sub1.universe, [60, 80, 110, 120])

    #generate rules membreship
    rule1 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Dmayor'], G_estrategica['Dmayor'])
    rule2 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Dmayor'], G_estrategica['Dmayor'])
    rule3 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Dmayor'], G_estrategica['Dmenor'])
    rule4 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Dmayor'], G_estrategica['Dmenor'])
    rule5 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Dmenor'], G_estrategica['Dmayor'])
    rule6 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Dmenor'], G_estrategica['Dmenor'])
    rule7 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Dmenor'], G_estrategica['Dmenor'])
    rule8 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Dmenor'], G_estrategica['Fmenor'])
    rule9 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Fmenor'], G_estrategica['Dmenor'])
    rule10 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Fmenor'], G_estrategica['Dmenor'])
    rule11 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Fmenor'], G_estrategica['Fmenor'])
    rule12 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Fmenor'], G_estrategica['Fmenor'])
    rule13 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Fmayor'], G_estrategica['Fmenor'])
    rule14 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Fmayor'], G_estrategica['Fmenor'])
    rule15 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Fmayor'], G_estrategica['Fmayor'])
    rule16 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Fmayor'], G_estrategica['Fmenor'])
    rule17 = ctrl.Rule(Inic3['Dmayor'], G_calidad['Dmayor'])
    rule18 = ctrl.Rule(Inic3['Dmenor'], G_calidad['Dmenor'])
    rule19 = ctrl.Rule(Inic3['Fmenor'], G_calidad['Fmenor'])
    rule20 = ctrl.Rule(Inic3['Fmayor'], G_calidad['Fmayor'])

    rule21 = ctrl.Rule(G_estrategica_ant['Dmayor'] & G_calidad_ant['Dmayor'], Sub1['Dmayor'])
    rule22 = ctrl.Rule(G_estrategica_ant['Dmenor'] & G_calidad_ant['Dmayor'], Sub1['Dmenor'])
    rule23 = ctrl.Rule(G_estrategica_ant['Fmenor'] & G_calidad_ant['Dmayor'], Sub1['Dmenor'])
    rule24 = ctrl.Rule(G_estrategica_ant['Fmayor'] & G_calidad_ant['Dmayor'], Sub1['Fmenor'])
    rule25 = ctrl.Rule(G_estrategica_ant['Dmayor'] & G_calidad_ant['Dmenor'], Sub1['Dmayor'])
    rule26 = ctrl.Rule(G_estrategica_ant['Dmenor'] & G_calidad_ant['Dmenor'], Sub1['Dmenor'])
    rule27 = ctrl.Rule(G_estrategica_ant['Fmenor'] & G_calidad_ant['Dmenor'], Sub1['Dmenor'])
    rule28 = ctrl.Rule(G_estrategica_ant['Fmayor'] & G_calidad_ant['Dmenor'], Sub1['Fmenor'])
    rule29 = ctrl.Rule(G_estrategica_ant['Dmayor'] & G_calidad_ant['Fmenor'], Sub1['Dmenor'])
    rule30 = ctrl.Rule(G_estrategica_ant['Dmenor'] & G_calidad_ant['Fmenor'], Sub1['Dmenor'])
    rule31 = ctrl.Rule(G_estrategica_ant['Fmenor'] & G_calidad_ant['Fmenor'], Sub1['Fmenor'])
    rule32 = ctrl.Rule(G_estrategica_ant['Fmayor'] & G_calidad_ant['Fmenor'], Sub1['Fmayor'])
    rule33 = ctrl.Rule(G_estrategica_ant['Dmayor'] & G_calidad_ant['Fmayor'], Sub1['Dmenor'])
    rule34 = ctrl.Rule(G_estrategica_ant['Dmenor'] & G_calidad_ant['Fmayor'], Sub1['Fmenor'])
    rule35 = ctrl.Rule(G_estrategica_ant['Fmenor'] & G_calidad_ant['Fmayor'], Sub1['Fmayor'])
    rule36 = ctrl.Rule(G_estrategica_ant['Fmayor'] & G_calidad_ant['Fmayor'], Sub1['Fmayor'])

    solving_G_estrategica_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16])
    solving_G_calidad_ctrl = ctrl.ControlSystem([rule17, rule18, rule19, rule20])
    solving_Sub1_ctrl = ctrl.ControlSystem([rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36])

    solving_G_estrategica = ctrl.ControlSystemSimulation(solving_G_estrategica_ctrl)
    solving_G_calidad = ctrl.ControlSystemSimulation(solving_G_calidad_ctrl)
    solving_Sub1 = ctrl.ControlSystemSimulation(solving_Sub1_ctrl)

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    solving_G_estrategica.input['Iniciativa 1'] = value_ini_41
    solving_G_estrategica.input['Iniciativa 2'] = value_ini_42
    solving_G_calidad.input['Iniciativa 3'] = value_ini_43

    # Crunch the numbers
    solving_G_estrategica.compute()
    solving_G_calidad.compute()

    G_estrategica_value = solving_G_estrategica.output['Gestion estrategica']
    G_calidad_value = solving_G_calidad.output['Gestion calidad']

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    solving_Sub1.input['Gestion estrategica antecedente'] = G_estrategica_value
    solving_Sub1.input['Gestion calidad antecedente'] = G_calidad_value

    # Crunch the numbers
    solving_Sub1.compute()

    Sub1_value = solving_Sub1.output['subsistema 1']

    m = 1

    #update table inic
    with open('static/data/data-inic.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_inic[m] = [data_inic[m][0], row['Valor']]
            m=m+1

    data_inic[7][1] = value_ini_41
    data_inic[8][1] = value_ini_42
    data_inic[9][1] = value_ini_43


    with open('static/data/data-inic.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data_inic)

    csvFile.close()

    return Sub1_value

def calculate_sub2(value_ini_44, value_ini_45, value_ini_46, value_ini_47):
    # Sub2 = subsistema de salida G. Administrativa y G Juridica.
    # Inic4 = Atender oportunamente los asuntos legales que surjan respecto a las actividades de la organización.
    # Inic5 = Crear una cultura de optimización del uso de los recurso de la emresa.
    # Inic6 = Garantizar la eficiencia y la eficacia en los subprocesos compras y almacén.
    # Inic7 = Garantizar que exista una información documental veraz y oportuna en la empresa.

    Inic4 = ctrl.Antecedent(np.arange(0, 110, 1), 'Iniciativa 4')
    Inic5 = ctrl.Antecedent(np.arange(0, 110, 1), 'Iniciativa 5')
    Inic6 = ctrl.Antecedent(np.arange(0, 110, 1), 'Iniciativa 6')
    Inic7 = ctrl.Antecedent(np.arange(0, 110, 1), 'Iniciativa 7')
    G_administrativa = ctrl.Consequent(np.arange(0, 110, 1), 'Gestion administrativa')
    G_juridica = ctrl.Consequent(np.arange(0, 110, 1), 'Gestion juridica')

    G_administrativa_ant = ctrl.Antecedent(np.arange(0, 110, 1), 'Gestion administrativa antecedente')
    G_juridica_ant = ctrl.Antecedent(np.arange(0, 110, 1), 'Gestion juridica antecedente')

    Sub2 = ctrl.Consequent(np.arange(0, 110, 1), 'subsistema 2')

    # Generate fuzzy membership functions
    Inic4['Dmayor'] = fuzz.trapmf(Inic4.universe, [-1, 0, 20, 30])
    Inic4['Dmenor'] = fuzz.trimf(Inic4.universe, [28, 40, 54])
    Inic4['Fmenor'] = fuzz.trimf(Inic4.universe, [50, 60, 77])
    Inic4['Fmayor'] = fuzz.trapmf(Inic4.universe, [69, 80, 110, 120])

    Inic5['Dmayor'] = fuzz.trapmf(Inic5.universe, [-1, 0, 20, 25])
    Inic5['Dmenor'] = fuzz.trimf(Inic5.universe, [24, 40, 48])
    Inic5['Fmenor'] = fuzz.trimf(Inic5.universe, [34, 60, 77])
    Inic5['Fmayor'] = fuzz.trapmf(Inic5.universe, [61, 80, 110, 120])

    Inic6['Dmayor'] = fuzz.trapmf(Inic6.universe, [-1, 0, 20, 33])
    Inic6['Dmenor'] = fuzz.trimf(Inic6.universe, [21, 40, 48])
    Inic6['Fmenor'] = fuzz.trimf(Inic6.universe, [47, 60, 80])
    Inic6['Fmayor'] = fuzz.trapmf(Inic6.universe, [75, 80, 110, 120])

    Inic7['Dmayor'] = fuzz.trapmf(Inic7.universe, [-1, 0, 20, 28])
    Inic7['Dmenor'] = fuzz.trimf(Inic7.universe, [27, 40, 62])
    Inic7['Fmenor'] = fuzz.trimf(Inic7.universe, [47, 60, 75])
    Inic7['Fmayor'] = fuzz.trapmf(Inic7.universe, [74, 80, 110, 120])

    G_administrativa['Dmayor'] = fuzz.trapmf(G_administrativa.universe, [-1, 0, 20, 40])
    G_administrativa['Dmenor'] = fuzz.trimf(G_administrativa.universe, [20, 40, 60])
    G_administrativa['Fmenor'] = fuzz.trimf(G_administrativa.universe, [40, 60, 80])
    G_administrativa['Fmayor'] = fuzz.trapmf(G_administrativa.universe, [60, 80, 110, 120])

    G_administrativa_ant['Dmayor'] = fuzz.trapmf(G_administrativa_ant.universe, [-1, 0, 20, 40])
    G_administrativa_ant['Dmenor'] = fuzz.trimf(G_administrativa_ant.universe, [20, 40, 60])
    G_administrativa_ant['Fmenor'] = fuzz.trimf(G_administrativa_ant.universe, [40, 60, 80])
    G_administrativa_ant['Fmayor'] = fuzz.trapmf(G_administrativa_ant.universe, [60, 80, 110, 120])

    G_juridica['Dmayor'] = fuzz.trapmf(G_juridica.universe, [-1, 0, 20, 40])
    G_juridica['Dmenor'] = fuzz.trimf(G_juridica.universe, [20, 40, 60])
    G_juridica['Fmenor'] = fuzz.trimf(G_juridica.universe, [40, 60, 80])
    G_juridica['Fmayor'] = fuzz.trapmf(G_juridica.universe, [60, 80, 110, 120])

    G_juridica_ant['Dmayor'] = fuzz.trapmf(G_juridica_ant.universe, [-1, 0, 20, 40])
    G_juridica_ant['Dmenor'] = fuzz.trimf(G_juridica_ant.universe, [20, 40, 60])
    G_juridica_ant['Fmenor'] = fuzz.trimf(G_juridica_ant.universe, [40, 60, 80])
    G_juridica_ant['Fmayor'] = fuzz.trapmf(G_juridica_ant.universe, [60, 80, 110, 120])

    Sub2['Dmayor'] = fuzz.trapmf(Sub2.universe, [-1, 0, 20, 40])
    Sub2['Dmenor'] = fuzz.trimf(Sub2.universe, [20, 40, 60])
    Sub2['Fmenor'] = fuzz.trimf(Sub2.universe, [40, 60, 80])
    Sub2['Fmayor'] = fuzz.trapmf(Sub2.universe, [60, 80, 110, 120])

    rule1 = ctrl.Rule(Inic4['Dmayor'], G_juridica['Dmayor'])
    rule2 = ctrl.Rule(Inic4['Dmenor'], G_juridica['Dmenor'])
    rule3 = ctrl.Rule(Inic4['Fmenor'], G_juridica['Fmenor'])
    rule4 = ctrl.Rule(Inic4['Fmayor'], G_juridica['Fmayor'])

    rule5 = ctrl.Rule(Inic5['Dmayor'] & Inic6['Dmayor'] & Inic7["Dmayor"], G_administrativa['Dmayor'])
    rule6 = ctrl.Rule(Inic5['Dmayor'] & Inic6['Dmenor'] & Inic7["Dmayor"], G_administrativa['Dmayor'])
    rule7 = ctrl.Rule(Inic5['Dmayor'] & Inic6['Fmenor'] & Inic7["Dmayor"], G_administrativa['Dmenor'])
    rule8 = ctrl.Rule(Inic5['Dmayor'] & Inic6['Fmayor'] & Inic7["Dmayor"], G_administrativa['Dmenor'])
    rule9 = ctrl.Rule(Inic5['Dmayor'] & Inic6['Dmayor'] & Inic7["Dmenor"], G_administrativa['Dmayor'])
    rule10 = ctrl.Rule(Inic5['Dmayor'] & Inic6['Dmenor'] & Inic7["Dmenor"], G_administrativa['Dmenor'])
    rule11 = ctrl.Rule(Inic5['Dmayor'] & Inic6['Fmenor'] & Inic7["Dmenor"], G_administrativa['Dmenor'])
    rule12 = ctrl.Rule(Inic5['Dmayor'] & Inic6['Fmayor'] & Inic7["Dmenor"], G_administrativa['Dmenor'])
    rule13 = ctrl.Rule(Inic5['Dmayor'] & Inic6['Dmayor'] & Inic7["Fmenor"], G_administrativa['Dmayor'])
    rule14 = ctrl.Rule(Inic5['Dmayor'] & Inic6['Dmenor'] & Inic7["Fmenor"], G_administrativa['Dmenor'])
    rule15 = ctrl.Rule(Inic5['Dmayor'] & Inic6['Fmenor'] & Inic7["Fmenor"], G_administrativa['Dmenor'])
    rule16 = ctrl.Rule(Inic5['Dmayor'] & Inic6['Fmayor'] & Inic7["Fmenor"], G_administrativa['Dmenor'])
    rule17 = ctrl.Rule(Inic5['Dmayor'] & Inic6['Dmayor'] & Inic7["Fmayor"], G_administrativa['Dmenor'])
    rule18 = ctrl.Rule(Inic5['Dmayor'] & Inic6['Dmenor'] & Inic7["Fmayor"], G_administrativa['Fmenor'])
    rule19 = ctrl.Rule(Inic5['Dmayor'] & Inic6['Fmenor'] & Inic7["Fmayor"], G_administrativa['Fmenor'])
    rule20 = ctrl.Rule(Inic5['Dmayor'] & Inic6['Fmayor'] & Inic7["Fmayor"], G_administrativa['Fmenor'])

    rule21 = ctrl.Rule(Inic5['Dmenor'] & Inic6['Dmayor'] & Inic7["Dmayor"], G_administrativa['Dmayor'])
    rule22 = ctrl.Rule(Inic5['Dmenor'] & Inic6['Dmenor'] & Inic7["Dmayor"], G_administrativa['Dmayor'])
    rule23 = ctrl.Rule(Inic5['Dmenor'] & Inic6['Fmenor'] & Inic7["Dmayor"], G_administrativa['Dmenor'])
    rule24 = ctrl.Rule(Inic5['Dmenor'] & Inic6['Fmayor'] & Inic7["Dmayor"], G_administrativa['Dmenor'])
    rule25 = ctrl.Rule(Inic5['Dmenor'] & Inic6['Dmayor'] & Inic7["Dmenor"], G_administrativa['Dmayor'])
    rule26 = ctrl.Rule(Inic5['Dmenor'] & Inic6['Dmenor'] & Inic7["Dmenor"], G_administrativa['Dmenor'])
    rule27 = ctrl.Rule(Inic5['Dmenor'] & Inic6['Fmenor'] & Inic7["Dmenor"], G_administrativa['Dmenor'])
    rule28 = ctrl.Rule(Inic5['Dmenor'] & Inic6['Fmayor'] & Inic7["Dmenor"], G_administrativa['Fmenor'])
    rule29 = ctrl.Rule(Inic5['Dmenor'] & Inic6['Dmayor'] & Inic7["Fmenor"], G_administrativa['Dmayor'])
    rule30 = ctrl.Rule(Inic5['Dmenor'] & Inic6['Dmenor'] & Inic7["Fmenor"], G_administrativa['Dmenor'])
    rule31 = ctrl.Rule(Inic5['Dmenor'] & Inic6['Fmenor'] & Inic7["Fmenor"], G_administrativa['Fmenor'])
    rule32 = ctrl.Rule(Inic5['Dmenor'] & Inic6['Fmayor'] & Inic7["Fmenor"], G_administrativa['Fmenor'])
    rule33 = ctrl.Rule(Inic5['Dmenor'] & Inic6['Dmayor'] & Inic7["Fmayor"], G_administrativa['Dmenor'])
    rule34 = ctrl.Rule(Inic5['Dmenor'] & Inic6['Dmenor'] & Inic7["Fmayor"], G_administrativa['Fmenor'])
    rule35 = ctrl.Rule(Inic5['Dmenor'] & Inic6['Fmenor'] & Inic7["Fmayor"], G_administrativa['Fmenor'])
    rule36 = ctrl.Rule(Inic5['Dmenor'] & Inic6['Fmayor'] & Inic7["Fmayor"], G_administrativa['Fmenor'])

    rule37 = ctrl.Rule(Inic5['Fmenor'] & Inic6['Dmayor'] & Inic7["Dmayor"], G_administrativa['Dmayor'])
    rule38 = ctrl.Rule(Inic5['Fmenor'] & Inic6['Dmenor'] & Inic7["Dmayor"], G_administrativa['Dmenor'])
    rule39 = ctrl.Rule(Inic5['Fmenor'] & Inic6['Fmenor'] & Inic7["Dmayor"], G_administrativa['Dmenor'])
    rule40 = ctrl.Rule(Inic5['Fmenor'] & Inic6['Fmayor'] & Inic7["Dmayor"], G_administrativa['Fmenor'])
    rule41 = ctrl.Rule(Inic5['Fmenor'] & Inic6['Dmayor'] & Inic7["Dmenor"], G_administrativa['Dmayor'])
    rule42 = ctrl.Rule(Inic5['Fmenor'] & Inic6['Dmenor'] & Inic7["Dmenor"], G_administrativa['Dmenor'])
    rule43 = ctrl.Rule(Inic5['Fmenor'] & Inic6['Fmenor'] & Inic7["Dmenor"], G_administrativa['Fmenor'])
    rule44 = ctrl.Rule(Inic5['Fmenor'] & Inic6['Fmayor'] & Inic7["Dmenor"], G_administrativa['Fmenor'])
    rule45 = ctrl.Rule(Inic5['Fmenor'] & Inic6['Dmayor'] & Inic7["Fmenor"], G_administrativa['Dmenor'])
    rule46 = ctrl.Rule(Inic5['Fmenor'] & Inic6['Dmenor'] & Inic7["Fmenor"], G_administrativa['Fmenor'])
    rule47 = ctrl.Rule(Inic5['Fmenor'] & Inic6['Fmenor'] & Inic7["Fmenor"], G_administrativa['Fmenor'])
    rule48 = ctrl.Rule(Inic5['Fmenor'] & Inic6['Fmayor'] & Inic7["Fmenor"], G_administrativa['Fmenor'])
    rule49 = ctrl.Rule(Inic5['Fmenor'] & Inic6['Dmayor'] & Inic7["Fmayor"], G_administrativa['Dmenor'])
    rule50 = ctrl.Rule(Inic5['Fmenor'] & Inic6['Dmenor'] & Inic7["Fmayor"], G_administrativa['Fmenor'])
    rule51 = ctrl.Rule(Inic5['Fmenor'] & Inic6['Fmenor'] & Inic7["Fmayor"], G_administrativa['Fmenor'])
    rule52 = ctrl.Rule(Inic5['Fmenor'] & Inic6['Fmayor'] & Inic7["Fmayor"], G_administrativa['Fmayor'])

    rule53 = ctrl.Rule(Inic5['Fmayor'] & Inic6['Dmayor'] & Inic7["Dmayor"], G_administrativa['Dmayor'])
    rule54 = ctrl.Rule(Inic5['Fmayor'] & Inic6['Dmenor'] & Inic7["Dmayor"], G_administrativa['Dmenor'])
    rule55 = ctrl.Rule(Inic5['Fmayor'] & Inic6['Fmenor'] & Inic7["Dmayor"], G_administrativa['Fmenor'])
    rule56 = ctrl.Rule(Inic5['Fmayor'] & Inic6['Fmayor'] & Inic7["Dmayor"], G_administrativa['Fmenor'])
    rule57 = ctrl.Rule(Inic5['Fmayor'] & Inic6['Dmayor'] & Inic7["Dmenor"], G_administrativa['Dmenor'])
    rule58 = ctrl.Rule(Inic5['Fmayor'] & Inic6['Dmenor'] & Inic7["Dmenor"], G_administrativa['Dmenor'])
    rule59 = ctrl.Rule(Inic5['Fmayor'] & Inic6['Fmenor'] & Inic7["Dmenor"], G_administrativa['Fmenor'])
    rule60 = ctrl.Rule(Inic5['Fmayor'] & Inic6['Fmayor'] & Inic7["Dmenor"], G_administrativa['Fmenor'])
    rule61 = ctrl.Rule(Inic5['Fmayor'] & Inic6['Dmayor'] & Inic7["Fmenor"], G_administrativa['Dmenor'])
    rule62 = ctrl.Rule(Inic5['Fmayor'] & Inic6['Dmenor'] & Inic7["Fmenor"], G_administrativa['Fmenor'])
    rule63 = ctrl.Rule(Inic5['Fmayor'] & Inic6['Fmenor'] & Inic7["Fmenor"], G_administrativa['Fmenor'])
    rule64 = ctrl.Rule(Inic5['Fmayor'] & Inic6['Fmayor'] & Inic7["Fmenor"], G_administrativa['Fmayor'])
    rule65 = ctrl.Rule(Inic5['Fmayor'] & Inic6['Dmayor'] & Inic7["Fmayor"], G_administrativa['Fmenor'])
    rule66 = ctrl.Rule(Inic5['Fmayor'] & Inic6['Dmenor'] & Inic7["Fmayor"], G_administrativa['Fmenor'])
    rule67 = ctrl.Rule(Inic5['Fmayor'] & Inic6['Fmenor'] & Inic7["Fmayor"], G_administrativa['Fmayor'])
    rule68 = ctrl.Rule(Inic5['Fmayor'] & Inic6['Fmayor'] & Inic7["Fmayor"], G_administrativa['Fmayor'])

    rule69 = ctrl.Rule(G_juridica_ant['Dmayor'] & G_administrativa_ant['Dmayor'], Sub2['Dmayor'])
    rule70 = ctrl.Rule(G_juridica_ant['Dmenor'] & G_administrativa_ant['Dmayor'], Sub2['Dmenor'])
    rule71 = ctrl.Rule(G_juridica_ant['Fmenor'] & G_administrativa_ant['Dmayor'], Sub2['Dmenor'])
    rule72 = ctrl.Rule(G_juridica_ant['Fmayor'] & G_administrativa_ant['Dmayor'], Sub2['Fmenor'])
    rule73 = ctrl.Rule(G_juridica_ant['Dmayor'] & G_administrativa_ant['Dmenor'], Sub2['Dmayor'])
    rule74 = ctrl.Rule(G_juridica_ant['Dmenor'] & G_administrativa_ant['Dmenor'], Sub2['Dmenor'])
    rule75 = ctrl.Rule(G_juridica_ant['Fmenor'] & G_administrativa_ant['Dmenor'], Sub2['Fmenor'])
    rule76 = ctrl.Rule(G_juridica_ant['Fmayor'] & G_administrativa_ant['Dmenor'], Sub2['Fmenor'])
    rule77 = ctrl.Rule(G_juridica_ant['Dmayor'] & G_administrativa_ant['Fmenor'], Sub2['Dmenor'])
    rule78 = ctrl.Rule(G_juridica_ant['Dmenor'] & G_administrativa_ant['Fmenor'], Sub2['Dmenor'])
    rule79 = ctrl.Rule(G_juridica_ant['Fmenor'] & G_administrativa_ant['Fmenor'], Sub2['Fmenor'])
    rule80 = ctrl.Rule(G_juridica_ant['Fmayor'] & G_administrativa_ant['Fmenor'], Sub2['Fmayor'])
    rule81 = ctrl.Rule(G_juridica_ant['Dmayor'] & G_administrativa_ant['Fmayor'], Sub2['Dmenor'])
    rule82 = ctrl.Rule(G_juridica_ant['Dmenor'] & G_administrativa_ant['Fmayor'], Sub2['Dmenor'])
    rule83 = ctrl.Rule(G_juridica_ant['Fmenor'] & G_administrativa_ant['Fmayor'], Sub2['Fmayor'])
    rule84 = ctrl.Rule(G_juridica_ant['Fmayor'] & G_administrativa_ant['Fmayor'], Sub2['Fmayor'])

    solving_G_juridica_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
    solving_G_administrativa_ctrl = ctrl.ControlSystem([rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36,
                                                rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50, rule51, rule52,
                                                rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60, rule61, rule62, rule63, rule64, rule65, rule66, rule67, rule68])
    solving_Sub2_ctrl = ctrl.ControlSystem([rule69, rule70, rule71, rule72, rule73, rule74, rule75, rule76, rule77, rule78, rule79, rule80, rule81, rule82, rule83, rule84])

    solving_G_juridica = ctrl.ControlSystemSimulation(solving_G_juridica_ctrl)
    solving_G_administrativa = ctrl.ControlSystemSimulation(solving_G_administrativa_ctrl)
    solving_sub2 = ctrl.ControlSystemSimulation(solving_Sub2_ctrl)

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    solving_G_juridica.input['Iniciativa 4'] = value_ini_44
    solving_G_administrativa.input['Iniciativa 5'] = value_ini_45
    solving_G_administrativa.input['Iniciativa 6'] = value_ini_46
    solving_G_administrativa.input['Iniciativa 7'] = value_ini_47
    # Crunch the numbers
    solving_G_juridica.compute()
    solving_G_administrativa.compute()

    G_juridica_value = solving_G_juridica.output['Gestion juridica']
    G_administrativa_value = solving_G_administrativa.output['Gestion administrativa']

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    solving_sub2.input['Gestion juridica antecedente'] = G_juridica_value
    solving_sub2.input['Gestion administrativa antecedente'] = G_administrativa_value

    # Crunch the numbers
    solving_sub2.compute()

    Sub2_value = solving_sub2.output['subsistema 2']

    m = 1
    #update table inic
    with open('static/data/data-inic.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_inic[m] = [data_inic[m][0], row['Valor']]
            m=m+1

    data_inic[10][1] = value_ini_44
    data_inic[11][1] = value_ini_45
    data_inic[12][1] = value_ini_46
    data_inic[13][1] = value_ini_47

    with open('static/data/data-inic.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data_inic)

    csvFile.close()

    return Sub2_value

def calculate_sub3(value_ini_48, value_ini_49):
    # Sub3 = G de la experiencia y G de mercadeo y ventas.
    # Inic1 = Realizar una getion eficiente de cartera.
    # Inic2 = Exceder las expectativas del cliente.

    # New Antecedent/Consequent objects hold universe variables and membership
    # functions
    Inic1 = ctrl.Antecedent(np.arange(0, 110, 1), 'Iniciativa 1')
    Inic2 = ctrl.Antecedent(np.arange(0, 110, 1), 'Iniciativa 2')

    G_experiencia = ctrl.Consequent(np.arange(0, 110, 1), 'Gestion experiencia')
    G_mercadeo = ctrl.Consequent(np.arange(0, 110, 1), 'Gestion mercadeo')

    G_experiencia_ant = ctrl.Antecedent(np.arange(0, 110, 1), 'Gestion experiencia antecedente')
    G_mercadeo_ant = ctrl.Antecedent(np.arange(0, 110, 1), 'Gestion mercadeo antecedente')

    Sub3 = ctrl.Consequent(np.arange(0, 110, 1), 'subsistema 3')

    # Generate fuzzy membership functions
    Inic1['Dmayor'] = fuzz.trapmf(Inic1.universe, [-1, 0, 20, 30])
    Inic1['Dmenor'] = fuzz.trimf(Inic1.universe, [28, 40, 54])
    Inic1['Fmenor'] = fuzz.trimf(Inic1.universe, [50, 60, 77])
    Inic1['Fmayor'] = fuzz.trapmf(Inic1.universe, [69, 80, 110, 120])

    Inic2['Dmayor'] = fuzz.trapmf(Inic2.universe, [-1, 0, 20, 26])
    Inic2['Dmenor'] = fuzz.trimf(Inic2.universe, [15, 40, 46])
    Inic2['Fmenor'] = fuzz.trimf(Inic2.universe, [33, 60, 68])
    Inic2['Fmayor'] = fuzz.trapmf(Inic2.universe, [67, 80, 110, 120])

    G_experiencia['Dmayor'] = fuzz.trapmf(G_experiencia.universe, [-1, 0, 20, 40])
    G_experiencia['Dmenor'] = fuzz.trimf(G_experiencia.universe, [20, 40, 60])
    G_experiencia['Fmenor'] = fuzz.trimf(G_experiencia.universe, [40, 60, 80])
    G_experiencia['Fmayor'] = fuzz.trapmf(G_experiencia.universe, [60, 80, 110, 120])

    G_experiencia_ant['Dmayor'] = fuzz.trapmf(G_experiencia_ant.universe, [-1, 0, 20, 40])
    G_experiencia_ant['Dmenor'] = fuzz.trimf(G_experiencia_ant.universe, [20, 40, 60])
    G_experiencia_ant['Fmenor'] = fuzz.trimf(G_experiencia_ant.universe, [40, 60, 80])
    G_experiencia_ant['Fmayor'] = fuzz.trapmf(G_experiencia_ant.universe, [60, 80, 110, 120])

    G_mercadeo['Dmayor'] = fuzz.trapmf(G_mercadeo.universe, [-1, 0, 20, 40])
    G_mercadeo['Dmenor'] = fuzz.trimf(G_mercadeo.universe, [20, 40, 60])
    G_mercadeo['Fmenor'] = fuzz.trimf(G_mercadeo.universe, [40, 60, 80])
    G_mercadeo['Fmayor'] = fuzz.trapmf(G_mercadeo.universe, [60, 80, 110, 120])

    G_mercadeo_ant['Dmayor'] = fuzz.trapmf(G_mercadeo_ant.universe, [-1, 0, 20, 40])
    G_mercadeo_ant['Dmenor'] = fuzz.trimf(G_mercadeo_ant.universe, [20, 40, 60])
    G_mercadeo_ant['Fmenor'] = fuzz.trimf(G_mercadeo_ant.universe, [40, 60, 80])
    G_mercadeo_ant['Fmayor'] = fuzz.trapmf(G_mercadeo_ant.universe, [60, 80, 110, 120])

    Sub3['Dmayor'] = fuzz.trapmf(Sub3.universe, [-1, 0, 20, 40])
    Sub3['Dmenor'] = fuzz.trimf(Sub3.universe, [20, 40, 60])
    Sub3['Fmenor'] = fuzz.trimf(Sub3.universe, [40, 60, 80])
    Sub3['Fmayor'] = fuzz.trapmf(Sub3.universe, [60, 80, 110, 120])

    rule1 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Dmayor'], G_experiencia['Dmayor'])
    rule2 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Dmayor'], G_experiencia['Dmayor'])
    rule3 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Dmayor'], G_experiencia['Dmenor'])
    rule4 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Dmayor'], G_experiencia['Fmenor'])
    rule5 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Dmenor'], G_experiencia['Dmayor'])
    rule6 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Dmenor'], G_experiencia['Dmenor'])
    rule7 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Dmenor'], G_experiencia['Fmenor'])
    rule8 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Dmenor'], G_experiencia['Fmenor'])
    rule9 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Fmenor'], G_experiencia['Dmenor'])
    rule10 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Fmenor'], G_experiencia['Fmenor'])
    rule11 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Fmenor'], G_experiencia['Fmenor'])
    rule12 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Fmenor'], G_experiencia['Fmayor'])
    rule13 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Fmayor'], G_experiencia['Dmenor'])
    rule14 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Fmayor'], G_experiencia['Dmenor'])
    rule15 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Fmayor'], G_experiencia['Fmayor'])
    rule16 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Fmayor'], G_experiencia['Fmayor'])

    rule17 = ctrl.Rule(Inic2['Dmayor'], G_mercadeo['Dmayor'])
    rule18 = ctrl.Rule(Inic2['Dmenor'], G_mercadeo['Dmenor'])
    rule19 = ctrl.Rule(Inic2['Fmenor'], G_mercadeo['Fmenor'])
    rule20 = ctrl.Rule(Inic2['Fmayor'], G_mercadeo['Fmayor'])

    rule21 = ctrl.Rule(G_experiencia_ant['Dmayor'] & G_mercadeo_ant['Dmayor'], Sub3['Dmayor'])
    rule22 = ctrl.Rule(G_experiencia_ant['Dmenor'] & G_mercadeo_ant['Dmayor'], Sub3['Dmenor'])
    rule23 = ctrl.Rule(G_experiencia_ant['Fmenor'] & G_mercadeo_ant['Dmayor'], Sub3['Dmenor'])
    rule24 = ctrl.Rule(G_experiencia_ant['Fmayor'] & G_mercadeo_ant['Dmayor'], Sub3['Fmenor'])
    rule25 = ctrl.Rule(G_experiencia_ant['Dmayor'] & G_mercadeo_ant['Dmenor'], Sub3['Dmayor'])
    rule26 = ctrl.Rule(G_experiencia_ant['Dmenor'] & G_mercadeo_ant['Dmenor'], Sub3['Dmenor'])
    rule27 = ctrl.Rule(G_experiencia_ant['Fmenor'] & G_mercadeo_ant['Dmenor'], Sub3['Dmenor'])
    rule28 = ctrl.Rule(G_experiencia_ant['Fmayor'] & G_mercadeo_ant['Dmenor'], Sub3['Fmenor'])
    rule29 = ctrl.Rule(G_experiencia_ant['Dmayor'] & G_mercadeo_ant['Fmenor'], Sub3['Dmenor'])
    rule30 = ctrl.Rule(G_experiencia_ant['Dmenor'] & G_mercadeo_ant['Fmenor'], Sub3['Dmenor'])
    rule31 = ctrl.Rule(G_experiencia_ant['Fmenor'] & G_mercadeo_ant['Fmenor'], Sub3['Fmenor'])
    rule32 = ctrl.Rule(G_experiencia_ant['Fmayor'] & G_mercadeo_ant['Fmenor'], Sub3['Fmayor'])
    rule33 = ctrl.Rule(G_experiencia_ant['Dmayor'] & G_mercadeo_ant['Fmayor'], Sub3['Dmenor'])
    rule34 = ctrl.Rule(G_experiencia_ant['Dmenor'] & G_mercadeo_ant['Fmayor'], Sub3['Fmenor'])
    rule35 = ctrl.Rule(G_experiencia_ant['Fmenor'] & G_mercadeo_ant['Fmayor'], Sub3['Fmayor'])
    rule36 = ctrl.Rule(G_experiencia_ant['Fmayor'] & G_mercadeo_ant['Fmayor'], Sub3['Fmayor'])

    solving_G_experiencia_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16])
    solving_G_mercadeo_ctrl = ctrl.ControlSystem([rule17, rule18, rule19, rule20])
    solving_Sub3_ctrl = ctrl.ControlSystem([rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36])

    solving_G_experiencia = ctrl.ControlSystemSimulation(solving_G_experiencia_ctrl)
    solving_G_mercadeo = ctrl.ControlSystemSimulation(solving_G_mercadeo_ctrl)
    solving_Sub3 = ctrl.ControlSystemSimulation(solving_Sub3_ctrl)

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    solving_G_experiencia.input['Iniciativa 1'] = value_ini_48
    solving_G_experiencia.input['Iniciativa 2'] = value_ini_49
    solving_G_mercadeo.input['Iniciativa 2'] = value_ini_49

    # Crunch the numbers
    solving_G_experiencia.compute()
    solving_G_mercadeo.compute()

    G_experiencia_value = solving_G_experiencia.output['Gestion experiencia']
    G_mercadeo_value = solving_G_mercadeo.output['Gestion mercadeo']

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    solving_Sub3.input['Gestion experiencia antecedente'] = G_experiencia_value
    solving_Sub3.input['Gestion mercadeo antecedente'] = G_mercadeo_value

    # Crunch the numbers
    solving_Sub3.compute()

    Sub3_value = solving_Sub3.output['subsistema 3']

    m = 1
    #update table inic
    with open('static/data/data-inic.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_inic[m] = [data_inic[m][0], row['Valor']]
            m=m+1

    data_inic[14][1] = value_ini_48
    data_inic[15][1] = value_ini_49

    with open('static/data/data-inic.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data_inic)

    csvFile.close()


    return Sub3_value

def calculate_obj4(value_sub1, value_sub2, value_sub3):    
    #OBJETIVO 4: OPTAR POR LA EXCELENCIA OPERACIONAL
    # Generate universe variables
    #   El rango de las iniciativas estrategicas es [0,100]
    #   El rango del objetivo de salida es [0,100]
    # Sub1 = Subsistema de G. estratégica y G. de la calidad
    # Sub2 = Subsistema de G. jurídica y G. administrativa
    # Sub3 = Subsistema de servicios TIC, G. de la experiencia y G. de mercadeo y ventas

    # New Antecedent/Consequent objects hold universe variables and membership
    # functions
    Sub1 = ctrl.Antecedent(np.arange(0, 110, 1), 'Sub1')
    Sub2 = ctrl.Antecedent(np.arange(0, 110, 1), 'Sub2')
    Sub3 = ctrl.Antecedent(np.arange(0, 110, 1), 'Sub3')
    Obj4 = ctrl.Consequent(np.arange(0, 110, 1), 'Objetivo 4')

    # Generate fuzzy membership functions
    Sub1['Dmayor'] = fuzz.trapmf(Sub1.universe, [-1, 0, 20, 40])
    Sub1['Dmenor'] = fuzz.trimf(Sub1.universe, [20, 40, 60])
    Sub1['Fmenor'] = fuzz.trimf(Sub1.universe, [40, 60, 80])
    Sub1['Fmayor'] = fuzz.trapmf(Sub1.universe, [60, 80, 110, 120])

    Sub2['Dmayor'] = fuzz.trapmf(Sub2.universe, [-1, 0, 20, 40])
    Sub2['Dmenor'] = fuzz.trimf(Sub2.universe, [20, 40, 60])
    Sub2['Fmenor'] = fuzz.trimf(Sub2.universe, [40, 60, 80])
    Sub2['Fmayor'] = fuzz.trapmf(Sub2.universe, [60, 80, 110, 120])

    Sub3['Dmayor'] = fuzz.trapmf(Sub3.universe, [-1, 0, 20, 40])
    Sub3['Dmenor'] = fuzz.trimf(Sub3.universe, [20, 40, 60])
    Sub3['Fmenor'] = fuzz.trimf(Sub3.universe, [40, 60, 80])
    Sub3['Fmayor'] = fuzz.trapmf(Sub3.universe, [60, 80, 110, 120])

    Obj4['Dmayor'] = fuzz.trapmf(Obj4.universe, [-1, 0, 20, 40])
    Obj4['Dmenor'] = fuzz.trimf(Obj4.universe, [20, 40, 60])
    Obj4['Fmenor'] = fuzz.trimf(Obj4.universe, [40, 60, 80])
    Obj4['Fmayor'] = fuzz.trapmf(Obj4.universe, [60, 80, 110, 120])

    #generate rules membreship
    rule1 = ctrl.Rule(Sub1['Dmayor'] & Sub2['Dmayor'] & Sub3["Dmayor"], Obj4['Dmayor'])
    rule2 = ctrl.Rule(Sub1['Dmayor'] & Sub2['Dmenor'] & Sub3["Dmayor"], Obj4['Dmayor'])
    rule3 = ctrl.Rule(Sub1['Dmayor'] & Sub2['Fmenor'] & Sub3["Dmayor"], Obj4['Dmayor'])
    rule4 = ctrl.Rule(Sub1['Dmayor'] & Sub2['Fmayor'] & Sub3["Dmayor"], Obj4['Dmayor'])
    rule5 = ctrl.Rule(Sub1['Dmayor'] & Sub2['Dmayor'] & Sub3["Dmenor"], Obj4['Dmayor'])
    rule6 = ctrl.Rule(Sub1['Dmayor'] & Sub2['Dmenor'] & Sub3["Dmenor"], Obj4['Dmayor'])
    rule7 = ctrl.Rule(Sub1['Dmayor'] & Sub2['Fmenor'] & Sub3["Dmenor"], Obj4['Dmenor'])
    rule8 = ctrl.Rule(Sub1['Dmayor'] & Sub2['Fmayor'] & Sub3["Dmenor"], Obj4['Dmenor'])
    rule9 = ctrl.Rule(Sub1['Dmayor'] & Sub2['Dmayor'] & Sub3["Fmenor"], Obj4['Dmayor'])
    rule10 = ctrl.Rule(Sub1['Dmayor'] & Sub2['Dmenor'] & Sub3["Fmenor"], Obj4['Dmenor'])
    rule11 = ctrl.Rule(Sub1['Dmayor'] & Sub2['Fmenor'] & Sub3["Fmenor"], Obj4['Dmenor'])
    rule12 = ctrl.Rule(Sub1['Dmayor'] & Sub2['Fmayor'] & Sub3["Fmenor"], Obj4['Dmenor'])
    rule13 = ctrl.Rule(Sub1['Dmayor'] & Sub2['Dmayor'] & Sub3["Fmayor"], Obj4['Dmenor'])
    rule14 = ctrl.Rule(Sub1['Dmayor'] & Sub2['Dmenor'] & Sub3["Fmayor"], Obj4['Dmenor'])
    rule15 = ctrl.Rule(Sub1['Dmayor'] & Sub2['Fmenor'] & Sub3["Fmayor"], Obj4['Fmenor'])
    rule16 = ctrl.Rule(Sub1['Dmayor'] & Sub2['Fmayor'] & Sub3["Fmayor"], Obj4['Fmenor'])

    rule17 = ctrl.Rule(Sub1['Dmenor'] & Sub2['Dmayor'] & Sub3["Dmayor"], Obj4['Dmayor'])
    rule18 = ctrl.Rule(Sub1['Dmenor'] & Sub2['Dmenor'] & Sub3["Dmayor"], Obj4['Dmenor'])
    rule19 = ctrl.Rule(Sub1['Dmenor'] & Sub2['Fmenor'] & Sub3["Dmayor"], Obj4['Dmenor'])
    rule20 = ctrl.Rule(Sub1['Dmenor'] & Sub2['Fmayor'] & Sub3["Dmayor"], Obj4['Dmenor'])
    rule21 = ctrl.Rule(Sub1['Dmenor'] & Sub2['Dmayor'] & Sub3["Dmenor"], Obj4['Dmenor'])
    rule22 = ctrl.Rule(Sub1['Dmenor'] & Sub2['Dmenor'] & Sub3["Dmenor"], Obj4['Dmenor'])
    rule23 = ctrl.Rule(Sub1['Dmenor'] & Sub2['Fmenor'] & Sub3["Dmenor"], Obj4['Dmenor'])
    rule24 = ctrl.Rule(Sub1['Dmenor'] & Sub2['Fmayor'] & Sub3["Dmenor"], Obj4['Dmenor'])
    rule25 = ctrl.Rule(Sub1['Dmenor'] & Sub2['Dmayor'] & Sub3["Fmenor"], Obj4['Dmenor'])
    rule26 = ctrl.Rule(Sub1['Dmenor'] & Sub2['Dmenor'] & Sub3["Fmenor"], Obj4['Dmenor'])
    rule27 = ctrl.Rule(Sub1['Dmenor'] & Sub2['Fmenor'] & Sub3["Fmenor"], Obj4['Fmenor'])
    rule28 = ctrl.Rule(Sub1['Dmenor'] & Sub2['Fmayor'] & Sub3["Fmenor"], Obj4['Fmenor'])
    rule29 = ctrl.Rule(Sub1['Dmenor'] & Sub2['Dmayor'] & Sub3["Fmayor"], Obj4['Dmenor'])
    rule30 = ctrl.Rule(Sub1['Dmenor'] & Sub2['Dmenor'] & Sub3["Fmayor"], Obj4['Dmenor'])
    rule31 = ctrl.Rule(Sub1['Dmenor'] & Sub2['Fmenor'] & Sub3["Fmayor"], Obj4['Fmenor'])
    rule32 = ctrl.Rule(Sub1['Dmenor'] & Sub2['Fmayor'] & Sub3["Fmayor"], Obj4['Fmenor'])

    rule33 = ctrl.Rule(Sub1['Fmenor'] & Sub2['Dmayor'] & Sub3["Dmayor"], Obj4['Dmenor'])
    rule34 = ctrl.Rule(Sub1['Fmenor'] & Sub2['Dmenor'] & Sub3["Dmayor"], Obj4['Dmenor'])
    rule35 = ctrl.Rule(Sub1['Fmenor'] & Sub2['Fmenor'] & Sub3["Dmayor"], Obj4['Dmenor'])
    rule36 = ctrl.Rule(Sub1['Fmenor'] & Sub2['Fmayor'] & Sub3["Dmayor"], Obj4['Fmenor'])
    rule37 = ctrl.Rule(Sub1['Fmenor'] & Sub2['Dmayor'] & Sub3["Dmenor"], Obj4['Dmenor'])
    rule38 = ctrl.Rule(Sub1['Fmenor'] & Sub2['Dmenor'] & Sub3["Dmenor"], Obj4['Dmenor'])
    rule39 = ctrl.Rule(Sub1['Fmenor'] & Sub2['Fmenor'] & Sub3["Dmenor"], Obj4['Fmenor'])
    rule40 = ctrl.Rule(Sub1['Fmenor'] & Sub2['Fmayor'] & Sub3["Dmenor"], Obj4['Fmenor'])
    rule41 = ctrl.Rule(Sub1['Fmenor'] & Sub2['Dmayor'] & Sub3["Fmenor"], Obj4['Dmenor'])
    rule42 = ctrl.Rule(Sub1['Fmenor'] & Sub2['Dmenor'] & Sub3["Fmenor"], Obj4['Fmenor'])
    rule43 = ctrl.Rule(Sub1['Fmenor'] & Sub2['Fmenor'] & Sub3["Fmenor"], Obj4['Fmenor'])
    rule44 = ctrl.Rule(Sub1['Fmenor'] & Sub2['Fmayor'] & Sub3["Fmenor"], Obj4['Fmenor'])
    rule45 = ctrl.Rule(Sub1['Fmenor'] & Sub2['Dmayor'] & Sub3["Fmayor"], Obj4['Dmenor'])
    rule46 = ctrl.Rule(Sub1['Fmenor'] & Sub2['Dmenor'] & Sub3["Fmayor"], Obj4['Fmenor'])
    rule47 = ctrl.Rule(Sub1['Fmenor'] & Sub2['Fmenor'] & Sub3["Fmayor"], Obj4['Fmenor'])
    rule48 = ctrl.Rule(Sub1['Fmenor'] & Sub2['Fmayor'] & Sub3["Fmayor"], Obj4['Fmayor'])

    rule49 = ctrl.Rule(Sub1['Fmayor'] & Sub2['Dmayor'] & Sub3["Dmayor"], Obj4['Dmenor'])
    rule50 = ctrl.Rule(Sub1['Fmayor'] & Sub2['Dmenor'] & Sub3["Dmayor"], Obj4['Dmenor'])
    rule51 = ctrl.Rule(Sub1['Fmayor'] & Sub2['Fmenor'] & Sub3["Dmayor"], Obj4['Fmenor'])
    rule52 = ctrl.Rule(Sub1['Fmayor'] & Sub2['Fmayor'] & Sub3["Dmayor"], Obj4['Fmenor'])
    rule53 = ctrl.Rule(Sub1['Fmayor'] & Sub2['Dmayor'] & Sub3["Dmenor"], Obj4['Dmenor'])
    rule54 = ctrl.Rule(Sub1['Fmayor'] & Sub2['Dmenor'] & Sub3["Dmenor"], Obj4['Dmenor'])
    rule55 = ctrl.Rule(Sub1['Fmayor'] & Sub2['Fmenor'] & Sub3["Dmenor"], Obj4['Fmenor'])
    rule56 = ctrl.Rule(Sub1['Fmayor'] & Sub2['Fmayor'] & Sub3["Dmenor"], Obj4['Fmenor'])
    rule57 = ctrl.Rule(Sub1['Fmayor'] & Sub2['Dmayor'] & Sub3["Fmenor"], Obj4['Dmenor'])
    rule58 = ctrl.Rule(Sub1['Fmayor'] & Sub2['Dmenor'] & Sub3["Fmenor"], Obj4['Fmenor'])
    rule59 = ctrl.Rule(Sub1['Fmayor'] & Sub2['Fmenor'] & Sub3["Fmenor"], Obj4['Fmayor'])
    rule60 = ctrl.Rule(Sub1['Fmayor'] & Sub2['Fmayor'] & Sub3["Fmenor"], Obj4['Fmayor'])
    rule61 = ctrl.Rule(Sub1['Fmayor'] & Sub2['Dmayor'] & Sub3["Fmayor"], Obj4['Fmenor'])
    rule62 = ctrl.Rule(Sub1['Fmayor'] & Sub2['Dmenor'] & Sub3["Fmayor"], Obj4['Fmenor'])
    rule63 = ctrl.Rule(Sub1['Fmayor'] & Sub2['Fmenor'] & Sub3["Fmayor"], Obj4['Fmayor'])
    rule64 = ctrl.Rule(Sub1['Fmayor'] & Sub2['Fmayor'] & Sub3["Fmayor"], Obj4['Fmayor'])

    #create system control and simulation
    solving_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32, rule33, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50, rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60, rule61, rule62, rule63, rule64])
    solving = ctrl.ControlSystemSimulation(solving_ctrl)

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    solving.input['Sub1'] = value_sub1
    solving.input['Sub2'] = value_sub1
    solving.input['Sub3'] = value_sub1
    # Crunch the numbers
    solving.compute()

    Obj4_result = solving.output['Objetivo 4']

    #update data
    n = 1

    with open('static/data/datamain.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[n] = ['Objetivo', row['Valor']]
            n=n+1
     
    #update table obj
    data[4][1] = Obj4_result
    
    with open('static/data/datamain.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data)

    csvFile.close()

    return Obj4_result

def calculate_obj5(value_ini_51):
    #OBJETIVO 5: Garantizar la información oportuna y confiable
    # Generate universe variables
    #   El rango de las iniciativas estrategicas es [0,110]
    #   El rango del objetivo de salida es [0,110]
    # Inic1 = Desarrolar una cultura de comunicación e información que facilite el alcance de los objetivos estratégicos de la Empresa. 

    # New Antecedent/Consequent objects hold universe variables and membership
    # functions
    Inic1 = ctrl.Antecedent(np.arange(0, 110, 1), 'Inic1')

    Obj5 = ctrl.Consequent(np.arange(0, 110, 1), 'Objetivo 5')

    # Generate fuzzy membership functions
    Inic1['Dmayor'] = fuzz.trapmf(Inic1.universe, [-1, 0, 20, 27])
    Inic1['Dmenor'] = fuzz.trimf(Inic1.universe, [12, 40, 44])
    Inic1['Fmenor'] = fuzz.trimf(Inic1.universe, [26, 60, 66])
    Inic1['Fmayor'] = fuzz.trapmf(Inic1.universe, [53, 80, 110, 120])

    Obj5['Dmayor'] = fuzz.trapmf(Obj5.universe, [-1, 0, 20, 40])
    Obj5['Dmenor'] = fuzz.trimf(Obj5.universe, [20, 40, 60])
    Obj5['Fmenor'] = fuzz.trimf(Obj5.universe, [40, 60, 80])
    Obj5['Fmayor'] = fuzz.trapmf(Obj5.universe, [60, 80, 110, 120])

    #generate rules membreship
    rule1 = ctrl.Rule(Inic1['Dmenor'], Obj5['Dmenor'])
    rule2 = ctrl.Rule(Inic1['Dmayor'], Obj5['Dmayor'])
    rule3 = ctrl.Rule(Inic1['Fmenor'], Obj5['Fmenor'])
    rule4 = ctrl.Rule(Inic1['Fmayor'], Obj5['Fmayor'])

    #create system control and simulation
    solving_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
    solving = ctrl.ControlSystemSimulation(solving_ctrl)

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    solving.input['Inic1'] = value_ini_51
    # Crunch the numbers
    solving.compute()

    Obj5_result = solving.output['Objetivo 5']

    #update data
    n = 1
    m = 1

    with open('static/data/datamain.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[n] = ['Objetivo', row['Valor']]
            n=n+1
     
    #update table 
    data[5][1] = Obj5_result
    
    with open('static/data/datamain.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data)

    with open('static/data/data-inic.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_inic[m] = [data_inic[m][0], row['Valor']]
            m=m+1

    data_inic[16][1] = value_ini_51

    with open('static/data/data-inic.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data_inic)

    csvFile.close()

def calculate_obj6(value_ini_61, value_ini_62):
    #OBJETIVO 6:Desarrollar integralmente al talento humano de la empresa
    # Generate universe variables
    #   El rango de las iniciativas estrategicas es [0,110]
    #   El rango del objetivo de salida es [0,110]
    # Inic1 = Mejorar las capacidades, conocimientos y entrenamiento de los colaboradores
    # Inic2 = Mejorar la Cultura y Clima Organizacional


    # New Antecedent/Consequent objects hold universe variables and membership
    # functions
    Inic1 = ctrl.Antecedent(np.arange(0, 110, 1), 'Inic1')
    Inic2 = ctrl.Antecedent(np.arange(0, 110, 1), 'Inic2')
    Obj6 = ctrl.Consequent(np.arange(0, 110, 1), 'Objetivo 6')

    # Generate fuzzy membership functions
    Inic1['Dmayor'] = fuzz.trapmf(Inic1.universe, [-1, 0, 20, 28])
    Inic1['Dmenor'] = fuzz.trimf(Inic1.universe, [18, 40, 52])
    Inic1['Fmenor'] = fuzz.trimf(Inic1.universe, [45, 60, 78])
    Inic1['Fmayor'] = fuzz.trapmf(Inic1.universe, [76, 80, 110, 120])

    Inic2['Dmayor'] = fuzz.trapmf(Inic2.universe, [-1, 0, 20, 29])
    Inic2['Dmenor'] = fuzz.trimf(Inic2.universe, [21, 40, 51])
    Inic2['Fmenor'] = fuzz.trimf(Inic2.universe, [50, 60, 77])
    Inic2['Fmayor'] = fuzz.trapmf(Inic2.universe, [76, 80, 110, 120])


    Obj6['Dmayor'] = fuzz.trapmf(Obj6.universe, [-1, 0, 20, 40])
    Obj6['Dmenor'] = fuzz.trimf(Obj6.universe, [20, 40, 60])
    Obj6['Fmenor'] = fuzz.trimf(Obj6.universe, [40, 60, 80])
    Obj6['Fmayor'] = fuzz.trapmf(Obj6.universe, [60, 80, 110, 120])
        
    #generate rules membreship
    rule1 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Dmayor'], Obj6['Dmayor'])
    rule2 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Dmayor'], Obj6['Dmenor'])
    rule3 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Dmayor'], Obj6['Dmenor'])
    rule4 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Dmayor'], Obj6['Fmenor'])
    rule5 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Dmenor'], Obj6['Dmayor'])
    rule6 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Dmenor'], Obj6['Dmenor'])
    rule7 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Dmenor'], Obj6['Fmenor'])
    rule8 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Dmenor'], Obj6['Fmenor'])
    rule9 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Fmenor'], Obj6['Dmenor'])
    rule10 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Fmenor'], Obj6['Dmenor'])
    rule11 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Fmenor'], Obj6['Fmenor'])
    rule12 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Fmenor'], Obj6['Fmayor'])
    rule13 = ctrl.Rule(Inic1['Dmayor'] & Inic2['Fmayor'], Obj6['Dmenor'])
    rule14 = ctrl.Rule(Inic1['Dmenor'] & Inic2['Fmayor'], Obj6['Dmenor'])
    rule15 = ctrl.Rule(Inic1['Fmenor'] & Inic2['Fmayor'], Obj6['Fmayor'])
    rule16 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Fmayor'], Obj6['Fmayor'])

    #create system control and simulation
    solving_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16])
    solving = ctrl.ControlSystemSimulation(solving_ctrl)

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    solving.input['Inic1'] = value_ini_61
    solving.input['Inic2'] = value_ini_62
    # Crunch the numbers
    solving.compute()

    Obj6_result = solving.output['Objetivo 6']

    #update data
    n = 1
    m = 1

    with open('static/data/datamain.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[n] = ['Objetivo', row['Valor']]
            n=n+1
     
    #update table 
    data[6][1] = Obj6_result
    
    with open('static/data/datamain.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data)

    with open('static/data/data-inic.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_inic[m] = [data_inic[m][0], row['Valor']]
            m=m+1

    data_inic[17][1] = value_ini_61
    data_inic[18][1] = value_ini_62

    with open('static/data/data-inic.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data_inic)

    csvFile.close()

def calculate_obj7(value_ini_71):
    #OBJETIVO 7: Garantizar una infraestructura tecnologica adecuada y suficiente en la empresa.
    # Generate universe variables
    #   El rango de las iniciativas estrategicas es [0,110]
    #   El rango del objetivo de salida es [0,110]
    # Inic1 = Integrar efectivamente la infraestructura tecnologica en la empresa

    # New Antecedent/Consequent objects hold universe variables and membership
    # functions
    Inic1 = ctrl.Antecedent(np.arange(0, 110, 1), 'Inic1')
    Obj7 = ctrl.Consequent(np.arange(0, 110, 1), 'Objetivo 7')

    # Generate fuzzy membership functions
    Inic1['Dmayor'] = fuzz.trapmf(Inic1.universe, [-1, 0, 20, 33])
    Inic1['Dmenor'] = fuzz.trimf(Inic1.universe, [28, 40, 55])
    Inic1['Fmenor'] = fuzz.trimf(Inic1.universe, [40, 60, 74])
    Inic1['Fmayor'] = fuzz.trapmf(Inic1.universe, [72, 80, 110, 120])

    Obj7['Dmayor'] = fuzz.trapmf(Obj7.universe, [-1, 0, 20, 40])
    Obj7['Dmenor'] = fuzz.trimf(Obj7.universe, [20, 40, 60])
    Obj7['Fmenor'] = fuzz.trimf(Obj7.universe, [40, 60, 80])
    Obj7['Fmayor'] = fuzz.trapmf(Obj7.universe, [60, 80, 110, 120])

    #generate rules membreship
    rule1 = ctrl.Rule(Inic1['Dmenor'], Obj7['Dmenor'])
    rule2 = ctrl.Rule(Inic1['Dmayor'], Obj7['Dmayor'])
    rule3 = ctrl.Rule(Inic1['Fmenor'], Obj7['Fmenor'])
    rule4 = ctrl.Rule(Inic1['Fmayor'], Obj7['Fmayor'])

    #create system control and simulation
    solving_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
    solving = ctrl.ControlSystemSimulation(solving_ctrl)

   # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    solving.input['Inic1'] = value_ini_71
    # Crunch the numbers
    solving.compute()

    Obj7_result = solving.output['Objetivo 7']

     #update data
    n = 1
    m = 1

    with open('static/data/datamain.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[n] = ['Objetivo', row['Valor']]
            n=n+1
     
    #update table 
    data[7][1] = Obj7_result
    
    with open('static/data/datamain.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data)

    with open('static/data/data-inic.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_inic[m] = [data_inic[m][0], row['Valor']]
            m=m+1

    data_inic[19][1] = value_ini_71

    with open('static/data/data-inic.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data_inic)

    csvFile.close()

from flask import Flask, render_template, request
import os
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import csv
import fuzzy
import json
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import Image, Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from flask import make_response
from io import StringIO
from io import BytesIO
from reportlab.lib.utils import ImageReader
import io
from datetime import datetime



app = Flask(__name__)

def read_data_bsc_acc():
    numero_filas = 32
    numero_columnas = 18
    # Versión mas compacta
    matriz = [range(numero_columnas) for i in range(numero_filas)]

    # Variación de la anterior
    matriz = [[None] * numero_columnas for i in range(numero_filas)]

    n=1
    with open('static/data/data-bsc-acc.csv', mode="r", encoding="utf-8", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        matriz[0] = ["Id", "Objetivo estratégico", "Iniciativa", "Accion", "Meta", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre", "Cumplimiento"]
        for row in reader:
            matriz[n] = [row['Id'], row['Objetivo estratégico'], row['Iniciativa'], row['Accion'], row['Meta'], row['Enero'], row['Febrero'], row['Marzo'], row['Abril'], row['Mayo'], row['Junio'], row['Julio'], row['Agosto'], row['Septiembre'], row['Octubre'], row['Noviembre'], row['Diciembre'], row['Diciembre'] ]
            n=n+1

    return matriz

def readdata():
    n = 1
    data = [['Objetivo', 'Valor'], 
        ['Objetivo 1', 0], 
        ['Objetivo 2', 0],
        ['Objetivo 3', 0],
        ['Objetivo 4', 0],
        ['Objetivo 5', 0],
        ['Objetivo 6', 0],
        ['Objetivo 7', 0]]
    with open('static/data/datamain.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[n] = ['Objetivo', row['Valor']]
            n=n+1
    return data

def readdatabsc():
    n = 1
    data = [['Objetivo', 'Valor'], 
        ['Objetivo 1', 0], 
        ['Objetivo 2', 0],
        ['Objetivo 3', 0],
        ['Objetivo 4', 0],
        ['Objetivo 5', 0],
        ['Objetivo 6', 0],
        ['Objetivo 7', 0]]
    with open('static/data/data-bsc.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[n] = ['Objetivo', row['Valor']]
            n=n+1
    return data

def read_data_inic():
    n=1
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

    with open('static/data/data-inic.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_inic[n] = [data_inic[n][0], row['Valor']]
            n=n+1
    return data_inic

@app.route('/datajson', methods=["GET", "POST"])
def get_data():
    datos = readdata() 
    return json.dumps(datos)

@app.route('/databscacc', methods=["GET", "POST"])
def get_data_bsc_acc():
    datos = read_data_bsc_acc()
    
    return json.dumps(datos)

@app.route('/data-bsc-json', methods=["GET", "POST"])
def get_data_bsc():
    datos = readdatabsc()
    return json.dumps(datos)

@app.route('/data-inic-json', methods=["GET", "POST"])
def get_data_inic():
    datos_inic = read_data_inic()
    return json.dumps(datos_inic)

@app.route("/")
@app.route("/home")
def index():
    titulo = "Home"
    return render_template("index.html", titulo=titulo)

@app.route("/infobsc", methods=["GET", "POST"])
def infobsc():
    if request.method == "POST":
        value_enero = request.form["enero"]
        #print(value_enero)
        value_febrero = request.form["febrero"]
        value_marzo = request.form["marzo"]
        value_abril = request.form["abril"]
        value_mayo = request.form["mayo"]
        value_junio = request.form["junio"]
        value_julio = request.form["julio"]
        value_agosto = request.form["agosto"]
        value_septiembre = request.form["septiembre"]
        value_octubre = request.form["octubre"]
        value_noviembre = request.form["noviembre"]
        value_diciembre = request.form["diciembre"]
        
        value_posicion = request.form["posicion"]
        posicion_int = int(value_posicion)
        # print(value_posicion)

        matriz = read_data_bsc_acc()
        posicion_int = posicion_int
        matriz[posicion_int] = [matriz[posicion_int][0], matriz[posicion_int][1], matriz[posicion_int][2], matriz[posicion_int][3], matriz[posicion_int][4], value_enero, value_febrero, value_marzo, value_abril, value_mayo, value_junio, value_julio, value_agosto, value_septiembre, value_octubre, value_noviembre, value_diciembre, value_diciembre]
        

        with open('static/data/data-bsc-acc.csv', 'w', encoding="utf-8") as csvFile:
            writer = csv.writer(csvFile)  
            writer.writerows(matriz)
         
        csvFile.close()
       

        return render_template("bsc_crud.html")
    return render_template("bsc_crud.html")

@app.route('/pdf')
def pdf():
    
    buffer = io.BytesIO()

    c = canvas.Canvas(buffer, pagesize=A4)
    logo = ImageReader('C:/Users/Alvar/fuzzyflask-v3/static/img/Logo2.jpg')
    
    c.drawImage(logo, 460, 745, width=89, height=70)
    #ImageLogo = "LogoEmtel.png"
    #logo2 = Image(ImageLogo, 2*cm, 2*cm)
    #c.drawImage(logo2, 90, 750, mask='auto')
    
    # Header
    c.setLineWidth(.3)
    c.setFont('Helvetica', 20)
    c.drawString(50, 775, 'EMTEL')
    c.setFont('Helvetica', 12)
    c.drawString(50, 762, 'Report')

    now = datetime.now()
    year = now.year
    year = str(year)
    month = now.month
    month = str(month)
    day = now.day
    day = str(day)

    fecha = day + "/" + month + "/" + year

    c.setFont('Helvetica', 12)
    c.drawString(275, 765, fecha)
    c.line(255, 763, 345, 763)

    c.setFont('Helvetica-Bold',12)
    c.drawString(50, 700, 'Cumplimiento Plan Estratégico:')

    

    #strategic processes table
    processes = [{'#':'1', 'name':'(PA) Gestión Administrativa', '# acciones':'21', 'cumplimiento':'80%'},
                  {'#':'2', 'name':'(PM) Servicios TIC, Sistemas', '# acciones':'4', 'cumplimiento':'96%'},
                  {'#':'3', 'name':'(PA) Gestión Jurídica', '# acciones':'4', 'cumplimiento':'95%'},
                  {'#':'4', 'name':'(PA) Gestión Financiera', '# acciones':'3', 'cumplimiento':'83%'},
                  {'#':'5', 'name':'(PE) Gestión Extratégica', '# acciones':'8', 'cumplimiento':'99%'},
                  {'#':'6', 'name':'(PA) Gestión de la Calidad', '# acciones':'2', 'cumplimiento':'85%'},
                  {'#':'7', 'name':'(PA) Gestión de la comunicación', '# acciones':'2', 'cumplimiento':'90%'},
                  {'#':'8', 'name':'(PM) Gestión Mercadeo y Ventas', '# acciones':'9', 'cumplimiento':'90%'},
                  {'#':'9', 'name':'(PM) Gestión de la Experiencia', '# acciones':'7', 'cumplimiento':'70%'},
                  {'#':'10', 'name':'(PM) Gestión Servicios TIC', '# acciones':'9', 'cumplimiento':'80%'},
                  {'#':'11', 'name':'(PM) Integración Tecnológica', '# acciones':'1', 'cumplimiento':'87%'}] 
    
    #Table Header
    styles = getSampleStyleSheet()
    styleBH =  styles["Normal"]
    styleBH.alignment = TA_CENTER
    styleBH.fontSize = 10

    numero = Paragraph('''No.''',styleBH)
    proceso = Paragraph('''Procesos''',styleBH)
    num_acciones = Paragraph('''Acciones Estratégicas''',styleBH)
    cumplimiento = Paragraph('''Cumplimiento % Acciones''',styleBH)

    data = []
    data.append([numero, proceso, num_acciones, cumplimiento])

    #Table
    styleN = styles["BodyText"]
    styleN.alignment = TA_CENTER
    styleN.fontSize = 6

    high = 650
    for process in processes:
        this_process = [process['#'], process['name'], process['# acciones'], process['cumplimiento']]
        data.append(this_process)
        high = high-18

    #Table size
    width, height = A4
    table = Table(data, colWidths=[1.9*cm, 9.5*cm, 3*cm, 3*cm, 1.9*cm, 1.9*cm])
    table.setStyle(TableStyle([ #estilos de la tabla 
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black), ]))
    #pdf size
    table.wrapOn(c, width, height)
    table.drawOn(c, 50, high)
    c.showPage


    c.setFont('Helvetica-Bold',12)
    c.drawString(50, 400, 'Cumplimiento Gestión Administrativa:')

    #Gestion administrativa
    objectives = [{'#':'1', 'name':'Realizar un diagnostico ambiental anual de requisitos legales', 'meta':'100%', 'cumplimiento':'90%'},
                  {'#':'2', 'name':'Elaborar planes de trabajo de actividades generales', 'meta':'100%', 'cumplimiento':'85%'},
                  {'#':'3', 'name':'Seguir y monitorear las medidas de manejo ambiental', 'meta':'100%', 'cumplimiento':'80%'},
                  {'#':'4', 'name':'Evaluar los resultados de manejo ambiental', 'meta':'100%', 'cumplimiento':'87%'},
                  {'#':'5', 'name':'Actualizar la politica y objetivos ambientales', 'meta':'100%', 'cumplimiento':'90%'},
                  {'#':'6', 'name':'Identificar e implementar las medidas de manejo ambiental', 'meta':'100%', 'cumplimiento':'90%'},
                  {'#':'7', 'name':'Documentar el proceso gestión documental', 'meta':'100%', 'cumplimiento':'90%'},
                  {'#':'8', 'name':'Organizar y transferir archivo de gestión', 'meta':'100%', 'cumplimiento':'70%'},
                  {'#':'9', 'name':'Manejar la herramienta Orfeo', 'meta':'100%', 'cumplimiento':'90%'},
                  {'#':'10', 'name':'Implementar  tablas de retención ', 'meta':'100%', 'cumplimiento':'70%'},
                  {'#':'11', 'name':'Realizar inventario de la documentación determinada', 'meta':'100%', 'cumplimiento':'90%'},
                  {'#':'12', 'name':'Rendir informes', 'meta':'100%', 'cumplimiento':'100%'}]

    #Table Header
    styles = getSampleStyleSheet()
    styleBH =  styles["Normal"]
    styleBH.alignment = TA_CENTER
    styleBH.fontSize = 10

    

    numero = Paragraph('''No.''',styleBH)
    accion = Paragraph(''' Accion Estratégica''',styleBH)
    meta = Paragraph('''Meta %''',styleBH)
    cumplimiento = Paragraph('''Cumplimiento %''',styleBH)

    data_ges_admin = []
    data_ges_admin.append([numero, accion, meta, cumplimiento])

    #Table
    styleN = styles["BodyText"]
    styleN.alignment = TA_CENTER
    styleN.fontSize = 6

    

    high_ges_admin_table = 350
    for objetive in objectives:
        this_objetive = [objetive['#'], objetive['name'], objetive['meta'], objetive['cumplimiento']]
        data_ges_admin.append(this_objetive)
        high_ges_admin_table = high_ges_admin_table - 18

    #Table ges_admin size
    width, height = A4
    table_ges_admin = Table(data_ges_admin, colWidths=[1.9*cm, 10*cm, 2.7*cm, 2.7*cm, 1.9*cm, 1.9*cm])
    table_ges_admin.setStyle(TableStyle([ #estilos de la tabla 
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black), ]))
    #pdfsize
    table_ges_admin.wrapOn(c, width, height)
    table_ges_admin.drawOn(c, 50, high_ges_admin_table)
    c.showPage
    
    c.save()
    pdf = buffer.getvalue()

    response = make_response(pdf)
    response.headers['Content-Disposition'] = "attachment; filename= emtel-report.pdf"
    response.mimetype = 'application/pdf'

    buffer.close()

    return response


@app.route("/obj_form", methods=["GET", "POST"])
@app.route("/obj_form/<string:url_obj>", methods=["GET", "POST"])
def obj_form(url_obj="nav-obj1"):
    if url_obj == "nav-obj1" and request.method == "POST":
        
        #save values iniciativa 1 iniciativa 2        
        inic1 = request.form["iniciativa_1_1"]
        inic2 = request.form["iniciativa_1_2"]
        inic1 = int(inic1)
        inic2 = int(inic2)
        #calculate fuzzy objetivo 1
        fuzzy.calculate_obj1(inic1, inic2)
        
        return render_template("obj_form.html", url_obj=url_obj)

    elif url_obj == "nav-obj2" and request.method == "POST":
        
        #save values iniciativa 1 iniciativa 2 iniciativa 3       
        inic1 = request.form["iniciativa_2_1"]
        inic2 = request.form["iniciativa_2_2"]
        inic3 = request.form["iniciativa_2_3"]
        inic1 = int(inic1)
        inic2 = int(inic2)
        inic3 = int(inic3)
        #calculate fuzzy objetivo 2
        fuzzy.calculate_obj2(inic1, inic2, inic3)
        print(inic3)
        
        return render_template("obj_form.html", url_obj=url_obj)

    elif url_obj == "nav-obj3" and request.method == "POST":
        inic1 = request.form["iniciativa_3_1"]
        inic1 = int(inic1)
        #calculate fuzzy objetivo 3
        fuzzy.calculate_obj3(inic1)
        print(inic1)
        
        return render_template("obj_form.html", url_obj=url_obj)

    elif url_obj == "nav-obj4" and request.method == "POST":
        inic1 = request.form["iniciativa_4_1"]
        inic1 = int(inic1)
        inic2 = request.form["iniciativa_4_2"]
        inic2 = int(inic2)
        inic3 = request.form["iniciativa_4_3"]
        inic3 = int(inic3)
        inic4 = request.form["iniciativa_4_4"]
        inic4 = int(inic4)
        inic5 = request.form["iniciativa_4_5"]
        inic5 = int(inic5)
        inic6 = request.form["iniciativa_4_6"]
        inic6 = int(inic6)
        inic7 = request.form["iniciativa_4_7"]
        inic7 = int(inic7)
        inic8 = request.form["iniciativa_4_8"]
        inic8 = int(inic8)
        inic9 = request.form["iniciativa_4_9"]
        inic9 = int(inic9)
        #calculate fuzzy objetivo 3
        #fuzzy.calculate_obj4(inic1, inic2, inic3, inic4, inic5, inic6, inic7, inic8, inic9)
        value_sub1 = fuzzy.calculate_sub1(inic1, inic2, inic3)
        value_sub2 = fuzzy.calculate_sub2(inic4, inic5, inic6, inic7)
        value_sub3 = fuzzy.calculate_sub3(inic8, inic9)
        print(value_sub1, value_sub2, value_sub3)
        fuzzy.calculate_obj4(value_sub1, value_sub2, value_sub3)
        
        return render_template("obj_form.html", url_obj=url_obj)

    elif url_obj == "nav-obj5" and request.method == "POST":
        inic1 = request.form["iniciativa_5_1"]
        inic1 = int(inic1)
        fuzzy.calculate_obj5(inic1)
        print(inic1)

        return render_template("obj_form.html", url_obj=url_obj)

    elif url_obj == "nav-obj6" and request.method == "POST":
        inic1 = request.form["iniciativa_6_1"]
        inic1 = int(inic1)
        inic2 = request.form["iniciativa_6_2"]
        inic2 = int(inic2)
        fuzzy.calculate_obj6(inic1, inic2)
        print(inic2)

        return render_template("obj_form.html", url_obj=url_obj)

    elif url_obj =="nav-obj7" and request.method == "POST":
        inic1 = request.form["iniciativa_7_1"]
        inic1 = int(inic1)
        fuzzy.calculate_obj7(inic1)
        print(inic1)

        return render_template("obj_form.html", url_obj= url_obj)


    return render_template("obj_form.html", url_obj=url_obj)



if __name__ == "__main__":
    app.run(debug=True)
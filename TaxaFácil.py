import shapefile
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import subprocess
import os
import datetime
from tkinter.ttk import Label
from xml.dom.minidom import Element
import win32file

#VERSÃO 04/03/2022

#--------TAREFAS---------
#CRIAR LOG EM TXT: 
#INSERIR TEXTO NO ARQUIVO:FEITO
#INSERIR ESTRUTURA DE PASTAS PARA CADA MÁQUINA: FEITO!!!
#CONVERTER "," PARA "." E REMOVER ESPAÇOS DA TAXA E DO NOME: FEITO
#DEFINIR VALOR PADRÃO PARA 0: FEITO

drive_list = []
def locate_usb():
    drivebits=win32file.GetLogicalDrives()
    for d in range(1,26):
        mask=1 << d
        if drivebits & mask:
            # here if the drive is at least there
            drname='%c:\\' % chr(ord('A')+d)
            t=win32file.GetDriveType(drname)
            if t == win32file.DRIVE_REMOVABLE:
                drive_list.append(drname)
    return drive_list

def app():
    current_time = datetime.datetime.now() 
    areas_dict = {'Area 2 e Zé':{1  :  0 ,2  :  0 ,3  :  0 ,4  :  0 ,5  :  0 ,6  :  0 ,7  :  0 ,8  :  0 }, 'Area 3':{9:0}, 'Area 4':{10:0},'Area 6':{11:0},'Area 8':{12  :  0 ,13  :  0 ,14  :  0 ,15  :  0 ,16  :  0 ,17  :  0 ,18  :  0 ,19  :  0 }, 'Area 9':{20  :  0 ,21  :  0 },'Area 12':{22  :  0 ,23  :  0 ,24  :  0 },'Area 13':{25  :  0 ,26  :  0 },'Area 14':{27:0}, 'Area 17':{28  :  0 ,29  :  0 ,30  :  0},'Area 19':{31  :  0 ,32  :  0 ,33  :  0 ,34  :  0 ,35  :  0 ,36  :  0},'Area 20 Dimas':{37:0},'Area 21':{38:0},'Area Gordo':{39  :  0 ,40  :  0 ,41  :  0 ,42  :  0 ,43  :  0 ,44  :  0},'Pivô 1':{45  :  0 ,46  :  0 ,47  :  0 ,48  :  0 ,49  :  0 ,50  :  0 ,51  :  0 ,52  :  0 ,53  :  0 ,54  :  0},'Pivô 2':{55  :  0 ,56  :  0 ,57  :  0 ,58  :  0 ,59  :  0 ,60  :  0},'Pivô 3':{61  :  0 ,62  :  0 ,63  :  0},'Pivô 4':{64  :  0 ,65  :  0 ,66  :  0 ,67  :  0 ,68  :  0 ,69  :  0 ,70  :  0},'Pivô 5':{71  :  0 ,72  :  0 ,73  :  0 ,74  :  0 ,75  :  0 ,76  :  0 },'Pivô 6':{77  :  0 ,78  :  0 ,79  :  0 ,80  :  0 ,81  :  0 ,82  :  0},'Pivô 7':{83  :  0 ,84  :  0 ,85  :  0 ,86  :  0 ,87  :  0 ,88  :  0 ,89  :  0 ,90  :  0 ,91  :  0 ,92  :  0},'Pivô 8, 9 e area 16':{93  :  0 ,94  :  0 ,95  :  0 ,96  :  0 ,97  :  0 ,98  :  0 ,99  :  0 ,100  :  0 ,101  :  0 ,102  :  0 ,103  :  0 ,104  :  0 ,105  :  0 ,106  :  0},'Pivô 10':{107  :  0 ,108  :  0 ,109  :  0 ,110  :  0 ,111  :  0 ,112  :  0 ,113  :  0 },'Pivô 11':{114  :  0 ,115  :  0 ,116  :  0 ,117  :  0},'Pivô 12 Antigo':{131  :  0 ,132  :  0 ,133  :  0 ,134:0},'Pivô 12 2022':{118:0,119:0,120:0,121:0, 122:0,123:0,124:0},'Pivô 13 e 14':{125  :  0 ,126  :  0 ,127  :  0 ,128  :  0 ,129  :  0 ,130  :  0},'Pivô 15':{135:0,136:0,137:0,138:0}}
    areas = ['Area 2 e Zé', 'Area 3', 'Area 4','Area 6','Area 8', 'Area 9','Area 12','Area 13','Area 14', 'Area 17','Area 19','Area 20 Dimas','Area 21','Area Gordo','Pivô 1','Pivô 2','Pivô 3','Pivô 4','Pivô 5','Pivô 6','Pivô 7','Pivô 8, 9 e area 16','Pivô 10','Pivô 11','Pivô 12 Antigo','Pivô 12 2022','Pivô 13 e 14','Pivô 15',]

    window1 = tk.Tk()
    window1.geometry('700x220') #largura x altura
    window1.option_add('*Font','32') # altera tamanho da fonte
    window1.resizable(False,False)
    window1.title('Taxa Fácil 1.0')

    name = tk.Label(text = '')
    name.grid(column = 1, row = 0)

    name = tk.Label(text = 'Tipo de aplicação:')
    name.grid(column = 1, row = 1)
    tipo_var = tk.StringVar()
    select_tipo = ttk.Combobox(window1, textvariable=tipo_var) #TIPO
    select_tipo.grid(column=2, row=1)
    select_tipo['values'] = ('População (sementes/metro)','KCL', 'Ureia', 'MAP','Calcário')

    name = tk.Label(text = '')
    name.grid(column = 1, row = 2)

    maquina = tk.Label(text = 'Máquinário:')
    maquina.grid(column = 1, row = 3)
    maquina_var = tk.StringVar()
    select_maquina = ttk.Combobox(window1, textvariable=maquina_var) #TIPO
    select_maquina.grid(column=2, row=3)
    select_maquina['values'] = ('Stara','Kuhn Accura')

    name = tk.Label(text = '')
    name.grid(column = 1, row = 4)

    name = tk.Label(text = 'Área:')
    name.grid(column = 3, row = 3)
    area_var = tk.StringVar(window1) # associação a string_var
    select_area = ttk.Combobox(window1, value = areas, state='readonly')# combobox de area selecionada
    select_area.grid(column=4, row=3)
    select_area.set('Area 2 e Zé')#valor padrão selecionado

    drive_list = []
    def locate_usb():
        drivebits=win32file.GetLogicalDrives()
        for d in range(1,26):
            mask=1 << d
            if drivebits & mask:
                # here if the drive is at least there
                drname='%c:\\' % chr(ord('A')+d)
                t=win32file.GetDriveType(drname)
                if t == win32file.DRIVE_REMOVABLE:
                    drive_list.append(drname)
        return drive_list
    locate_usb()

    saida_nome = tk.Label(text = 'Pen-Drive:')
    saida_nome.grid(column = 3, row = 1)
    saida_drive = tk.StringVar(window1) # associação a string_var
    saida_drive = ttk.Combobox(window1, value = drive_list, state='readonly')# combobox de area selecionada
    saida_drive.grid(column=4, row=1)
    if drive_list:
        saida_drive.set(drive_list[0])#valor padrão selecionado
    else:
        drive_list = False

    sair = ttk.Button(window1,text = 'SAIR',command = lambda:window1.quit())
    sair.grid(column=3, row = 7)

    data = list(f'{current_time.day}_{current_time.month}_{current_time.year:2}')
    del data[len(data) - 3]
    del data[len(data) - 2]
    nome_data = ''.join(data)

    tk.messagebox.showinfo(title='Aviso', message=f'Apague os arquivos do pen-drive antes de continuar!',icon = 'warning')

    def cria_shp(gleba_num, hoje, tamanho): # EMFCI 
        saida = saida_drive.get()
        maquina = select_maquina.get()
        if maquina == 'Stara':
            path = f"{saida}\\Dados\Mapas"
            if not os.path.exists(f"{saida}\\Dados\Mapas"):
            # if the demo_folder directory is not present 
            # then create it.
                os.makedirs(f"{saida}\Dados\Mapas")
        elif maquina == 'Kuhn Accura':
            path = f"{saida}\\AgGPS\Prescriptions"
            if not os.path.exists(f"{saida}\\AgGPS\Prescriptions"):
            # if the demo_folder directory is not present 
            # then create it.
                os.makedirs(f"{saida}\AgGPS\Prescriptions")
        elif maquina == '':
            path = saida
        
        sf = shapefile.Reader('C:\\Program Files\Taxa fácil\Aguaclara_20221')
        
        def projec(texto):
            prj = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.000,298.25722356]],PRIMEM["Greenwich",0],UNIT["Degree",0.01745329251994]]'
            projeção = open(f"{path}\{texto}.prj","w+")
            projeção.write(f'{prj}')

        tipo = select_tipo.get()
        if tipo == 'População (sementes/metro)':
            tipo = 'populacao'
        elif tipo == 'Calcário':
            tipo = 'Ca'
        elif tipo == 'Ureia':
            tipo = 'adubo_N'
        elif tipo == 'KCL':
            tipo = 'KCL'
        elif tipo == '':
            tipo = ''
        def ajeita_nome():
            global area_n
            print(hoje,'hoje')
            area_n = list(hoje)
            del area_n[1]
            del area_n[1]
            del area_n[1]
            del area_n[1]

            #del area_n[4]
            area_n = ''.join(area_n)
            area_n.replace(' ', '_')
            return area_n

        if hoje == areas[0]:
            area_nome = 'A2'
        elif hoje == areas[11]:
            area_nome = 'Dima'
        elif hoje == areas[13]:
            area_nome = 'Gordo'
        elif hoje == areas[21]:
            area_nome = 'P8_9'
        elif hoje == areas[24]:
            area_nome = 'P12'
        elif hoje == areas[25]:
            area_nome = 'P12'
        elif hoje == areas[26]:
            area_nome = 'P13'
        else:
            ajeita_nome()
            area_nome = area_n

        #writer class
        print('NOME DA AREA',area_nome)#PONTO DE CONTROLE
        texto = f'{nome_data}_{tipo}_{area_nome}'#NOME ARQUIVO
        l = []
        n = 0
        gleba = gleba_num
        contador = 0
        #windows-1252
        #utf8
        with shapefile.Writer(fr'{path}\{texto}',encoding = 'windows-1252', shapeType = 5) as w:
            # momento em que se determina a classe das feições, bem como seu título.
            fields = sf.fields

            print('-' * 10,fields[1][0])# PONTO DE CONTROLE
            w.field(fields[1][0], 'C',size = 25 ) #'C' creates text fields, 'N' numbers
            w.field('TAXA', 'N', decimal = 2)
            quebra = False
            print('controle', contador, tamanho)# PONTO DE CONTROLE

            while contador < len(tamanho): # menor que o area_de_hoje
                if quebra:
                    break

                records = sf.record(n)
                shapes = sf.shape(n)
                dicionário_valores = records.as_dict()
                sorted(dicionário_valores.items())

                while dicionário_valores['CODE'] != str(gleba): #Elemento que define a gleba como parametro
                    if len(sf) == n:# Aqui ele compara o número de feições com o nosso número de indexação
                        print('NÃO HÁ FEIÇÕES COM ESSE NÚMERO!')# PONTO DE CONTROLE
                        quebra = True
                        break
                    records = sf.record(n)
                    shapes = sf.shape(n)
                    dicionário_valores = records.as_dict()
                    sorted(dicionário_valores.items())
                    n += 1

                l = []
                l.append(shapes.points)#Assimilação da geometria a uma lista, no caso os pontos do polígono

                bolha = str(areas_dict[hoje][gleba])
                bolha = bolha.replace(',','.')
                if bolha == '':
                    bolha = 0
                areas_dict[hoje][gleba] = float(bolha)

                w.poly(l)
                w.record(dicionário_valores['CODE'], areas_dict[hoje][gleba])
                print('TAXA',areas_dict[hoje][gleba],dicionário_valores['CODE'], 'CONTADOR:', contador, 'GLEBA:', gleba, 'LEN:', len(sf.record(contador))) #PONTO DE CONTROLE
                gleba += 1
                n = 0
                contador += 1
            projec(texto) 
        w.close()
        tk.messagebox.showinfo(title='Aviso', message=f'Arquivo de taxas criado com sucesso!')
        subprocess.Popen(fr'explorer /select, {path}\{texto}')

    def len1(area, num_gleba, tamanho):
        def associar():
            areas_dict[area][gleba1] = str(g1entry.get())# aqui que ele associa ao dicionário
            
            cria_shp(num_gleba, area, tamanho)
    # criação da gui
        window2 = tk.Tk()
        window2.geometry('450x300') #largura x altura
        window2.option_add('*Font','27') # altera tamanho da fonte
        window2.resizable(False,False)
        window2.title(f'Taxa Fácil 1.0 - {area}')

        gleba1 = num_gleba #este é o index da gleba
        g1Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {num_gleba}')
        g1Texto.grid(column = 0, row = 1)
        g1entry = ttk.Entry(window2)
        g1entry.grid(column=1, row=1)

        def press():
            associar()
            window2.destroy()

        button = ttk.Button(window2,text= 'GERAR ARQUIVO', command = press)
        button.grid(column=1, row=2)

    def len2(area, num_gleba, tamanho):
        def associar():
            areas_dict[area][gleba1] = g1entry.get() # aqui que ele associa ao dicionário
            areas_dict[area][gleba2] = g2entry.get() # após associado cabe ao EMFCI associar os valores do dicionário ao shp
            
            cria_shp(num_gleba,area,tamanho)
    # criação da gui
        window2 = tk.Tk()
        window2.geometry('450x300') #largura x altura
        window2.option_add('*Font','27') # altera tamanho da fonte
        window2.resizable(False,False)
        window2.title(f'Taxa Fácil 1.0 - {area}')

        gleba1 = num_gleba #este é o index da gleba
        g1Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {num_gleba}')
        g1Texto.grid(column = 0, row = 1)
        g1entry = ttk.Entry(window2)
        g1entry.grid(column=1, row=1)

        gleba2 = num_gleba + 1 #este é o index da gleba
        g2Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba2}') 
        g2Texto.grid(column = 0, row = 2)
        g2entry = ttk.Entry(window2)
        g2entry.grid(column=1, row=2)

        def press():
            associar()
            window2.destroy()

        button = ttk.Button(window2,text= 'GERAR ARQUIVO', command = press)
        button.grid(column=1, row=10)

    def len3(area, num_gleba, tamanho):
        def associar():
            areas_dict[area][gleba1] = g1entry.get() # aqui que ele associa ao dicionário
            areas_dict[area][gleba2] = g2entry.get() # após associado cabe ao EMFCI associar os valores do dicionário ao shp
            areas_dict[area][gleba3] = g3entry.get()

            cria_shp(num_gleba,area,tamanho)
    # criação da gui
        window2 = tk.Tk()
        window2.geometry('450x300') #largura x altura
        window2.option_add('*Font','27') # altera tamanho da fonte
        window2.resizable(False,False)
        window2.title(f'Taxa Fácil 1.0 - {area}')

        gleba1 = num_gleba #este é o index da gleba
        g1Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {num_gleba}')
        g1Texto.grid(column = 0, row = 1)
        g1entry = ttk.Entry(window2)
        g1entry.grid(column=1, row=1)

        gleba2 = num_gleba + 1 #este é o index da gleba
        g2Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba2}') 
        g2Texto.grid(column = 0, row = 2)
        g2entry = ttk.Entry(window2)
        g2entry.grid(column=1, row=2)

        gleba3 = num_gleba + 2 #este é o index da gleba
        g3Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba3}') 
        g3Texto.grid(column = 0, row = 3)# NÃO ESQUECER
        g3entry = ttk.Entry(window2)
        g3entry.grid(column=1, row=3) # NÃO ESQUECER

        def press():
            associar()
            window2.destroy()

        button = ttk.Button(window2,text= 'GERAR ARQUIVO', command = press)
        button.grid(column=1, row=10)

    def len4(area, num_gleba, tamanho):
        def associar():
            areas_dict[area][gleba1] = g1entry.get() # aqui que ele associa ao dicionário
            areas_dict[area][gleba2] = g2entry.get() # após associado cabe ao EMFCI associar os valores do dicionário ao shp
            areas_dict[area][gleba3] = g3entry.get()
            areas_dict[area][gleba4] = g4entry.get()


            cria_shp(num_gleba,area,tamanho)
    # criação da gui
        window2 = tk.Tk()
        window2.geometry('450x300') #largura x altura
        window2.option_add('*Font','27') # altera tamanho da fonte
        window2.resizable(False,False)
        window2.title(f'Taxa Fácil 1.0 - {area}')

        gleba1 = num_gleba #este é o index da gleba
        g1Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {num_gleba}')
        g1Texto.grid(column = 0, row = 1)
        g1entry = ttk.Entry(window2)
        g1entry.grid(column=1, row=1)

        gleba2 = num_gleba + 1 #este é o index da gleba
        g2Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba2}') 
        g2Texto.grid(column = 0, row = 2)
        g2entry = ttk.Entry(window2)
        g2entry.grid(column=1, row=2)

        gleba3 = num_gleba + 2 #este é o index da gleba
        g3Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba3}') 
        g3Texto.grid(column = 0, row = 3)# NÃO ESQUECER
        g3entry = ttk.Entry(window2)
        g3entry.grid(column=1, row=3) # NÃO ESQUECER

        gleba4 = num_gleba + 3 #este é o index da gleba
        g4Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba4}') 
        g4Texto.grid(column = 0, row = 4)# NÃO ESQUECER
        g4entry = ttk.Entry(window2)
        g4entry.grid(column=1, row=4) # NÃO ESQUECER

        def press():
            associar()
            window2.destroy()

        button = ttk.Button(window2,text= 'GERAR ARQUIVO', command = press)
        button.grid(column=1, row=10)

    def len5(area, num_gleba, tamanho):
        def associar():
            areas_dict[area][gleba1] = g1entry.get() # aqui que ele associa ao dicionário
            areas_dict[area][gleba2] = g2entry.get() # após associado cabe ao EMFCI associar os valores do dicionário ao shp
            areas_dict[area][gleba3] = g3entry.get()
            areas_dict[area][gleba4] = g4entry.get()
            areas_dict[area][gleba5] = g5entry.get()


            cria_shp(num_gleba,area,tamanho)
    # criação da gui
        window2 = tk.Tk()
        window2.geometry('450x300') #largura x altura
        window2.option_add('*Font','27') # altera tamanho da fonte
        window2.resizable(False,False)
        window2.title(f'Taxa Fácil 1.0 - {area}')

        gleba1 = num_gleba #este é o index da gleba
        g1Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {num_gleba}')
        g1Texto.grid(column = 0, row = 1)
        g1entry = ttk.Entry(window2)
        g1entry.grid(column=1, row=1)

        gleba2 = num_gleba + 1 #este é o index da gleba
        g2Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba2}') 
        g2Texto.grid(column = 0, row = 2)
        g2entry = ttk.Entry(window2)
        g2entry.grid(column=1, row=2)

        gleba3 = num_gleba + 2 #este é o index da gleba
        g3Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba3}') 
        g3Texto.grid(column = 0, row = 3)# NÃO ESQUECER
        g3entry = ttk.Entry(window2)
        g3entry.grid(column=1, row=3) # NÃO ESQUECER

        gleba4 = num_gleba + 3 #este é o index da gleba
        g4Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba4}') 
        g4Texto.grid(column = 0, row = 4)# NÃO ESQUECER
        g4entry = ttk.Entry(window2)
        g4entry.grid(column=1, row=4) # NÃO ESQUECER

        gleba5 = num_gleba + 4 #este é o index da gleba
        g5Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba5}') 
        g5Texto.grid(column = 0, row = 5)# NÃO ESQUECER
        g5entry = ttk.Entry(window2)
        g5entry.grid(column=1, row=5) # NÃO ESQUECER

        def press():
            associar()
            window2.destroy()

        button = ttk.Button(window2,text= 'GERAR ARQUIVO', command = press)
        button.grid(column=1, row=10)

    def len6(area, num_gleba, tamanho):
        def associar():
            areas_dict[area][gleba1] = g1entry.get() # aqui que ele associa ao dicionário
            areas_dict[area][gleba2] = g2entry.get() # após associado cabe ao EMFCI associar os valores do dicionário ao shp
            areas_dict[area][gleba3] = g3entry.get()
            areas_dict[area][gleba4] = g4entry.get()
            areas_dict[area][gleba5] = g5entry.get()
            areas_dict[area][gleba6] = g6entry.get()


            cria_shp(num_gleba,area,tamanho)
    # criação da gui
        window2 = tk.Tk()
        window2.geometry('450x300') #largura x altura
        window2.option_add('*Font','27') # altera tamanho da fonte
        window2.resizable(False,False)
        window2.title(f'Taxa Fácil 1.0 - {area}')

        gleba1 = num_gleba #este é o index da gleba
        g1Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {num_gleba}')
        g1Texto.grid(column = 0, row = 1)
        g1entry = ttk.Entry(window2)
        g1entry.grid(column=1, row=1)

        gleba2 = num_gleba + 1 #este é o index da gleba
        g2Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba2}') 
        g2Texto.grid(column = 0, row = 2)
        g2entry = ttk.Entry(window2)
        g2entry.grid(column=1, row=2)

        gleba3 = num_gleba + 2 #este é o index da gleba
        g3Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba3}') 
        g3Texto.grid(column = 0, row = 3)# NÃO ESQUECER
        g3entry = ttk.Entry(window2)
        g3entry.grid(column=1, row=3) # NÃO ESQUECER

        gleba4 = num_gleba + 3 #este é o index da gleba
        g4Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba4}') 
        g4Texto.grid(column = 0, row = 4)# NÃO ESQUECER
        g4entry = ttk.Entry(window2)
        g4entry.grid(column=1, row=4) # NÃO ESQUECER

        gleba5 = num_gleba + 4 #este é o index da gleba
        g5Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba5}') 
        g5Texto.grid(column = 0, row = 5)# NÃO ESQUECER
        g5entry = ttk.Entry(window2)
        g5entry.grid(column=1, row=5) # NÃO ESQUECER

        gleba6 = num_gleba + 5 #este é o index da gleba
        g6Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba6}') 
        g6Texto.grid(column = 0, row = 6)# NÃO ESQUECER
        g6entry = ttk.Entry(window2)
        g6entry.grid(column=1, row=6) # NÃO ESQUECER

        def press():
            associar()
            window2.destroy()

        button = ttk.Button(window2,text= 'GERAR ARQUIVO', command = press)
        button.grid(column=1, row=10)

    def len7(area, num_gleba, tamanho):
        def associar():
            areas_dict[area][gleba1] = g1entry.get() # aqui que ele associa ao dicionário
            areas_dict[area][gleba2] = g2entry.get() # após associado cabe ao EMFCI associar os valores do dicionário ao shp
            areas_dict[area][gleba3] = g3entry.get()
            areas_dict[area][gleba4] = g4entry.get()
            areas_dict[area][gleba5] = g5entry.get()
            areas_dict[area][gleba6] = g6entry.get()
            areas_dict[area][gleba7] = g7entry.get()


            cria_shp(num_gleba,area,tamanho)
    # criação da gui
        window2 = tk.Tk()
        window2.geometry('450x300') #largura x altura
        window2.option_add('*Font','27') # altera tamanho da fonte
        window2.resizable(False,False)
        window2.title(f'Taxa Fácil 1.0 - {area}')

        gleba1 = num_gleba #este é o index da gleba
        g1Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {num_gleba}')
        g1Texto.grid(column = 0, row = 1)
        g1entry = ttk.Entry(window2)
        g1entry.grid(column=1, row=1)

        gleba2 = num_gleba + 1 #este é o index da gleba
        g2Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba2}') 
        g2Texto.grid(column = 0, row = 2)
        g2entry = ttk.Entry(window2)
        g2entry.grid(column=1, row=2)

        gleba3 = num_gleba + 2 #este é o index da gleba
        g3Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba3}') 
        g3Texto.grid(column = 0, row = 3)# NÃO ESQUECER
        g3entry = ttk.Entry(window2)
        g3entry.grid(column=1, row=3) # NÃO ESQUECER

        gleba4 = num_gleba + 3 #este é o index da gleba
        g4Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba4}') 
        g4Texto.grid(column = 0, row = 4)# NÃO ESQUECER
        g4entry = ttk.Entry(window2)
        g4entry.grid(column=1, row=4) # NÃO ESQUECER

        gleba5 = num_gleba + 4 #este é o index da gleba
        g5Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba5}') 
        g5Texto.grid(column = 0, row = 5)# NÃO ESQUECER
        g5entry = ttk.Entry(window2)
        g5entry.grid(column=1, row=5) # NÃO ESQUECER

        gleba6 = num_gleba + 5 #este é o index da gleba
        g6Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba6}') 
        g6Texto.grid(column = 0, row = 6)# NÃO ESQUECER
        g6entry = ttk.Entry(window2)
        g6entry.grid(column=1, row=6) # NÃO ESQUECER

        gleba7 = num_gleba + 6 #este é o index da gleba
        g7Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba7}') 
        g7Texto.grid(column = 0, row = 7)# NÃO ESQUECER
        g7entry = ttk.Entry(window2)
        g7entry.grid(column=1, row=7) # NÃO ESQUECER

        def press():
            associar()
            window2.destroy()


        button = ttk.Button(window2,text= 'GERAR ARQUIVO', command = press)
        button.grid(column=1, row=10)

    def len8(area, num_gleba, tamanho):
        def associar():
            areas_dict[area][gleba1] = g1entry.get() # aqui que ele associa ao dicionário
            areas_dict[area][gleba2] = g2entry.get() # após associado cabe ao EMFCI associar os valores do dicionário ao shp
            areas_dict[area][gleba3] = g3entry.get()
            areas_dict[area][gleba4] = g4entry.get()
            areas_dict[area][gleba5] = g5entry.get()
            areas_dict[area][gleba6] = g6entry.get()
            areas_dict[area][gleba7] = g7entry.get()
            areas_dict[area][gleba8] = g8entry.get()


            cria_shp(num_gleba,area,tamanho)
    # criação da gui
        window2 = tk.Tk()
        window2.geometry('450x300') #largura x altura
        window2.option_add('*Font','27') # altera tamanho da fonte
        window2.resizable(False,False)
        window2.title(f'Taxa Fácil 1.0 - {area}')

        gleba1 = num_gleba #este é o index da gleba
        g1Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {num_gleba}')
        g1Texto.grid(column = 0, row = 1)
        g1entry = ttk.Entry(window2)
        g1entry.grid(column=1, row=1)

        gleba2 = num_gleba + 1 #este é o index da gleba
        g2Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba2}') 
        g2Texto.grid(column = 0, row = 2)
        g2entry = ttk.Entry(window2)
        g2entry.grid(column=1, row=2)

        gleba3 = num_gleba + 2 #este é o index da gleba
        g3Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba3}') 
        g3Texto.grid(column = 0, row = 3)# NÃO ESQUECER
        g3entry = ttk.Entry(window2)
        g3entry.grid(column=1, row=3) # NÃO ESQUECER

        gleba4 = num_gleba + 3 #este é o index da gleba
        g4Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba4}') 
        g4Texto.grid(column = 0, row = 4)# NÃO ESQUECER
        g4entry = ttk.Entry(window2)
        g4entry.grid(column=1, row=4) # NÃO ESQUECER

        gleba5 = num_gleba + 4 #este é o index da gleba
        g5Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba5}') 
        g5Texto.grid(column = 0, row = 5)# NÃO ESQUECER
        g5entry = ttk.Entry(window2)
        g5entry.grid(column=1, row=5) # NÃO ESQUECER

        gleba6 = num_gleba + 5 #este é o index da gleba
        g6Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba6}') 
        g6Texto.grid(column = 0, row = 6)# NÃO ESQUECER
        g6entry = ttk.Entry(window2)
        g6entry.grid(column=1, row=6) # NÃO ESQUECER

        gleba7 = num_gleba + 6 #este é o index da gleba
        g7Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba7}') 
        g7Texto.grid(column = 0, row = 7)# NÃO ESQUECER
        g7entry = ttk.Entry(window2)
        g7entry.grid(column=1, row=7) # NÃO ESQUECER

        gleba8 = num_gleba + 7 #este é o index da gleba
        g8Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba8}') 
        g8Texto.grid(column = 0, row = 8)# NÃO ESQUECER
        g8entry = ttk.Entry(window2)
        g8entry.grid(column=1, row=8) # NÃO ESQUECER

        def press():
            associar()
            window2.destroy()

        button = ttk.Button(window2,text= 'GERAR ARQUIVO', command = press)
        button.grid(column=1, row=10)

    def len9(area, num_gleba, tamanho):
        def associar():
            areas_dict[area][gleba1] = g1entry.get() # aqui que ele associa ao dicionário
            areas_dict[area][gleba2] = g2entry.get() # após associado cabe ao EMFCI associar os valores do dicionário ao shp
            areas_dict[area][gleba3] = g3entry.get()
            areas_dict[area][gleba4] = g4entry.get()
            areas_dict[area][gleba5] = g5entry.get()
            areas_dict[area][gleba6] = g6entry.get()
            areas_dict[area][gleba7] = g7entry.get()
            areas_dict[area][gleba8] = g8entry.get()
            areas_dict[area][gleba9] = g9entry.get()


            cria_shp(num_gleba,area,tamanho)
    # criação da gui
        window2 = tk.Tk()
        window2.geometry('450x300') #largura x altura
        window2.option_add('*Font','27') # altera tamanho da fonte
        window2.resizable(False,False)
        window2.title(f'Taxa Fácil 1.0 - {area}')

        gleba1 = num_gleba #este é o index da gleba
        g1Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {num_gleba}')
        g1Texto.grid(column = 0, row = 1)
        g1entry = ttk.Entry(window2)
        g1entry.grid(column=1, row=1)

        gleba2 = num_gleba + 1 #este é o index da gleba
        g2Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba2}') 
        g2Texto.grid(column = 0, row = 2)
        g2entry = ttk.Entry(window2)
        g2entry.grid(column=1, row=2)

        gleba3 = num_gleba + 2 #este é o index da gleba
        g3Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba3}') 
        g3Texto.grid(column = 0, row = 3)# NÃO ESQUECER
        g3entry = ttk.Entry(window2)
        g3entry.grid(column=1, row=3) # NÃO ESQUECER

        gleba4 = num_gleba + 3 #este é o index da gleba
        g4Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba4}') 
        g4Texto.grid(column = 0, row = 4)# NÃO ESQUECER
        g4entry = ttk.Entry(window2)
        g4entry.grid(column=1, row=4) # NÃO ESQUECER

        gleba5 = num_gleba + 4 #este é o index da gleba
        g5Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba5}') 
        g5Texto.grid(column = 0, row = 5)# NÃO ESQUECER
        g5entry = ttk.Entry(window2)
        g5entry.grid(column=1, row=5) # NÃO ESQUECER

        gleba6 = num_gleba + 5 #este é o index da gleba
        g6Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba6}') 
        g6Texto.grid(column = 0, row = 6)# NÃO ESQUECER
        g6entry = ttk.Entry(window2)
        g6entry.grid(column=1, row=6) # NÃO ESQUECER

        gleba7 = num_gleba + 6 #este é o index da gleba
        g7Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba7}') 
        g7Texto.grid(column = 0, row = 7)# NÃO ESQUECER
        g7entry = ttk.Entry(window2)
        g7entry.grid(column=1, row=7) # NÃO ESQUECER

        gleba8 = num_gleba + 7 #este é o index da gleba
        g8Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba8}') 
        g8Texto.grid(column = 0, row = 8)# NÃO ESQUECER
        g8entry = ttk.Entry(window2)
        g8entry.grid(column=1, row=8) # NÃO ESQUECER

        gleba9 = num_gleba + 8 #este é o index da gleba
        g9Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba9}') 
        g9Texto.grid(column = 0, row = 9)# NÃO ESQUECER
        g9entry = ttk.Entry(window2)
        g9entry.grid(column=1, row=9) # NÃO ESQUECER

        def press():
            associar()
            window2.destroy()

        button = ttk.Button(window2,text= 'GERAR ARQUIVO', command = press)
        button.grid(column=1, row=10)

    def len10(area, num_gleba, tamanho):
        def associar():
            areas_dict[area][gleba1] = g1entry.get() # aqui que ele associa ao dicionário
            areas_dict[area][gleba2] = g2entry.get() # após associado cabe ao EMFCI associar os valores do dicionário ao shp
            areas_dict[area][gleba3] = g3entry.get()
            areas_dict[area][gleba4] = g4entry.get()
            areas_dict[area][gleba5] = g5entry.get()
            areas_dict[area][gleba6] = g6entry.get()
            areas_dict[area][gleba7] = g7entry.get()
            areas_dict[area][gleba8] = g8entry.get()
            areas_dict[area][gleba9] = g9entry.get()
            areas_dict[area][gleba10] = g10entry.get()


            cria_shp(num_gleba,area,tamanho)
    # criação da gui
        window2 = tk.Tk()
        window2.geometry('450x300') #largura x altura
        window2.option_add('*Font','27') # altera tamanho da fonte
        window2.resizable(False,False)
        window2.title(f'Taxa Fácil 1.0 - {area}')

        gleba1 = num_gleba #este é o index da gleba
        g1Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {num_gleba}')
        g1Texto.grid(column = 0, row = 1)
        g1entry = ttk.Entry(window2)
        g1entry.grid(column=1, row=1)

        gleba2 = num_gleba + 1 #este é o index da gleba
        g2Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba2}') 
        g2Texto.grid(column = 0, row = 2)
        g2entry = ttk.Entry(window2)
        g2entry.grid(column=1, row=2)

        gleba3 = num_gleba + 2 #este é o index da gleba
        g3Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba3}') 
        g3Texto.grid(column = 0, row = 3)# NÃO ESQUECER
        g3entry = ttk.Entry(window2)
        g3entry.grid(column=1, row=3) # NÃO ESQUECER

        gleba4 = num_gleba + 3 #este é o index da gleba
        g4Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba4}') 
        g4Texto.grid(column = 0, row = 4)# NÃO ESQUECER
        g4entry = ttk.Entry(window2)
        g4entry.grid(column=1, row=4) # NÃO ESQUECER

        gleba5 = num_gleba + 4 #este é o index da gleba
        g5Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba5}') 
        g5Texto.grid(column = 0, row = 5)# NÃO ESQUECER
        g5entry = ttk.Entry(window2)
        g5entry.grid(column=1, row=5) # NÃO ESQUECER

        gleba6 = num_gleba + 5 #este é o index da gleba
        g6Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba6}') 
        g6Texto.grid(column = 0, row = 6)# NÃO ESQUECER
        g6entry = ttk.Entry(window2)
        g6entry.grid(column=1, row=6) # NÃO ESQUECER

        gleba7 = num_gleba + 6 #este é o index da gleba
        g7Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba7}') 
        g7Texto.grid(column = 0, row = 7)# NÃO ESQUECER
        g7entry = ttk.Entry(window2)
        g7entry.grid(column=1, row=7) # NÃO ESQUECER

        gleba8 = num_gleba + 7 #este é o index da gleba
        g8Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba8}') 
        g8Texto.grid(column = 0, row = 8)# NÃO ESQUECER
        g8entry = ttk.Entry(window2)
        g8entry.grid(column=1, row=8) # NÃO ESQUECER

        gleba9 = num_gleba + 8 #este é o index da gleba
        g9Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba9}') 
        g9Texto.grid(column = 0, row = 9)# NÃO ESQUECER
        g9entry = ttk.Entry(window2)
        g9entry.grid(column=1, row=9) # NÃO ESQUECER

        gleba10 = num_gleba + 9 #este é o index da gleba
        g10Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba10}') 
        g10Texto.grid(column = 0, row = 10)# NÃO ESQUECER
        g10entry = ttk.Entry(window2)
        g10entry.grid(column=1, row=10) # NÃO ESQUECER

        def press():
            associar()
            window2.destroy()

        button = ttk.Button(window2,text= 'GERAR ARQUIVO', command = press)
        button.grid(column=1, row=11)

    def len11(area, num_gleba, tamanho):
        def associar():
            areas_dict[area][gleba1] = g1entry.get() # aqui que ele associa ao dicionário
            areas_dict[area][gleba2] = g2entry.get() # após associado cabe ao EMFCI associar os valores do dicionário ao shp
            areas_dict[area][gleba3] = g3entry.get()
            areas_dict[area][gleba4] = g4entry.get()
            areas_dict[area][gleba5] = g5entry.get()
            areas_dict[area][gleba6] = g6entry.get()
            areas_dict[area][gleba7] = g7entry.get()
            areas_dict[area][gleba8] = g8entry.get()
            areas_dict[area][gleba9] = g9entry.get()
            areas_dict[area][gleba10] = g10entry.get()
            areas_dict[area][gleba11] = g11entry.get()

            cria_shp(num_gleba,area,tamanho)
    # criação da gui
        window2 = tk.Tk()
        window2.geometry('450x400') #largura x altura
        window2.option_add('*Font','27') # altera tamanho da fonte
        window2.resizable(False,False)
        window2.title(f'Taxa Fácil 1.0 - {area}')

        gleba1 = num_gleba #este é o index da gleba
        g1Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {num_gleba}')
        g1Texto.grid(column = 0, row = 1)
        g1entry = ttk.Entry(window2)
        g1entry.grid(column=1, row=1)

        gleba2 = num_gleba + 1 #este é o index da gleba
        g2Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba2}') 
        g2Texto.grid(column = 0, row = 2)
        g2entry = ttk.Entry(window2)
        g2entry.grid(column=1, row=2)

        gleba3 = num_gleba + 2 #este é o index da gleba
        g3Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba3}') 
        g3Texto.grid(column = 0, row = 3)# NÃO ESQUECER
        g3entry = ttk.Entry(window2)
        g3entry.grid(column=1, row=3) # NÃO ESQUECER

        gleba4 = num_gleba + 3 #este é o index da gleba
        g4Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba4}') 
        g4Texto.grid(column = 0, row = 4)# NÃO ESQUECER
        g4entry = ttk.Entry(window2)
        g4entry.grid(column=1, row=4) # NÃO ESQUECER

        gleba5 = num_gleba + 4 #este é o index da gleba
        g5Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba5}') 
        g5Texto.grid(column = 0, row = 5)# NÃO ESQUECER
        g5entry = ttk.Entry(window2)
        g5entry.grid(column=1, row=5) # NÃO ESQUECER

        gleba6 = num_gleba + 5 #este é o index da gleba
        g6Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba6}') 
        g6Texto.grid(column = 0, row = 6)# NÃO ESQUECER
        g6entry = ttk.Entry(window2)
        g6entry.grid(column=1, row=6) # NÃO ESQUECER

        gleba7 = num_gleba + 6 #este é o index da gleba
        g7Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba7}') 
        g7Texto.grid(column = 0, row = 7)# NÃO ESQUECER
        g7entry = ttk.Entry(window2)
        g7entry.grid(column=1, row=7) # NÃO ESQUECER

        gleba8 = num_gleba + 7 #este é o index da gleba
        g8Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba8}') 
        g8Texto.grid(column = 0, row = 8)# NÃO ESQUECER
        g8entry = ttk.Entry(window2)
        g8entry.grid(column=1, row=8) # NÃO ESQUECER

        gleba9 = num_gleba + 8 #este é o index da gleba
        g9Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba9}') 
        g9Texto.grid(column = 0, row = 9)# NÃO ESQUECER
        g9entry = ttk.Entry(window2)
        g9entry.grid(column=1, row=9) # NÃO ESQUECER

        gleba10 = num_gleba + 9 #este é o index da gleba
        g10Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba10}') 
        g10Texto.grid(column = 0, row = 10)# NÃO ESQUECER
        g10entry = ttk.Entry(window2)
        g10entry.grid(column=1, row=10) # NÃO ESQUECER

        gleba11 = num_gleba + 10 #este é o index da gleba
        g11Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba11}') 
        g11Texto.grid(column = 0, row = 11)# NÃO ESQUECER
        g11entry = ttk.Entry(window2)
        g11entry.grid(column=1, row=11) # NÃO ESQUECER

        def press():
            associar()
            window2.destroy()

        button = ttk.Button(window2,text= 'GERAR ARQUIVO', command = press)
        button.grid(column=1, row=15)
    
    def len12(area, num_gleba, tamanho):
        def associar():
            areas_dict[area][gleba1] = g1entry.get() # aqui que ele associa ao dicionário
            areas_dict[area][gleba2] = g2entry.get() # após associado cabe ao EMFCI associar os valores do dicionário ao shp
            areas_dict[area][gleba3] = g3entry.get()
            areas_dict[area][gleba4] = g4entry.get()
            areas_dict[area][gleba5] = g5entry.get()
            areas_dict[area][gleba6] = g6entry.get()
            areas_dict[area][gleba7] = g7entry.get()
            areas_dict[area][gleba8] = g8entry.get()
            areas_dict[area][gleba9] = g9entry.get()
            areas_dict[area][gleba10] = g10entry.get()
            areas_dict[area][gleba11] = g11entry.get()
            areas_dict[area][gleba12] = g12entry.get()

            cria_shp(num_gleba,area,tamanho)
    # criação da gui
        window2 = tk.Tk()
        window2.geometry('450x400') #largura x altura
        window2.option_add('*Font','27') # altera tamanho da fonte
        window2.resizable(False,False)
        window2.title(f'Taxa Fácil 1.0 - {area}')

        gleba1 = num_gleba #este é o index da gleba
        g1Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {num_gleba}')
        g1Texto.grid(column = 0, row = 1)
        g1entry = ttk.Entry(window2)
        g1entry.grid(column=1, row=1)

        gleba2 = num_gleba + 1 #este é o index da gleba
        g2Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba2}') 
        g2Texto.grid(column = 0, row = 2)
        g2entry = ttk.Entry(window2)
        g2entry.grid(column=1, row=2)

        gleba3 = num_gleba + 2 #este é o index da gleba
        g3Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba3}') 
        g3Texto.grid(column = 0, row = 3)# NÃO ESQUECER
        g3entry = ttk.Entry(window2)
        g3entry.grid(column=1, row=3) # NÃO ESQUECER

        gleba4 = num_gleba + 3 #este é o index da gleba
        g4Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba4}') 
        g4Texto.grid(column = 0, row = 4)# NÃO ESQUECER
        g4entry = ttk.Entry(window2)
        g4entry.grid(column=1, row=4) # NÃO ESQUECER

        gleba5 = num_gleba + 4 #este é o index da gleba
        g5Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba5}') 
        g5Texto.grid(column = 0, row = 5)# NÃO ESQUECER
        g5entry = ttk.Entry(window2)
        g5entry.grid(column=1, row=5) # NÃO ESQUECER

        gleba6 = num_gleba + 5 #este é o index da gleba
        g6Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba6}') 
        g6Texto.grid(column = 0, row = 6)# NÃO ESQUECER
        g6entry = ttk.Entry(window2)
        g6entry.grid(column=1, row=6) # NÃO ESQUECER

        gleba7 = num_gleba + 6 #este é o index da gleba
        g7Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba7}') 
        g7Texto.grid(column = 0, row = 7)# NÃO ESQUECER
        g7entry = ttk.Entry(window2)
        g7entry.grid(column=1, row=7) # NÃO ESQUECER

        gleba8 = num_gleba + 7 #este é o index da gleba
        g8Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba8}') 
        g8Texto.grid(column = 0, row = 8)# NÃO ESQUECER
        g8entry = ttk.Entry(window2)
        g8entry.grid(column=1, row=8) # NÃO ESQUECER

        gleba9 = num_gleba + 8 #este é o index da gleba
        g9Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba9}') 
        g9Texto.grid(column = 0, row = 9)# NÃO ESQUECER
        g9entry = ttk.Entry(window2)
        g9entry.grid(column=1, row=9) # NÃO ESQUECER

        gleba10 = num_gleba + 9 #este é o index da gleba
        g10Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba10}') 
        g10Texto.grid(column = 0, row = 10)# NÃO ESQUECER
        g10entry = ttk.Entry(window2)
        g10entry.grid(column=1, row=10) # NÃO ESQUECER

        gleba11 = num_gleba + 10 #este é o index da gleba
        g11Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba11}') 
        g11Texto.grid(column = 0, row = 11)# NÃO ESQUECER
        g11entry = ttk.Entry(window2)
        g11entry.grid(column=1, row=11) # NÃO ESQUECER

        gleba12 = num_gleba + 11 #este é o index da gleba
        g12Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba12}') 
        g12Texto.grid(column = 0, row = 12)# NÃO ESQUECER
        g12entry = ttk.Entry(window2)
        g12entry.grid(column=1, row=12) # NÃO ESQUECER

        def press():
            associar()
            window2.destroy()

        button = ttk.Button(window2,text= 'GERAR ARQUIVO', command = press)
        button.grid(column=1, row=15)

    def len13(area, num_gleba, tamanho):
        def associar():
            areas_dict[area][gleba1] = g1entry.get() # aqui que ele associa ao dicionário
            areas_dict[area][gleba2] = g2entry.get() # após associado cabe ao EMFCI associar os valores do dicionário ao shp
            areas_dict[area][gleba3] = g3entry.get()
            areas_dict[area][gleba4] = g4entry.get()
            areas_dict[area][gleba5] = g5entry.get()
            areas_dict[area][gleba6] = g6entry.get()
            areas_dict[area][gleba7] = g7entry.get()
            areas_dict[area][gleba8] = g8entry.get()
            areas_dict[area][gleba9] = g9entry.get()
            areas_dict[area][gleba10] = g10entry.get()
            areas_dict[area][gleba11] = g11entry.get()
            areas_dict[area][gleba12] = g12entry.get()
            areas_dict[area][gleba13] = g13entry.get()


            cria_shp(num_gleba,area,tamanho)
    # criação da gui
        window2 = tk.Tk()
        window2.geometry('450x400') #largura x altura
        window2.option_add('*Font','27') # altera tamanho da fonte
        window2.resizable(False,False)
        window2.title(f'Taxa Fácil 1.0 - {area}')

        gleba1 = num_gleba #este é o index da gleba
        g1Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {num_gleba}')
        g1Texto.grid(column = 0, row = 1)
        g1entry = ttk.Entry(window2)
        g1entry.grid(column=1, row=1)

        gleba2 = num_gleba + 1 #este é o index da gleba
        g2Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba2}') 
        g2Texto.grid(column = 0, row = 2)
        g2entry = ttk.Entry(window2)
        g2entry.grid(column=1, row=2)

        gleba3 = num_gleba + 2 #este é o index da gleba
        g3Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba3}') 
        g3Texto.grid(column = 0, row = 3)# NÃO ESQUECER
        g3entry = ttk.Entry(window2)
        g3entry.grid(column=1, row=3) # NÃO ESQUECER

        gleba4 = num_gleba + 3 #este é o index da gleba
        g4Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba4}') 
        g4Texto.grid(column = 0, row = 4)# NÃO ESQUECER
        g4entry = ttk.Entry(window2)
        g4entry.grid(column=1, row=4) # NÃO ESQUECER

        gleba5 = num_gleba + 4 #este é o index da gleba
        g5Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba5}') 
        g5Texto.grid(column = 0, row = 5)# NÃO ESQUECER
        g5entry = ttk.Entry(window2)
        g5entry.grid(column=1, row=5) # NÃO ESQUECER

        gleba6 = num_gleba + 5 #este é o index da gleba
        g6Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba6}') 
        g6Texto.grid(column = 0, row = 6)# NÃO ESQUECER
        g6entry = ttk.Entry(window2)
        g6entry.grid(column=1, row=6) # NÃO ESQUECER

        gleba7 = num_gleba + 6 #este é o index da gleba
        g7Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba7}') 
        g7Texto.grid(column = 0, row = 7)# NÃO ESQUECER
        g7entry = ttk.Entry(window2)
        g7entry.grid(column=1, row=7) # NÃO ESQUECER

        gleba8 = num_gleba + 7 #este é o index da gleba
        g8Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba8}') 
        g8Texto.grid(column = 0, row = 8)# NÃO ESQUECER
        g8entry = ttk.Entry(window2)
        g8entry.grid(column=1, row=8) # NÃO ESQUECER

        gleba9 = num_gleba + 8 #este é o index da gleba
        g9Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba9}') 
        g9Texto.grid(column = 0, row = 9)# NÃO ESQUECER
        g9entry = ttk.Entry(window2)
        g9entry.grid(column=1, row=9) # NÃO ESQUECER

        gleba10 = num_gleba + 9 #este é o index da gleba
        g10Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba10}') 
        g10Texto.grid(column = 0, row = 10)# NÃO ESQUECER
        g10entry = ttk.Entry(window2)
        g10entry.grid(column=1, row=10) # NÃO ESQUECER

        gleba11 = num_gleba + 10 #este é o index da gleba
        g11Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba11}') 
        g11Texto.grid(column = 0, row = 11)# NÃO ESQUECER
        g11entry = ttk.Entry(window2)
        g11entry.grid(column=1, row=11) # NÃO ESQUECER

        gleba12 = num_gleba + 11 #este é o index da gleba
        g12Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba12}') 
        g12Texto.grid(column = 0, row = 12)# NÃO ESQUECER
        g12entry = ttk.Entry(window2)
        g12entry.grid(column=1, row=12) # NÃO ESQUECER

        gleba13 = num_gleba + 12 #este é o index da gleba
        g13Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba13}') 
        g13Texto.grid(column = 0, row = 13)# NÃO ESQUECER
        g13entry = ttk.Entry(window2)
        g13entry.grid(column=1, row=13) # NÃO ESQUECER

        def press():
            associar()
            window2.destroy()

        button = ttk.Button(window2,text= 'GERAR ARQUIVO', command = press)
        button.grid(column=1, row=15)

    def len14(area, num_gleba, tamanho):
        def associar():
            areas_dict[area][gleba1] = g1entry.get() # aqui que ele associa ao dicionário
            areas_dict[area][gleba2] = g2entry.get() # após associado cabe ao EMFCI associar os valores do dicionário ao shp
            areas_dict[area][gleba3] = g3entry.get()
            areas_dict[area][gleba4] = g4entry.get()
            areas_dict[area][gleba5] = g5entry.get()
            areas_dict[area][gleba6] = g6entry.get()
            areas_dict[area][gleba7] = g7entry.get()
            areas_dict[area][gleba8] = g8entry.get()
            areas_dict[area][gleba9] = g9entry.get()
            areas_dict[area][gleba10] = g10entry.get()
            areas_dict[area][gleba11] = g11entry.get()
            areas_dict[area][gleba12] = g12entry.get()
            areas_dict[area][gleba13] = g13entry.get()
            areas_dict[area][gleba14] = g14entry.get()
            cria_shp(num_gleba,area,tamanho)
    # criação da gui
        window2 = tk.Tk()
        window2.geometry('450x400') #largura x altura
        window2.option_add('*Font','27') # altera tamanho da fonte
        window2.resizable(False,False)
        window2.title(f'Taxa Fácil 1.0 - {area}')

        gleba1 = num_gleba #este é o index da gleba
        g1Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {num_gleba}')
        g1Texto.grid(column = 0, row = 1)
        g1entry = ttk.Entry(window2)
        g1entry.grid(column=1, row=1)

        gleba2 = num_gleba + 1 #este é o index da gleba
        g2Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba2}') 
        g2Texto.grid(column = 0, row = 2)
        g2entry = ttk.Entry(window2)
        g2entry.grid(column=1, row=2)

        gleba3 = num_gleba + 2 #este é o index da gleba
        g3Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba3}') 
        g3Texto.grid(column = 0, row = 3)# NÃO ESQUECER
        g3entry = ttk.Entry(window2)
        g3entry.grid(column=1, row=3) # NÃO ESQUECER

        gleba4 = num_gleba + 3 #este é o index da gleba
        g4Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba4}') 
        g4Texto.grid(column = 0, row = 4)# NÃO ESQUECER
        g4entry = ttk.Entry(window2)
        g4entry.grid(column=1, row=4) # NÃO ESQUECER

        gleba5 = num_gleba + 4 #este é o index da gleba
        g5Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba5}') 
        g5Texto.grid(column = 0, row = 5)# NÃO ESQUECER
        g5entry = ttk.Entry(window2)
        g5entry.grid(column=1, row=5) # NÃO ESQUECER

        gleba6 = num_gleba + 5 #este é o index da gleba
        g6Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba6}') 
        g6Texto.grid(column = 0, row = 6)# NÃO ESQUECER
        g6entry = ttk.Entry(window2)
        g6entry.grid(column=1, row=6) # NÃO ESQUECER

        gleba7 = num_gleba + 6 #este é o index da gleba
        g7Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba7}') 
        g7Texto.grid(column = 0, row = 7)# NÃO ESQUECER
        g7entry = ttk.Entry(window2)
        g7entry.grid(column=1, row=7) # NÃO ESQUECER

        gleba8 = num_gleba + 7 #este é o index da gleba
        g8Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba8}') 
        g8Texto.grid(column = 0, row = 8)# NÃO ESQUECER
        g8entry = ttk.Entry(window2)
        g8entry.grid(column=1, row=8) # NÃO ESQUECER

        gleba9 = num_gleba + 8 #este é o index da gleba
        g9Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba9}') 
        g9Texto.grid(column = 0, row = 9)# NÃO ESQUECER
        g9entry = ttk.Entry(window2)
        g9entry.grid(column=1, row=9) # NÃO ESQUECER

        gleba10 = num_gleba + 9 #este é o index da gleba
        g10Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba10}') 
        g10Texto.grid(column = 0, row = 10)# NÃO ESQUECER
        g10entry = ttk.Entry(window2)
        g10entry.grid(column=1, row=10) # NÃO ESQUECER

        gleba11 = num_gleba + 10 #este é o index da gleba
        g11Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba11}') 
        g11Texto.grid(column = 0, row = 11)# NÃO ESQUECER
        g11entry = ttk.Entry(window2)
        g11entry.grid(column=1, row=11) # NÃO ESQUECER

        gleba12 = num_gleba + 11 #este é o index da gleba
        g12Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba12}') 
        g12Texto.grid(column = 0, row = 12)# NÃO ESQUECER
        g12entry = ttk.Entry(window2)
        g12entry.grid(column=1, row=12) # NÃO ESQUECER

        gleba13 = num_gleba + 12 #este é o index da gleba
        g13Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba13}') 
        g13Texto.grid(column = 0, row = 13)# NÃO ESQUECER
        g13entry = ttk.Entry(window2)
        g13entry.grid(column=1, row=13) # NÃO ESQUECER

        gleba14 = num_gleba + 13 #este é o index da gleba
        g14Texto = tk.Label(window2, text = f'Insira uma taxa pra a gleba {gleba14}') 
        g14Texto.grid(column = 0, row = 14)# NÃO ESQUECER
        g14entry = ttk.Entry(window2)
        g14entry.grid(column=1, row=14) # NÃO ESQUECER

        def press():
            associar()
            window2.destroy()

        button = ttk.Button(window2,text= 'GERAR ARQUIVO', command = press)
        button.grid(column=1, row=15)

    def printar():
        area_selecionada = select_area.get()

        element = 0
        indexes = list(areas_dict[area_selecionada]) #elemento indexes é a lista das glebas
        index = indexes[element] # elemento index é o número da primeira gleba da área
        print(index, indexes,len(indexes))

        if len(indexes) == 1:
            len1(area_selecionada, index, indexes) #area_selecionada é: , index é: e indexes é tamanho
        elif len(indexes) == 2:
            len2(area_selecionada, index, indexes)
        elif len(indexes) == 3:
            len3(area_selecionada, index, indexes)
        elif len(indexes) == 4:
            len4(area_selecionada, index, indexes)
        elif len(indexes) == 5:
            len5(area_selecionada, index, indexes)
        elif len(indexes) == 6:
            len6(area_selecionada, index, indexes)
        elif len(indexes) == 7:
            len7(area_selecionada, index, indexes)
        elif len(indexes) == 8:
            len8(area_selecionada, index, indexes)
        elif len(indexes) == 9:
            len9(area_selecionada, index, indexes)
        elif len(indexes) == 10:
            len10(area_selecionada, index, indexes)
        elif len(indexes) == 11:
            len11(area_selecionada, index, indexes)
        elif len(indexes) == 12:
            len12(area_selecionada, index, indexes)
        elif len(indexes) == 13:
            len13(area_selecionada, index, indexes)
        elif len(indexes) == 14:
            len14(area_selecionada, index, indexes)

    name = tk.Label(text = '')
    name.grid(column = 1, row = 4)
    button = ttk.Button(window1, text = 'INSERIR TAXAS', command = printar)
    button.grid(column = 3, row = 6)

    window1.mainloop()
locate_usb()
if drive_list:
    app()
else:
    tk.messagebox.showinfo(title='Erro', message=f'Insira um Pen-drive!!!',icon = 'error')

import shapefile

#Criação do banco de dados para usarmos como referência de idexação
#Acesso a chave do dct: areas['Area2eZe'][1], areas['Area2eZe'][1] = 120

areas = {'Area 2 e Zé':{1  :  0 ,2  :  0 ,3  :  0 ,4  :  0 ,5  :  0 ,6  :  0 ,7  :  0 ,8  :  0 }, 'Area 3':{9:0}, 'Area 4':{10:0},'Area 6':{11:0},'Area 8':{12  :  0 ,13  :  0 ,14  :  0 ,15  :  0 ,16  :  0 ,17  :  0 ,18  :  0 ,19  :  0 }, 'Area 9':{20  :  0 ,21  :  0 },'Area 12':{22  :  0 ,23  :  0 ,24  :  0 },'Area 13':{25  :  0 ,26  :  0 },'Area 14':{27}, 'Area 17':{28  :  0 ,29  :  0 ,30  :  0},'Area 19':{31  :  0 ,32  :  0 ,33  :  0 ,34  :  0 ,35  :  0 ,36  :  0},'Area 20 Dimas':{37},'Area 21':{38},'Area Gordo':{39  :  0 ,40  :  0 ,41  :  0 ,42  :  0 ,43  :  0 ,44  :  0},'Pivô 1':{45  :  0 ,46  :  0 ,47  :  0 ,48  :  0 ,49  :  0 ,50  :  0 ,51  :  0 ,52  :  0 ,53  :  0 ,54  :  0},'Pivô 2':{55  :  0 ,56  :  0 ,57  :  0 ,58  :  0 ,59  :  0 ,60  :  0},'Pivô 3':{61  :  0 ,62  :  0 ,63  :  0},'Pivô 4':{64  :  0 ,65  :  0 ,66  :  0 ,67  :  0 ,68  :  0 ,69  :  0 ,70  :  0},'Pivô 5':{71  :  0 ,72  :  0 ,73  :  0 ,74  :  0 ,75  :  0 ,76  :  0 },'Pivô 6':{77  :  0 ,78  :  0 ,79  :  0 ,80  :  0 ,81  :  0 ,82  :  0},'Pivô 7':{83  :  0 ,84  :  0 ,85  :  0 ,86  :  0 ,87  :  0 ,88  :  0 ,89  :  0 ,90  :  0 ,91  :  0 ,92  :  0},'Pivô 8, 9 e area 16':{93  :  0 ,94  :  0 ,95  :  0 ,96  :  0 ,97  :  0 ,98  :  0 ,99  :  0 ,100  :  0 ,101  :  0 ,102  :  0 ,103  :  0 ,104  :  0 ,105  :  0 ,106  :  0},'Pivô 10':{107  :  0 ,108  :  0 ,109  :  0 ,110  :  0 ,111  :  0 ,112  :  0 ,113  :  0 },'Pivô 11':{114  :  0 ,115  :  0 ,116  :  0 ,117  :  0},'Pivô 12':{131  :  0 ,132  :  0 ,133  :  0 ,134:0},'Pivô 13 e 14':{125  :  0 ,126  :  0 ,127  :  0 ,128  :  0 ,129  :  0 ,130  :  0},'Pivô 15':{135:0,136:0,137:0,138:0}}

for i in areas:
    print(i)
area = input("Digite o nome da área: ")
for n in areas[area]:
    print(f'Há {len(areas[area])} Glebas na area.')
    taxa = int(input(f'Insira a taxa em kg/ha para a gleba {n}: '))
    print()
    areas[area][n] = taxa

for m in areas[area]:
    print(f'Gleba {m} : {areas[area][m]} kg/ha')

sf = shapefile.Reader('C:\\Program Files\Taxa fácil\Aguaclara_20221')

def projec(texto):
    prj = 'PROJCS["SIRGAS_2000_UTM_Zone_22S",GEOGCS["GCS_SIRGAS_2000",DATUM["D_SIRGAS_2000",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",10000000.0],PARAMETER["Central_Meridian",-51.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]'
    projeção = open(f"C:\\Users\Josué\Desktop\Testes pyshp\{texto}.prj","w+")
    projeção.write(f'{prj}')

#writer class
texto = 'shp1teste'
l = []
n = 0
gleba = 1
contador = 0

with shapefile.Writer(fr'C:\\Users\Josué\Desktop\Testes pyshp\{texto}', shapeType = 5) as w:
    # momento em que se determina a classe das feições, bem como seu título.
    fields = sf.fields

    w.field(fields[1][0], 'C',size = 25 )
    w.field('TAXA', 'N', decimal = 2)
    quebra = False
    while contador < len(areas[area]): #o key error vinha ocorrendo pois a nossa condição não satisfaz a necessidade, gravando 9 shapes e tentando pegar o 9º valor do dicionário
        if quebra:
            break
        records = sf.record(n)
        shapes = sf.shape(n)
        dicionário_valores = records.as_dict()
        sorted(dicionário_valores.items())
        while dicionário_valores['CODE'] != str(gleba): #Elemento que define a gleba como parametro
            if len(sf) == n:# Aqui ele compara o número de feições com o nosso número de indexação
                print('NÃO HÁ FEIÇÕES COM ESSE NÚMERO!')
                quebra = True
                break
            records = sf.record(n)
            shapes = sf.shape(n)
            dicionário_valores = records.as_dict()
            sorted(dicionário_valores.items())
            n += 1

        l = []
        l.append(shapes.points)#Assimilação da geometria a uma lista, no caso os pontos do polígono

        w.poly(l)
        w.record(dicionário_valores['CODE'], areas[area][gleba])

        print(dicionário_valores, dicionário_valores['CODE'], 'CONTADOR:', contador, 'GLEBA:', gleba, 'LEN:', len(sf.record(contador))) #PONTO DE CONTROLE

        gleba += 1
        n = 0
        contador += 1
    projec(texto) 
w.close()

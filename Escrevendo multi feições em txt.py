import shapefile
import csv

sf = shapefile.Reader('C:\\Users\Josué\Desktop\Testes pyshp\Glebas_totais')

print(sf.shapeTypeName)
print(2, sf.shape())

#geometria
s = sf.shape(2)
print(3, ['%.3f' % coord for coord in s.bbox])

l = []

n = 0
while n < len(sf.shapes()) - 1:
        records = sf.record(n)
        index = records.oid
      #Nome dos atributos geométricos dentro do shp
        shapes = sf.shape(n)
      #usando o atributo geométrico
        print(len(sf.shapes()))
        print(shapes.points)
        l.append(shapes.points)
        n += 1

my_file = open(f"C:\\Users\Josué\Desktop\Testes pyshp\Pontos index {index} {11}.txt","w+")
my_file.write(f'{l}')
       


import numpy
# размерность строк
x = 3
# размерность столбцов 
y = 3
array = numpy.random.randint(1,10,size=x*y)
matrix = numpy.matrix(array).reshape(x,y)
#матрица
print(matrix)
maxs = numpy.max(matrix, axis=1)
#максимумы
print(maxs)
mins = numpy.min(matrix, axis=1)
#минимумы
print(mins)
import numpy
# размерность строк
x = 3
# размерность столбцов 
y = 3
# правильный вариант
matrix = numpy.random.randint(1,10, size=[x,y])
print(matrix)

# а вот так я сделал первый раз. Тоже работает, но лишняя опервация
array = numpy.random.randint(1,10,size=x*y)
matrix = numpy.matrix(array).reshape([x,y])
print(matrix)

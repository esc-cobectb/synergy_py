algebra = set(input().split())
geometry = set(input().split())
trigonometry = set(input().split())
inter1 = algebra.intersection(geometry,trigonometry)
if(len(inter1)):
	print(" ".join(sorted(inter1)))
else :
	print("Все три задачи никто не решил")

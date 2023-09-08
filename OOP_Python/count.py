class C:
	counter = 0
	def __init__(self):
		type(self).counter += 1

	def __del__(self):
		type(self).counter -= 1


x = C()
print("NUmber of instances: : " + str(C.counter))
y = C()
print("NUmber of instances: : " + str(C.counter))
del x
print("NUmber of instances: : " + str(C.counter))
del y
print("NUmber of instances: : " + str(C.counter))
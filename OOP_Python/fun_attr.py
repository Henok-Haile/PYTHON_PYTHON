def f(x):
	f.counter = getattr(f, "counter", 0) + 1
	return "Monty Python"

for i in range(10):
	x = f(i)
	print(i)
	print(x)
	print(f.counter)
	print("---")
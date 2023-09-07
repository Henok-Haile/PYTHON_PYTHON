class Robot:
	def __init__(self, name, build_year):
		self.name = name
		self.build_year = build_year

	def __repr__(self):
		return "Robot('" + self.name + "', " + str(self.build_year) + ")"
	
	def __str__(self):
		return "Name: " + self.name + ", Build Year: " + str(self.build_year)

x = Robot("Marvin", 1979)
x_str = str(x)
print(str(x))
print(x_str)
print("Type of x_str: ", type(x_str))

print(x)

x_repr = repr(x)
print(x_repr, type(x_repr))
new = eval(x_repr)
print(new)
print("Type of new: ", type(new))
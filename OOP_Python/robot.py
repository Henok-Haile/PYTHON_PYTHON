class Robot:
	def __init__(self, name=None, build_year=None):
		self.__name = name
		self.__build_year = build_year

	def say_hi(self):
		if self.__name:
			print("Hi I am " + self.__name)
		else:
			print("Hi I am a robot without a name")

		if self.__build_year:
			print("I was built in " + str(self.__build_year))
		else:
			print("It's not known, when I was created!")
	
	def set_name(self, name):
		self.__name = name

	def get_name(self):
		return self.__name
	
	def set_build_year(self, by):
		self.__build_year = by

	def get_build_year(self):
		return self.__build_year
	
	def __repr__(self):
		return "Robot('" + self.__name + "', " + str(self.__build_year) + ")"
	
	def __str__(self):
		return "Name: " + self.__name + ", Build Year: " + str(self.__build_year)

x = Robot("Marvin", 1979)
y= Robot("Caliban", 1943)
for rob in [x, y]:
	rob.say_hi()
	if rob.get_name() == "Caliban":
		rob.set_build_year(1993)
	print("I was biult in the year " + str(rob.get_build_year()) + "!")
x._Robot__build_year = 1993
print(x.get_build_year())
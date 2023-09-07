def hi(obj):
	print("Hi, I am " + obj.name + "!")

class Robot:
	say_hi = hi

x = Robot()
x.name = "Marvin"
x.build_year = "1993"

type(x).say_hi(x)
Robot.say_hi(x)
x.say_hi()
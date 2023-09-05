class Person:
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print("Hello, my name is", self.name)


p = Person('Henok')
p.say_hi()
# The previous two lines can also be written as
# Person("Henok").say_hi()
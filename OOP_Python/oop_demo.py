class Robot:
	pass

x = Robot()
x.name = "Marvin"
x.build_year = "1979"
Robot.brand = "Kuka"
x.brand = "Thales"
x.energy = getattr(x, "energy", 100)
x.energy = getattr(x, "energy", 50) + 1

y = Robot()
y.name = "Caliban"
y.build_year = "1993"

print(x.__dict__, "--->", x.name, x.build_year, x.brand)
print(y.__dict__, "--->", y.name, y.build_year, y.brand)
print(Robot.__dict__, "--->", Robot.brand)

class Student():
    def __init__(self, name):
        self.name = name

students = reload() # recreate the list of Student objects from a file
std = Student("Henok")
students.append(std)
save(students) # save all Student objects to a filec
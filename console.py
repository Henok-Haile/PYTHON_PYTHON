import cmd

class MyConsole(cmd.Cmd):
    prompt = "Airbnb>> "
    


user = MyConsole()
print(user.prompt)

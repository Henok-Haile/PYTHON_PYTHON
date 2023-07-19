class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [D, C, B]:
    try:
        raise cls()
    except B:
        print("B")
    except C:
        print("C")
    except B:
        print("B")
import sys

# try:
#     print("Hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

if len(sys.argv) < 2:
    sys.exit("Two few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1])
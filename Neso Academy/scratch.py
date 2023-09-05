import sys
def linux_interaction():
	assert ('linux' in sys.platform), "This code can only run on Linux only."
	print("Doing something...")

try:
	linux_interaction()
except AssertionError as error:
	print(error)
	print("The linux_interaction() function was not executed")
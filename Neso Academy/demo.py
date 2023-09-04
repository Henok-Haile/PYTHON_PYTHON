
a = 5
b = 2 #0

try:
	print("resource open")
	print(a/b)
	#print("resource closed")
	k = int(input("Enter a number: "))
	print(k)
except ZeroDivisionError as e:
	print("Hey. You can't divide a number by Zero.", e)
	#print("resource closed")

except ValueError as e:
	print("Invalid Input.", e)

except Exception as e:
	print("Somthing went Wrong...")

# print("Bye")
finally:
	print("resource closed")
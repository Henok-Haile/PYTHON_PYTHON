import logging

values = [10, 5, 6, 0, 9, 8, 'Henok', 2]

for value in values:	
	try:
		print(10 / int(value))
	except ValueError as e:
		print("Value error is raised")
		raise
	except ZeroDivisionError as e:
		print("Zero division error")

	except Exception as e:
		logging.exception(e)

	else:
		print("No exception")

	finally:
		print("Always Executing...")

	# some code down here
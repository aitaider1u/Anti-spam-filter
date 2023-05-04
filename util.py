import pickle


def input_number(start,end,display):
	while True:
		num = input(display)
		try:
			num = int(num)
			if (num <start or num >end):
				raise ValueError("entre "+str(start) +"et"+str(end))
			return num
		except ValueError as e:
			print("Vieullez saisir un entier  " + str(e))


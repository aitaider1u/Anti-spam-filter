import pickle
import os

def input_number(start,end,display):
	while True:
		num = input(display)
		try:
			num = int(num)
			if (num <start or num >end):
				raise ValueError("")
			return num
		except ValueError as e:
			string = "Vieullez saisir un entier  " + "entre "+str(start) +" et "+str(end)
			print("\033[91m"+string+"\033[0m")


def input_string(display,defaultValue):
    string = input(display)
    return string

#function to load a Classifier like a Classifieur object
def loadClassifier():
	while True:
		fileName = input("Veuillez enter the nom du classifier a charger :")
		try:
			if (not os.path.isfile(fileName)):
				raise ValueError("Aucun classifieur trouvé avec ce nom : "+ fileName)
			f = open (fileName,"rb")
			classifier = pickle.load(f)
			f.close()
			return classifier
		except ValueError as e:
			print("\033[91m"+str(e)+"\033[0m")



    
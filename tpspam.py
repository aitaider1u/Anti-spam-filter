import numpy as np
import os
import math

def lireMail(fichier, dictionnaire):
	""" 
	Lire un fichier et retourner un vecteur de booléens en fonctions du dictionnaire
	"""
	f = open(fichier, "r",encoding="ascii", errors="surrogateescape")
	mots = f.read().split(" ")
	
	x = [False] * len(dictionnaire) 
	dictionnaire =np.array(dictionnaire)
	# modifié ..............................
	for i in range(len(mots)):			
		index = np.where(dictionnaire == mots[i].upper())[0]
		if len(index) >0:
			x[index[0]] = True
	f.close()
	return x

def charge_dico(fichier):
	f = open(fichier, "r")
	mots = f.read().split("\n")
	print("Chargé " + str(len(mots)) + " mots dans le dictionnaire")
	f.close()
	
	return mots[:-1]

def apprendBinomial(dossier, fichiers, dictionnaire):
	"""
	Fonction d'apprentissage d'une loi binomiale a partir des fichiers d'un dossier
	Retourne un vecteur b de paramètres 
	"""
	nb = len(fichiers)
	epsilon = 1
	
	occurencesMots = np.zeros(len(dictionnaire))
	for fichier in fichiers:
		mail = lireMail(fichier,dictionnaire)
		occurencesMots = occurencesMots + mail

	#Lissage des paramètres 
	b = ((occurencesMots + epsilon)/ (nb+2*epsilon ))
	return b   # vecteur de paramètres binomiaux


def prediction(x, Pspam, Pham, bspam, bham):
	"""
		Prédit si un mail représenté par un vecteur booléen x est un spam
		à partir du modèle de paramètres Pspam, Pham, bspam, bham.
		Retourne True ou False.
		
	"""
	



	return False  # à modifier...
	
def test(dossier, isSpam, Pspam, Pham, bspam, bham):
	"""
		Test le classifieur de paramètres Pspam, Pham, bspam, bham 
		sur tous les fichiers d'un dossier étiquetés 
		comme SPAM si isSpam et HAM sinon
		
		Retourne le taux d'erreur 
	"""
	fichiers = os.listdir(dossier)
	for fichier in fichiers:
		print("Mail " + dossier+"/"+fichier)		

		
		# à compléter...

	return 0  # à modifier...


############ programme principal ############

dossier_spams = "spam/baseapp/spam"	# à vérifier
dossier_hams = "spam/baseapp/ham"

fichiersspams = list(map(lambda e : dossier_spams+"/"+ e ,os.listdir(dossier_spams)))  
fichiershams = list(map(lambda e : dossier_hams+"/"+ e ,os.listdir(dossier_hams)))  

mSpam = len(fichiersspams)
mHam = len(fichiershams)

# Chargement du dictionnaire:
dictionnaire = charge_dico("dictionnaire1000en.txt")
print(dictionnaire)

# Apprentissage des bspam et bham:
print("apprentissage de bspam...")
bspam = apprendBinomial(dossier_spams, fichiersspams, dictionnaire)

print("apprentissage de bham...")
bham = apprendBinomial(dossier_hams, fichiershams, dictionnaire)

print(bspam)
#print(bham)


# Calcul des probabilités a priori Pspam et Pham:
Pspam = mSpam/(mSpam+mHam) 
Pham =  mHam/(mSpam+mHam)

# Calcul des erreurs avec la fonction test():



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
	motsPlusDe3lettre = [mot for mot in mots[:-1] if len(mot) >= 3]
	return motsPlusDe3lettre

def apprendBinomial(dossier, fichiers, dictionnaire):
	"""
	Fonction d'apprentissage d'une loi binomiale a partir des fichiers d'un dossier
	Retourne un vecteur b de paramètres 
	"""
	nb = len(fichiers)
	epsilon = 1
	
	occurencesMots = np.zeros(len(dictionnaire))
	for fichier in fichiers:
		mail = lireMail(dossier+"/"+fichier,dictionnaire)
		occurencesMots = occurencesMots + mail

	#Lissage des paramètres 
	b = ((occurencesMots + epsilon)/ (nb+2*epsilon ))
	return b  # vecteur de paramètres binomiaux


def prediction(x, Pspam, Pham, bspam, bham):
	"""
		Prédit si un mail représenté par un vecteur booléen x est un spam
		à partir du modèle de paramètres Pspam, Pham, bspam, bham.
		Retourne True ou False.
	"""

	#calcul de P(Y=Spam | X=x) 
	#Pspam_x= math.log(Pspam) + np.sum(np.log((bspam ** x) * ((1-bspam) ** (1-np.array(x)))))
	Px_spam = np.prod((bspam ** x) * ((1-bspam) ** (1-np.array(x))))
	Pspam_x=  Pspam * Px_spam
	
	#calcul de P(Y=Ham | X=x)
	#Pham_x = math.log(Pham) + np.sum(np.log((bham ** x) * ((1-bham) ** (1-np.array(x)))))
	Px_ham = np.prod( (bham ** x) * ((1-bham) ** (1-np.array(x))))
	Pham_x=  Pham * Px_ham

	if (Pspam_x >= Pham_x):
		return True
	return False  # à modifier...
	
def test(dossier, isSpam, Pspam, Pham, bspam, bham):
	"""
		Test le classifieur de paramètres Pspam, Pham, bspam, bham 
		sur tous les fichiers d'un dossier étiquetés 
		comme SPAM si isSpam et HAM sinon
		
		Retourne le taux d'erreur 
	"""
	fichiers = os.listdir(dossier)
	nbErreur = 0 
	dictionnaire=  charge_dico("dictionnaire1000en.txt")
	for fichier in fichiers:
		res = prediction(lireMail(dossier+"/"+fichier,dictionnaire),Pspam, Pham, bspam, bham)
		if (res+isSpam)%2 == 1:
			print(("SPAM" if isSpam else "HAM") +" " + dossier+"/"+fichier + " identifié comme un "+("SPAM" if (not isSpam) else "HAM")+" *** erreur ***")		
		else:
			print(("SPAM" if isSpam else "HAM") +" "+dossier+"/"+fichier + " identifié comme un "+("SPAM" if (isSpam) else "HAM"))		

		if (res+isSpam)%2 == 0:
			nbErreur = nbErreur +1  

	tauxErreur = nbErreur/len(fichiers)
	return 1-tauxErreur # à modifier...


############ programme principal ############

dossier_spams = "spam/baseapp/spam"	# à vérifier
dossier_hams = "spam/baseapp/ham"

fichiersspams = os.listdir(dossier_spams)
fichiershams =  os.listdir(dossier_hams) 

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


# Calcul des probabilités a priori Pspam et Pham:
Pspam = mSpam/(mSpam+mHam) 
Pham =  mHam/(mSpam+mHam)

# Calcul des erreurs avec la fonction test():
erreurSpam =test("spam/baseTest/spam",True,Pspam,Pham,bspam,bham)
erreurHam = test("spam/baseTest/ham",False,Pspam,Pham,bspam,bham)

print("Erreur de test sur 500 SPAM      : " +str(round(erreurSpam, 4)*100) +"%")
print("Erreur de test sur 500 HAM       : " +str(round(erreurHam, 4)*100) +"%")
print("Erreur de test globale sur 600 mails   : " +str((round(erreurSpam, 4)*100+round(erreurHam, 4)*100)/2) +"%")


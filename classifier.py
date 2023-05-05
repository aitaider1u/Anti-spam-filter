import pickle
import numpy as np

#Classe qui represente d'objet d'un classifieur.
#Les champs de la classe sont :
# nbSpam : nombre de spam au cours de l’apprentissage précédent
# nbHam : nombre de Ham au cours de l’apprentissage précédent
# coefBinomiaux : est de type dict qui enregistre des parametres du classifieur (coefficients Binomiaux)

EPSILON = 1

class Classifier: 
	#constructor 
	def __init__(self,bspam,bham,nbSpam, nbHam):
		self.coefBinomiaux =  {}   #dict 	
		for i in range (len(bspam)):
			self.coefBinomiaux['spam'+str(i)] = bspam[i]
		for i in range (len(bspam)):
			self.coefBinomiaux['ham'+str(i)] = bham[i]
		self.nbSpam = nbSpam
		self.nbHam = nbHam
		self.name = ""

	def save(self): 	#Save the Classifieur object
		with open(self.name, 'wb') as file:
			pickle.dump(self, file)
	
	def online_learning_spam(self,mail):	#enline learning from one new mail which is a spam.
		for i in range(len(mail)): 
			coefBinomal = self.coefBinomiaux['spam'+str(i)]
			n_i_spam = (coefBinomal*(self.nbSpam+2*EPSILON)) + mail[i] 
			self.coefBinomiaux['spam'+str(i)] = n_i_spam /(self.nbSpam +1 +2*EPSILON)
		self.nbSpam = self.nbSpam + 1 

	def online_learning_ham(self,mail): 	#online learning from one new mail which is a ham.
		for i in range(len(mail)): 
			coefBinomal = self.coefBinomiaux['ham'+str(i)]
			n_i_ham = (coefBinomal*(self.nbHam+2*EPSILON)) + mail[i] 
			self.coefBinomiaux['ham'+str(i)] = n_i_ham /(self.nbHam+1+2*EPSILON)
		self.nbHam = self.nbHam + 1 
	
	def get_bSpam(self):
		return np.array([value for key, value in self.coefBinomiaux.items() if "spam" in key])
	
	def get_bHam(self):
		return np.array ([value for key, value in self.coefBinomiaux.items() if "ham" in key])

	def get_PSpam(self):
		return self.nbSpam/(self.nbSpam+self.nbHam)
		
	def get_PHam(self):
		return self.nbHam/(self.nbSpam+self.nbHam)



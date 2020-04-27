class compteBancaire(object):
	def __init__(self, titulaire = 'Dupont', sold = 1000):
		print("L'objet à bien été crée !")
		print("La méthode est appelé automatiquement à la déclaration de l'objet")
		self._titulaire = titulaire 
		self._sold = sold

	def _get_sold(self):
		print("Récupération du sold")
		return self._sold

	def _set_sold(self, newValue):
		print("Changement du sold")
		self._sold  =  newValue

	def _get_titulaire(self):
		print("Récupération du titulaire")
		return self._titulaire

	def _set_titulaire(self, newValue):
		print("Changement du titulaire")
		self._titulaire = newValue

	def depot(self, depotValue):
		print("new depot")
		self._sold = self._sold + depotValue

	def retrait(self, retraitValue):
		print("new retrait")
		self._sold = self._sold - retraitValue

	def affiche(self):
		print(self._sold)

	sold=property(_get_sold, _set_sold)
	titulaire=property(_get_titulaire, _set_titulaire)

compte1 = compteBancaire('Duchmol', 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()
compte2 = compteBancaire()
compte2.depot(25)
compte2.affiche()

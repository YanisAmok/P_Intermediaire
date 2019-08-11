import sys
from PySide2.QtWidgets import (QApplication, QWidget)
from ui_IHM import Ui_Form
import numpy as np
import matplotlib.pyplot as plt
import json

with open('Projet intermediaire.json') as json_data:
    dico = json.load(json_data)
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        for a in dico["academies"]:
            self.ui.cbAcademie.addItem(a["nom"])
            for e in a["etablissements"]:
                self.ui.cbEtablissement.addItem(e["nom"])
                for c in e["classes"]:
                    self.ui.cbClasse.addItem(c["nom"])
        # self.ui.cbAcademie.currentIndexChanged.connect(self.afficherdico)

    # def afficherdico(self):
    #     for a in dico["academies"]:
    #         print(a["nom"])

#         self.ui.cbAcademie.currentIndexChanged.connect(self.updateEtablissements)
#         self.ui.cbEtablissement.currentIndexChanged.connect(self.updateClasses)
#         self.ui.cbClasse.currentIndexChanged.connect(self.updateMatieres)

    # def updateAcademie(self):
    #     self.ui.cbAcademie.clear()
    #     maliste = []
    #     for a in self.dico["academies"]:
    #         maliste.append("Paris")
    #         self.ui.cbAcademie.addItems(a["nom"])
    #         self.ui.cbAcademie.addItems(maliste)
    # def updateEtablissements (self):
    #     self.ui.cbEtablissement.clear()
    #     for e in self.dico["academies"][self.ui.cbAcademie.currentIndex()] ["etablissements"]:
    #         self.ui.cbEtablissement.addItems(e["nom"])
    #
    # def updateClasses (self):
    #     self.ui.cbClasse.clear()
    #     for c in self.dico["academies"][self.ui.cbAcademie.currentIndex()] ["etablissements"][self.ui.cbEtablissement.currentIndex()] ["classes"]:
    #         self.ui.cbClasse.addItems(c["nom"])
    #
    # def updateMatieres (self):
    #     dicoClasse = self.dico["academies"][self.ui.cbAcademie.currentIndex()]["etablissements"][self.ui.cbEtablissement.currentIndex()]["classes"][self.ui.cbClasse.currentIndex()] ["matieres"]:
    #     listeMatieres = []
    #     for eleve in dicoClasse["eleves"]:
    #         for matiere in eleve["matieres"]:
    #             listeMatieres.append(matiere["nom"])
    #     listeMatieresUniques = np.unique(listeMatieres)
    #     self.ui.cbMatiere.addItems(listeMatieresUniques)#addItems crée une liste
    #                                                     #addItem rajoute les elements un par un
#
#     def updateSaisieEleve(self):
#         listeEleves = []
#         cpt = 0
#         self.ui.twNotes.clear()
#         self.ui.twNotes.setColumnCount(2)
#         dicoClasse = self.dico["academies"][self.ui.cbAcademie.currentIndex()]["etablissements"][self.ui.cbEtablissement.currentIndex()] ["classes"][self.ui.cbClasse.currentIndex()]["matieres"][self.ui.cbMatiere.currentIndex()]
#         for eleve in dicoClasse["eleves"]:
#             for matiere in eleve ["matieres"]:
#                 mat = self.ui.cbMatiere.currentText()
#                 if matiere["nom"] == mat :
#                     nomE = eleve["nom"]
#                     self.ui.twNotes.setRowCount(cp+1)
#                     spinB = QDoubleSpinBox()
#                     spinB.setProperty("nom","nomE")
#                     self.ui.twNotes.setCellWidget(cpt,1,spinB)
#                     cpt=cpt+1
#         self.ui.twNotes.setHorizontalHeaderLabels(['Nom','Note'])
#
# #dico["academies"][0] ["etablissement"].append("{"nom:Arenes","adresse":"Billieres","classes:[]"})
#
#
# #def ajout Etablissement (dicoAcademie, nom, adresse):
#
#
#
# #def ajout Classe(dicoEtablissement, "nom", "annee", "PP"):
#
#
# #def getData(dictionnaire, cle):
#
#
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
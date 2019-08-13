import sys
from PySide2.QtWidgets import (QApplication, QWidget, QTableWidgetItem)
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
        self.ui.cbAcademie.currentIndexChanged.connect(self.updateEtablissements)
        self.ui.cbEtablissement.currentIndexChanged.connect(self.updateClasses)
        # self.ui.cbClasse.currentIndexChanged.connect(self.updateMatieres)

        # self.ui.pbAjoutAcademie.clicked.connect(self.ajoutAcademie)
        # self.ui.pbAjoutEtablissement.clicked.connect(self.ajoutEtablissement)
        # self.ui.pbAjoutClasse.clicked.connect(self.ajoutClasse)
        # self.ui.pbAjoutMatiere.clicked.connect(self.ajouMatiere)

        listEl = []
        arrMat = np.array([])
        self.ui.cbAcademie.addItem("Toutes les academies")
        self.ui.cbEtablissement.addItem("Tous les établissements")
        self.ui.cbClasse.addItem("Toutes les classes")
        for a in dico["academies"]:
            self.ui.cbAcademie.addItem(a["nom"])
            for e in a["etablissements"]:
                self.ui.cbEtablissement.addItem(e["nom"])
                for c in e["classes"]:
                    self.ui.cbClasse.addItem(c["nom"])

                    for el in c["eleves"]:
                        listEl.append([str(el["nom"]), str(el["prenom"])])

                        for mat in el["matieres"]:
                            arrMat = np.append(arrMat, str(mat["nom"]))

                            # print(arrMat)
        # print(["academies"][0])
        # print(listeMatieresUniques)
        self.ui.twNotes.setRowCount(len(listEl))
        self.ui.twNotes.clear()
        self.ui.twNotes.setColumnCount(3)

        arrMatieresUniques = np.unique(arrMat)
        self.ui.cbMatiere.addItems(arrMatieresUniques)


    # def ajoutAcademie (self):
    #     self.ui.cbAcademie.clear()
    #     self.ui.cbAcademie.addItems()
    #
    #
    # def ajoutEtablissement (self):
    #     self.ui.cbEtablissement.clear()
    #     self.ui.cbEtablissement.addItems()
    #
    # def ajoutClasse (self):
    #     self.ui.cbClasse.clear()
    #     self.ui.cbClasse.addItems()
    #
    # def ajouMatiere (self):
    #     self.ui.cbMatiere.clear()
    #     self.ui.cbMatiere.addItems()

        for cpt in range(len(listEl)):
            self.ui.twNotes.setItem(cpt, 0, QTableWidgetItem(str(listEl[cpt][0])))
            self.ui.twNotes.setItem(cpt, 1, QTableWidgetItem(str(listEl[cpt][1])))



            # self.ui.cbAcademie.currentIndexChanged.connect(self.afficherdico)




    # def updateAcademie(self):
    #     self.ui.cbAcademie.clear()
    #     maliste = []
    #     for a in self.dico["academies"]:
    #         maliste.append("Paris")
    #         self.ui.cbAcademie.addItems(a["nom"])
    #         self.ui.cbAcademie.addItems(maliste)

    def updateEtablissements (self):
        self.ui.cbEtablissement.clear()
        self.ui.cbEtablissement.addItem("Tous les etablissements")

        for e in dico["academies"][self.ui.cbAcademie.currentIndex()-1]["etablissements"]:
            self.ui.cbEtablissement.addItem(e["nom"])

    def updateClasses (self):
        self.ui.cbClasse.clear()
        self.ui.cbClasse.addItem("Toutes les classes")
        for c in dico["academies"][self.ui.cbAcademie.currentIndex()-1]["etablissements"][self.ui.cbEtablissement.currentIndex()]["classes"]:
            self.ui.cbClasse.addItem(c["nom"])
    #
    # def updateMatieres (self):
    #     dicoClasse = dico["academies"][self.ui.cbAcademie.currentIndex()]["etablissements"][self.ui.cbEtablissement.currentIndex()]["classes"][self.ui.cbClasse.currentIndex()]["matieres"]
    #     listeMatieres = []
    #     for eleve in dicoClasse["eleves"]:
    #         for matiere in eleve["matieres"]:
    #             listeMatieres.append(matiere["nom"])
    #     listeMatieresUniques = np.unique(listeMatieres)
    #     self.ui.cbMatiere.addItems(listeMatieresUniques)#addItems crée une liste
    #                                                     #addItem rajoute les elements un par un
    #
    # def updateSaisieEleve(self):
    #     listEl = []
    #     cpt = 0
    #     self.ui.twNotes.clear()
    #     self.ui.twNotes.setColumnCount(2)
    #     dicoClasse = self.dico["academies"][self.ui.cbAcademie.currentIndex()]["etablissements"][self.ui.cbEtablissement.currentIndex()] ["classes"][self.ui.cbClasse.currentIndex()]["matieres"][self.ui.cbMatiere.currentIndex()]
    #     for eleve in dicoClasse["eleves"]:
    #         for matiere in eleve ["matieres"]:
    #             mat = self.ui.cbMatiere.currentText()
    #             if matiere["nom"] == mat :
    #                 nomE = eleve["nom"]
    #                 self.ui.twNotes.setRowCount(cp+1)
    #                 spinB = QDoubleSpinBox()
    #                 spinB.setProperty("nom","nomE")
    #                 self.ui.twNotes.setCellWidget(cpt,1,spinB)
    #                 cpt=cpt+1
    #     self.ui.twNotes.setHorizontalHeaderLabels(['Nom','notes'])
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
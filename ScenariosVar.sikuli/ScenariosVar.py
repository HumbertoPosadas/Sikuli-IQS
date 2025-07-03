from sikuli import *
import shutil, time, datetime, socket, os, subprocess, sys

def pathFixer(path):
    newPath = path.replace("\\","/")
    return newPath

def stringFixer(originalString):
    return originalString.replace(" ", "_")

scenarios = {
        "EntreeApplication" : {
            "dossierClient" : "",
            "scenario" : "Entree Application",
            "raccourci" : pathFixer("C:/Sikuli/scenarios_Test/IQSEntreeApplication.sikuli/raccourci/raccourci.LNK"),
            "dossierResultats" : pathFixer("C:/Sikuli/scenarios_Test/IQSEntreeApplication.sikuli/reports"),
            "etapes" : ["Entree Application", "Entree Collaborateur"],
            },
        "TVA" : {
            "dossierClient" : "30409",
            "scenario" : "TVA",
            "raccourci" : pathFixer("C:/Sikuli/scenarios_Test/IQSTVA.sikuli/raccourci/raccourci.LNK"),
            "dossierResultats" : pathFixer("C:/Sikuli/scenarios_Test/IQSTVA.sikuli/reports"),
            "etapes" : [
                "Creation de la declaration TVA", 
                "Ouverture de la declaration TVA", 
                "Fermeture onglet TVA", 
                "Ouverture declaration TVA 2", 
                "Ouverture Journal TVA detaille", 
                "Ouverture synthese decla TVA", 
                "Ouverture synthese decla TVA 2", 
                "Ouverture cloture et teletransmission", 
                "Ouverture cloture et teletransmission 2"
                ],
            },
        "GrandLivreAnalytique" : {
            "dossierClient" : "30817",
            "scenario" : "Grand Livre Analytique",
            "raccourci" : pathFixer("C:/Sikuli/scenarios_Test/IQSGrandLivreAnalytique.sikuli/raccourci/raccourci.LNK"),
            "dossierResultats" : pathFixer("C:/Sikuli/scenarios_Test/IQSGrandLivreAnalytique.sikuli/reports"),
            "etapes" : [
                "Ouverture compte 6013", 
                "Ouverture compte 601103", 
                "Sauvegarde activite", 
                "Sauvegarde activites compte 6013", 
                "Filtre Regroupement"
                ],
            },
        "EnvoiEP" : {
            "dossierClient" : "1048",
            "scenario" : "EnvoiEP",
            "raccourci" : pathFixer("C:/Sikuli/scenarios_Test/IQSEnvoiEP.sikuli/raccourci/raccourci.LNK"),
            "dossierResultats" : pathFixer("C:/Sikuli/scenarios_Test/IQSEnvoiEP.sikuli/reports"),
            "etapes" : ["Selection dossier", "Envoi dossier"]
            },
        "OuvertureFenetres" : {
            "dossierClient" : "1048",
            "scenario" : "OuvertureFenetres",
            "raccourci" : pathFixer("C:/Sikuli/scenarios_Test/IQSOuvertureFenetres.sikuli/raccourci/raccourci.LNK"),
            "dossierResultats" : pathFixer("C:/Sikuli/scenarios_Test/IQSOuvertureFenetres.sikuli/reports"),
            "etapes" : [
                "Ouverture Fenetre Exercice", 
                "Ouverture Fenetre Exercice 2", 
                "Ouverture Saisie piece", 
                "Ouverture Saisie piece 2", 
                "Ouverture Grand Livre", 
                "Ouverture Grand Livre 2", 
                "Ouverture Balance", 
                "Ouverture Balance 2", 
                "Ouverture CodeTva", 
                "Ouverture CodeTva 2", 
                "Ouverture libelle auto", 
                "Ouverture libelle auto 2", 
                "Ouverture journaux", 
                "Ouverture journaux 2", 
                "Ouverture recherche", 
                "Ouverture recherche 2", 
                "Ouverture lettrage", 
                "Ouverture lettrage 2", 
                "Ouverture Intervalle de compte", 
                "Ouverture Intervalle de compte 2", 
                "Ouverture Analytique", 
                "Ouverture Analytique 2"
                ]
            },
        "ConsultationGrandLivreEtVirements" : {
            "dossierClient" : "30409",
            "scenario" : "Consultation Grand Livre et Virements",
            "dossierResultats" : pathFixer("C:/Sikuli/scenarios_Test/IQSConsultationGrandLivreEtVirements.sikuli/reports"),
            "etapes" : [
                "Virement 1 mouvement", 
                "Virement 100 Mouvements",
                "Virement 900 Mouvements",
                "Ouverture compte 2011",
                "Ouverture compte 511"
                ]
            },
        "RemonteeDossier" : {
            "dossierClient" : "30409",
            "scenario" : "Remontee Dossier",
            "dossierResultats" : pathFixer("C:/Sikuli/scenarios_Test/IQSRemonteeDossier.sikuli/reports"),
            "etapes" : [
                "RemonteeDossier", 
                "Entree dossier", 
                "Entree dossier 2"
            ]
            }
        }


















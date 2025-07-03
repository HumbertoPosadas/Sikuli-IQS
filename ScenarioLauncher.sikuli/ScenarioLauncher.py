from sikuli import *
import shutil, time, datetime, socket, os, subprocess, sys
import ScenariosVar
import LaunchEnv
import ToolboxEnv
import ExcelCreation



import IQSConsultationGrandLivreEtVirements
import IQSEnvoiEP
import IQSEntreeApplication
import IQSGrandLivreAnalytique
import IQSOuvertureFenetres
import IQSRemonteeDossier
import IQSTVA

rejouer = 5

IQSEntreeApplication.ScenarioEntreeApplication(rejouer)
IQSRemonteeDossier.ScenarioRemonteeDossier(rejouer)
IQSEnvoiEP.ScenarioEnvoiEP(rejouer)
IQSConsultationGrandLivreEtVirements.ScenarioConsultationGrandLivreEtVirements(rejouer) 
IQSGrandLivreAnalytique.ScenarioGrandLivreAnalytique(rejouer)
IQSOuvertureFenetres.ScenarioOuvertureFenetres(rejouer)
IQSTVA.ScenarioTVA(rejouer)
from sikuli import *
import shutil, time, datetime, socket, os, subprocess, sys

import LaunchEnv

def timestampNow():
    return int(time.time()*1000)  # Convertir les nanosecondes en millisecondes

def lancementCompta():
    os.system(LaunchEnv.lancementCompta)

def lancementComptaAuthentification(codeCollaborateur, password):
    arguments = [
            "/IP.AUTHENTICATION.DomainId=5526",
            "/IP.AUTHENTICATION.DataSetLabel=P:\\agiris\\" + LaunchEnv.millesime + "\\IsaGiwf\\CECAG.GI",
            "/IP.AUTHENTICATION.Login=" + codeCollaborateur,
            "/IP.AUTHENTICATION.Password=" + password
            ]

    print(LaunchEnv.lancementCompta + " " + " ".join(arguments))
    os.system(LaunchEnv.lancementCompta + " " + " ".join(arguments))

def lancementComptaAuthentificationDossier(codeCollaborateur, password, codeDossier):
    arguments = [
            "/IP.AUTHENTICATION.DomainId=5526",
            "/IP.AUTHENTICATION.DataSetLabel=P:\\agiris\\" + LaunchEnv.millesime + "\\IsaGiwf\\CECAG.GI",
            "/IP.AUTHENTICATION.Login=" + codeCollaborateur,
            "/IP.AUTHENTICATION.Password=" + password,
            "/CO.Entree.Dossier=" + codeDossier
            ]

    print(LaunchEnv.lancementCompta + " " + " ".join(arguments))
    os.system(LaunchEnv.lancementCompta + " " + " ".join(arguments))



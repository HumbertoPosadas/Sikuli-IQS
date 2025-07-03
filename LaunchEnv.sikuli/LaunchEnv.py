from sikuli import *
import shutil, time, datetime, socket, os, subprocess

def get_version(directory):
    files = os.listdir(directory) if os.path.exists(directory) else []
    if files:
        return os.path.splitext(files[0])[0]
    else:
        return "A remplir"

def get_patch(directory):
    files = os.listdir(directory) if os.path.exists(directory) else []
    if files:
        return os.path.splitext(files[0])[0]
    else:
        return ""

def get_full_version(version, patch):
    if len(patch) > 1:
        return version + " Patch " + patch
    else:
        return version

def versionMillesime(directory):
    files = os.listdir(directory) if os.path.exists(directory) else []
    if files:
        return os.path.splitext(files[0])[0]
    else:
        return ""

envDir = "C:\\ScenarioBuilder\\Env\\"
version = get_version(envDir + "\\Version\\")
patch = get_patch(envDir + "\\Patch\\")
versionCompta = get_full_version(version, patch)
millesime = versionMillesime(envDir + "\\Millesime\\")
pcName = "VM IQS CO"
lancementCompta = 'start C:\\agiris\\' + millesime +'\\Isacowp.gi\\Client\\CO.Application.exe'
application = "ISACOMPTA-CLIENT"
dateLancement = str(time.strftime("%d/%m/%Y %H:%M:%S"))
date = datetime.datetime.now().strftime("%d%m%Y%H%M")
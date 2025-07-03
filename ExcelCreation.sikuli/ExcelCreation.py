from sikuli import *
import shutil, time, datetime, socket, os, subprocess, sys
import ScenariosVar
import LaunchEnv
import ToolboxEnv as TbE


header = ["ID", "Application" , "Version", "ParamID", "id Machine", "Date de lancement" , "Scenario", "Num dossier",  "Num Iteration", "Etape", "Temps", "TopTemps", "EndTime", "AGarder?"]

timeArray = []
perfmonTable = []


def tempsEcouleEnMillisecondes(timestamp1, timestamp2):
    return (timestamp2 - timestamp1)

def addEtapeToTableau(e_start, e_end, etapeIndex, etapeIteration, scenario):
    global timeArray
    
    timeArray.append([
        str(TbE.dateNow() + str(etapeIteration + 1) + ScenariosVar.scenarios[scenario]["etapes"][etapeIndex]),  # ID, 0
        LaunchEnv.application,                             # Application, 1
        LaunchEnv.versionCompta,                           # Version, 2
        "N/A",                                             # ParamID, 3
        LaunchEnv.pcName,                                  # ID Machine, 4
        LaunchEnv.dateLancement,                           # Date de lancement, 5
        ScenariosVar.scenarios[scenario]["scenario"],           # Scenario, 6
        ScenariosVar.scenarios[scenario]["dossierClient"],      # Num dossier, 7
        str(etapeIteration + 1),                           # Num Iteration, 8
        ScenariosVar.scenarios[scenario]["etapes"][etapeIndex], # Etape, 9
        tempsEcouleEnMillisecondes(e_start, e_end), # Temps, 10
        e_start,                                           # TopTemps, 11
        e_end,                                             # EndTime, 12
        "1"                                                # AGarder?, 13
    ])


def addAllEtapesToTableau(times, i, scenario, completed):
    stepPlayed = 0
    for step, time in enumerate(times.values()):
        addEtapeToTableau(time[0], time[1], step, i, scenario)
        stepPlayed = stepPlayed + 1
    #remplit les etapes qui n auraient pas ete jouees et enleve le temps des valeurs a garder
    while (stepPlayed<len(ScenariosVar.scenarios[scenario]["etapes"])):
        addEtapeToTableau(0, 0, stepPlayed, i, scenario)
        #valeur A garder
        timeArray[stepPlayed][13] = 0
        stepPlayed = stepPlayed + 1
        
def ExcludeHigherAndSmallerFromTab(scenario):
    etapes = ScenariosVar.scenarios[scenario]["etapes"]
    for etape in etapes:
        etape_items = [item for item in timeArray if item[9] == etape]
        min_item = min(etape_items, key=lambda x: x[10])
        max_item = max(etape_items, key=lambda x: x[10])
        min_item[13] = 0
        max_item[13] = 0

def defineExcelName(excelDirectory, excelName):
    date = TbE.dateNow()
    fileName = ScenariosVar.pathFixer("C:/Sikuli/scenarios_Test/reports/{}/{}{}.csv".format(excelDirectory,excelName,date))
    return fileName

def timesFile():
    return defineExcelName("times", "Chrono-" + ScenariosVar.stringFixer(LaunchEnv.versionCompta))

def createCSVWithHeader(csvFile, headerArray):
    with open(csvFile, mode='w') as file:
        file.write(';'.join(headerArray) + '\n')

def writeLinesToCSVFile(csvFile, dataArray):
    with open(csvFile, mode='a') as file:
        for row in dataArray:
            file.write(';'.join(map(str,row)) + '\n')

timesFile = timesFile()
createCSVWithHeader(timesFile, header)

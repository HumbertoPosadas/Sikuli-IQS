from sikuli import *
import shutil, time, datetime, socket, os, subprocess, sys
import ScenariosVar
import LaunchEnv

#################Fonctions######################

def dateNow():
    return str(datetime.datetime.now().strftime("%d%m%Y%H%M%S"))

def deleteFilesInFolder(folderPath):
    if os.path.exists(folderPath) and os.path.isdir(folderPath):
        files = os.listdir(folderPath)
        if files:
            for file in files:
                file_path = os.path.join(folderPath, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)

def defineFileName(scenario) : 
    date = dateNow()
    fileName = "{}/{}{}.csv".format(ScenariosVar.scenarios[scenario]["dossierResultats"],scenario, date)
    return fileName 

def copyFile(scenario):
    copieDossier = 'xcopy P:\\DossierCO_ExecIQS\\S'+ScenariosVar.scenarios[scenario]["dossierClient"]+'.SVG C:\\agiris\\' + LaunchEnv.millesime +'\\IsaCowp.gi\\Maj_CECAG /Y'
    os.system(copieDossier)

def createPerformanceCollector(scenarioName):
    log_name = "Perf-" + ScenariosVar.stringFixer(scenarioName) + "-" +  ScenariosVar.stringFixer(LaunchEnv.versionCompta)
    csv_path = ScenariosVar.pathFixer("C:/Sikuli/scenarios_Test/reports/perfmon/") + log_name + ".csv"
    blg_path = ScenariosVar.pathFixer("C:/Sikuli/scenarios_Test/reports/perfmon/") + log_name + ".blg"

    logman_create = 'logman create counter {} -f csv -si 00:05 -o "{}" -c "\\Processor(_Total)\\% Processor Time" "\\Memory\\Available MBytes" "\\Processor(_Total)\\% Idle Time" "\\Process(CO.Application)\\% Processor Time" "\\PhysicalDisk(1 P:)\\Disk Reads/sec" "\\Process(CO.Application)\\Working Set" "\\PhysicalDisk(1 P:)\\Disk Writes/sec"'.format(log_name, csv_path)

    os.system(logman_create)
    print(logman_create)

    return log_name

def startPerformanceCollector(collectorName):
    os.system('logman start {}'.format(collectorName))

def stopPerformanceCollector(collectorName):
    os.system('logman stop {}'.format(collectorName))   

def deletePerformanceCollector(collectorName):
    os.system('logman delete {}'.format(collectorName))


###################### Test Fionctions #################
#copyFile("GrandLivreAnalytique")

#Imports librairies
from sikuli import *
import shutil, time, datetime, socket, os, subprocess
import LaunchEnv
import ScenariosVar
import ToolboxEnv as TbE
import ToolboxScenarios as TbS
import ExcelCreation as ExcelC

from collections import OrderedDict
###########################Variables##################################

copieDossier = 'xcopy P:\\DossierCO_ExecIQS\\S30817.SVG C:\\agiris\\' + LaunchEnv.millesime +'\\IsaCowp.gi\\Maj_CECAG /Y'

#process = subprocess.Popen(commande, shell=True)
##########################################################################################

    
############# Copie dossier sur MAJ ###########################

def ScenarioGrandLivreAnalytique(NbIterations):
    scenario = "GrandLivreAnalytique"
    collector = TbE.createPerformanceCollector(scenario)
    #fileName = TbE.defineFileName(scenario)
    #ExcelC.createCSVWithHeader(fileName, ExcelC.header)
    iteration=0
    while(iteration < NbIterations):
        completed = False
        times = OrderedDict()
        TbE.startPerformanceCollector(collector)
        TbE.copyFile(scenario)
        wait(5)    
        os.system(LaunchEnv.lancementCompta)
        if exists(Pattern("1728032042313-1.png").similar(0.92), 120):
            if exists(Pattern("1729578622104.png").similar(0.92),3):
                type("COMPT")
            click(Pattern("1728046051490.png").similar(0.92))
            if exists(Pattern("1728032296996-1.png").similar(0.89), 360):
                wait(5)
                type(Pattern("1728045780509.png").similar(0.94), "TOUS LES DOSSIERS" + Key.TAB)
                wait(2)
                type("30817" + Key.ENTER)
                wait(2)
                click(findAnyList([Pattern("1728046051490-1.png").similar(0.92), Pattern("1734950380031.png").similar(0.92)]))
                if exists (Pattern("1728378437354.png").similar(0.92),30):
                    click(Pattern("1728378476715.png").similar(0.92))
                    wait(5)
                click(Pattern("1728378663496.png").similar(0.92))
                wait(5)
                click(Pattern("1728378728945.png").similar(0.92))
                if exists(Pattern("1728378776548.png").similar(0.92),30):
                    type(Pattern("1728378807438.png").similar(0.92), "6013" + Key.ENTER)
                    e0s = TbS.timestampNow()
                    if exists(Pattern("1728378950246.png").similar(0.92),120):
                        e0e = TbS.timestampNow()
                        times['e0'] = [e0s, e0e]
                        wait(5)
                        type(Pattern("1728379419078.png").similar(0.92), "601103" + Key.TAB)
                        e1s = TbS.timestampNow()
                        if exists(Pattern("1728379542078.png").similar(0.92), 30):
                            e1e = TbS.timestampNow()
                            times['e1'] = [e1s, e1e]
                            wait(5)
                            type("41" + Key.ENTER)
                            type("41" + Key.ENTER)
                            type("41")
                            wait(5)
                            if exists(Pattern("1728381332649.png").similar(0.92),5):
                                type('s', KeyModifier.CTRL)
                                e2s = TbS.timestampNow()
                                if exists (Pattern("1728381721118.png").similar(0.92),10):
                                    e2e = TbS.timestampNow()
                                    times['e2'] = [e2s, e2e]
                                    wait(5)
                                    type(Pattern("1728381923264.png").similar(0.92), "6013" + Key.TAB)
                                    wait(5)
                                    type("42" + Key.ENTER)
                                    type("33" + Key.ENTER)
                                    for i in range(8):
                                        type(Key.DOWN)
                                    type("42" + Key.ENTER + Key.ENTER + "48")
                                    wait(5)
                                    if exists(Pattern("1728381332649.png").similar(0.92),5):
                                        type('s', KeyModifier.CTRL)
                                        e3s = TbS.timestampNow()
                                        if exists (Pattern("1728381721118.png").similar(0.92),10):
                                            e3e = TbS.timestampNow()
                                            times['e3'] = [e3s, e3e]
                                            wait(5)
                                            click(Pattern("1728383229888.png").similar(0.92))
                                            click(Pattern("1728383287519.png").similar(0.92))
                                            click(Pattern("1728383331850.png").similar(0.92))
                                            e4s = TbS.timestampNow()
                                            if exists (Pattern("1728383420899.png").similar(0.92), 30):
                                                e4e = TbS.timestampNow()
                                                times['e4'] = [e4s, e4e]
                                                wait(5)
        type(Key.F4, KeyModifier.ALT)
        if exists(Pattern("1728383913615.png").similar(0.92),30):
            click(Pattern("1728383973496.png").similar(0.92))
            wait(3)
            click(Pattern("1728383913615.png").similar(0.92))
            click(Pattern("1728383973496.png").similar(0.92))
        ExcelC.addAllEtapesToTableau(times, iteration, scenario, completed)
        iteration = iteration+1
        TbE.stopPerformanceCollector(collector)
        wait(60)
    ExcelC.ExcludeHigherAndSmallerFromTab(scenario)
    ExcelC.writeLinesToCSVFile(ExcelC.timesFile, ExcelC.timeArray)
    ExcelC.timeArray[:] = []
    TbE.deletePerformanceCollector(collector)
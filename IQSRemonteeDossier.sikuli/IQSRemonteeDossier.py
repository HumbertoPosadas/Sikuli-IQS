#Imports librairies
from sikuli import *
import shutil, time, datetime, socket, os, subprocess
import LaunchEnv
import ScenariosVar
import ToolboxEnv as TbE
import ToolboxScenarios as TbS
import ExcelCreation as ExcelC

from collections import OrderedDict

def ScenarioRemonteeDossier(NbIterations):
    scenario = "RemonteeDossier"
    collector = TbE.createPerformanceCollector(scenario)
    #fileName = TbE.defineFileName(scenario)
    #ExcelC.createCSVWithHeader(fileName, ExcelC.header)
    iteration = 0
    while(iteration<NbIterations):
        completed = False
        times = OrderedDict()
        TbE.startPerformanceCollector(collector)
        ############# Copie dossier sur MAJ ###########################
        TbE.copyFile(scenario)
        wait(5)
        os.system(LaunchEnv.lancementCompta)
        if exists(Pattern("1728032042313-1.png").similar(0.92), 120):
            click(Pattern("1731511193172.png").similar(0.92))
            e0s = TbS.timestampNow()
            if exists(Pattern("1728032296996-1.png").similar(0.89), 360):
                e0e = TbS.timestampNow()
                times['e0'] = [e0s, e0e]
                wait(5)
                type(Pattern("1728045780509.png").similar(0.94), "TOUS LES DOSSIERS" + Key.TAB)
                wait(2)
                type("30409" + Key.ENTER)
                wait(2)
                click(findAnyList([Pattern("1728046051490.png").similar(0.92), Pattern("1734950380031.png").similar(0.92)]))
                if exists(Pattern("1728046138376.png").similar(0.93), 10):
                    click(Pattern("1728046182219.png").similar(0.90))                
                if exists(Pattern("1733324633676.png").similar(0.92), 360):
                    wait(5)
                    type(Key.F4, KeyModifier.ALT)
                    wait(30)
                    os.system(LaunchEnv.lancementCompta)
                    if exists(Pattern("1728032042313-1.png").similar(0.92), 120):
                        click(Pattern("1731511193172.png").similar(0.92))
                        if exists(Pattern("1728045780509.png").similar(0.94), 120):
                            type(Pattern("1728045780509.png").similar(0.94), "TOUS LES DOSSIERS" + Key.TAB)
                            wait(2)
                            type("30409" + Key.ENTER)
                            wait(2)
                            click(findAnyList([Pattern("1728046051490.png").similar(0.92), Pattern("1734950380031.png").similar(0.92)])) 
                            if exists(Pattern("1728046138376.png").similar(0.93), 10):
                                click(Pattern("1728046182219.png").similar(0.90))
                                e1s = TbS.timestampNow()
                                if exists(Pattern("1733324633676.png").similar(0.92), 360):                        
                                    e1e = TbS.timestampNow()
                                    times['e1'] = [e1s, e1e]
                                    wait(5)
                                    type(Key.F4, KeyModifier.ALT)
                                    wait(30)
                                    os.system(LaunchEnv.lancementCompta)
                                    if exists(Pattern("1728032042313-1.png").similar(0.92), 120):
                                        click(Pattern("1731511193172.png").similar(0.92))
                                        if exists(Pattern("1728032296996-1.png").similar(0.89), 360):
                                            type(Pattern("1728045780509.png").similar(0.94), "TOUS LES DOSSIERS" + Key.TAB)
                                            wait(2)
                                            type("30409" + Key.ENTER)
                                            wait(2)
                                            click(findAnyList([Pattern("1728046051490.png").similar(0.92), Pattern("1734950380031.png").similar(0.92)]))
                                            if exists(Pattern("1728046138376.png").similar(0.93), 10):
                                                click(Pattern("1728046182219.png").similar(0.90))
                                                e2s = TbS.timestampNow()
                                                if exists(Pattern("1733324633676.png").similar(0.92), 360):
                                                    e2e = TbS.timestampNow()
                                                    times['e2'] = [e2s, e2e]
                                                    completed = True
        type(Key.F4, KeyModifier.ALT)
        ExcelC.addAllEtapesToTableau(times, iteration, scenario, completed)
        iteration = iteration+1
        TbE.stopPerformanceCollector(collector)
        wait(60)     
    ExcelC.ExcludeHigherAndSmallerFromTab(scenario)
    ExcelC.writeLinesToCSVFile(ExcelC.timesFile, ExcelC.timeArray)
    ExcelC.timeArray[:] = []
    TbE.deletePerformanceCollector(collector)
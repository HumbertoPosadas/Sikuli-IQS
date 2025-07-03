#Imports librairies
from sikuli import *
import shutil, time, datetime, socket, os, subprocess
import LaunchEnv
import ScenariosVar
import ToolboxEnv as TbE
import ToolboxScenarios as TbS
import ExcelCreation as ExcelC
from collections import OrderedDict

copieDossier = 'xcopy P:\\DossierCO_ExecIQS\\S30409.SVG C:\\agiris\\' + LaunchEnv.millesime +'\\IsaCowp.gi\\Maj_CECAG /Y'

def ScenarioConsultationGrandLivreEtVirements(NbIterations) : 
    scenario = "ConsultationGrandLivreEtVirements"
    collector = TbE.createPerformanceCollector(scenario)
    #fileName = TbE.defineFileName(scenario)
    #ExcelC.createCSVWithHeader(fileName, ExcelC.header)
    iteration = 0
    while (iteration < NbIterations):
        TbE.copyFile(scenario)
        wait(5)
        completed = False
        times = OrderedDict()
        TbE.startPerformanceCollector(collector)
        print(times)
        os.system(LaunchEnv.lancementCompta)
        if exists(Pattern("1728032042313-1.png").similar(0.92), 120):
            if exists(Pattern("1729578622104.png").similar(0.92),3):
                type("COMPT")
            click(Pattern("1730821467531.png").similar(0.92))
            if exists(Pattern("1728032296996-1.png").similar(0.89), 360):
                wait(5)
                type(Pattern("1728045780509.png").similar(0.94), "TOUS LES DOSSIERS" + Key.TAB)
                wait(2)
                type(ScenariosVar.scenarios["ConsultationGrandLivreEtVirements"]["dossierClient"] + Key.ENTER)
                click(findAnyList([Pattern("1730821467531.png").similar(0.92),Pattern("1748003880463.png").similar(0.92)]))
                if exists(Pattern("1730821513451.png").similar(0.93),60):
                    click(Pattern("1730821548648.png").similar(0.92))          
                #--------- Virement 1 mouvement ----------------
                if exists(Pattern("1730821818754.png").similar(0.92), 120):
                    wait(5)
                    click(Pattern("1730821818754.png").similar(0.92))
                    click(Pattern("1730821851760.png").similar(0.92))
                    if exists(Pattern("1730821911140.png").similar(0.92),30):
                        type(Pattern("1730821948803.png").similar(0.92), "7610000" + Key.ENTER)
                        wait(3)
                        click(Pattern("1730822125979.png").similar(0.92))
                        click(Pattern("1730822162894.png").similar(0.92))
                        if exists(Pattern("1730822211025.png").similar(0.92),30):
                            type(Pattern("1730822318070.png").similar(0.90), "401" + Key.ENTER)
                            click(Pattern("1730822416600.png").similar(0.92))
                            e0s = TbS.timestampNow()
                            if exists (Pattern("1734443830439.png").similar(0.92),360):
                                e0e = TbS.timestampNow()
                                times['e0'] = [e0s, e0e]
                                wait(3)
                                click(findAnyList([Pattern("1731493842257.png").similar(0.92), Pattern("1748326754159.png").similar(0.93)]))
                                if exists (Pattern("1732721717745.png").similar(0.92),120):  
                                    wait(3)
                                    #------------ Virement 100 mouvements --------------
                                    type(Pattern("1731494215663.png").similar(0.93), "45510000" + Key.ENTER)
                                    if exists(Pattern("1731494384332.png").similar(0.92), 30):
                                        click(Pattern("1731494437300.png").similar(0.92))
                                        if exists(Pattern("1731494483081.png").similar(0.92), 30):
                                            click(Pattern("1730822162894.png").similar(0.92))
                                            if exists(Pattern("1731494545973.png").similar(0.92), 30):
                                                type(Pattern("1730822318070.png").similar(0.90), "511" + Key.ENTER)
                                                click(Pattern("1730822416600.png").similar(0.92))
                                                e1s = TbS.timestampNow()
                                                if exists (Pattern("1734443830439.png").similar(0.92),360):
                                                    e1e = TbS.timestampNow() 
                                                    times['e1'] = [e1s, e1e]
                                                    wait(3)
                                                    click(Pattern("1734438581994.png").similar(0.93))
                                                    if exists(Pattern("1732721851511.png").similar(0.92),120):
                                                        wait(3)
                                                        #-------- Virement 900 mouvements ----------
                                                        type(Pattern("1731494927102.png").similar(0.92), "51250000" + Key.ENTER)
                                                        if exists (Pattern("1731495532826.png").similar(0.92),60):
                                                            click(Pattern("1731494437300.png").similar(0.92))
                                                            if exists (Pattern("1731495727783.png").similar(0.92), 60):
                                                                click(Pattern("1730822162894.png").similar(0.92))
                                                                type(Pattern("1730822318070.png").similar(0.90), "20110000" + Key.ENTER)
                                                                e2s = TbS.timestampNow()
                                                                if exists (Pattern("1734443830439.png").similar(0.92),360):
                                                                    e2e = TbS.timestampNow()
                                                                    times['e2'] = [e2s, e2e]     
                                                                    wait(10)
                                                                    click(Pattern("1734438581994.png").similar(0.93))
                                                                    if exists(Pattern("1732718287142.png").similar(0.92),120):                                                                           
                                                                        type(Key.F4, KeyModifier.ALT)
                                                                        wait(30)
                                                                        os.system(LaunchEnv.lancementCompta)
                                                                        if exists(Pattern("1728032042313-1.png").similar(0.92), 120):
                                                                            if exists(Pattern("1729578622104.png").similar(0.92),3):
                                                                                type("COMPT")
                                                                            click(Pattern("1730821467531.png").similar(0.92))
                                                                            if exists(Pattern("1728032296996-1.png").similar(0.89), 360):
                                                                                wait(5)
                                                                                type(Pattern("1728045780509.png").similar(0.94), "TOUS LES DOSSIERS" + Key.TAB)
                                                                                wait(2)
                                                                                type(ScenariosVar.scenarios["ConsultationGrandLivreEtVirements"]["dossierClient"] + Key.ENTER)
                                                                                click(Pattern("1730821467531.png").similar(0.92))
                                                                                if exists(Pattern("1730821513451.png").similar(0.93),60):
                                                                                    click(Pattern("1730821548648.png").similar(0.92))                                                                    
                                                                                    #-------- Ouverture Compte 2011 -----------
                                                                                    if exists(Pattern("1730821818754.png").similar(0.92), 120):
                                                                                        wait(5)
                                                                                        click(Pattern("1730821818754.png").similar(0.92))
                                                                                        click(Pattern("1730821851760.png").similar(0.92))
                                                                                        if exists(Pattern("1730821911140.png").similar(0.92),30):
                                                                                            type(Pattern("1730821948803.png").similar(0.92), "20110000" + Key.ENTER)
                                                                                            e3s = TbS.timestampNow()
                                                                                            if exists (Pattern("1731514420705.png").similar(0.92),60):
                                                                                                e3e = TbS.timestampNow()
                                                                                                times['e3'] = [e3s, e3e]
                                                                                                wait(3)
                                                                                                #----- Ouverture Compte 511 -------
                                                                                                type(Pattern("1731514663508.png").similar(0.92), "511" + Key.ENTER)
                                                                                                e4s = TbS.timestampNow()
                                                                                                if exists (Pattern("1731516612058.png").similar(0.92), 30):
                                                                                                    e4e = TbS.timestampNow()
                                                                                                    times['e4'] = [e4s, e4e]
                                                                                                    completed = True
                                                                                                    wait(5)
        type(Key.F4, KeyModifier.ALT)
        ExcelC.addAllEtapesToTableau(times, iteration, scenario, completed)
        iteration = iteration+1
        TbE.stopPerformanceCollector(collector)
        wait(60)
    ExcelC.ExcludeHigherAndSmallerFromTab(scenario)
    ExcelC.writeLinesToCSVFile(ExcelC.timesFile, ExcelC.timeArray)
    ExcelC.timeArray[:] = []  
    TbE.deletePerformanceCollector(collector)
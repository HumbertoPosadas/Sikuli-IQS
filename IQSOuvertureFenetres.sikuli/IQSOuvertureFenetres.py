#Imports librairies
from sikuli import *
import shutil, time, datetime, socket, os, subprocess
import LaunchEnv
import ScenariosVar
import ToolboxEnv as TbE
import ToolboxScenarios as TbS
import ExcelCreation as ExcelC
from collections import OrderedDict

copieDossier = 'xcopy P:\\DossierCO_ExecIQS\\S1048.SVG C:\\agiris\\' + LaunchEnv.millesime +'\\IsaCowp.gi\\Maj_CECAG /Y'

def ScenarioOuvertureFenetres(NbIterations): 
    scenario = "OuvertureFenetres"
    collector = TbE.createPerformanceCollector(scenario)
    #fileName = TbE.defineFileName(scenario)
    #ExcelC.createCSVWithHeader(fileName, ExcelC.header)
    iteration = 0
    while (iteration < NbIterations):
        completed = False
        times = OrderedDict()
        TbE.startPerformanceCollector(collector)
        os.system(LaunchEnv.lancementCompta)
        if exists(Pattern("1728032042313.png").similar(0.92),120):
            if exists(Pattern("1729578622104.png").similar(0.92),3):
                type("COMPT")
            click("1730198443952.png")   
            if exists (Pattern("1728032296996.png").similar(0.89), 360):
                wait(5)
                type(Pattern("1728045780509.png").similar(0.94), "TOUS LES DOSSIERS" + Key.TAB)
                wait(2)
                type("1048" + Key.ENTER)
                wait(2)
                click(findAnyList([Pattern("1728046051490.png").similar(0.92), Pattern("1734950380031.png").similar(0.92)]))
                if exists (Pattern("1730188545522.png").similar(0.92),120):
                    click(Pattern("1730188571601.png").similar(0.91))
                    wait(5)
                    #------------------------- Fenetre Exercice -------------------------
                click(Pattern("1730188684700.png").similar(0.92))
                e0s = TbS.timestampNow()
                if exists (Pattern("1730188762857.png").similar(0.92), 10):
                    e0e = TbS.timestampNow()
                    times['e0'] = [e0s, e0e]
                    type(Key.F4, KeyModifier.CTRL)
                    mouseMove(Region(971,77,173,52))
                    click(Pattern("1730188684700.png").similar(0.92))
                    e1s = TbS.timestampNow()
                    if exists (Pattern("1730188762857.png").similar(0.92), 10):
                        e1e = TbS.timestampNow()
                        times['e1'] = [e1s, e1e]
                        type(Key.F4, KeyModifier.CTRL)
                        wait(5)
                        #--------------------- Saisie Piece -------------------------
                        click(Pattern("1730191101867.png").similar(0.92))
                        click(Pattern("1730191145805.png").similar(0.92))
                        e2s = TbS.timestampNow()
                        if exists (Pattern("1730191322983.png").similar(0.92),10):
                            e2e = TbS.timestampNow()
                            times['e2'] = [e2s, e2e]
                            wait(5)
                            type(Key.F4, KeyModifier.CTRL)
                            mouseMove(Region(971,77,173,52))
                            wait(5)
                            click(Pattern("1730191145805.png").similar(0.92))
                            e3s = TbS.timestampNow()
                            if exists (Pattern("1730191322983.png").similar(0.92),10):
                                e3e = TbS.timestampNow()
                                times['e3'] = [e3s, e3e]
                                wait(5)
                                type(Key.F4, KeyModifier.CTRL)
                                wait(5)
                                #---------------------- Grand Livre -------------------------
                                click(Pattern("1730192548909.png").similar(0.92))
                                e4s = TbS.timestampNow()
                                if exists(Pattern("1730192640962.png").similar(0.92),30):
                                    e4e = TbS.timestampNow()
                                    times['e4'] = [e4s, e4e]
                                    mouseMove(Region(971,77,173,52))
                                    type(Key.F4, KeyModifier.CTRL)
                                    wait(5)
                                    click(Pattern("1730192548909.png").similar(0.92))
                                    e5s = TbS.timestampNow()
                                    if exists(Pattern("1730192640962.png").similar(0.92),30):
                                        e5e = TbS.timestampNow()
                                        times['e5'] = [e5s, e5e]
                                        wait(5)
                                        type(Key.F4, KeyModifier.CTRL)
                                        #------------------------- Balance -----------------------
                                        click(Pattern("1730192996626.png").similar(0.92))
                                        e6s = TbS.timestampNow()
                                        if exists(Pattern("1730193096171.png").similar(0.92),30):
                                            e6e = TbS.timestampNow()
                                            times['e6'] = [e6s, e6e]
                                            mouseMove(Region(971,77,173,52))
                                            type(Key.F4, KeyModifier.CTRL)
                                            wait(5)
                                            click(Pattern("1730192996626.png").similar(0.92))
                                            e7s = TbS.timestampNow()
                                            if exists(Pattern("1730193096171.png").similar(0.92),30):
                                                e7e = TbS.timestampNow()
                                                times['e7'] = [e7s, e7e]
                                                wait(5)
                                                type(Key.F3, KeyModifier.CTRL)
                                                wait(5)
                                                #-----------------------------CodeTva ----------------------------
                                                click(Pattern("1730193388212.png").similar(0.92))
                                                click(Pattern("1730193442562.png").similar(0.93))
                                                e8s = TbS.timestampNow()
                                                if exists (Pattern("1730193547627.png").similar(0.92),30):
                                                    e8e = TbS.timestampNow()
                                                    times['e8'] = [e8s, e8e]
                                                    wait(5)
                                                    type(Key.F4, KeyModifier.CTRL)
                                                    mouseMove(Region(971,77,173,52))
                                                    wait(5)
                                                    click(Pattern("1730193442562.png").similar(0.93))
                                                    e9s = TbS.timestampNow()
                                                    if exists (Pattern("1730193547627.png").similar(0.92),30):
                                                        e9e = TbS.timestampNow()
                                                        times['e9'] = [e9s, e9e]
                                                        wait(5)
                                                        type(Key.F4, KeyModifier.CTRL)
                                                        #----------------------- Libelle auto -------------------
                                                        click(Pattern("1730193778539.png").similar(0.92))
                                                        e10s = TbS.timestampNow()
                                                        if exists(Pattern("1730193831513.png").similar(0.92),30):
                                                            e10e = TbS.timestampNow()
                                                            times['e10'] = [e10s, e10e]
                                                            wait(5)
                                                            type(Key.F4, KeyModifier.CTRL)
                                                            mouseMove(Region(971,77,173,52))
                                                            wait(5)
                                                            click(Pattern("1730193778539.png").similar(0.92))
                                                            e11s = TbS.timestampNow()
                                                            if exists(Pattern("1730193831513.png").similar(0.92),30):
                                                                e11e = TbS.timestampNow()
                                                                times['e11'] = [e11s, e11e]
                                                                wait(5)
                                                                type(Key.F3, KeyModifier.CTRL)
                                                                wait(5)
                                                                #------------- Journaux -------------
                                                                click(Pattern("1730191101867.png").similar(0.92))
                                                                click(Pattern("1730194168863.png").similar(0.92))
                                                                e12s = TbS.timestampNow()
                                                                if exists (Pattern("1730194228284.png").similar(0.92),30):
                                                                    e12e = TbS.timestampNow()
                                                                    times['e12'] = [e12s, e12e]
                                                                    wait(5)
                                                                    type(Key.F4, KeyModifier.CTRL)
                                                                    mouseMove(Region(971,77,173,52))
                                                                    wait(5)
                                                                    click(Pattern("1730194168863.png").similar(0.92))
                                                                    e13s = TbS.timestampNow()
                                                                    if exists (Pattern("1730194228284.png").similar(0.92),30):
                                                                        e13e = TbS.timestampNow()
                                                                        times['e13'] = [e13s, e13e]
                                                                        wait(5)
                                                                        type(Key.F4, KeyModifier.CTRL)
                                                                        wait(5)
                                                                        #--------------- Recherche -----------------
                                                                        click(Pattern("1730194449160.png").similar(0.92))
                                                                        e14s = TbS.timestampNow()
                                                                        if exists (Pattern("1730194583590.png").similar(0.92),30):
                                                                            e14e = TbS.timestampNow()
                                                                            times['e14'] = [e14s, e14e]
                                                                            wait(5)
                                                                            type(Key.F4, KeyModifier.CTRL)
                                                                            mouseMove(Region(971,77,173,52))
                                                                            click(Pattern("1730194449160.png").similar(0.92))
                                                                            e15s = TbS.timestampNow()
                                                                            if exists (Pattern("1730194583590.png").similar(0.92),30):
                                                                                e15e = TbS.timestampNow()
                                                                                times['e15'] = [e15s, e15e]
                                                                                wait(5)
                                                                                type(Key.F4, KeyModifier.CTRL)
                                                                                wait(5)
                                                                                #------------- Lettrage --------------
                                                                                click(Pattern("1730194852892.png").similar(0.92))
                                                                                e16s = TbS.timestampNow()
                                                                                if exists(Pattern("1730194922962.png").similar(0.92),30):
                                                                                    e16e = TbS.timestampNow()
                                                                                    times['e16'] = [e16s, e16e]
                                                                                    wait(5)
                                                                                    type(Key.F4, KeyModifier.CTRL)
                                                                                    mouseMove(Region(971,77,173,52))
                                                                                    wait(5)
                                                                                    click(Pattern("1730194852892.png").similar(0.92))
                                                                                    e17s = TbS.timestampNow()
                                                                                    if exists(Pattern("1730194922962.png").similar(0.92),30):
                                                                                        e17e = TbS.timestampNow()
                                                                                        times['e17'] = [e17s, e17e]
                                                                                        wait(5)
                                                                                        type(Key.F3, KeyModifier.CTRL)
                                                                                        wait(5)
                                                                                        #-------------------- Intervalle Compte --------------------------
                                                                                        click(Pattern("1730197085232.png").similar(0.92))
                                                                                        click("1730197122052.png")
                                                                                        click(Pattern("1730197155745.png").similar(0.92))
                                                                                        click(Pattern("1730197210581.png").similar(0.92))
                                                                                        if exists("1730197319992.png",5):
                                                                                            click("1730197319992.png")
                                                                                            click(Pattern("1730197344279.png").similar(0.92))
                                                                                        else:
                                                                                            click("1732886085163.png")
                                                                                        
                                                                                        e18s = TbS.timestampNow()
                                                                                        if exists(Pattern("1730197403555.png").similar(0.92),30):
                                                                                            e18e = TbS.timestampNow()
                                                                                            times['e18'] = [e18s, e18e]
                                                                                            wait(5)
                                                                                            type(Key.F4, KeyModifier.CTRL)
                                                                                            wait(5)
                                                                                            if exists("1730197319992.png",5):
                                                                                                click("1730197319992.png")
                                                                                                click(Pattern("1730197344279.png").similar(0.92))
                                                                                            else:
                                                                                                click("1732886085163.png")
                                                                                            e19s = TbS.timestampNow()
                                                                                            if exists(Pattern("1730197403555.png").similar(0.92),30):
                                                                                                e19e = TbS.timestampNow()
                                                                                                times['e19'] = [e19s, e19e]
                                                                                                wait(5)
                                                                                                type(Key.F3, KeyModifier.CTRL)
                                                                                                wait(5)
                                                                                                #--------------- Ouverture GL Analytique ---------
                                                                                                click(Pattern("1730197765131.png").similar(0.92))
                                                                                                click(Pattern("1730197838775.png").similar(0.92))
                                                                                                e20s = TbS.timestampNow()
                                                                                                if exists (Pattern("1730197942499.png").similar(0.92),30):
                                                                                                    e20e = TbS.timestampNow()
                                                                                                    times['e20'] = [e20s, e20e]
                                                                                                    wait(5)
                                                                                                    type(Key.F4, KeyModifier.CTRL)
                                                                                                    mouseMove(Region(971,77,173,52))
                                                                                                    wait(5)
                                                                                                    click(Pattern("1730197838775.png").similar(0.92))
                                                                                                    e21s = TbS.timestampNow()
                                                                                                    if exists (Pattern("1730197942499.png").similar(0.92),30):
                                                                                                        e21e = TbS.timestampNow()
                                                                                                        times['e21'] = [e21s, e21e]
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

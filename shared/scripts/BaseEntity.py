#!/usr/bin/env python
# -*- coding: utf-8 -*-
import __builtin__
source(findFile("scripts", "Logger.py"))
class BaseEntity(__builtin__.object):

    
    isLogged = False
    screenIndex = 0
    logger = Logger.getInstance()

    def __init__(self):
        source(findFile("scripts", "CommonFunctions.py"))
        source(findFile("testdata", "TestImport.tsv"))
        source(findFile("testdata", "TestExport.tsv"))
        source(findFile("scripts", "Logger.py"))
        source(findFile("scripts", "MainForm.py"))
        source(findFile("scripts", "textbox.py"))
        source(findFile("scripts", "MenuItem.py"))
        source(findFile("scripts", "Button.py"))
        source(findFile("scripts", "Combobox.py"))
        source(findFile("scripts", "WorkspaceForm.py"))
        source(findFile("scripts", "SaveProjectForm.py"))
        self.ctx = BaseEntity.getApplicationContext()

    def step(self, message):
        self.logger.step(message)

    def formatLogMsg(self, message):
        pass

    def debug(self, message):
        self.logger.debug(String.format("[%1$s] %2$s", self, self.formatLogMsg(message)))

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.makeScreen()
        self.logger.error(message)

    def fatal(self, message):
        self.makeScreen()
        self.logger.fatal(message)
            
    def assertIsPresent(self,wildcard,name="Элемент"):
        obj = wildcard
        if (not object.exists(obj)):
            snooze(5)
        if (not object.exists(obj)):
            self.fatal("%s не найден!"%name)
    
    def verifyIsPresent(self,wildcard):
        obj = wildcard
        if (not object.exists(obj)):
            snooze(5)
        test.verify(object.exists(obj),"Проверка существования объекта [%s]"% wildcard)
        if (not object.exists(obj)):
            self.makeScreen()

    @classmethod
    def getApplicationContext(cls):
        if (not currentApplicationContext().isRunning):    
            startApplication("astudio")
    
    def quitApp(self):
        MainForm().menuNavigate("File>Exit")

    def makeScreen(self):
        saveDesktopScreenshot(CommonFunctions.getCurrentFolder() + "\\result\\screen_%s.png"% CommonFunctions.getTimeStamp())

source(findFile("scripts", "BaseTest.py"))

class WorkspaceLoadUnloadScan(BaseTest):
    
    def runTest(self):
        self.logger.logTestName("Раздел: Edit Функция: Remove scans")  
           
        self.step(1)
        #импорт модели 
        mainForm = MainForm()     
        mainForm.importObj((CommonFunctions.getCurrentFolder()+testData.field(testData.dataset("TestImport.tsv")[0],"path")).replace("\\\\","\\"))
        #TODO: Screenshot verification point # 1 (Shared)

        self.step(2)
        #File>Save Project
        mainForm.menuNavigate("File>Save Project")
        saveProject = SaveProjectForm()
        pathP = CommonFunctions.getCurrentFolder()+"\\result\\projects\\"
        nameP = CommonFunctions.getTimeStamp()
        saveProject.fillDataAndSave(nameP,pathP)
        snooze(2)
        mainForm.verifyLastLogs("Project saved in %(path)s%(name)s\\\\%(name)s.sproj"%{"path":pathP.replace("\\","\\\\"), "name":nameP})

        self.step(3)
        #выбор Unload scans
        mainForm.menuNavigate("Window>Workspace",False)
        workspace = WorkspaceForm()
        workspace.performContextMenuItemAction("Unload scans")
        snooze(2)
        #TODO: Screenshot of main window verification point # 2
        
        self.step(4)
        #выбор Load scans
        workspace.performContextMenuItemAction("Load scans")
        snooze(2)
        #TODO: Screenshot verification point # 1 (Shared)
        
def main():
    WorkspaceLoadUnloadScan().runTest()


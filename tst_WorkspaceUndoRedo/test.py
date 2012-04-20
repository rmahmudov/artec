source(findFile("scripts", "BaseTest.py"))

class WorkspaceUndoRedo(BaseTest):
    
    def runTest(self):
        self.logger.logTestName("Раздел: Edit Функция: Remove scans")  
           
        self.step(1)
        #импорт модели 
        mainForm = MainForm()     
        mainForm.importObj((CommonFunctions.getCurrentFolder()+testData.field(testData.dataset("TestImport.tsv")[0],"path")).replace("\\\\","\\"))
        #TODO: Screenshot verification point # 1 (Shared)

        self.step(2)
        #выбор скана в воркспейсе
        mainForm.menuNavigate("Window>Workspace",False)
        workspace = WorkspaceForm()
        workspace.select()
        
        self.step(3)
        #Edit>Remove scans
        mainForm.menuNavigate("Edit>Remove scans")
        snooze(2)
        #TODO: Screenshot of workspace panel verification point # 2
        
        self.step(4)
        #Edit>Undo
        mainForm.menuNavigate("Edit>Undo")
        snooze(2)
        #TODO: Screenshot of workspace panel verification point # 3
        mainForm.verifyLastLogs("Command \[Remove 1 scans\] undone")
        
        self.step(5)
        #Edit>Redo
        mainForm.menuNavigate("Edit>Redo")
        snooze(2)
        #TODO: Screenshot of workspace panel verification point # 4
        mainForm.verifyLastLogs("Command \[Remove 1 scans\] redone")
        
        
def main():
    WorkspaceUndoRedo().runTest()


source(findFile("scripts", "BaseTest.py"))

class Turn3DRenderingOnOff(BaseTest):
    
    def runTest(self):
        self.logger.logTestName("Раздел: View Функция: Turn 3D rendering on/off")     
        
        self.step(1) 
        mainForm = MainForm()     
        mainForm.importObj((CommonFunctions.getCurrentFolder()+testData.field(testData.dataset("TestImport.tsv")[0],"path")).replace("\\\\","\\"))
        snooze(2)
        #TODO: Screenshot verification point # 1 (Shared)
        test.vp("VP1")
        
        self.step(2)
        mainForm.menuNavigate("View>Turn 3D rendering on/off")
        snooze(2)
        #TODO: Screenshot verification point # 2
        test.vp("VP2")

        self.step(3)
        mainForm.menuNavigate("View>Turn 3D rendering on/off")
        snooze(2)
        #TODO: Screenshot verification point # 1 (Shared)
        test.vp("VP1")
        
def main():
    Turn3DRenderingOnOff().runTest()
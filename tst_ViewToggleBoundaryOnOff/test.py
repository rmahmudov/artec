source(findFile("scripts", "BaseTest.py"))

class ViewToggleBoundaryOnOff(BaseTest):
    
    def runTest(self):
        self.logger.logTestName("Раздел: View Функция: Toggle boundary on/off")     
        
        self.step(1) 
        mainForm = MainForm()     
        mainForm.importObj((CommonFunctions.getCurrentFolder()+testData.field(testData.dataset("TestImport.tsv")[0],"path")).replace("\\\\","\\"))
        snooze(2)
        #TODO: Screenshot verification point # 1 (Shared)
        test.vp("VPmain")
        
        self.step(2)
        mainForm.menuNavigate("View>Toggle boundary on/off")
        snooze(2)
        #TODO: Screenshot verification point # 2
        test.vp("VPmain2")
        #TODO: заменить на приемлемый скриншот
        
        self.step(3)
        mainForm.menuNavigate("View>Toggle boundary on/off")
        snooze(2)
        #TODO: Screenshot verification point # 1 (Shared)
        test.vp("VPmain3")
        #TODO: заменить на приемлемый скриншот
        
def main():
    ViewToggleBoundaryOnOff().runTest()
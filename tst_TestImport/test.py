source(findFile("scripts", "BaseTest.py"))

class TestImport(BaseTest):
    
    def runTest(self):
        self.logger.logTestName("Раздел: File Функция: Import...")
        n = 1     
        for record in testData.dataset("TestImport.tsv"):
            self.step(n) 
            mainForm = MainForm()
            mainForm.importObj((CommonFunctions.getCurrentFolder()+testData.field(record,"path")).replace("\\\\","\\"))
            n = n+1

def main():
    TestImport().runTest()
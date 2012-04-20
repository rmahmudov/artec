source(findFile("scripts", "BaseTest.py"))

class TestExportScan(BaseTest):
    
    def runTest(self):
        self.logger.logTestName("Раздел: File Функция: Export scans")
        n = 1     
        for record in testData.dataset("TestExport.tsv"):
            self.step(n) 
            mainForm = MainForm()
            mainForm.importObj((CommonFunctions.getCurrentFolder()+testData.field(record,"import")).replace("\\\\","\\"))
            test.vp(testData.field(record,"import").split('\\').pop())
            n = n+1
            self.step(n)
            mainForm.exportScan((CommonFunctions.getCurrentFolder()+testData.field(record,"export")).replace("\\\\","\\"))
            n = n+1 
            self.quitApp()
def main():
    TestExportScan().runTest()
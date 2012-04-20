source(findFile("scripts", "BaseForm.py"))

class MainForm(BaseForm):

    #Элементы главного окна
    strWindow = "container=':Artec Studio_Window'"
    strImportWindow = "container~='.*import_Dialog.*'"
    strConsoleAppOK = "{%s type='Edit' text~='.*Application started.*'}"% strWindow
    mainmenuBar = "{text='%s' type='MenuItem'}"
    
    #Элементы Окна Импорта
    btnImportOpen = "{%s text='Open' type='Button'}"% strImportWindow

    def __init__(self):
        super(MainForm, self).__init__(self.strConsoleAppOK,"Главная форма")
        self.txtConsole = Textbox("{text~='Application started' type='Edit'}","Консоль")
        self.txtStrConsole = "{text~='%s' type='Edit'}"
    
    def importObj(self,pathToFile):
        self.menuNavigate("File>Import...")
        Textbox("{%s type='Edit'}"% self.strImportWindow,"Путь к файлу").type(pathToFile)
        Button(self.btnImportOpen,"Выбрать").click()
        snooze(5)
        self.verifyLastLogs("1 scans were successfully imported")
        
    def exportScan(self,pathToFileExport):
        self.menuNavigate("File>Export scans...")
        Textbox("{container=':Export scans_Dialog' type='Edit'}","Путь к файлу").type(pathToFileExport)
        Combobox(":Export scans_ComboBox","Scan export format").select("scan")
        Button("{container=':Export scans_Dialog' text='OK' type='Button'}","OK").click()
        snooze(5)
        self.verifyLastLogs("1 scans were successfully exported")  
    
    def menuNavigate(self,path,clickIfAllreadyChecked = True):
        words = str(path).split(">")
        MenuItem("{container~='_MenuBar' text='%s' type='MenuItem'}"%words[0],words[0]).click()
        item = MenuItem("{container~='%(first)s_MenuItem' text='%(second)s' type='MenuItem'}"% {"first":words[0],"second":words[1]}, words[1])
        if (clickIfAllreadyChecked): 
            item.click()
        else:
            if (item.obj.checked==0):
                item.click()
        snooze(1);
        
    def verifyLastLogs(self,line):
        exists = CommonFunctions.regexpMatch(line+"\s$",(waitForObject(self.txtStrConsole%line.split('\\')[0])).text)
        test.verify(not exists is None, "Проверка появления в логах надписи [%s]"%line)   

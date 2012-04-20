source(findFile("scripts", "BaseForm.py"))

class SaveProjectForm(BaseForm):

    def __init__(self):
        super(SaveProjectForm, self).__init__(":Select place where project will be saved_Dialog","Окно сохранения проекта")
    
    def fillDataAndSave(self,name=CommonFunctions.getTimeStamp(),path=CommonFunctions.getCurrentFolder()+"\\result\\projects\\"):
        Textbox(":Select place where project will be saved.Name:_Edit","Имя проекта").type(name)
        Textbox(":Select place where project will be saved.Location:_Edit","Путь к проекту").type(path)
        Button(":Select place where project will be saved.Save_Button","Сохранить").click()
        
source(findFile("scripts", "BaseElement.py"))

class Textbox(BaseElement):

    elemName = "Текстовое поле"

    def __init__(self,loc,n):
        super(Textbox, self).__init__(loc,n)
        try:
            self.obj = waitForObject(self.locator)
        except:
            self.assertIsPresent(self.locator)

    def type(self,value):
        self.clear()
        self.info(self.name +" > " + " вводим '" + str(value) + "'")
        type(self.obj, str(value))
    
    def clear(self):
        while str(self.obj.text).__len__() > 0:           
            type(self.obj, "<Delete>")

source(findFile("scripts", "BaseElement.py"))

class Combobox(BaseElement):

    elemName = "Комбобокс"

    def __init__(self,loc,n):
        super(Combobox, self).__init__(loc,n)
        try:
            self.obj = waitForObject(self.locator)
        except:
            self.assertIsPresent(self.locator) 
    
    def select(self,value):
        self.logger.info(self.name +" > " + " выбираем значение '%s'"%value)
        snooze(1)
        expand(self.obj)
        snooze(1)
        mouseClick(waitForObjectItem(self.locator, value))
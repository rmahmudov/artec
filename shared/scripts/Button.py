source(findFile("scripts", "BaseElement.py"))

class Button(BaseElement):
    
    elemName = "Кнопка"

    def __init__(self,loc,n):
        super(Button, self).__init__(loc,n)
        try:
            self.obj = waitForObject(self.locator)
        except:
            self.assertIsPresent(self.locator)
  
    def click(self):
        self.info(self.name +" > " + " нажимаем")
        clickButton(self.obj)
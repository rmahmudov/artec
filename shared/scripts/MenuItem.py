source(findFile("scripts", "BaseElement.py"))

class MenuItem(BaseElement): 

    elemName = "Пункт меню"

    def __init__(self,loc,n):
        super(MenuItem, self).__init__(loc,n)
        try:
            self.obj = waitForObject(self.locator)
        except:
            self.assertIsPresent(self.locator,n)
  
    def click(self):
        self.info(self.name +" > " + " нажимаем")
        mouseClick(self.obj)
import itertools
source(findFile("scripts", "BaseEntity.py"))

class BaseElement(BaseEntity):
    name = None
    locator = None
    obj = None
    elemName = "Элемент"  

    def __init__(self,loc,n):
        source(findFile("scripts", "Logger.py"))
        source(findFile("scripts", "CommonFunctions.py"))
        self.name = self.getName()+" '%s'"% n
        self.locator = loc
     
    def getName(self):
        return self.elemName
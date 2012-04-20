source(findFile("scripts", "BaseEntity.py"))

class BaseForm(BaseEntity):

    def __init__(self,locator,name):
        self.locator = locator
        self.name = name
        try:
            self.obj = waitForObject(locator, CommonFunctions.getTimeOut())
        except:
            self.assertIsPresent(self.locator,name)

    def formatLogMsg(self, message):
        return message
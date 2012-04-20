source(findFile("scripts", "BaseEntity.py"))

class BaseTest(BaseEntity):    

    def xTest(self):
        try:
            logger.logTestName(self)
            self.runTest()
            logger.logTestEnd(self)
        except (Throwable, ), e:
            logger.warn("loc.test.failed")
            raise e

    def after(self):
        pass

    def formatLogMsg(self, message):
        return message


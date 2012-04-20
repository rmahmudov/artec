class Logger:

    instance = None
    LOG_DELIMITER = "::"
    logSteps = True

    def __init__(self):
        pass

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = Logger()
        return cls.instance

    def step(self, step):
        self.logDelimMsg("Шаг № " + str(step))

    def step_0(self, fromStep, toStep):
        self.logDelimMsg("loc.logger.steps" + str(fromStep) + "-" + str(toStep))

    def logDelimMsg(self, msg):
            self.info(msg)

    def logTestName(self, testName):
        if self.logSteps:
            formattedName = "=====================  %(tst)s: '%(name)s' ====================="% {"tst":"ТЕСТ-СЦЕНАРИЙ","name": testName}
            delims = ""
            nChars = len(formattedName)
            ## for-while
            i = 0
            while i < nChars:
                delims += "-"
                i += 1
            self.info(delims)
            self.info(formattedName)
            self.info(delims)

    def printDots(self, count):
        delims = ""
        ## for-while
        i = 0
        while i < count:
            delims += "."
            i += 1
        self.info(delims)

    def logTestEnd(self, testName):
        if self.logSteps:
            self.info("")
            formattedEnd = String.format("***** %1$s: '%2$s' %3$s! *****", "loc.logger.test.case", testName, "loc.logger.test.passed")
            stars = ""
            nChars = len(formattedEnd)
            ## for-while
            i = 0
            while i < nChars:
                stars += "*"
                i += 1
            self.info(stars)
            self.info(formattedEnd)
            self.info(stars)
            self.info("")

    def logPrereqName(self, testName):
        if self.logSteps:
            self.info(String.format("=====================  %1$s: '%2$s' =====================", "loc.logger.test.prerequisite.case", testName))
            self.info("----------------------------------------------------------------------------------------------------")
            self.logDelimMsg("Preconditions")

    def logPrereq(self, testName):
        if self.logSteps:
            self.info("----------------------------------------------------------------------------------------------------")
            self.info(String.format("=====================  %1$s: '%2$s' =====================", "loc.logger.test.prerequisite.case.creating", testName))
            self.info("----------------------------------------------------------------------------------------------------")

    def logPrereqEnd(self, testName):
        if self.logSteps:
            self.info(String.format("===================== %1$s: '%2$s' =====================", "loc.logger.test.prerequisite.case.succes", testName))
            self.info("----------------------------------------------------------------------------------------------------")

    def debug(self, message):
        pass

    def info(self, message):
        msg = "INFO: " + str(message)
        print msg
        test.log(msg)

    def warn(self, message):
        msg = "WARN: " + str(message)
        print msg
        test.log(msg)

    def error(self, message):
        msg = "ERROR: " + str(message)
        print msg
        test.error(msg)

    def fatal(self, message):
        msg = "FATAL: " + str(message)
        print msg
        test.fatal(msg)
        



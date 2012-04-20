#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import re

class CommonFunctions:

    def __init__(self):
        pass
        
    @classmethod
    def getTimeOut(self):
        return 10000
    
    @classmethod    
    def getCurrentFolder(self):
        return os.path.dirname(os.getcwd())
    
    @classmethod
    def regexpMatch(self,str1,str2):
        return re.search(str1,str2)
    
    @classmethod
    def getTimeStamp(cls):
        return str(datetime.datetime.now()).replace(':','_')   
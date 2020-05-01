from configparser import SafeConfigParser
import logging
import os

class ConfigParserSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(ConfigParserSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ConfigParser(metaclass = ConfigParserSingleton):
    pass

    def __init__(self):		
        self.config = SafeConfigParser()
        #self.data = 1
        #self.config.read(filename)	

    def getConfigParser(self, filename):
        #self.data = self.data +1
        #print(self.data)
        self.config.read('{0}{1}'.format(os.getcwd(),filename))
        return self.config

class LoggerSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(LoggerSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass = LoggerSingleton):
    pass

 
    def getLogger(self, moduleName):
        self.logger = logging.getLogger(moduleName)
        self.logger.setLevel(logging.INFO)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        fh = logging.FileHandler('applog.log')
        fh.setLevel(logging.INFO)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # add ch to logger
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

        return self.logger


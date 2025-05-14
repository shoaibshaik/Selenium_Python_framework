import configparser
class ReadConfig:
    config = configparser.RawConfigParser()
    config.read('.\\Configurations\\config.ini')

    @staticmethod
    def getApplicationUrl():
        return ReadConfig.config.get('common info', 'baseURL')

    @staticmethod
    def getUserName():
        return ReadConfig.config.get('common info', 'user_email')

    @staticmethod
    def getPassword():
        return ReadConfig.config.get('common info', 'password')

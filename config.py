import configparser
import os


class Config:
    __config = None

    @staticmethod
    def __instance():
        if Config.__config is None:
            Config.__config = configparser.ConfigParser()
            Config.__config.read('config.ini')

    @staticmethod
    def get_prop(key):
        Config.__instance()

        if key.find('.') != -1:
            arr = key.split('.')
            result = None
            for k in arr:
                if result is None:
                    result = Config.__config[k]
                else:
                    result = result[k]
            return result
        else:
            return Config.__config[key]

    @staticmethod
    def get_jdbc_url():
        return Config.get_prop('jdbc.url')

    @staticmethod
    def get_database():
        url = Config.get_jdbc_url()
        return url[url.rfind('/') + 1:]

    @staticmethod
    def get_host():
        url = Config.get_jdbc_url()
        return url[url.find('//') + 2:url.rfind(':')]

    @staticmethod
    def get_port():
        url = Config.get_jdbc_url()
        return url[url.rfind(':') + 1:url.rfind('/')]

    @staticmethod
    def chage_to_path(string):
        return string.replace('.', os.sep)

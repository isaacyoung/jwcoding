import configparser
import os


class Config:
    _config = None

    @staticmethod
    def _instance():
        if Config._config is None:
            Config._config = configparser.ConfigParser()
            Config._config.read('config.ini')

    @staticmethod
    def get_prop(key):
        Config._instance()

        if key.find('.') != -1:
            arr = key.split('.')
            result = None
            for k in arr:
                if result is None:
                    result = Config._config[k]
                else:
                    result = result[k]
            return result
        else:
            return Config._config[key]

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

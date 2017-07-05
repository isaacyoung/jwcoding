import configparser


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

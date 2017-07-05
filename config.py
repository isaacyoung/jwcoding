import configparser

config = configparser.ConfigParser()
config.read('config.ini')

jdbc = config['jdbc']
print(jdbc['url'])

import configparser


class SessionConfig(configparser.ConfigParser):
    def __init__(self, config_name):
        configparser.ConfigParser.__init__(self)
        self.config_name = config_name

    def read_config(self):
        self.read(self.config_name)
        return self['EXPORT']['EXPORT_PATH']

    def write_config(self, config_path):
        self.config_path = config_path
        self['EXPORT']['EXPORT_PATH'] = self.config_path
        with open(self.config_name, 'w') as self.configfile:
            self.write(self.configfile)

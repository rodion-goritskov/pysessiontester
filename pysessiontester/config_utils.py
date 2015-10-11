import configparser
import os.path


class SessionConfig(configparser.ConfigParser):
    def __init__(self, config_name):
        configparser.ConfigParser.__init__(self)
        self.config_name = config_name

    def read_config(self):
        if (os.path.isfile(self.config_name) is False):
            self['EXPORT'] = {}
            self['EXPORT']['EXPORT_PATH'] = '~/'
            with open(self.config_name, 'w') as self.configfile:
                self.write(self.configfile)
        self.read(self.config_name)
        return self['EXPORT']['EXPORT_PATH']

    def write_config(self, config_path):
        self.config_path = config_path
        self['EXPORT']['EXPORT_PATH'] = self.config_path
        with open(self.config_name, 'w') as self.configfile:
            self.write(self.configfile)

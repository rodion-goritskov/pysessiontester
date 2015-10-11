import configparser
import os
import getpass


class SessionConfig(configparser.ConfigParser):
    def __init__(self, config_name):
        configparser.ConfigParser.__init__(self)
        self.config_name = config_name
        if (os.path.isfile(self.config_name) is False):
            default_folder = os.path.join(os.path.expanduser('~'), 'pysessiontester','')
            if (os.path.isdir(default_folder) is False):
                os.mkdir(default_folder)
            self['EXPORT'] = {}
            self['EXPORT']['EXPORT_PATH'] = default_folder
            with open(self.config_name, 'w') as self.configfile:
                self.write(self.configfile)

    def read_config(self):
        self.read(self.config_name)
        return self['EXPORT']['EXPORT_PATH']

    def write_config(self, config_path):
        self.config_path = config_path
        self['EXPORT']['EXPORT_PATH'] = self.config_path
        with open(self.config_name, 'w') as self.configfile:
            self.write(self.configfile)

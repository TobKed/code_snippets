from tkinter import filedialog
from tkinter import *
import os
import os.path
import configparser

root = Tk()

config_file_name = "/config.ini"
config_file_path = os.getcwd() + config_file_name
config = configparser.ConfigParser()


def open_filedialog():
    last_dir = get_opt_from_cfg(cfg_path=config_file_path, section="DEFAULT", option="last directory")
    if last_dir:
        init_dir = last_dir
    else:
        init_dir = os.getcwd()
    root.filename = filedialog.askopenfilename(initialdir=init_dir, title="Select file",
                                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    save_opt_to_cfg(cfg_path=config_file_path, section="DEFAULT", option="last directory",
                    value=os.path.dirname(root.filename))


def get_opt_from_cfg(cfg_path, section, option):
    if os.path.isfile(cfg_path):
        print("{} exists".format(cfg_path))
        with open(cfg_path) as f:
            config.read_file(f)
            if config.has_option(section, option):
                print("'{}' in option '{}' from section '{}' retrieved from '{}'".format(config.get(section, option),
                                                                                 option, section, cfg_path))
                return config.get(section, option)
            else:
                print("option '{}' in section '{}' doesn't exist".format(option, section))
                return None
    else:
        print("'{}' doesn't exist".format(config_file_path))
        return None


def save_opt_to_cfg(cfg_path, section, option, value):
    config.set(section, option, value)
    with open(cfg_path, 'w') as f:
        config.write(f)
        print("'{}' in option '{}' from section '{}' saved to '{}'".format(value, option, section, cfg_path))


if __name__ == "__main__":
    open_filedialog()

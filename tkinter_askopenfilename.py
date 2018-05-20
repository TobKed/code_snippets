from tkinter import filedialog
from tkinter import *
import os
import configparser
import os.path

root = Tk()

config_file_name = "/config.ini"
config_file_path = os.getcwd() + config_file_name
config = configparser.ConfigParser()


def open_filedialog():
    init_dir = get_path_from_cfg()
    root.filename = filedialog.askopenfilename(initialdir=init_dir, title="Select file",
                                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    print(root.filename)
    save_path_to_cfg(os.path.dirname(root.filename))


def get_path_from_cfg():
    if os.path.isfile(config_file_path):
        print("config.ini exists")
        with open(config_file_path) as f:
            config.read_file(f)
            if config.has_option('DEFAULT', 'last directory'):
                return config.get('DEFAULT', 'last directory')
    else:
        print("config.ini doesn't exist")
        return os.getcwd()


def save_path_to_cfg(dir):
    config.set('DEFAULT', 'last directory', dir)
    with open(config_file_path, 'w') as f:
        config.write(f)
        print("last directory {} saved to config.ini".format(dir))


if __name__ == "__main__":
    open_filedialog()

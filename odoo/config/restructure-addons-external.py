#!/usr/bin/env python3
import os
import yaml
import shutil

YML_PATH = "/home/odoo/config/addons-external.yml"
DESTINATION = "/home/odoo/src/addons-external/"
SOURCE_PATH = "/home/odoo/temp/addons-external/"
GITHUB_DIRECTORIES = ('branches', 'hooks', 'info', 'logs', 'objects', 'refs', '.git')


if __name__ == "__main__":
    for (root, dirs, files) in os.walk(SOURCE_PATH, topdown=True):
        for dir_name in dirs:
            if dir_name in GITHUB_DIRECTORIES:
                continue
            shutil.move(f"{root}/{dir_name}", DESTINATION)

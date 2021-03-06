#!/usr/bin/env python3

import os
from os import path
import yaml
import shutil

YML_PATH = "/home/odoo/config/external-repositories.yml"
DESTINATION = "/home/odoo/src/addons-external/"
SOURCE = "/home/odoo/temp/"
IGNORE_DIRECTORIES = ('branches', 'hooks', 'info', 'logs', 'objects', 'refs', '.git', 'setup')


if __name__ == "__main__":
    with open(YML_PATH) as file:
        doc = yaml.full_load(file)
        for repository, attributes in doc.items():
            dir_name = repository.split('/')[-1]
            for (root, dirs, files) in os.walk(f"{SOURCE}/{dir_name}"):
                modules = attributes.get('modules', dirs)
                if isinstance(modules, str):
                    modules = modules.split(',')
                for dir_name in modules:
                    if dir_name in IGNORE_DIRECTORIES:
                        continue
                    source = f"{root}/{dir_name}"
                    if path.exists(source):
                        shutil.move(source, f"{DESTINATION}/{dir_name}")
                break
        shutil.rmtree(SOURCE)

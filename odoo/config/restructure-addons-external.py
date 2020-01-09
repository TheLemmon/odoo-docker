#!/usr/bin/env python3
import os
import yaml
import shutil

YML_PATH = "/home/odoo/config/addons-external.yml"
DESTINATION = "/home/odoo/src/addons-external/"
MAIN_PATH = "/home/odoo/temp/addons-external"
GITHUB_DIRECTORIES = ('branches', 'hooks', 'info', 'logs', 'objects', 'refs', '.git')


if __name__ == "__main__":
    with open(YML_PATH) as file:
        doc = yaml.safe_load(file)
        paths_to_move = doc.keys()
        
        for (root, dirs, files) in os.walk(MAIN_PATH, topdown=True):
            current_path = f"./{root.split('/')[-1]}"
            if current_path not in paths_to_move:
                continue
            
            for dir_name in dirs:
                if dir_name in GITHUB_DIRECTORIES:
                    continue
                source = f"{root}/{dir_name}"
                print(source, DESTINATION)
                shutil.move(source, DESTINATION)

import os
import yaml
import shutil

yml_path = "/home/odoo/config/addons-external.yml"
src_path = "/home/odoo/src/addons-external"
main_path = "/home/odoo/temp/addons-external"

if __name__ == "__main__":
    with open(path) as file:
        doc = yaml.full_load(file)
        paths_to_move = doc.keys()
        
        for (root, dirs, files) in os.walk(main_path, topdown=True):
            current_path = f"./{root.split('/')[-1]}"        
            if current_path not in paths_to_move:
                continue
            
            for dir_name in dirs:
                shutil.move(f"{root}/{dir_name}", src_path)

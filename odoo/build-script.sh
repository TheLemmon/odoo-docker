#!/bin/bash

set -e
python3 /home/odoo/config/restructure-addons-external.py
exec "$@"


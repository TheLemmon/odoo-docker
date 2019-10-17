# file run:sh
#!/bin/sh

pre = "https://"
token = $GIT_TOKEN
branch = $GIT_BRANCH
odoo_addons = "@github.com/nahualventure/odoo-addons"
odoo_addons_external = "@github.com/nahualventure/odoo-addons-external"

addons_url = $pre$token$odoo_addons
git clone -b $branch $odoo_addons

addons_external_url = $pre$token$odoo_addons_external
git clone -b $branch $odoo_addons_external

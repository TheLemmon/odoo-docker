# file run:sh
#!/bin/sh

pre="https://"
token=$GIT_TOKEN
branch=$GIT_BRANCH
odoo_addons="@github.com/nahualventure/odoo-addons"
odoo_addons_external="@github.com/nahualventure/odoo-addons-external"
odoo_enterprise="@github.com/odoo/enterprise.git"

addons_url=$pre$token$odoo_addons
git clone -b $branch $addons_url

addons_external_url=$pre$token$odoo_addons_external
git clone -b $branch $addons_external_url

enterprise_url=$pre$token$odoo_enterprise
git clone -b $branch $enterprise_url

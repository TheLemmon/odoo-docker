# Latest odoo system requirements
FROM thelemmon/odoo13-system-base:latest

ARG GIT_BRANCH
ARG ODOO_VERSION
ARG GITHUB_TOKEN

# Install Odoo
RUN set -x; \
        curl -o odoo.deb -sSL http://nightly.odoo.com/${ODOO_VERSION}/nightly/deb/odoo_${ODOO_VERSION}.latest_all.deb \
        && dpkg --force-depends -i odoo.deb \
        && apt-get update \
        && apt-get -y install -f --no-install-recommends \
        && rm -rf /var/lib/apt/lists/* odoo.deb

WORKDIR /home/odoo/config
# Install custom python requirements
COPY config/requirements.txt ./requirements.txt
COPY config/repositories.yml ./repositories.yml
COPY config/addons-external.yml ./addons-external.yml

COPY config/restructure-addons-external.py ./restructure-addons-external.py
RUN chmod -R 755 ./restructure-addons-external.py

RUN pip3 install -r ./requirements.txt

# Clone Github repositories (Custom modules)
WORKDIR /home/odoo/src
RUN gitaggregate -c /home/odoo/config/repositories.yml --expand-env

# Clone third party repositories
WORKDIR  /home/odoo/temp/addons-external
RUN gitaggregate -c /home/odoo/config/addons-external.yml --expand-env

WORKDIR /home/odoo

# Reeemplace wait-for-psql.py
COPY wait-for-psql.py /usr/local/bin/wait-for-psql.py
RUN chmod -R 755 /usr/local/bin/wait-for-psql.py

# Copy odoo.conf and set as default config file
COPY config/odoo.conf /home/odoo.conf
ENV ODOO_RC /home/odoo.conf

# Copy entrypoint script
COPY ./entrypoint.sh bin/
RUN chmod +x bin/entrypoint.sh
# Copy build-script
COPY ./build-script.sh bin/
RUN chmod +x bin/build-script.sh

# Expose Odoo services
# Web service - Longpolling - XML-RPC
EXPOSE 8069 8071 8072

VOLUME ["/var/lib/odoo"]

ENTRYPOINT ["bin/entrypoint.sh"]
CMD ["odoo"]

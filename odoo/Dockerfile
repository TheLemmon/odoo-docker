# Latest odoo system requirements
FROM thelemmon/odoo-system-base:latest

# Define odoo args to build the image 
ARG GIT_BRANCH
ARG GIT_TOKEN
ARG ODOO_RELEASE
ARG ODOO_VERSION
ARG ODOO_SHA

# Install Odoo
RUN set -x; \
        curl -o odoo.deb -sSL http://nightly.odoo.com/${ODOO_VERSION}/nightly/deb/odoo_${ODOO_VERSION}.${ODOO_RELEASE}_all.deb \
        && echo "${ODOO_SHA} odoo.deb" | sha1sum -c - \
        && dpkg --force-depends -i odoo.deb \
        && apt-get update \
        && apt-get -y install -f --no-install-recommends \
        && rm -rf /var/lib/apt/lists/* odoo.deb

# Clone addons and addons-external
COPY git_clone.sh git_clone.sh
RUN chmod +x git_clone.sh
RUN ./git_clone.sh

# Install custom python requirements
RUN pip3 install -r requirements.txt

# Copy Odoorc and set as default config file
COPY ./odoorc ./odoorc
ENV ODOO_RC ./odoorc


# Set default user when runnig the container
USER odoo

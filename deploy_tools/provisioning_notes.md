Provisioning a new site
======================

## Required packages

* nginx
* python-setuptools
* Git
* virtualenv

eg, on Ubuntu:

	sudo apt-get install nginx git python-setuptools
	sudo easy_install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with. eg, 'your_domain'

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, 'your_domain'

## Folder structure:
Assume we have a user account at /home/username

/home/username
|__sites
   |__SITENAME
      |--database
      |--source
      |--static
      |--virtualenv

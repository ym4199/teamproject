from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

DATABASES = config_secret_deploy['django']['database']

WSGI_APPLICATION = 'config.wsgi.deploy.application'


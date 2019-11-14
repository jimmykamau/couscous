import os


current_environment = os.getenv('ENVIRONMENT_SETTINGS')

if current_environment == "PRODUCTION":
    from couscous.settings.production import *
elif current_environment == "DEVELOPMENT":
    from couscous.settings.development import *

import json
import os

from couscous.settings.base import *

ALLOWED_HOSTS = json.loads(os.environ.get('ALLOWED_HOSTS', '[]'))

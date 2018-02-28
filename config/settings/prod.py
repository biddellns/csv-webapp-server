import os
from .base import *

DEBUG = False

base_domain = '.' + os.environ['DOMAIN']
ALLOWED_HOSTS = [ base_domain, ]

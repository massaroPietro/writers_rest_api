from .base import *
from .base import env

SECRET_KEY = env("DJANGO_SECRET_KEY", default="dNC6kbpS_ac9uRhVLHvjrc6NO9OqClF9Ccqu6E_-qp7QprQ5_HM")

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
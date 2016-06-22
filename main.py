from os import getcwd

from whitenoise import WhiteNoise

from api.app import get_app


application = WhiteNoise(get_app(), root='{}/static'.format(getcwd()))

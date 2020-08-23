from .common import *

CHANNEL_LAYERS = {
    'default': {
        # TODO: This doesn't work for the selenium tests
        # since it won't allow cross-process messaging.
        # A fake Redis server is needed instead
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}
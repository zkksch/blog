from .base import *

DELAY = 1

MIDDLEWARE.extend([
    'utils.delay.delay_middleware'
])

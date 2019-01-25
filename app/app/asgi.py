# Map this ASGI application for production

import os
import django
from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()
application = get_default_application()

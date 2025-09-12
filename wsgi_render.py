import sys
import os

# Add your project folder to path
sys.path.append(os.path.join(os.path.dirname(__file__), "EmailProject-backup"))

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EmailProject-backup.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

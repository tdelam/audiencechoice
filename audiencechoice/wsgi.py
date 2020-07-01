import os
import sys

sys.stdout = sys.stderr

# Add the virtual Python environment site-packages directory to the path
import site
site.addsitedir('/srv/virtualenvs/audiencechoice/lib/python2.7/site-packages')

#If your project is not on your PYTHONPATH by default you can add the following
sys.path.append('/srv/virtualenvs/audiencechoice/')
sys.path.append('/srv/virtualenvs/audiencechoice/audiencechoice')

os.environ['DJANGO_SETTINGS_MODULE'] = 'audiencechoice.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

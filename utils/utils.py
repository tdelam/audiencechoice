import sha, random

from django.contrib.sites.models import Site

def get_full_path():
    current_site = Site.objects.get_current()    
    full_path = ('http://', current_site.domain)
    return ''.join(full_path)

def activation_key(email):
    salt = sha.new(str(random.random())).hexdigest()[:12]
    key = sha.new(salt+str(email)).hexdigest()
    return key
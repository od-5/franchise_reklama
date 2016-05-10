import datetime
from core.models import Setup

__author__ = 'alexy'


def site_setup(request):
    try:
        qs = Setup.objects.first()
    except:
        qs = None
    print qs
    return {
        'SETUP': qs
    }

# coding=utf-8
from PIL import Image
from django.conf import settings
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize
from core.files import upload_to

__author__ = 'alexy'

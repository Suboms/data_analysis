import random
import os
import sys
import django
from faker import Faker
fake = Faker()
DJANGO_PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(DJANGO_PROJECT_PATH)
os.environ["DJANGO_SETTINGS_MODULE"] = "data_analysis.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_analysis.settings")
django.setup()
from dataset.models import *
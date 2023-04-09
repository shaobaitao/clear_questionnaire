from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(
    [PROJECT, QUESTION, SUBMIT, ANSWER, Q_NOTE, Q_COMPLETION, Q_CHOICE, Q_TABLE, Q_TABLE_OPTIONS, Q_IMAGE, A_IMAGE,
     A_CHOICE, A_COMPLETION, A_TABLE])

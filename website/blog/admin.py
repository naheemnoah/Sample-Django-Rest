from django.contrib import admin
from .models import Poll, Choice, Vote, CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Vote)
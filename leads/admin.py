from django.contrib import admin
from .models import User,Agent,Leads

admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Leads)
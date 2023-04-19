from django.contrib import admin
from polls.models import Signin
from polls.models import Person
from polls.models import Testlogin

admin.site.register(Signin)
admin.site.register(Person)
admin.site.register(Testlogin)

# Register your models here.

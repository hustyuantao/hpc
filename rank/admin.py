from django.contrib import admin
from rank.models import TopOneHundred, TopFiveHundred

# Register your models here.
admin.site.register(TopOneHundred)
admin.site.register(TopFiveHundred)

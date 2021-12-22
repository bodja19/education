from django.contrib import admin

from .models import People, MyMoney, NotMyMoney

admin.site.register(People)
admin.site.register(MyMoney)
admin.site.register(NotMyMoney)

from django.contrib import admin

from auth1.forms import User


class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)

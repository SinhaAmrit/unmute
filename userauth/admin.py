from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from userauth.models import Profile


class ProfileAdmin(ImportExportModelAdmin):
    list_display = ["user"]


admin.site.register(Profile, ProfileAdmin)

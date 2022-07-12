from django.contrib import admin
from .models import PC, Dep, Vendors, License, User, Sessions


class SessionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'date_start', 'num_lic', 'pc_id', 'lic_id')
    search_fields = ('id', 'user_id', )


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_user', 'dep_id')


class DepAdmin(admin.ModelAdmin):
    list_display = ('id', 'num_dep')


class PCAdmin(admin.ModelAdmin):
    list_display = ('id', 'num_pc')


class VendorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_vendor')


class LicenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendor_id', 'name_lic')


admin.site.register(License, LicenseAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(PC, PCAdmin)
admin.site.register(Sessions, SessionsAdmin)
admin.site.register(Vendors, VendorsAdmin)
admin.site.register(Dep, DepAdmin)

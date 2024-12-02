from django.contrib import admin
from .models import MyUser

#----UD8.1.d----
#Registrar el modelo de usuario en el admin
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('email','username', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username','is_superuser')
    ordering = ('pk',)
    list_filter = ('is_active', 'is_staff', 'is_superuser')

admin.site.register(MyUser, MyUserAdmin)
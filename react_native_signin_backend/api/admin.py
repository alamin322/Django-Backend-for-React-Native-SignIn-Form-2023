from api.models import SignIn
from django.contrib import admin


# Register your models here.
@admin.register(SignIn)
class SignInAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_email', 'password']

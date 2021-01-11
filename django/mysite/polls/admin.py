from django.contrib import admin

# Register your models here.
from .models import Blog

# 클래스를 어드민 사이트에 등록한다.
#admin.site.register(Budget)
admin.site.register(Blog)

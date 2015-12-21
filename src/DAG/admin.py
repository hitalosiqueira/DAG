from django.contrib import admin

# Register your models here.
from .models import Despesa
from .models import Fonte
from .models import Natureza

admin.site.register(Despesa)
admin.site.register(Fonte)
admin.site.register(Natureza)
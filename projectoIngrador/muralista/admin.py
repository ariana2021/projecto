from django.contrib import admin

# Register your models here.

from .models import Muralista
from .models import Contacto 
from .models import Estilo
from .models import Color
from .models import Paleta


admin.site.register(Estilo)
admin.site.register(Contacto)
admin.site.register(Muralista)
admin.site.register(Color)
admin.site.register(Paleta)
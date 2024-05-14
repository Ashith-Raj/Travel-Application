from django.contrib import admin
from .models import Destination
from .models import Hotels
from .models import Restuarants
from. models import Tourpackages
from. models import Customer

admin.site.register(Destination)
admin.site.register(Hotels)
admin.site.register(Restuarants)
admin.site.register(Tourpackages)
admin.site.register(Customer)
# Register your models here.

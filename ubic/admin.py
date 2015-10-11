from django.contrib import admin

# Register your models here.
from .models import Ubic, UbicInstance, User, WeeklySchedule, Webinar, Resource, Video

admin.site.register(Ubic)
admin.site.register(UbicInstance)
admin.site.register(User)
admin.site.register(WeeklySchedule)
admin.site.register(Webinar)
admin.site.register(Resource)
admin.site.register(Video)
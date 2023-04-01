from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# admin.site.register(Tour)
# admin.site.register(Location)
# admin.site.register(Package)
# admin.site.register(TravelOffer)
# admin.site.register(RecentPost)
# admin.site.register(TourGuide)
@admin.register(Tour)
class ViewAdmin(ImportExportModelAdmin):
    pass
@admin.register(Location)
class ViewAdmin(ImportExportModelAdmin):
    pass
@admin.register(Package)
class ViewAdmin(ImportExportModelAdmin):
    pass
# @admin.register(TravelOffer)
# class ViewAdmin(ImportExportModelAdmin):
#     pass
# @admin.register(RecentPost)
# class ViewAdmin(ImportExportModelAdmin):
#     pass
# @admin.register(TourGuide)
# class ViewAdmin(ImportExportModelAdmin):
#     pass
@admin.register(Contact)
class ViewAdmin(ImportExportModelAdmin):
    pass
@admin.register(Enquire)
class ViewAdmin(ImportExportModelAdmin):
    pass
@admin.register(About)
class ViewAdmin(ImportExportModelAdmin):
    pass
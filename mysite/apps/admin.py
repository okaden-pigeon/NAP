from django.contrib import admin

from .models import Users,Items,Genres,Images
# ,ItemClassification,ItemImage,UserListing,Likes

# Register your models here.
admin.site.register(Users)
# admin.site.register(Universities)
admin.site.register(Items)
admin.site.register(Genres)
admin.site.register(Images)
# admin.site.register(ItemClassification)
# admin.site.register(ItemImage)
# admin.site.register(UserListing)
# admin.site.register(Likes)
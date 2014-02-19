from django.contrib import admin
from rango.models import Category, Page, PageAdmin

# Import the UserProfile model individually.
from rango.models import UserProfile

# Import the UserProfile model with Category and Page.
# If you choose this option, you'll want to modify the import statement you've already got to include UserProfile.
from rango.models import Category, Page, UserProfile


admin.site.register(Category)
# admin.site.register(Page)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
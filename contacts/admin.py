from django.contrib import admin

# Contacts Admib Customization to see that in the Django Admin Dashboard
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
	"""docstring for ContactAdmin"""
	list_display = ('id', 'name', 'listing', 'email', 'contact_date')
	list_display_links = ('id', 'name')
	search_fields = ('name', 'email', 'listing')
	list_per_page = 25


admin.site.register(Contact, ContactAdmin)

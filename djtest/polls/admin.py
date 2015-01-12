from polls.models import Poll
from django.contrib import admin


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]


admin.site.register(Poll, PollAdmin)

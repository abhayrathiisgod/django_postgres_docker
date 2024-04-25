from django.contrib import admin
from .models import Job, Candidate


# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Title', 'Open_date',
                    'Close_date', 'Created_at', 'Updated_at')
    list_filter = ('Title', 'Job_Type', 'Open_date',
                   'Close_date', 'Created_at', 'Updated_at')
    list_display_links = ('Id', 'Title', 'Open_date',
                          'Close_date', 'Created_at', 'Updated_at')
    readonly_fields = ('Created_at', 'Updated_at')


class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Email', 'Phone', 'Position', 'Created_at')
    list_filter = ('Name', 'Email', 'Position', 'Created_at', 'Updated_at')
    list_display_links = ('id', 'Name', 'Email', 'Phone',
                          'Position', 'Created_at')
    readonly_fields = ('Created_at', 'Updated_at')

    def get_form(self, request, obj=None, **kwargs):
        form = super(CandidateAdmin, self).get_form(request, obj, **kwargs)
        field = form.base_fields["Position"]
        field.widget.can_add_related = True
        field.widget.can_change_related = True
        field.widget.can_delete_related = True
        return form


admin.site.register(Job, JobAdmin)
admin.site.register(Candidate, CandidateAdmin)

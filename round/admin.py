from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from round.models import Round, Team, Score, ScoreLine, Profile


class ScoreLineInline(admin.TabularInline):
    model = ScoreLine
    max_num = 0
    fields = ('hole', 'strokes', 'points')
    readonly_fields = ('hole',)
    can_delete = False


class ScoreAdmin(admin.ModelAdmin):
    inlines = [
        ScoreLineInline,
    ]

    readonly_fields = ('team',)

    def get_queryset(self, request):
        qs = super(ScoreAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(team__user=request.user)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# Register your models here.
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Round)
admin.site.register(Team)
admin.site.register(Score, ScoreAdmin)
admin.site.site_header = 'Lans Invitational'
admin.site.site_url = '/round'

from django.contrib import admin
from round.models import Round, Team, Score, ScoreLine


class ScoreLineInline(admin.TabularInline):
    model = ScoreLine
    max_num = 0
    fields = ('hole', 'strokes',)
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


# Register your models here.
admin.site.register(Round)
admin.site.register(Team)
admin.site.register(Score, ScoreAdmin)

from django.contrib import admin
from .models import (
    PortfolioPage, PortfolioPost, StatisticsPage, ServicesPage, TeamPage, AboutMePage, Skill, MessagePage, BlogDetailPage, CommentPage
    )


@admin.register(PortfolioPage)
class PortfolioPageAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(PortfolioPost)
class PortfolioPostAdmin(admin.ModelAdmin):
    list_display = ('id','name','about','data','status')


@admin.register(StatisticsPage)
class StatisticsPageAdmin(admin.ModelAdmin):
    list_display = ('works_completed', 'years_of_experience', 'total_clients', 'award_won')


@admin.register(ServicesPage)
class ServicesPageAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(TeamPage)
class TeamPageAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(AboutMePage)
class AboutMePageAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(MessagePage)
class MessagePageAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(BlogDetailPage)
class BlogDetailPageAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(CommentPage)
class CommentPageAdmin(admin.ModelAdmin):
    list_display = ('name', )


# admin.site.register(PortfolioPage)
# admin.site.register(PortfolioPost)


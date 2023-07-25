from django.contrib import admin
from .models import MainContent, Comment

class MainContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_date']
    search_fields=['title']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
    search_fields = ['author']

admin.site.register(MainContent, MainContentAdmin) #관리자 페이지에 MainContent항목 추가
admin.site.register(Comment, CommentAdmin) #관리자 페이지에 Comment 항목 추가
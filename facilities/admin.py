from django.contrib import admin
from .models import *


'''-----Visit------'''
class ImageToVisitInlineAdmin(admin.TabularInline):
    model = ImageToVisit
    fields = ('image',)
    max_num = 5


class CommentToVisitInlineAdmin(admin.TabularInline):
    model = CommentToVisit
    fields = ('body',)
    max_num = 10


class LikeToVisitInlineAdmin(admin.TabularInline):
    model = LikeToVisit
    fields = ('like',)


@admin.register(PlaceToVisit)
class PlaceToVisitAdmin(admin.ModelAdmin):
    inlines = [ImageToVisitInlineAdmin, CommentToVisitInlineAdmin, LikeToVisitInlineAdmin]


'''-----Eat------'''
class ImageToEatInlineAdmin(admin.TabularInline):
    model = ImageToEat
    fields = ('image',)
    max_num = 5


class CommentToEatInlineAdmin(admin.TabularInline):
    model = CommentToEat
    fields = ('body',)
    max_num = 10


class LikeToEatInlineAdmin(admin.TabularInline):
    model = LikeToEat
    fields = ('like',)


@admin.register(PlaceToEat)
class PlaceToEatAdmin(admin.ModelAdmin):
    inlines = [ImageToEatInlineAdmin, CommentToEatInlineAdmin, LikeToEatInlineAdmin]


'''-----Stay------'''
class ImageToStayInlineAdmin(admin.TabularInline):
    model = ImageToStay
    fields = ('image',)
    max_num = 5


class CommentToStayInlineAdmin(admin.TabularInline):
    model = CommentToStay
    fields = ('body',)
    max_num = 10


class LikeToStayInlineAdmin(admin.TabularInline):
    model = LikeToStay
    fields = ('like',)


@admin.register(PlaceToStay)
class PlaceToStayAdmin(admin.ModelAdmin):
    inlines = [ImageToStayInlineAdmin, CommentToStayInlineAdmin, LikeToStayInlineAdmin]


admin.site.register(Trip)
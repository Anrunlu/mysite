from django.contrib import admin
from .models import BlogType, Blog

# 定制化后台
admin.site.site_header = "RunluBlog Admin"
admin.site.site_title = "RUnluBlog Admin Area"
admin.site.index_title = "Welcome to the RunluBlog admin area"

# 注册博文类型model
# 定制化博文类型model
@admin.register(BlogType)
class BlogTypeAmdin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

# 注册博文管理model
# 定制化博文管理model
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # 里面可以传递该模型拥有的方法名，例如这里的 get_read_num 是 Blog 类里面的一个方法
    list_display = ('id', 'title', 'blog_type', 'author', 'get_read_num', 'created_time', 'last_update_time')


# 注册阅读统计model
# 定制化阅读统计model
# @admin.register(ReadNum)
# class ReadAdmin(admin.ModelAdmin):
#     list_display = ('read_num', 'blog')
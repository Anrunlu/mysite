from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod, ReadDetail

# 创建博客分类模型
class BlogType(models.Model):
    # 博文类型名
    type_name = models.CharField(max_length=15)

    # 描述字符
    def __str__(self):
        return self.type_name

# 创建博客模型
class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    read_details = GenericRelation(ReadDetail) # 关联阅读统计模型
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    # 描述字符
    def __str__(self):
        return "<Blog: %s>" % self.title

    def get_url(self):
        return reverse('blog_detail', kwargs={'blog_pk': self.pk})

    def get_user(self):
        return self.author

    class Meta:
        ordering = ['-created_time']


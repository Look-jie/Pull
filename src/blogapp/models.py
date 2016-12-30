from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    contents = models.TextField(max_length=1500, verbose_name='内容')
    like = models.IntegerField(blank=True, null=True, verbose_name='喜欢数')
    counts = models.IntegerField(blank=True, null=True, verbose_name='点击次数')
    comments = models.IntegerField(blank=True, null=True, verbose_name='评论数')
    user = models.CharField(max_length=20, blank=True, null=True, verbose_name='作者')
    tag = models.CharField(max_length=20, blank=True, verbose_name='标签')
    creat_time = models.TimeField(auto_created=True, verbose_name="blog时间")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-creat_time']

    def __str__(self):
        return self.title

class comment(models.Model):
    contents = models.TextField(max_length=150, verbose_name="评论内容")
    user = models.CharField(max_length=20, verbose_name="用户")
    blogtitle = models.CharField(max_length=20, verbose_name="标题")
    creat_time = models.TimeField(auto_created=True, verbose_name="评论时间")

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        ordering = ['-creat_time']

    def __str__(self):
        return str(self.id)

class tag(models.Model):
    name = models.CharField(max_length=10, verbose_name="标签")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class blog_user(models.Model):
    username = models.CharField(max_length=10, verbose_name="用户名")
    password = models.CharField(max_length=20, verbose_name="密码")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username

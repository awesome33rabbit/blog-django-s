from django.db import models


# django从入到精通
class ArticleCategory(models.Model):
    name = models.CharField("分类名称", max_length=16)
    desc = models.CharField("描述", max_length=128)

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"

    class Meta:
        db_table = "article_category"
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name


# python django drf
class ArticleTag(models.Model):
    name = models.CharField("标签名称", max_length=16)

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"

    class Meta:
        db_table = "article_tag"
        verbose_name = "文章标签"
        verbose_name_plural = verbose_name


class Article(models.Model):
    title = models.CharField("文章标题", max_length=64)
    cover = models.URLField("文章封面", default="")
    abstract = models.CharField("摘要", max_length=256, default="")
    content = models.TextField("文章内容")

    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, blank=True, null=True)
    tag = models.ManyToManyField(ArticleTag, blank=True, db_table="article_tag_many")

    date_joined = models.DateTimeField("创建日期", auto_now_add=True)
    date_update = models.DateTimeField("修改日期", auto_now=True)

    def __str__(self):
        return f"{self.__class__.__name__}({self.title})"

    class Meta:
        db_table = "article"
        verbose_name = "文章"
        verbose_name_plural = verbose_name


class ArticleComment(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    content = models.CharField("评论内容", max_length=256)

    date_joined = models.DateTimeField("创建日期", auto_now_add=True)
    date_update = models.DateTimeField("修改日期", auto_now=True)

    def __str__(self):
        return f"{self.__class__.__name__}({self.article})"

    class Meta:
        db_table = "article_comment"
        verbose_name = "文章评论"
        verbose_name_plural = verbose_name

from django.db import models

# Create your models here.
class Article(models.Model):
    class Meta:
        ordering = ('-timestamp',)
    slug = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_dark = models.BooleanField(default=False)
    background_img = models.FileField(blank=True, upload_to="/upload")
    background_img_url = models.CharField(max_length=500, blank=True)
    background_img_extra_css = models.CharField(max_length=500, blank=True)

    hero_img = models.FileField(blank=True, upload_to="/upload")
    hero_img_url = models.CharField(max_length=500, blank=True)
    is_hero_portrait = models.BooleanField(default=False)
    hero_link_url = models.CharField(max_length=500, blank=True)
    hero_desc = models.CharField(max_length=500)
    content = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    def get_background_url(self):
        if self.background_img.name:
            return self.background_img.url
        if self.background_img_url:
            return self.background_img_url
        if self.hero_img.name:
            return self.hero_img.url
        return self.hero_img_url

    def get_hero_url(self):
        if self.hero_img.name:
            return self.hero_img.url
        return self.hero_img_url

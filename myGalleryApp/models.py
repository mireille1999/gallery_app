from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =50)

    @classmethod
    def tag_articles(cls):
        tags = cls.objects.all()
        return tags

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate

    def __str__(self):
        return self.name  

class Image(models.Model):
    img_title = models.CharField(max_length =60)
    img_description = models.TextField()
    img_location = models.ForeignKey(Location,null = True, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    Boom = models.ImageField(upload_to = 'images/')
    @classmethod
    def search_by_title(cls,search_term):
        my_img = cls.objects.filter(img_title__icontains=search_term)
        return my_img


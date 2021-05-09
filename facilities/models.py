from .utils import PlaceMixin, CommentMixin
from django.db import models
from account.models import MyUser


class PlaceToVisit(PlaceMixin):
    pass


class LikeToVisit(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='likes_to_visit')
    visit = models.ForeignKey(PlaceToVisit, on_delete=models.CASCADE, related_name='likes_to_visit')
    like = models.BooleanField(default=False)


class CommentToVisit(CommentMixin):
    visit = models.ForeignKey(PlaceToVisit, related_name='comments_to_visit', on_delete=models.CASCADE)
    author = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name='comments_to_visit')


class ImageToVisit(models.Model):
    visit = models.ForeignKey(PlaceToVisit, related_name='images_to_visit', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='visit')


class RatingToVisit(models.Model):
    CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='ratings_to_visit')
    visit = models.ForeignKey(PlaceToVisit, on_delete=models.CASCADE, related_name='ratings_to_visit')
    rating = models.CharField(choices=CHOICES, max_length=30)


class PlaceToEat(PlaceMixin):
    pass


class LikeToEat(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='likes_to_eat')
    eat = models.ForeignKey(PlaceToEat, on_delete=models.CASCADE, related_name='likes_to_eat')
    like = models.BooleanField(default=False)


class CommentToEat(CommentMixin):
    eat = models.ForeignKey(PlaceToEat, related_name='comments_to_eat', on_delete=models.CASCADE)
    author = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name='comments_to_eat')


class ImageToEat(models.Model):
    eat = models.ForeignKey(PlaceToEat, related_name='images_to_eat', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='eat')


class RatingToEat(models.Model):
    CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='ratings_to_eat')
    eat = models.ForeignKey(PlaceToEat, on_delete=models.CASCADE, related_name='ratings_to_eat')
    rating = models.CharField(choices=CHOICES, max_length=30)


class PlaceToStay(PlaceMixin):
    pass


class LikeToStay(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='likes_to_stay')
    stay = models.ForeignKey(PlaceToStay, on_delete=models.CASCADE, related_name='likes_to_stay')
    like = models.BooleanField(default=False)


class CommentToStay(CommentMixin):
    stay = models.ForeignKey(PlaceToStay, related_name='comments_to_stay', on_delete=models.CASCADE)
    author = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name='comments_to_stay')


class ImageToStay(models.Model):
    stay = models.ForeignKey(PlaceToStay, related_name='images_to_stay', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='stay')


class RatingToStay(models.Model):
    CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='ratings_to_stay')
    stay = models.ForeignKey(PlaceToStay, on_delete=models.CASCADE, related_name='ratings_to_stay')
    rating = models.CharField(choices=CHOICES, max_length=30)


class Trip(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    hostel = models.ManyToManyField(PlaceToStay, related_name='hostels', blank=True)
    eat = models.ManyToManyField(PlaceToEat, related_name='eats', blank=True)
    place = models.ManyToManyField(PlaceToVisit, related_name='places', blank=True)

    def __str__(self):
        return self.name


class News(models.Model):
    image = models.ImageField(upload_to='news', null=True, blank=True)

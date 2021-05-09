from rest_framework import serializers
from .models import *


'''-----Visit------'''
class PlaceToVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceToVisit
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = PlaceToVisitImageSerializer(instance.images_to_visit.all(), many=True, context=self.context).data
        representation['comments'] = CommentToVisitSerializer(instance.comments_to_visit.all(), many=True, context=self.context).data
        representation['likes'] = len(LikeToVisitSerializer(instance.likes_to_visit.filter(like=True), many=True, context=self.context).data)
        representation['rating'] = RatingToVisitSerializer(instance.ratings_to_visit.all(), many=True, context=self.context).data
        return representation


class PlaceToVisitImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageToVisit
        fields = '__all__'

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


class LikeToVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeToVisit
        fields = '__all__'

    def get_fields(self):
        action = self.context.get('action')
        fields = super().get_fields()
        if action == 'create':
            fields.pop('user')
            fields.pop('like')
        return fields

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        visit = validated_data.get('visit')
        like = LikeToVisit.objects.get_or_create(user=user, visit=visit)[0]
        if not like.like:
            like.like = True
        else:
            like.like = False
        like.save()
        return like


class CommentToVisitSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%d %B %Y %H:%M', read_only=True)

    class Meta:
        model = CommentToVisit
        fields = '__all__'

    def get_fields(self):
        action = self.context.get('action')
        fields = super().get_fields()
        if action == 'create' or action == 'update':
            fields.pop('author')
        return fields

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        comment = CommentToVisit.objects.create(author=user, **validated_data)
        return comment

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance


'''-----Eat------'''
class PlaceToEatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceToEat
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = PlaceToEatImageSerializer(instance.images_to_eat.all(), many=True, context=self.context).data
        representation['comments'] = CommentToEatSerializer(instance.comments_to_visit.all(), many=True, context=self.context).data
        representation['likes'] = len(LikeToEatSerializer(instance.likes_to_eat.filter(like=True), many=True, context=self.context).data)
        representation['rating'] = RatingToEatSerializer(instance.ratings_to_eat.all(), many=True, context=self.context).data
        return representation


class LikeToEatSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeToEat
        fields = '__all__'

    def get_fields(self):
        action = self.context.get('action')
        fields = super().get_fields()
        if action == 'create':
            fields.pop('user')
            fields.pop('like')
        return fields

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        eat = validated_data.get('eat')
        like = LikeToEat.objects.get_or_create(user=user, eat=eat)[0]
        if not like.like:
            like.like = True
        else:
            like.like = False
        like.save()
        return like


class CommentToEatSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%d %B %Y %H:%M', read_only=True)

    class Meta:
        model = CommentToEat
        fields = '__all__'

    def get_fields(self):
        action = self.context.get('action')
        fields = super().get_fields()
        if action == 'create' or action == 'update':
            fields.pop('author')
        return fields

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        comment = CommentToEat.objects.create(author=user, **validated_data)
        return comment

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['comment'] = self.eat
        return representation


class PlaceToEatImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageToEat
        fields = '__all__'

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


'''-----Stay------'''
class PlaceToStaySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceToStay
        fields = '__all__


class CommentToStaySerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%d %B %Y %H:%M', read_only=True)

    class Meta:
        model = CommentToStay
        fields = '__all__'

    def get_fields(self):
        action = self.context.get('action')
        fields = super().get_fields()
        if action == 'create' or action == 'update':
            fields.pop('author')
        return fields

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        comment = CommentToStay.objects.create(author=user, **validated_data)
        return comment

    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['comment'] = self.stay
        return representation


class PlaceToStayImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageToStay
        fields = '__all__'

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


class LikeToStaySerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeToStay
        fields = '__all__'

    def get_fields(self):
        action = self.context.get('action')
        fields = super().get_fields()
        if action == 'create':
            fields.pop('user')
            fields.pop('like')
        return fields

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        stay = validated_data.get('stay')
        like = LikeToStay.objects.get_or_create(user=user, stay=stay)[0]
        if not like.like:
            like.like = True
        else:
            like.like = False
        like.save()
        return like


'''-------Trip-------'''
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


'''-----Rating-----'''
class RatingToEatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingToEat
        fields = '__all__'
        read_only_fields = ('user', 'id')

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        eat = validated_data.get('eat')
        rat = validated_data.get('rating')
        rating = RatingToEat.objects.get_or_create(user=user, eat=eat)[0]
        rating.rating = rat
        rating.save()
        return rating


class RatingToStaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingToStay
        fields = '__all__'
        read_only_fields = ('user', 'id')

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        stay = validated_data.get('stay')
        rat = validated_data.get('rating')
        rating = RatingToStay.objects.get_or_create(user=user, stay=stay)[0]
        rating.rating = rat
        rating.save()
        return rating


class RatingToVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingToVisit
        fields = '__all__'
        read_only_fields = ('user', 'id')

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        visit = validated_data.get('visit')
        rat = validated_data.get('rating')
        rating = RatingToVisit.objects.get_or_create(user=user, visit=visit)[0]
        rating.rating = rat
        rating.save()
        return rating


class NewsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    link = serializers.CharField(max_length=500)

    class Meta:
        model = News
        fields = ('title', 'link', 'image')

    def _get_image_url(self, obj):
        image = obj.get('image')
        if image:
            url = image
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation

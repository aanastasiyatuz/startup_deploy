from django.shortcuts import render
from rest_framework import viewsets, generics, mixins, status
from .permissions import IsAuthorPermission
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from django.db.models import Q
from rest_framework.response import Response
from .parsing import main
from rest_framework.views import APIView


'''-----Visit------'''
class PlaceToVisitViewSet(viewsets.ModelViewSet):
    queryset = PlaceToVisit.objects.all()
    serializer_class = PlaceToVisitSerializer

    '''============Search============'''
    @action(methods=['GET'], detail=False)
    def search(self, request):
        query = request.query_params.get('q')
        queryset = self.get_queryset().filter(Q(name__icontains=query) | Q(location__icontains=query))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    '''===========Filter============='''
    @action(methods=['GET'], detail=False)
    def sort(self, request):
        filter = request.query_params.get('filter')
        if filter == 'A-Z':
            queryset = self.get_queryset().order_by('location')
        elif filter == 'Z-A':
            queryset = self.get_queryset().order_by('-location')
        else:
            queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlaceToVisitImageView(generics.ListCreateAPIView):
    queryset = ImageToVisit.objects.all()
    serializer_class = PlaceToVisitImageSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class CommentToVisitViewSet(viewsets.ModelViewSet):
    queryset = CommentToVisit.objects.all()
    serializer_class = CommentToVisitSerializer
    permission_classes = [IsAuthenticated, IsAuthorPermission]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}


class LikeToVisitViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = LikeToVisit.objects.all()
    serializer_class = LikeToVisitSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}


'''-----Eat------'''
class PlaceToEatViewSet(viewsets.ModelViewSet):
    queryset = PlaceToEat.objects.all()
    serializer_class = PlaceToEatSerializer

    '''============Search============'''
    @action(methods=['GET'], detail=False)
    def search(self, request):
        query = request.query_params.get('q')
        queryset = self.get_queryset().filter(Q(name__icontains=query) | Q(location__icontains=query))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    '''===========Filter============='''
    @action(methods=['GET'], detail=False)
    def sort(self, request):
        filter = request.query_params.get('filter')
        if filter == 'A-Z':
            queryset = self.get_queryset().order_by('location')
        elif filter == 'Z-A':
            queryset = self.get_queryset().order_by('-location')
        else:
            queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PlaceToEatImageView(generics.ListCreateAPIView):
    queryset = ImageToEat.objects.all()
    serializer_class = PlaceToEatImageSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class CommentToEatViewSet(viewsets.ModelViewSet):
    queryset = CommentToEat.objects.all()
    serializer_class = CommentToEatSerializer
    permission_classes = [IsAuthenticated, IsAuthorPermission]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}


class LikeToEatViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = LikeToEat.objects.all()
    serializer_class = LikeToEatSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}


'''-----Stay------'''
class PlaceToStayViewSet(viewsets.ModelViewSet):
    queryset = PlaceToStay.objects.all()
    serializer_class = PlaceToStaySerializer

    '''============Search============'''
    @action(methods=['GET'], detail=False)
    def search(self, request):
        query = request.query_params.get('q')
        queryset = self.get_queryset().filter(Q(name__icontains=query) | Q(location__icontains=query))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    '''===========Filter============='''
    @action(methods=['GET'], detail=False)
    def sort(self, request):
        filter = request.query_params.get('filter')
        if filter == 'A-Z':
            queryset = self.get_queryset().order_by('location')
        elif filter == 'Z-A':
            queryset = self.get_queryset().order_by('-location')
        else:
            queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlaceToStayImageView(generics.ListCreateAPIView):
    queryset = ImageToStay.objects.all()
    serializer_class = PlaceToStayImageSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class CommentToStayViewSet(viewsets.ModelViewSet):
    queryset = CommentToStay.objects.all()
    serializer_class = CommentToStaySerializer
    permission_classes = [IsAuthenticated, IsAuthorPermission]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}


class LikeToStayViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = LikeToStay.objects.all()
    serializer_class = LikeToStaySerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}


'''------Trip-------'''
class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    '''============Search============'''
    @action(methods=['GET'], detail=False)
    def search(self, request):
        query = request.query_params.get('trip')
        queryset = self.get_queryset().filter(slug__icontains=query)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


'''--------Rating---------'''
class RatingToVisitViewSet(viewsets.ModelViewSet):
    queryset = RatingToVisit.objects.all()
    serializer_class = RatingToVisitSerializer


class RatingToEatViewSet(viewsets.ModelViewSet):
    queryset = RatingToEat.objects.all()
    serializer_class = RatingToEatSerializer


class RatingToStayViewSet(viewsets.ModelViewSet):
    queryset = RatingToStay.objects.all()
    serializer_class = RatingToStaySerializer


class News(APIView):
    def get(self, request):
        info = main()
        serializer = NewsSerializer(instance=info, many=True)
        return Response(serializer.data)

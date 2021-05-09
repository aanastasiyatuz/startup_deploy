from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from facilities.views import *
from transport.views import *


schema_view = get_schema_view(
   openapi.Info(
      title="Travel Startup API",
      default_version='v1',
      description="Travel Startup",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router_rating = DefaultRouter()
router_rating.register('to_visit', RatingToVisitViewSet)
router_rating.register('to_eat', RatingToEatViewSet)
router_rating.register('to_stay', RatingToStayViewSet)

router_places = DefaultRouter()
router_places.register('places_to_visit', PlaceToVisitViewSet)
router_places.register('places_to_eat', PlaceToEatViewSet)
router_places.register('places_to_stay', PlaceToStayViewSet)

router_comment = DefaultRouter()
router_comment.register('to_visit', CommentToVisitViewSet)
router_comment.register('to_stay', CommentToStayViewSet)
router_comment.register('to_eat', CommentToEatViewSet)

router_like = DefaultRouter()
router_like.register('to_visit', LikeToVisitViewSet)
router_like.register('to_stay', LikeToStayViewSet)
router_like.register('to_eat', LikeToEatViewSet)

router_transport = DefaultRouter()
router_transport.register('', TransportViewSet)
router_transport.register('vehicle', VehicleViewSet)
router_transport.register('line', LineViewSet)
router_transport.register('timetable', TimetableViewSet)

router_trip = DefaultRouter()
router_trip.register('', TripViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('account/', include('account.urls')),
    path('news/', News.as_view(), name='news'),
    path('trip/', include(router_trip.urls)),
    path('facilities/', include(router_places.urls)),
    path('transport/', include(router_transport.urls)),
    path('comment/', include(router_comment.urls)),
    path('like/', include(router_like.urls)),
    path('rating/', include(router_rating.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

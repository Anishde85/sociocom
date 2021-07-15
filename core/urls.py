from django.contrib import admin
from django.urls import path, include
from users.views import register,logout_view,login_view
from users.roomidviews import roomno,createroom
from chat import views
from users import views as user_views,updateprofileviews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('register/',register,name='verify'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('profile/<str:username>/', user_views.profile, name='profile'),
    path('recommendations/', user_views.recommendations, name='recommendations'),
    path('profile/update', updateprofileviews.profileupd, name='updateprofile'),
    path('room/',roomno,name="roomno"),
    path('room/createroom/',createroom,name='createroom'),
]
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
from users.views import register,logout_view,login_view
from users import views as user_views,updateprofileviews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('register/',register,name='verify'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('profile/<str:username>/', user_views.profile, name='profile'),
    path('profile/update', updateprofileviews.profileupd, name='updateprofile'),
]
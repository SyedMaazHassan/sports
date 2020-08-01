from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('leagues/<leagueName>', views.per_league, name="leagues"),
    path('profile', views.profile, name="profile"),
    path('add_team', views.add_team, name="add_team"),
    path('add_player', views.add_player, name="add_player"),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

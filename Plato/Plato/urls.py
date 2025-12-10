"""
URL configuration for Plato project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Republic import views
from Republic.views import MovieDetailView
from django.conf import settings
from django.conf.urls.static import static
from Republic.views import SearchResultsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main', views.main),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('genres/', views.genres_list, name='genres_list'),
    path('genres/<int:genre_id>/', views.genre_detail, name='genre_detail'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

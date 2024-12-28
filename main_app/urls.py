from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library_blog.urls')),
    path('', include('books_by_categories.urls')),
    path('', include('Basket.urls')),
    path('', include('parser_app.urls')),
    path('', include('users.urls')),
    path('', include('recepti.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
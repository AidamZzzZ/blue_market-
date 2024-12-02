from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from products.views import home

urlpatterns = [
    path("", home, name="home"),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('products/', include("products.urls"))
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
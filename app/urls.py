from django.urls import path
from django.conf.urls.static import static
from vagadiya_exim_backend import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("products/", views.products, name="products"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

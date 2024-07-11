from django.urls import path
from django.conf.urls.static import static
from vagadiya_exim_backend import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path(
        "submit-contact-form",
        views.submit_contact_form,
        name="submit_contact_form",
    ),
    path("products/", views.products, name="products"),
    path("products/<int:pk>/", views.product_detail, name="product_detail"),
    path(
        "products/category/<int:pk>/",
        views.products_by_category,
        name="products_by_category",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import (
    HomePage,
    HomePageBottomBanner,
    HomePageServicesItem,
    HomePageProvidingsItem,
    ProvidingsItemPoint,
    AboutUsPage,
    AboutUsStory,
    AboutUsStoryValue,
    AboutUsPageBottomBanner,
    ContactPage,
    ContactDetails,
    ContactPageForm,
    ProductPageDetails,
    ProductCategory,
    Product,
)


def index(request):
    home_page = HomePage.objects.latest("id")
    home_page_services_items = HomePageServicesItem.objects.all()[:4]
    home_page_providings_items = HomePageProvidingsItem.objects.all()[:3]
    home_page_bottom_banner = HomePageBottomBanner.objects.latest("id")
    context = {
        "home_page": home_page,
        "home_page_services_items": home_page_services_items,
        "home_page_providings_items": home_page_providings_items,
        "home_page_bottom_banner": home_page_bottom_banner,
    }
    return render(request, "index.html", context)


def about(request):
    about_us_page = AboutUsPage.objects.latest("id")
    about_us_story = AboutUsStory.objects.latest("id")
    about_us_story_values = AboutUsStoryValue.objects.all()
    about_us_page_bottom_banner = AboutUsPageBottomBanner.objects.latest("id")
    context = {
        "about_us_page": about_us_page,
        "about_us_story": about_us_story,
        "about_us_story_values": about_us_story_values,
        "about_us_page_bottom_banner": about_us_page_bottom_banner,
    }
    return render(request, "about.html", context)


def contact(request):
    contact_page = ContactPage.objects.latest("id")
    contact_details = ContactDetails.objects.latest("id")
    context = {
        "contact_page": contact_page,
        "contact_details": contact_details,
    }
    return render(request, "contact.html", context)


def submit_contact_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact_number = request.POST.get("contact_number")
        email = request.POST.get("email")
        message = request.POST.get("message")
        ContactPageForm.objects.create(
            name=name,
            contact_number=contact_number,
            email=email,
            message=message,
        )
    return redirect(reverse("contact"))


def products_by_category(request, pk):
    product_page_details = ProductPageDetails.objects.latest("id")
    products = Product.objects.filter(category=pk)
    category = ProductCategory.objects.get(pk=pk)
    context = {
        "product_page_details": product_page_details,
        "products": products,
        "category": category,
        "is_category": True,
    }
    return render(request, "products.html", context)


def products(request):
    product_page_details = ProductPageDetails.objects.latest("id")
    products = Product.objects.all()
    context = {
        "product_page_details": product_page_details,
        "products": products,
    }
    return render(request, "products.html", context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    related_products = Product.objects.filter(category=product.category)[:4]
    product_page_details = ProductPageDetails.objects.latest("id")

    context = {
        "product": product,
        "related_products": related_products,
        "product_page_details": product_page_details,
    }
    return render(request, "product_detail.html", context)

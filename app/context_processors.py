from .models import ContactDetails, ProductCategory


def global_data(request):
    product_categories = ProductCategory.objects.all()
    contact_details = ContactDetails.objects.latest("id")
    return {
        "product_categories": product_categories,
        "contact_details": contact_details,
    }

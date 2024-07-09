from django.db import models


# Create your models here.
class HomePage(models.Model):
    top_banner_image = models.ImageField(upload_to="images")
    top_banner_title = models.CharField(max_length=100)
    top_banner_text = models.TextField()
    top_banner_button_text = models.CharField(max_length=50)
    section_one_title = models.CharField(max_length=100)
    section_two_title = models.CharField(max_length=100)
    section_two_text = models.TextField()

    def __str__(self):
        return

    class Meta:
        verbose_name = "Home Page Detail"
        verbose_name_plural = "Home Page Detail"


class HomePageBottomBanner(models.Model):
    bottom_banner_title = models.CharField(max_length=100)
    bottom_banner_text = models.TextField()
    bottom_banner_button_text = models.CharField(max_length=50)
    bottom_banner_point_one_number = models.IntegerField()
    bottom_banner_point_one_text = models.CharField(max_length=100)
    bottom_banner_point_two_number = models.IntegerField()
    bottom_banner_point_two_text = models.CharField(max_length=100)
    bottom_banner_point_three_number = models.IntegerField()
    bottom_banner_point_three_text = models.CharField(max_length=100)

    def __str__(self):
        return

    class Meta:
        verbose_name = "Home Page Bottom Banner"
        verbose_name_plural = "Home PageBottom Banner"


class HomePageServicesItem(models.Model):
    service_image = models.ImageField(upload_to="images")
    service_title = models.CharField(max_length=100)

    def __str__(self):
        return

    class Meta:
        verbose_name = "Home Page Services Item"
        verbose_name_plural = "Home Page Services Items"


class HomePageProvidingsItem(models.Model):
    providing_image = models.ImageField(upload_to="images")
    providing_title = models.CharField(max_length=100)
    providing_text = models.TextField()
    providing_button_text = models.CharField(max_length=50)

    def __str__(self):
        return

    class Meta:
        verbose_name = "Home Page Providings Item"
        verbose_name_plural = "Home Page Providings Items"


class AboutUsPage(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    point_one_title = models.CharField(max_length=100)
    point_one_number = models.IntegerField()
    point_two_title = models.CharField(max_length=100)
    point_two_number = models.IntegerField()
    point_three_title = models.CharField(max_length=100)
    point_three_number = models.IntegerField()
    button_text = models.CharField(max_length=50)
    video = models.FileField(upload_to="videos")

    def __str__(self):
        return

    class Meta:
        verbose_name = "About Us Page"
        verbose_name_plural = "About Us Page"


class AboutUsStory(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to="images")
    values_title = models.CharField(max_length=100)

    def __str__(self):
        return

    class Meta:
        verbose_name = "About Us Story"
        verbose_name_plural = "About Us Story"


class AboutUsStoryValue(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return

    class Meta:
        verbose_name = "About Us Story Value"
        verbose_name_plural = "About Us Story Values"


class AboutUsPageBottomBanner(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    button_text = models.CharField(max_length=50)

    def __str__(self):
        return

    class Meta:
        verbose_name = "About Us Page Bottom Banner"
        verbose_name_plural = "About Us Page Bottom Banner"


class ContactPage(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    download_catalog_title = models.CharField(max_length=100)
    catalog_pdf_title = models.CharField(max_length=100)
    catalog_pdf_link = models.CharField(max_length=100)
    catalog_doc_title = models.CharField(max_length=100)
    catalog_doc_link = models.CharField(max_length=100)

    def __str__(self):
        return

    class Meta:
        verbose_name = "Contact Page"
        verbose_name_plural = "Contact Page"


class ContactDetails(models.Model):
    title = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=100)

    def __str__(self):
        return

    class Meta:
        verbose_name = "Contact Details"
        verbose_name_plural = "Contact Details"


class ContactPageForm(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()
    submit_button_text = models.CharField(max_length=50)

    def __str__(self):
        return

    class Meta:
        verbose_name = "Contact Page Form"
        verbose_name_plural = "Contact Page Form"


class ProductCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    category = models.ForeignKey(
        ProductCategory, on_delete=models.SET_NULL, null=True
    )
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

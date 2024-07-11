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

    class Meta:
        verbose_name = "Home Page Detail"
        verbose_name_plural = "Home Page Detail"

    # delete old image on update
    def save(self, *args, **kwargs):
        try:
            this = HomePage.objects.get(id=self.id)
            if (
                this.top_banner_image != self.top_banner_image
                and this.top_banner_image
            ):
                this.top_banner_image.delete(save=False)
        except HomePage.DoesNotExist:
            pass
        super(HomePage, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.top_banner_image.delete(save=False)
        super(HomePage, self).delete(*args, **kwargs)

    def __str__(self):
        return self.top_banner_title


class HomePageBottomBanner(models.Model):
    bottom_banner_title = models.CharField(max_length=100)
    bottom_banner_text = models.TextField()
    bottom_banner_button_text = models.CharField(max_length=50)
    bottom_banner_point_one_number = models.CharField(max_length=100)
    bottom_banner_point_one_text = models.CharField(max_length=100)
    bottom_banner_point_two_number = models.CharField(max_length=100)
    bottom_banner_point_two_text = models.CharField(max_length=100)
    bottom_banner_point_three_number = models.CharField(max_length=100)
    bottom_banner_point_three_text = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Home Page Bottom Banner"
        verbose_name_plural = "Home PageBottom Banner"


class HomePageServicesItem(models.Model):
    service_image = models.ImageField(upload_to="images")
    service_title = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Home Page Services Item"
        verbose_name_plural = "Home Page Services Items"

    # delete old image on update
    def save(self, *args, **kwargs):
        try:
            this = HomePageServicesItem.objects.get(id=self.id)
            if this.service_image != self.service_image and this.service_image:
                this.service_image.delete(save=False)
        except HomePageServicesItem.DoesNotExist:
            pass
        super(HomePageServicesItem, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.service_image.delete(save=False)
        super(HomePageServicesItem, self).delete(*args, **kwargs)


class ProvidingsItemPoint(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Providings Item Point List"
        verbose_name_plural = "Providings Item Point List"


class HomePageProvidingsItem(models.Model):
    providing_image = models.ImageField(upload_to="images")
    providing_title = models.CharField(max_length=100)
    providing_text = models.TextField()
    providing_button_text = models.CharField(max_length=50)
    providing_points_list = models.ManyToManyField(
        ProvidingsItemPoint,
        blank=True,
        related_name="provinding_item_points",
    )

    class Meta:
        verbose_name = "Home Page Providings Item"
        verbose_name_plural = "Home Page Providings Items"

    # delete old image on update
    def save(self, *args, **kwargs):
        try:
            this = HomePageProvidingsItem.objects.get(id=self.id)
            if (
                this.providing_image != self.providing_image
                and this.providing_image
            ):
                this.providing_image.delete(save=False)
        except HomePageProvidingsItem.DoesNotExist:
            pass
        super(HomePageProvidingsItem, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.providing_image.delete(save=False)
        super(HomePageProvidingsItem, self).delete(*args, **kwargs)


class AboutUsPage(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    point_one_title = models.CharField(max_length=100)
    point_one_number = models.CharField(max_length=100)
    point_two_title = models.CharField(max_length=100)
    point_two_number = models.CharField(max_length=100)
    point_three_title = models.CharField(max_length=100)
    point_three_number = models.CharField(max_length=100)
    button_text = models.CharField(max_length=50)
    video = models.FileField(upload_to="videos")

    class Meta:
        verbose_name = "About Us Page"
        verbose_name_plural = "About Us Page"

    # delete old video on update
    def save(self, *args, **kwargs):
        try:
            this = AboutUsPage.objects.get(id=self.id)
            if this.video != self.video and this.video:
                this.video.delete(save=False)
        except AboutUsPage.DoesNotExist:
            pass
        super(AboutUsPage, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.video.delete(save=False)
        super(AboutUsPage, self).delete(*args, **kwargs)


class AboutUsStory(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to="images")
    values_title = models.CharField(max_length=100)

    class Meta:
        verbose_name = "About Us Story"
        verbose_name_plural = "About Us Story"

    # delete old image on update
    def save(self, *args, **kwargs):
        try:
            this = AboutUsStory.objects.get(id=self.id)
            if this.image != self.image and this.image:
                this.image.delete(save=False)
        except AboutUsStory.DoesNotExist:
            pass
        super(AboutUsStory, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(AboutUsStory, self).delete(*args, **kwargs)


class AboutUsStoryValue(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About Us Story Value"
        verbose_name_plural = "About Us Story Values"


class AboutUsPageBottomBanner(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    button_text = models.CharField(max_length=50)

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

    class Meta:
        verbose_name = "Contact Details"
        verbose_name_plural = "Contact Details"


class ContactPageForm(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    contact_number = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Contact Page Form"
        verbose_name_plural = "Contact Page Form"


class ProductPageDetails(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    product_button_text = models.CharField(max_length=50, null=True)
    related_products_text = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = "Product Page Details"
        verbose_name_plural = "Product Page Details"


class ProductCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_1 = models.ImageField(upload_to="products_images", null=True)
    image_2 = models.ImageField(upload_to="products_images", null=True)
    image_3 = models.ImageField(upload_to="products_images", null=True)
    image_4 = models.ImageField(upload_to="products_images", null=True)
    image_5 = models.ImageField(upload_to="products_images", null=True)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.SET_NULL, null=True
    )
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    # delete old images on update
    def save(self, *args, **kwargs):
        try:
            this = Product.objects.get(id=self.id)
            if this.image_1 != self.image_1 and this.image_1:
                this.image_1.delete(save=False)
            if this.image_2 != self.image_2 and this.image_2:
                this.image_2.delete(save=False)
            if this.image_3 != self.image_3 and this.image_3:
                this.image_3.delete(save=False)
            if this.image_4 != self.image_4 and this.image_4:
                this.image_4.delete(save=False)
            if this.image_5 != self.image_5 and this.image_5:
                this.image_5.delete(save=False)
        except Product.DoesNotExist:
            pass
        super(Product, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image_1.delete(save=False)
        self.image_2.delete(save=False)
        self.image_3.delete(save=False)
        self.image_4.delete(save=False)
        self.image_5.delete(save=False)
        super(Product, self).delete(*args, **kwargs)

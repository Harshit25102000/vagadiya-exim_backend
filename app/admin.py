from django.contrib import admin
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
    ProductCategory,
    Product,
)


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = (
        "top_banner_title",
        "section_one_title",
        "section_two_title",
    )
    search_fields = (
        "top_banner_title",
        "section_one_title",
        "section_two_title",
    )


@admin.register(HomePageBottomBanner)
class HomePageBottomBannerAdmin(admin.ModelAdmin):
    list_display = ("bottom_banner_title", "bottom_banner_button_text")
    search_fields = ("bottom_banner_title",)


@admin.register(HomePageServicesItem)
class HomePageServicesItemAdmin(admin.ModelAdmin):
    list_display = ("service_title",)
    search_fields = ("service_title",)


@admin.register(ProvidingsItemPoint)
class ProvidingsItemPointAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(HomePageProvidingsItem)
class HomePageProvidingsItemAdmin(admin.ModelAdmin):
    list_display = ("providing_title",)
    search_fields = ("providing_title",)


@admin.register(AboutUsPage)
class AboutUsPageAdmin(admin.ModelAdmin):
    list_display = ("title", "button_text")
    search_fields = ("title", "button_text")


@admin.register(AboutUsStory)
class AboutUsStoryAdmin(admin.ModelAdmin):
    list_display = ("title", "values_title")
    search_fields = ("title", "values_title")


@admin.register(AboutUsStoryValue)
class AboutUsStoryValueAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(AboutUsPageBottomBanner)
class AboutUsPageBottomBannerAdmin(admin.ModelAdmin):
    list_display = ("title", "button_text")
    search_fields = ("title", "button_text")


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ("title", "download_catalog_title")
    search_fields = ("title", "download_catalog_title")


@admin.register(ContactDetails)
class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ("title", "phone_number", "email")
    search_fields = ("title", "phone_number", "email")


@admin.register(ContactPageForm)
class ContactPageFormAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "submit_button_text")
    search_fields = ("name", "email")


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "category")
    search_fields = ("title", "category__title")
    list_filter = ("category",)

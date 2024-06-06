from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('shopping_bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('favourites/', include('favourites.urls')),
    path('contact_page/', include('contact.urls')),
    path('testimonials/', include('testimonials.urls')),
    path('profiles/', include('profiles.urls')),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt", content_type="text/plain")
        ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Set custom handler for 404 and 500 errors
handler404 = 'kiddie_corner.views.error_404'
handler500 = 'kiddie_corner.views.error_500'

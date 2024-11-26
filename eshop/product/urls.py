from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    # Routes pour les produits
    path('products/', views.get_products, name="products"),
    path('products/<int:pk>/', views.get_product, name="get_product_details"),
]

# Ajouter cette ligne pour servir les fichiers médias en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


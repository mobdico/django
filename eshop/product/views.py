from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .filters import ProductsFilter
from .serializers import ProductSerializer
from .models import Product

# Create your views here.

@api_view(['GET'])
def get_products(request):
    # Appliquer le filtre sur les produits
    filterset = ProductsFilter(request.GET, queryset=Product.objects.all().order_by('id'))

    # Pagination
    resPerPage = 11  # Définir le nombre de produits par page

    paginator = PageNumberPagination()
    paginator.page_size = resPerPage

    queryset = paginator.paginate_queryset(filterset.qs, request)

    # Sérialiser les produits, y compris l'image
    serializer = ProductSerializer(queryset, many=True)

    # Retourner la réponse avec les produits paginés et sérialisés
    return Response({ "products": serializer.data })


@api_view(['GET'])
def get_product(request, pk):
    # Récupérer un produit spécifique
    product = get_object_or_404(Product, id=pk)

    # Sérialiser le produit, y compris l'image
    serializer = ProductSerializer(product, many=False)

    # Retourner la réponse avec le produit sérialisé
    return Response({ "products": serializer.data })

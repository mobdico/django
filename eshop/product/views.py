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

    filterset = ProductsFilter(request.GET, queryset=Product.objects.all().order_by('id'))

    #Pagination 

    resPerPage = 5

    paginator = PageNumberPagination()

    paginator.page_size = resPerPage

    queryset = paginator.paginate_queryset(filterset.qs, request)

    serializer = ProductSerializer(queryset, many=True)

    return Response({ "products": serializer.data })



@api_view(['GET'])
def get_product(request, pk):

    product = get_object_or_404(Product, id=pk)
   #Je sérialise le produit
    serializer = ProductSerializer(product, many=False)

    return Response({ "products": serializer.data })
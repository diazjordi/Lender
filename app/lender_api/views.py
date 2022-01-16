from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from lender_api.models import Borrower, Item, Transaction
from lender_api.serializers import BorrowerSerializer, ItemSerializer, TransactionSerializer
from rest_framework.decorators import api_view

# All media listing page


def index(request):
    print("<---------You Made It!--------->")
    return HttpResponse("<---------You Made It!--------->")
    #queryset = Item.objects.all()
    # return render(request, "lendr/index.html", {'item': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'lender/index.html'

    def get(self, request):
        queryset = Item.objects.all()
        return Response({'item': queryset})


class list_all_items(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'lender/items_list.html'

    def get(self, request):
        queryset = Item.objects.all()
        return Response({'item': queryset})


@api_view(['GET', 'POST', 'DELETE'])
def items_list(request):
    if request.method == 'GET':
        items = Item.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            items = items.filter(title__icontains=title)

        items_serializer = ItemSerializer(items, many=True)
        return JsonResponse(items_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        item_serializer = ItemSerializer(data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse(item_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(item_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Item.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Items were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE', 'UPDATE'])
def borrow_item(request):
    # check request type

    # verify borrower allowed

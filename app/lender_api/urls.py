from django.urls import path
from lender_api import views as lender_api_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', lender_api_views.index.as_view(), name='home'),
    path('lender/items/', lender_api_views.items_list, name='items'),
    #path('lender/borrow/', lender_api_views.borrow_item,)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

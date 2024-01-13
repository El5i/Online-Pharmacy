# PharmacyApp/urls.py
from django.urls import path
from .views import home, RegistrationView, login_view, manager_page, client_page, magazine_view, register_supplier_view, register_product_view, manager_registration_view , product_registration , product_list, supplier_registration, supplier_list, buy_product, transaction_history


urlpatterns = [
    path('', home, name='home'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('register/manager/', manager_registration_view, name='manager_registration'),  
    path('login/', login_view, name='login'),  
    path('managerpage/', manager_page, name='manager_page'),
    path('clientpage/', client_page, name='client_page'),
    path('magazine/', magazine_view, name='magazine'),
    path('register_supplier/', register_supplier_view, name='register_supplier'),
    path('register_product/', register_product_view, name='register_product'),
    path('product-registration/', product_registration, name='product_registration'),
    path('product-list/', product_list, name='product_list'),
    path('supplier-registration/', supplier_registration, name='supplier_registration'),
    path('supplier-list/', supplier_list, name='supplier_list'),
    path('buy-product/', buy_product, name='buy_product'),
   path('transaction-history/', transaction_history, name='transaction_history'),
    # Add other URL patterns as needed
]


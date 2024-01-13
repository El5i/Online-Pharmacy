# PharmacyApp/urls.py
from django.urls import path
from .views import home, RegistrationView, login_view, manager_page, client_page, magazine_view, register_supplier_view, register_product_view, manager_registration_view


urlpatterns = [
    path('', home, name='home'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('register/manager/', manager_registration_view, name='manager_registration'),  # Moved up
    path('login/', login_view, name='login'),  # Moved down
    path('managerpage/', manager_page, name='manager_page'),
    path('clientpage/', client_page, name='client_page'),
    path('magazine/', magazine_view, name='magazine'),
    path('register_supplier/', register_supplier_view, name='register_supplier'),
    path('register_product/', register_product_view, name='register_product'),
    # Add other URL patterns as needed
]


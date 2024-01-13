

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import *

# Create your views here.


def home(request):
    return render(request, 'PharmacyApp/home.html')


@login_required
def manager_page(request):
    return render(request, 'PharmacyApp/managerpage.html')


@login_required
def client_page(request):
    return render(request, 'PharmacyApp/clientpage.html')


class RegistrationView(View):
    template_name = 'PharmacyApp/register.html'

    def get(self, request):
        form = RegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect to the home page or any desired page after registration
            return redirect('home')
        return render(request, self.template_name, {'form': form})




def login_view(request):
    msg = None
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                print(f"User: {user.username}, is_client: {user.is_client}, is_manager: {user.is_manager}")

                login(request, user)

                if user.is_client:
                    print("Redirecting to client_page")
                    return redirect('client_page')
                elif user.is_manager:
                    print("Redirecting to manager_page")
                    return redirect('manager_page')
                else:
                    # Redirect to a generic page or display an error message
                    messages.error(request, "Invalid user type.")
                    print("Redirecting to home")
                    return redirect('home')
            else:
                msg = "Invalid Login Credentials"
        else:
            msg = 'Form Error'

    return render(request, 'PharmacyApp/login_view.html', {'form': form, 'msg': msg})



def magazine_view(request):
    supplier_form = SupplierForm()
    product_form = ProductForm()
    return render(request, 'PharmacyApp/magazine.html', {'supplier_form': supplier_form, 'product_form': product_form})


def register_supplier_view(request):
    if request.method == 'POST':
        supplier_form = SupplierForm(request.POST)
        if supplier_form.is_valid():
            supplier_form.save()
            return redirect('magazine')
    else:
        supplier_form = SupplierForm()
    return render(request, 'PharmacyApp/magazine.html', {'supplier_form': supplier_form})


def register_product_view(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return redirect('magazine')
    else:
        product_form = ProductForm()
    return render(request, 'PharmacyApp/magazine.html', {'product_form': product_form})





def manager_registration_view(request):
    template_name = 'PharmacyApp/manager_registration.html'

    if request.method == 'POST':
        form = ManagerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_manager = True
            user.is_client = False
            user.role = 'Manager'
            user.save()

            login(request, user)  # Log in the user after registration
            return redirect('home')  # Redirect to the home page (customize as needed)
    else:
        form = ManagerRegistrationForm()

    return render(request, template_name, {'form': form})

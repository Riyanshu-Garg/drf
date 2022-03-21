"""DjangoEcommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from DjangoEcommerceApp import views
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    #authentication
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh',TokenRefreshView.as_view()),


    #USERS
    path('customUsers/',views.CustomUser_list_Create.as_view()),
    path('customUsers/<int:pk>/',views.CustomUser_list_Retrive.as_view()),

    path('staffUsers/',views.StaffUser_list_Create.as_view()),
    path('staffssers/<int:pk>/',views.StaffUser_list_Retrive.as_view()),

    path('adminusers/',views.AdminUser_list_Create.as_view()),
    path('adminusers/<int:pk>/',views.AdminUser_list_Retrive.as_view()),

    path('merchantusers/',views.MerchantUser_list_Create.as_view()),
    path('merchantusers/<int:pk>/',views.MerchantUser_list_Retrive.as_view()),

    path('customerusers/',views.CustomerUser_list_Create.as_view()),
    path('customerusers/<int:pk>/',views.CustomerUser_list_Retrive.as_view()),
    
    #categories
    path('categories/',views.Categories_list_Create.as_view()),
    path('categories/<int:pk>/',views.Categories_list_Retrive.as_view()),

    #subcategories
    path('subcategories/',views.SubCategories_list_Create.as_view()),
    path('subcategories/<int:pk>/',views.SubCategories_list_Retrive.as_view()),

    #products
    path('products/',views.Products_list_Create.as_view()),
    path('products/<int:pk>/',views.Products_list_Retrive.as_view()),

    #ABOUT
    path('products_about/',views.ProductAbout_list_Create.as_view()),
    path('products_about/<int:pk>/',views.ProductAbout_list_Retrive.as_view()),

    path('products_details/',views.ProductDetails_list_Create.as_view()),
    path('products_details/<int:pk>/',views.ProductDetails_list_Retrive.as_view()),

    path('product_varient/',views.ProductVarient_list_Create.as_view()),
    path('product_varient/<int:pk>/',views.ProductVarient_list_Retrive.as_view()),

    path('product_varient_items/',views.ProductsVarientsItems_list_Create.as_view()),
    path('product_varient_items/<int:pk>/',views.ProductsVarientsItems_list_Retrive.as_view()),

    path('produts_media/',views.ProductsMedia_Create.as_view()),
    path('products_media/<int:pk>/',views.ProductsMedia_Retrive.as_view()),

    path('troducts_transactions/',views.ProductsTransaction_Create.as_view()),
    path('products_transactions/<int:pk>/',views.ProductsTransaction_Retrive.as_view()),

    path('products_tags/',views.ProductsTgs_list_Create.as_view()),
    path('products_tags/<int:pk>/',views.ProductsTgs_list_Retrive.as_view()),

    path('products_questions/',views.ProductsQuestions_list_Create.as_view()),
    path('products_questions/<int:pk>/',views.ProductsQuestions_list_Retrive.as_view()),

    path('products_reviews/',views.ProductsReviews_list_Create.as_view()),
    path('products_reviews/<int:pk>/',views.ProductsReviews_list_Retrive.as_view()),

    path('product_review_voting/',views.ProductReviewVoting_list_Create.as_view()),
    path('product_review_voting/<int:pk>/',views.ProductReviewVoting_list_Retrive.as_view()),

    #ORDERS
    path('cart/',views.CustomerOrders_list_Create.as_view()),
    path('cart/<int:pk>/',views.CustomerOrders_list_Retrive.as_view()),

    path('orders/',views.AllOrders_list_Create.as_view()),
    path('orders/<int:pk>/',views.AllOrders_list_Retrive.as_view()),

    #DELIVERY STATUS
    path('order_delivery_status/',views.OrderDeliveryStatus_list_Create.as_view()),
    path('order_delivery_status/<int:pk>/',views.OrderDeliveryStatus_list_Retrive.as_view()),
]
    
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView , ListCreateAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


#custom user
class CustomUser_list_Create(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [OrderingFilter]
    ordering_fields='__all__'

class CustomUser_list_Retrive(RetrieveUpdateDestroyAPIView):#viewsets.ReadOnlyModelViewSet
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [OrderingFilter]
    ordering_fields='__all__'
   

#ADMIN USER
class AdminUser_list_Create(ListCreateAPIView):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer
    filter_backends = [OrderingFilter]
    ordering_fields='__all__'

class AdminUser_list_Retrive(RetrieveUpdateDestroyAPIView):#viewsets.ReadOnlyModelViewSet
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer
    filter_backends = [OrderingFilter]
    ordering_fields='__all__'


#MERCHANT USER
class MerchantUser_list_Create(ListCreateAPIView):
    queryset = MerchantUser.objects.all()
    serializer_class = MerchantUserSerializer
    filter_backends = [OrderingFilter]
    ordering_fields='__all__'

class MerchantUser_list_Retrive(RetrieveUpdateDestroyAPIView):#viewsets.ReadOnlyModelViewSet
    queryset = MerchantUser.objects.all()
    serializer_class = MerchantUserSerializer
    filter_backends = [OrderingFilter]
    ordering_fields='__all__'


#STAFF USER
class StaffUser_list_Create(ListCreateAPIView):
    queryset = StaffUser.objects.all()
    serializer_class = StaffUserSerializer
    filter_backends = [OrderingFilter]
    ordering_fields='__all__'

class StaffUser_list_Retrive(RetrieveUpdateDestroyAPIView):#viewsets.ReadOnlyModelViewSet
    queryset = StaffUser.objects.all()
    serializer_class = StaffUserSerializer
    filter_backends = [OrderingFilter]
    ordering_fields='__all__'


#CUSTOMER USER
class CustomerUser_list_Create(ListCreateAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = CustomerUserSerializer
    filter_backends = [OrderingFilter]
    ordering_fields='__all__'

class CustomerUser_list_Retrive(RetrieveUpdateDestroyAPIView):#viewsets.ReadOnlyModelViewSet
    queryset = CustomerUser.objects.all()
    serializer_class = CustomerUserSerializer
    filter_backends = [OrderingFilter]
    ordering_fields='__all__'


#CATEGORIES
class Categories_list_Create(ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    filter_backends = [OrderingFilter]
    ordering_fields='__all__'

class Categories_list_Retrive(RetrieveUpdateDestroyAPIView):#viewsets.ReadOnlyModelViewSet
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields='__all__'
    

#SUBCATEGORIES 
class SubCategories_list_Create(ListCreateAPIView):
    queryset = SubCategories.objects.all()
    serializer_class = SubCategoriesSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields='__all__'

class SubCategories_list_Retrive(RetrieveUpdateDestroyAPIView):
    queryset = SubCategories.objects.all()
    serializer_class = SubCategoriesSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields='__all__'


#PRODUCT 
class Products_list_Create(ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['product_name','brand']
    ordering_fields='__all__'

class Products_list_Retrive(RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields='__all__'


#PRODUCT_VARIENT  
class ProductVarient_list_Create(ListCreateAPIView):
    queryset = ProductVarient.objects.all()
    serializer_class = ProductVarientSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields='__all__'

class ProductVarient_list_Retrive(RetrieveUpdateDestroyAPIView):
    queryset = ProductVarient.objects.all()
    serializer_class = ProductVarientSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields='__all__'


#PRODUCT_VARIENT_ITEM 
class ProductsVarientsItems_list_Create(ListCreateAPIView):
    queryset = ProductsVarientsItems.objects.all()
    serializer_class = ProductsVarientsItemsSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields='__all__'

class ProductsVarientsItems_list_Retrive(RetrieveUpdateDestroyAPIView):
    queryset = ProductsVarientsItems.objects.all()
    serializer_class = ProductsVarientsItemsSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields='__all__'
    

#PRODUCT MEDIA
class ProductsMedia_Create(ListCreateAPIView):
    queryset = ProductsMedia.objects.all()
    serializer_class = ProductsMediaSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields='__all__'

class ProductsMedia_Retrive(RetrieveUpdateDestroyAPIView):
    queryset = ProductsMedia.objects.all()
    serializer_class = ProductsMediaSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields='__all__'


#PRODUCT TRANSACTION
class ProductsTransaction_Create(ListCreateAPIView):
    queryset = ProductsTransaction.objects.all()
    serializer_class = ProductsTransactionSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields='__all__'

class ProductsTransaction_Retrive(RetrieveUpdateDestroyAPIView):
    queryset = ProductsTransaction.objects.all()
    serializer_class = ProductsTransactionSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields='__all__'
     

#PRODUCT DETAILS
class ProductDetails_list_Create(ListCreateAPIView):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields='__all__'

class ProductDetails_list_Retrive(RetrieveUpdateDestroyAPIView):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields='__all__'


#PRODUCT ABOUT
class ProductAbout_list_Create(ListCreateAPIView):
    queryset = ProductAbout.objects.all()
    serializer_class = ProductAboutSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields='__all__'

class ProductAbout_list_Retrive(RetrieveUpdateDestroyAPIView):
    queryset = ProductAbout.objects.all()
    serializer_class = ProductAboutSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields='__all__'
    

#PRODUCT TAGS
class ProductsTgs_list_Create(ListCreateAPIView):
    queryset = ProductsTgs.objects.all()
    serializer_class = ProductsTgsSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['titile']
    ordering_fields='__all__'

class ProductsTgs_list_Retrive(RetrieveUpdateDestroyAPIView):
    queryset = ProductsTgs.objects.all()
    serializer_class = ProductsTgsSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['titile']
    ordering_fields='__all__'


#PRODUCTS QUESTIONS
class ProductsQuestions_list_Create(ListCreateAPIView):
    queryset = ProductsQuestions.objects.all()
    serializer_class = ProductsQuestionsSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['titile']
    ordering_fields='__all__'

class ProductsQuestions_list_Retrive(RetrieveUpdateDestroyAPIView):
    queryset = ProductsQuestions.objects.all()
    serializer_class = ProductsQuestionsSerializer   
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['titile']
    ordering_fields='__all__'


#PRODUCT REVIEW
class ProductsReviews_list_Create(ListCreateAPIView):
    queryset = ProductsReviews.objects.all()
    serializer_class = ProductsReviewsSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['titile']
    ordering_fields='__all__'

class ProductsReviews_list_Retrive(RetrieveUpdateDestroyAPIView):
    queryset = ProductsReviews.objects.all()
    serializer_class = ProductsReviewsSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['titile']
    ordering_fields='__all__' 


#REVIEWS VOTINGS
class ProductReviewVoting_list_Create(ListCreateAPIView):
    queryset = ProductReviewVoting.objects.all()
    serializer_class = ProductReviewVotingSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['titile']
    ordering_fields='__all__'

class ProductReviewVoting_list_Retrive(RetrieveUpdateDestroyAPIView):
    queryset = ProductReviewVoting.objects.all()
    serializer_class = ProductReviewVotingSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['titile']
    ordering_fields='__all__'


# CUSTOMER ORDERS  
class CustomerOrders_list_Create(ListCreateAPIView):
    queryset = CustomerOrders.objects.all()
    serializer_class = CustomerOrdersSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['titile']
    ordering_fields='__all__'
    
class CustomerOrders_list_Retrive(RetrieveUpdateDestroyAPIView):
    queryset = CustomerOrders.objects.all()
    serializer_class = CustomerOrdersSerializer
    
class AllOrders_list_Create(ListCreateAPIView):
    queryset = AllOrders.objects.all()
    serializer_class = AllOrdersSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['titile']
    ordering_fields='__all__'
    
class AllOrders_list_Retrive(RetrieveUpdateDestroyAPIView):
    queryset = AllOrders.objects.all()
    serializer_class = AllOrdersSerializer

#ORDER DELIVERY STATUS
class OrderDeliveryStatus_list_Create(ListCreateAPIView):
    queryset = OrderDeliveryStatus.objects.all()
    serializer_class = OrderDeliveryStatusSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['titile']
    ordering_fields='__all__'
      
class OrderDeliveryStatus_list_Retrive(RetrieveUpdateDestroyAPIView):
    queryset = OrderDeliveryStatus.objects.all()
    serializer_class = OrderDeliveryStatusSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['titile']
    ordering_fields='__all__'
      


@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminUser.objects.create(auth_user_id=instance)
        if instance.user_type==2:
            StaffUser.objects.create(auth_user_id=instance)
        if instance.user_type==3:
            MerchantUser.objects.create(auth_user_id=instance,company_name="",gst_details="",address="")
        if instance.user_type==4:
            CustomerUser.objects.create(auth_user_id=instance)

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
            instance.adminuser.save()
    if instance.user_type==2:
            instance.staffuser.save()
    if instance.user_type==3:
            instance.merchantuser.save()
    if instance.user_type==4:
            instance.customeruser.save()


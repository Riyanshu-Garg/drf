from .models import *
from rest_framework import serializers
 
class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
        model = CustomUser
        fields = '__all__'

class AdminUserSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = AdminUser
        fields = '__all__'
     def create(self, validate_data):
         return AdminUser.objects.create(**validate_data)   
     
class StaffUserSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = StaffUser
        fields = '__all__'
        
     def create(self, validate_data):
         return StaffUser.objects.create(**validate_data)   

class MerchantUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MerchantUser
        fields = '__all__'
    def create(self, validate_data):
         return MerchantUser.objects.create(**validate_data)   

class CustomerUserSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = CustomerUser
        fields = '__all__'
     def create(self, validate_data):
        return CustomerUser.objects.create(**validate_data)


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Categories
        fields = '__all__'
     def create(self, validate_data):
        return Categories.objects.create(**validate_data)
     def update(self, instance, validated_data):
        instance.title = validated_data.get('roll',instance.title)
        instance.save()
        return instance

class SubCategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategories
        fields = '__all__'
    def create(self, validate_data):
        return SubCategories.objects.create(**validate_data)



class ProductsSerializer(serializers.HyperlinkedModelSerializer):
     ProductAbout = serializers.StringRelatedField(many= True, read_only = True)
     ProductVarient = serializers.HyperlinkedRelatedField(many= True, read_only = True, view_name='varient-detail')
     class Meta:
        model = Products
        fields = '__all__'
     def create(self, validate_data):
        return  Products.objects.create(**validate_data)

class ProductsMediaSerializer(serializers.HyperlinkedModelSerializer):
     def create(self, validate_data):
        return  ProductsMedia.objects.create(**validate_data)
     
     class Meta:
        model = ProductsMedia
        fields = '__all__'

class ProductsTransactionSerializer(serializers.HyperlinkedModelSerializer):
    
    def create(self, validate_data):
        return ProductsTransaction.objects.create(**validate_data)
    
    class Meta:
        model = ProductsTransaction
        fields = '__all__'

class ProductDetailsSerializer(serializers.HyperlinkedModelSerializer):
     product = serializers.StringRelatedField(many= True, read_only = True)
     class Meta:
        model = ProductDetails
        fields = '__all__'
     def create(self, validate_data):
        return ProductDetails.objects.create(**validate_data)

class ProductAboutSerializer(serializers.HyperlinkedModelSerializer):
     product = serializers.StringRelatedField(many= True, read_only = True)
     class Meta:
        model = ProductAbout
        fields = '__all__'
     def create(self, validate_data):
        return ProductAbout.objects.create(**validate_data)

class ProductsTgsSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = ProductsTgs
        fields = '__all__'
     def create(self, validate_data):
        return ProductsTgs.objects.create(**validate_data)

class ProductsQuestionsSerializer(serializers.HyperlinkedModelSerializer):
     product = serializers.StringRelatedField(many= True, read_only = True)
     class Meta:
        model = ProductsQuestions
        fields = '__all__'
 
     def create(self, validate_data):
        return ProductsQuestions.objects.create(**validate_data)

class ProductsReviewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductsReviews
        fields = '__all__'
    def create(self, validate_data):
        return ProductsReviews.objects.create(**validate_data)

class ProductReviewVotingSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model =ProductReviewVoting
        fields = '__all__'
     def create(self, validate_data):
        return ProductReviewVoting.objects.create(**validate_data)

class ProductVarientSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = ProductVarient
        fields = '__all__'
     def create(self, validate_data):
        return ProductVarient.objects.create(**validate_data)

class ProductsVarientsItemsSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = ProductsVarientsItems
        fields = '__all__'
     def create(self, validate_data):
        return ProductsVarientsItems.objects.create(**validate_data)



class CustomerOrdersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerOrders
        fields = '__all__'
    def create(self, validate_data):
        return CustomerOrders.objects.create(**validate_data)


class AllOrdersSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
        model = AllOrders
        fields = '__all__'
   def create(self, validate_data):
        return AllOrders.objects.create(**validate_data)

class OrderDeliveryStatusSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = OrderDeliveryStatus
        fields = '__all__'
     def create(self, validate_data):
        return OrderDeliveryStatus.objects.create(**validate_data)



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
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractUser , PermissionsMixin, User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Avg
# Create your models here.

class CustomUser(AbstractUser,PermissionsMixin):
    username = None
    UserNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # = CustomUserManager()
    user_type_choices = (1,"Admin"),(2,"Staff"),(3,"Merchant"),(4,"Customer")
    user_type = models.CharField(max_length=255,choices =user_type_choices,default=1)

class AdminUser(models.Model):
    profile_pic= models.FileField(default="")
    auth_user_id=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)

class StaffUser(models.Model):
    profile_pic= models.FileField(default="")
    auth_user_id=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)

class MerchantUser(models.Model):
    profile_pic= models.FileField(default="")
    auth_user_id=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=255)
    address=models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)

class CustomerUser(models.Model):
    auth_user_id=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    profile_pic= models.FileField(default="")
    address = models.TextField(),
    created_at= models.DateTimeField(auto_now_add=True)


class Categories(models.Model):
    id= models.AutoField(primary_key=True)
    title= models.CharField(max_length=255)
    url_slug= models.CharField(max_length=255)
    thumbnail= models.FileField()
    description=models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default= 1)

class SubCategories(models.Model):
    id= models.AutoField(primary_key=True)
    category_id= models.ForeignKey(Categories,on_delete=models.CASCADE)
    title= models.CharField(max_length=255)
    url_slug= models.CharField(max_length=255)
    thumbnail= models.FileField()
    description=models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default= 1)

class Products(models.Model):
    id= models.AutoField(primary_key=True)
    url_slug=models.CharField(max_length=255)
    subcategories_id=models.ForeignKey(SubCategories,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=255)
    brand=models.CharField(max_length=255)
    product_max_price=models.CharField(max_length=255)
    product_discount_price=models.CharField(max_length=255)
    product_description=models.TextField()
    product_long_description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    added_by_merchant=models.ForeignKey(MerchantUser,on_delete=models.CASCADE)
    in_stock_total=models.IntegerField(default=1)
    is_active=models.IntegerField(default= 1)

class ProductsMedia(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    media_type_choice=((1,"Image"),(2,"Video"))
    media_type=models.CharField(max_length=255)
    media_content=models.FileField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default= 1)

class ProductsTransaction(models.Model):
    id=models.AutoField(primary_key=True)
    transaction_type_choices=((1,"buy"),(2,"Sell"))
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    transaction_product_count=models.IntegerField(default=1)
    transaction_type=models.CharField(choices=transaction_type_choices,max_length=255)
    transaction_description=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)


class ProductDetails(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    titile=models.CharField(max_length=255)
    titile_details=models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default= 1)

class ProductAbout(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    titile=models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default= 1)

class ProductsTgs(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    titile=models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default= 1)

class ProductsQuestions(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    user_id=models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    question=models.TextField()
    answer=models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default= 1)

class ProductsReviews(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    user_id=models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    review_image=models.FileField()
    rating=models.CharField(default="5",max_length=255)
    review=models.TextField(default="")
    rating_avg = Avg('rating')
    created_at=models.DateTimeField(auto_now_add=True)
    is_active= models.IntegerField(default= 1)

class ProductReviewVoting(models.Model):
    id=models.AutoField(primary_key=True)
    product_review_id=models.ForeignKey(ProductsReviews, on_delete=models.CASCADE)
    user_id_voting=models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default= 1)

class ProductVarient(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)

class ProductsVarientsItems(models.Model):
    id=models.AutoField(primary_key=True)
    product_varient_id=models.ForeignKey(ProductVarient,on_delete=models.CASCADE)
    products_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)

class CustomerOrders(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Products,on_delete=models.DO_NOTHING)
    purchase_price=models.CharField(max_length=255)
    coupan_code=models.CharField(max_length=255)
    discount_amt=models.CharField(max_length=255)  #amount_discount
    products_status=models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)

class AllOrders(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Products,on_delete=models.DO_NOTHING)
    purchase_price=models.CharField(max_length=255)
    products_status=models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)


class OrderDeliveryStatus(models.Model):
    id=models.AutoField(primary_key=True)
    order_id=models.ForeignKey(CustomerOrders,on_delete=models.CASCADE)
    status=models.CharField(max_length=255)
    status_message=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

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
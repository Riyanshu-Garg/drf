from django.contrib import admin
from DjangoEcommerceApp.models import *
# Register your models here.

#users
admin.site.register(CustomUser)
admin.site.register(StaffUser)
admin.site.register(AdminUser)
admin.site.register(MerchantUser)
admin.site.register(CustomerUser)

#categories
admin.site.register(Categories)
admin.site.register(SubCategories)

#products
admin.site.register(Products)
admin.site.register(ProductsMedia)
admin.site.register(ProductsTransaction)
admin.site.register(ProductDetails)
admin.site.register(ProductAbout)
admin.site.register(ProductsTgs)
admin.site.register(ProductsQuestions)
#reviews
admin.site.register(ProductsReviews)
admin.site.register(ProductReviewVoting)
#varients
admin.site.register(ProductVarient)
admin.site.register(ProductsVarientsItems)

#order and delivery
admin.site.register(CustomerOrders)
admin.site.register(OrderDeliveryStatus)



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


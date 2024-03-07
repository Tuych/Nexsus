from django.urls import path
from . import views

urlpatterns = [
    # home path
    path('',views.index, name='index'),
    path('category/',views.category,name='category'),
    path('index_2/',views.index_2,name='index_2'),
    path('index_3/',views.index_3,name='index_3'),

    # listings path
    path('listings/ad_gred/',views.listings_ad_gred,name='ad_gred'),
    path('listings/ad_listing/',views.listings_ad_list,name='ad_list'),
    path('listings/listing_deatil/',views.listings_list_deatil,name='list_detail'),

    #  pages path
    path('pages/about_us/',views.about,name='about_us'),
    path('pages/services/',views.services,name='services'),
    path('<int:product_id>/pages/ads_details/',views.ads_details,name='ads_details'),
    path('pages/ads_post/',views.ads_post,name='ads_post'),
    path('pages/packages/',views.packages,name='packages'),
    path('pages/testimonail/',views.testimonail,name='testimonail'),
    path('pages/faq/',views.faq,name='faq'),
    path('pages/a404/',views.a404,name='a404'),

   

    

    # contact path
    path('contact/',views.contact,name='contact'),

    

]


from django.shortcuts import render
from django.db.models import F
from django.db.models import Prefetch,Subquery,OuterRef  #  Productga tegishli bulgan asmlarni olib kelib beradi
from market.product.models import City,Category,Product,ProductImage
from market.user.models import User
from .search import Search


# Home views

def index(request):
    if request.GET:
        _search=Search(request,url='temp_category/category.html')
        
    else:
        _search=Search(request,url='temp_home/index.html')
        
    return _search


# Category views

def category(request):
    categor_search=Search(request,url='temp_category/category.html')
    
    return categor_search
    

# Listining views
def listings_ad_gred(request):
    return render(request,'temp_listining/adlistinggrid.html',{})

def listings_ad_list(request):
    return render(request,'temp_listining/adlistinglist.html',{})

def listings_list_deatil(request):
    return render(request,'temp_listining/ads-details.html',{})


# Pages views

def about(request):

    return render(request,'temp_pages/about.html',{})

def services(request):

    return render(request,'temp_pages/services.html',{})

def ads_details(request,product_id):

    one_products=Product.objects.filter(id=product_id).select_related('category','city','user').prefetch_related(
            Prefetch('productimage_set',queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name')) )
        
    one_format_products = []
    for i in one_products:
        one_format_products.append({
            'id':i.id,
            'title':i.title,
            'description':i.description,
            'price':i.price,
            'user':i.user.username,
            'phone_number':i.user.phone_number,
            'user_image':i.user.photo,
            'city':i.city.name,
            'category':i.category.name,
            'parent_category':i.parent_category_name,
            'discount':i.discount,
            'condition':i.condition,
            'status':i.status,
            'created_date':i.created_date,
            'image':i.productimage_set.all()[0].image,
            
        })
        
        print(one_format_products)



        products=Product.objects.select_related('category','city','user').prefetch_related(
                Prefetch('productimage_set',queryset=ProductImage.objects.all())
            ).annotate(
                parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name')) )[:5]
            

        format_products=[]
        for i in products:
            format_products.append({
                'id':i.id,
                'title':i.title,
                'price':i.price,
                'user':i.user.username,
                'category':i.category.name,
                'city':i.city.name,
                'image':i.productimage_set.all()[0].image,
            })


        print(products)






        context={
            'one_product':one_format_products[0],
            'products':format_products,
        }

    return render(request,'temp_pages/ads-details.html',context)

def ads_post(request):

    return render(request,'temp_pages/post-ads.html',{})

def packages(request):

    return render(request,'temp_pages/pricing.html',{})

def testimonail(request):

    return render(request,'temp_pages/testimonial.html',{})

def faq(request):

    return render(request,'temp_pages/faq.html',{})

def a404(request):

    return render(request,'temp_pages/404.html',{})




# blod views

def blog_rigth(request):
    return render(request,'temp_blog/blog.html',{})

def blog_left(request):
    return render(request,'temp_blog/blog-left-sidebar.html',{})

def full_width(request):
    return render(request,'temp_blog/blog-grid-full-width.html',{})

def blog_details(request):
    return render(request,'temp_blog/single-post.html',{})


# contact views
def contact(request):
    return render(request,'temp_contact/contact.html',{})





# delete path
def index_2(request):
    return render(request,'temp_home/index-2.html',{})

def index_3(request):
    return render(request,'temp_home/index-3.html',{})
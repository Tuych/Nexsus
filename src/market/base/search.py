from django.shortcuts import render
from django.db.models import F
from django.db.models import Prefetch,Subquery,OuterRef  #  Productga tegishli bulgan asmlarni olib kelib beradi
from market.product.models import City,Category,Product,ProductImage
from market.user.models import User

def Search(request,url=""):
    custom_word=request.GET.get('customword', None)
    city=request.GET.get('city', None)
    category=request.GET.get('category', None)

    city=int(city) if city and city.isdigit() else None
    category=int(category) if category and category.isdigit() else None
    
    

    cities=City.objects.all()
    categorys=Category.objects.all()
    
    if city and category and custom_word:
        products=Product.objects.filter(city_id=city).filter(category_id=category).filter(title__icontains=custom_word).select_related('category','city','user').prefetch_related(
        Prefetch('productimage_set',queryset=ProductImage.objects.all())
        ).annotate(
        parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name')) )


    elif city and category:
        products=Product.objects.filter(city_id=city).filter(category_id=category).select_related('category','city','user').prefetch_related(
        Prefetch('productimage_set',queryset=ProductImage.objects.all())
        ).annotate(
        parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name')) )

    elif city  and custom_word:
        products=Product.objects.filter(city_id=city).filter(title__icontains=custom_word).select_related('category','city','user').prefetch_related(
        Prefetch('productimage_set',queryset=ProductImage.objects.all())
        ).annotate(
        parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name')) )

    elif city:
        products=Product.objects.filter(city_id=city).select_related('category','city','user').prefetch_related(
        Prefetch('productimage_set',queryset=ProductImage.objects.all())
        ).annotate(
        parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name')) )


    elif category and custom_word:
        products=Product.objects.filter(category_id=category).filter(title__contains=custom_word).select_related('category','city','user').prefetch_related(
        Prefetch('productimage_set',queryset=ProductImage.objects.all())
        ).annotate(
        parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name')) )


    elif category:
        products=Product.objects.filter(category_id=category).select_related('category','city','user').prefetch_related(
        Prefetch('productimage_set',queryset=ProductImage.objects.all())
        ).annotate(
        parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name')) )


    elif custom_word:
        products=Product.objects.filter(title__icontains=custom_word).select_related('category','city','user').prefetch_related(
        Prefetch('productimage_set',queryset=ProductImage.objects.all())
        ).annotate(
        parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name')) )

    else:
        products=Product.objects.select_related('category','city','user').prefetch_related(
            Prefetch('productimage_set',queryset=ProductImage.objects.all())
        ).annotate(
            parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name')) )
        
    

    _format_products = []
    for i in products:
        _format_products.append({
            'id':i.id,
            'title':i.title,
            'description':i.description,
            'price':i.price,
            'user':i.user.username,
            'user_image':i.user.photo,
            'city':i.city.name,
            'category':i.category.name,
            'parent_category':i.parent_category_name,
            'discount':i.discount,
            'status':i.status,
            'created_date':i.created_date,
            'image':i.productimage_set.all()[0].image
            
        })
        
        


    context={
        'products':_format_products,
        'cities':cities,
        'categorys':categorys,
        'selected_city':city,
        'selected_ctg':category,
        'custom_word':custom_word,
        }
    
    result= render(request,url,context)
    
    return result
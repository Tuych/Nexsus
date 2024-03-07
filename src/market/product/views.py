from django.shortcuts import render
from .forms import ProductForm,ProductImageFormSet
from .models import ProductImage
# Create your views here.
def create_product(request):
    
    if request.POST:
        form=ProductForm(request.POST or None)
        # formset=ProductImageFormSet()
        print(request.POST.getlist('file'))
        if form.is_valid():
            product=form.save()
            fiels=request.POST.getlist('file')
            for f in fiels:
                ProductImage.objects.create(
                    product=product,
                    image=f"images/{f}"
                )
            product.user=request.user
            product.save()
    form=ProductForm()
    context={
        "form":form,
        # 'formset':formset
    }
    
    return render(request,'post_ads/post-ads.html',context)
    

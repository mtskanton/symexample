from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Product
from .forms import ProductForm
from symcrm.access_filter import access_filter
from symcrm.choice_filter import choice_filter
from django.contrib import messages


@login_required(login_url='login')
def products_list(request):
    access = access_filter(request)
    products = choice_filter(Product.objects.all(), request)

    products.choice('actual', 'True')
    products.choice('sanctioned')

    context = {
        'page_header': 'Продукты',
        'products': products.list,
        'dropdown': access,
        'sanction_status': Product.SANCTION_STATUS,
        'filter_choice': products.filter_choice
    }
    return render(request, 'products/list.html', context)


@login_required(login_url='login')
@permission_required('products.add_product', raise_exception=True)
def products_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:list')
    else:
        form = ProductForm()

    context = {
        'page_header': 'Добавить продукт',
        'form': form
    }
    return render(request, 'products/form.html', context)


@login_required(login_url='login')
def products_view(request, pk):
    product = Product.objects.get(id=pk)
    tasks = product.task_set.all()
    samples = product.sample_set.all()

    context = {
        'product': product,
        'tasks': tasks,
        'samples': samples,
        'subform_settings': '_product_subform',
    }
    return render(request, 'products/view.html', context)


@login_required(login_url='login')
@permission_required('products.change_product', raise_exception=True)
def products_update(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            context = {'product': product}
            return render(request, 'products/view.html', context)
        else:
            messages.error(request, 'Ошибка при обновлении. Обратитесь к администратору сайта')
            return redirect('products:view', pk=pk)

    context = {
        'page_header': 'Обновить продукт',
        'form': form
    }
    return render(request, 'products/form.html', context)


@login_required(login_url='login')
@permission_required('products.delete_product', raise_exception=True)
def products_delete(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('products:list')

    return render(request, 'delete-confirm.html', {'obj': product})


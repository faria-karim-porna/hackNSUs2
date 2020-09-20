from django.shortcuts import render, redirect
from inventory.forms import PurchaseForm
from inventory.models import Purchase

def home(request):
    return render(request,'index.html')

def purchase_add(request):
    
    if request.method == "POST":
        psupplier = request.POST['psupplier']
        psupplier_contact = request.POST['psupplier_contact']
        pproduct_category = request.POST['pproduct_category']
        pproduct_brand = request.POST['pproduct_brand']
        pproduct_name = request.POST['pproduct_name']
        pquantity = request.POST['pquantity']
        peach_price = request.POST['peach_price']
        ppurchase_date = request.POST['ppurchase_date']
        ptotal_price = pquantity*peach_price
        ptotal_price = request.POST['ptotal_price']


        # purchase_form = PurchaseForm(request.POST)
        purchase_form = Purchase(psupplier = psupplier,psupplier_contact = psupplier_contact,pproduct_category = pproduct_category,pproduct_brand = pproduct_brand,pproduct_name = pproduct_name,pquantity = pquantity,peach_price = peach_price,ppurchase_date = ppurchase_date,ptotal_price = ptotal_price)
        purchase_form.save()
    #     if purchase_form.is_valid():
    #         try:
    #    purchase_form.save()
    #             return redirect('/purchase_show')
    #         except:
    #             pass
    # else:
    #     purchase_form = Purchase()
    return render(request, "purchase_add.html", {'purchase_form':purchase_form})

def purchase_show(request):
    purchases = Purchase.objects.all()
    return render(request, "purchase_show.html", {'purchases':purchases})

def purchase_edit(request,id):
    purchase = Purchase.objects.get(id = id)
    return render(request, "purchase_edit.html", {'purchase':purchase})

def purchase_update(request,id):
    purchase = Purchase.objects.get(id = id)
    purchase_form = PurchaseForm(request.POST, instance= purchase)
    if purchase_form.is_valid():
        purchase_form.save()
        return redirect('/purchase_show')
    return render(request, "purchase_edit.html", {'purchase':purchase})

def purchase_delete(request,id):
    purchase = Purchase.objects.get(id = id)
    purchase.delete()
    return redirect('/purchase_show')




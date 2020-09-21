from django.shortcuts import render, redirect, HttpResponse
from inventory.models import Purchase
from inventory.models import Stored_Product
from inventory.models import Stock_Out
from inventory.models import Sale
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home(request):
    return render(request,'index.html')
def tryAlert(request):
    return render(request,'tryAlert.html')
# purchase crud
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
        ptotal_price = int(pquantity)*int(peach_price)

        purchase_form = Purchase(psupplier = psupplier,psupplier_contact = psupplier_contact,pproduct_category = pproduct_category,pproduct_brand = pproduct_brand,pproduct_name = pproduct_name,pquantity = pquantity,peach_price = peach_price,ppurchase_date = ppurchase_date,ptotal_price = ptotal_price)
        purchase_form.save()
        # store product
        stored_form = Stored_Product(spproduct_category = pproduct_category,spproduct_brand = pproduct_brand,spproduct_name = pproduct_name,spquantity = pquantity,speach_price = peach_price)
        stored_form.save()
    return render(request, "purchase_add.html")

def purchase_show(request):
    purchases = Purchase.objects.all()
    return render(request, "purchase_show.html", {'purchases':purchases})

def purchase_edit(request,id):
    purchase = Purchase.objects.get(id = id)
    return render(request, "purchase_edit.html", {'purchase':purchase})

def purchase_update(request,id):
    purchase = Purchase.objects.get(id = id)
    psupplier = request.POST['psupplier']
    psupplier_contact = request.POST['psupplier_contact']
    pproduct_category = request.POST['pproduct_category']
    pproduct_brand = request.POST['pproduct_brand']
    pproduct_name = request.POST['pproduct_name']
    pquantity = request.POST['pquantity']
    peach_price = request.POST['peach_price']
    purchase_form = Purchase.objects.filter(id = id)

    purchase_form.update(psupplier = psupplier,psupplier_contact = psupplier_contact,pproduct_category = pproduct_category,pproduct_brand = pproduct_brand,pproduct_name = pproduct_name,pquantity = pquantity,peach_price = peach_price)
    if purchase_form:
         return redirect('/purchase_show')
    return render(request, "purchase_edit.html", {'purchase':purchase})

def purchase_delete(request,id):
    purchase = Purchase.objects.get(id = id)
    purchase.delete()
    return redirect('/purchase_show')

# store product
def stored_product_show(request):
    stored_products = Stored_Product.objects.all()
    return render(request, "stored_product_show.html", {'stored_products':stored_products})

# billing system

def billing_show(request):
    billing_products = Stored_Product.objects.all()
    return render(request, "billing_show.html", {'billing_products':billing_products})

def billing_edit(request,id):
    billing_product = Stored_Product.objects.get(id = id)
    return render(request, "billing_edit.html", {'billing_product':billing_product})

def billing_update(request,id):
    billing_product = Stored_Product.objects.get(id = id)
    sbuyer = request.POST['sbuyer']
    sbuyer_contact = request.POST['sbuyer_contact']
    spproduct_category = request.POST['spproduct_category']
    spproduct_brand = request.POST['spproduct_brand']
    spproduct_name = request.POST['spproduct_name']
    squantity = request.POST['squantity']
    speach_price = request.POST['speach_price']
    stotal_price = int(squantity)*float(speach_price)

    sale_form = Sale(sbuyer = sbuyer,sbuyer_contact = sbuyer_contact,
sproduct_category = spproduct_category,sproduct_brand = spproduct_brand,
sproduct_name = spproduct_name,squantity = squantity,seach_price = speach_price,stotal_price = stotal_price)
    sale_form.save()

    stored_product_form = Stored_Product.objects.filter(spproduct_category = spproduct_category,spproduct_brand = spproduct_brand, spproduct_name = spproduct_name)

    spquantity = Stored_Product.objects.raw('SELECT * FROM stored_product WHERE spproduct_category = %s AND spproduct_brand = %s AND spproduct_name = %s', [spproduct_category,spproduct_brand,spproduct_name])
    for spquantity in spquantity:
        newquantity = int(spquantity.spquantity) - int(squantity)
        if newquantity == 0:
            stock_out_form = Stock_Out(soproduct_category = spproduct_category,soproduct_brand = spproduct_brand,soproduct_name = spproduct_name,soquantity = 0,soeach_price = speach_price)
            stored_product = Stored_Product.objects.get(id = id)
            stock_out_form.save()
            stored_product.delete()

    stored_product_form.update(spquantity = newquantity)
    if sale_form:
         return redirect('/billing_show')
    return render(request, "billing_edit.html", {'billing_product':billing_product})
# store product
def stock_out_show(request):
    stock_out_products = Stock_Out.objects.all()
    return render(request, "stock_out_show.html", {'stock_out_products':stock_out_products})
# sale
def sale_show(request):
    sales = Sale.objects.all()
    return render(request, "sale_show.html", {'sales':sales})
# signup and login
def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Password is not correct")
            return redirect('home')
        
        newUser = User.objects.create_user(username, email, password)
        newUser.first_name = firstname
        newUser.last_name = lastname
        newUser.save()
        messages.success(request, "You account has been successfully created")
        return redirect('home')
    
    return render(request, "signup.html")

def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('home')

        else:
            messages.error(request, "Invalid Credentials please try again")
            return redirect('handleLogin')

    return render(request, "login.html")

def handleLogout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Successfully logged out")
        return redirect('login')

    return HttpResponse('logout')
    
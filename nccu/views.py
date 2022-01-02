from django.shortcuts import render
# Create your views here.
from datetime import datetime
from .models import Activity, Product,Manufacture_Order,Material, Remaining, Customer
from .filters import CustomerFilter

def home(request):
    return render(request, 'base.html')

def reg(request):
    if request.POST.get('product'):
        p_name = request.POST.get('product')
        p_quantity = request.POST.get('p_quantity')
        if p_quantity != None:
            Product.objects.filter(p_name=p_name).update(p_quantity=int(p_quantity))
    if request.POST.get('material'):
        m_name = request.POST.get('material')
        m_quantity = request.POST.get('m_quantity')
        if m_quantity != None:
            Material.objects.filter(m_name=m_name).update(m_quantity=int(m_quantity))
    product=Product.objects.all()
    material=Material.objects.all()
    return render(request,'test.html',locals())


def getwords(request):
    try:
        date=request.POST['date']
        date=datetime.strptime(date,'%Y-%m-%d')
        quantity=request.POST['quantity']
        p_name=request.POST['p_name']
        select=Product.objects.filter(p_name=p_name)
        inventory=select[0].p_quantity
        prepare=select[0].preparationtime
        epq=select[0].epq
        if inventory<int(quantity):
            productiondate = date - datetime.timedelta(days=prepare)
        else:
            productiondate='不用生產'
        if p_name=='巧克力麵包':
            m = Material.objects.filter(m_name__contains='巧克力')
            bread=Material.objects.filter(m_name='麵包')
            for mm in m:
                if mm.m_quantity<int(quantity):
                    orderdate=date-datetime.timedelta(days=prepare+mm.preparationtime)
                else:
                    orderdate='不用訂購'
            for b in bread:
                if b.m_quantity<int(quantity):
                    b_orderdate = date - datetime.timedelta(days=prepare + b.preparationtime)
                else:
                    b_orderdate='不用訂購'
        elif p_name=='紅豆麵包':
            m=Material.objects.filter(m_name__contains='紅豆')
            bread = Material.objects.filter(m_name='麵包')
            for mm in m:
                if mm.m_quantity<int(quantity):
                    orderdate=date-datetime.timedelta(days=prepare+mm.preparationtime)
                else:
                    orderdate='不用訂購'
            for b in bread:
                if b.m_quantity<int(quantity):
                    b_orderdate = date - datetime.timedelta(days=prepare + b.preparationtime)
                else:
                    b_orderdate='不用訂購'
        elif p_name=='卡士達麵包':
            m=Material.objects.filter(m_name__contains='卡士達')
            bread = Material.objects.filter(m_name='麵包')
            for mm in m:
                if mm.m_quantity<int(quantity):
                    orderdate=date-datetime.timedelta(days=prepare+mm.preparationtime)
                else:
                    orderdate='不用訂購'
            for b in bread:
                if b.m_quantity<int(quantity):
                    b_orderdate = date - datetime.timedelta(days=prepare + b.preparationtime)
                else:
                    b_orderdate='不用訂購'
        elif p_name=='海苔肉鬆麵包':
            m=Material.objects.filter(m_name__contains='海苔')|Material.objects.filter(m_name__contains='肉鬆')
            bread = Material.objects.filter(m_name='麵包')
            for mm in m:
                if mm.m_quantity<int(quantity):
                    orderdate=date-datetime.timedelta(days=prepare+mm.preparationtime)
                else:
                    orderdate='不用訂購'
            for b in bread:
                if b.m_quantity<int(quantity):
                    b_orderdate = date - datetime.timedelta(days=prepare + b.preparationtime)
                else:
                    b_orderdate='不用訂購'
        elif p_name=='香蒜乳酪麵包':
            m=Material.objects.filter(m_name__contains='蒜')|Material.objects.filter(m_name__contains='乳酪')
            bread = Material.objects.filter(m_name='麵包')
            for mm in m:
                if mm.m_quantity<int(quantity):
                    orderdate=date-datetime.timedelta(days=prepare+mm.preparationtime)
                else:
                    orderdate='不用訂購'
            for b in bread:
                if b.m_quantity<int(quantity):
                    b_orderdate = date - datetime.timedelta(days=prepare + b.preparationtime)
                else:
                    b_orderdate='不用訂購'
        return render(request,'result.html',locals())
    except:
        return render(request,'result_no.html')
    

def showactivity(request):
    activity = Activity.objects.all()
    a_context = {'activity': activity} 
    remaining = Remaining.objects.all()
    r_context = {'remaining': remaining}
    return render(request, 'activity.html', locals())


def index(request):
    customers = Customer.objects.all()
 
    customerFilter = CustomerFilter(queryset=customers)
 
    if request.method == "POST":
        customerFilter = CustomerFilter(request.POST, queryset=customers)
 
    context = {
        'customerFilter': customerFilter
    }
 
    return render(request, "index.html", context)

# Create your views here.

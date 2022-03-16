from django import forms
from django.shortcuts import render
# Create your views here.
from datetime import datetime,timedelta
from .models import Activity, Product,Manufacture_Order,Material, Remaining, Customer, chocolate, cheese, redbean, cream, meatfloss
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
    if request.method == 'POST':
        date=request.POST['date']
        date=datetime.strptime(date,'%Y-%m-%d')
        quantity=request.POST['quantity']
        p_name=request.POST['p_name']
        select=Product.objects.filter(p_name=p_name)
        inventory=select[0].p_quantity
        prepare=select[0].preparationtime
        epq=select[0].epq
        if inventory<int(quantity):
            productiondate = date - timedelta(days=prepare)
        else:
            productiondate='不用生產'
        if p_name=='巧克力麵包':
            m = Material.objects.filter(m_name__contains='巧克力')
            bread=Material.objects.filter(m_name='麵包')
            for mm in m:
                if mm.m_quantity<int(quantity):
                    orderdate=date-timedelta(days=prepare+mm.preparationtime)
                else:
                    orderdate='不用訂購'
            for b in bread:
                if b.m_quantity<int(quantity):
                    b_orderdate = date - timedelta(days=prepare + b.preparationtime)
                else:
                    b_orderdate='不用訂購'
        elif p_name=='紅豆麵包':
            m=Material.objects.filter(m_name__contains='紅豆')
            bread = Material.objects.filter(m_name='麵包')
            for mm in m:
                if mm.m_quantity<int(quantity):
                    orderdate=date-timedelta(days=prepare+mm.preparationtime)
                else:
                    orderdate='不用訂購'
            for b in bread:
                if b.m_quantity<int(quantity):
                    b_orderdate = date - timedelta(days=prepare + b.preparationtime)
                else:
                    b_orderdate='不用訂購'
        elif p_name=='卡士達麵包':
            m=Material.objects.filter(m_name__contains='卡士達')
            bread = Material.objects.filter(m_name='麵包')
            for mm in m:
                if mm.m_quantity<int(quantity):
                    orderdate=date-timedelta(days=prepare+mm.preparationtime)
                else:
                    orderdate='不用訂購'
            for b in bread:
                if b.m_quantity<int(quantity):
                    b_orderdate = date - timedelta(days=prepare + b.preparationtime)
                else:
                    b_orderdate='不用訂購'
        elif p_name=='海苔肉鬆麵包':
            m=Material.objects.filter(m_name__contains='海苔')|Material.objects.filter(m_name__contains='肉鬆')
            bread = Material.objects.filter(m_name='麵包')
            for mm in m:
                if mm.m_quantity<int(quantity):
                    orderdate=date-timedelta(days=prepare+mm.preparationtime)
                else:
                    orderdate='不用訂購'
            for b in bread:
                if b.m_quantity<int(quantity):
                    b_orderdate = date - timedelta(days=prepare + b.preparationtime)
                else:
                    b_orderdate='不用訂購'
        elif p_name=='香蒜乳酪麵包':
            m=Material.objects.filter(m_name__contains='蒜')|Material.objects.filter(m_name__contains='乳酪')
            bread = Material.objects.filter(m_name='麵包')
            for mm in m:
                if mm.m_quantity<int(quantity):
                    orderdate=date-timedelta(days=prepare+mm.preparationtime)
                else:
                    orderdate='不用訂購'
            for b in bread:
                if b.m_quantity<int(quantity):
                    b_orderdate = date - timedelta(days=prepare + b.preparationtime)
                else:
                    b_orderdate='不用訂購'
        return render(request,'result.html',locals())
    else:
        product=Product.objects.all()
        material=Material.objects.all()
        return render(request,'result_no.html', locals())
    

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

def forecasting(request):
    if request.method == 'POST':
        year = request.POST['year']
        month = request.POST['month']
        date = str(year) + "-" + str(month)
        #巧克力麵包
        select1 = chocolate.objects.filter(date=date)
        count1 = select1[0].count
        demand1 = select1[0].demand
        if count1 == 1:
            forecastdemand1 = demand1

        if count1 == 2:
            s1 = chocolate.objects.filter(count=count1 - 1)
            d1 = s1[0].demand
            forecastdemand1 = d1

        if count1 == 3:
            s1 = chocolate.objects.filter(count=count1 - 1)
            d1 = s1[0].demand
            s2 = chocolate.objects.filter(count=count1 - 2)
            d2 = s2[0].demand
            forecastdemand1 = 0.5 * d1 + 0.5 * d2

        if count1 >= 4:
            s1 = chocolate.objects.filter(count=count1 - 1)
            d1 = s1[0].demand
            s2 = chocolate.objects.filter(count=count1 - 2)
            d2 = s2[0].demand
            s3 = chocolate.objects.filter(count=count1 - 3)
            d3 = s3[0].demand
            forecastdemand1 = 0.5 * d1 + 0.3 * d2 + 0.2 * d3
        list = cho(date,forecastdemand1)
        #香蒜乳酪麵包
        select2 = cheese.objects.filter(date=date)
        count2 = select2[0].count
        demand2 = select2[0].demand
        if count2 == 1:
            forecastdemand2 = demand2

        if count2 == 2:
            s1 = cheese.objects.filter(count=count2 - 1)
            d1 = s1[0].demand
            forecastdemand2 = d1

        if count2 == 3:
            s1 = cheese.objects.filter(count=count2 - 1)
            d1 = s1[0].demand
            s2 = cheese.objects.filter(count=count2 - 2)
            d2 = s2[0].demand
            forecastdemand2 = 0.5 * d1 + 0.5 * d2

        if count2 >= 4:
            s1 = cheese.objects.filter(count=count2 - 1)
            d1 = s1[0].demand
            s2 = cheese.objects.filter(count=count2 - 2)
            d2 = s2[0].demand
            s3 = cheese.objects.filter(count=count2 - 3)
            d3 = s3[0].demand
            forecastdemand2 = 0.5 * d1 + 0.3 * d2 + 0.2 * d3
        list = garlic(request,date,forecastdemand2)
        #紅豆麵包
        select3 = redbean.objects.filter(date=date)
        count3 = select3[0].count
        demand3 = select3[0].demand
        if count3 == 1:
            forecastdemand3 = demand3

        if count3 == 2:
            s1 = redbean.objects.filter(count=count3 - 1)
            d1 = s1[0].demand
            forecastdemand3 = d1

        if count3 == 3:
            s1 = redbean.objects.filter(count=count3 - 1)
            d1 = s1[0].demand
            s2 = redbean.objects.filter(count=count3 - 2)
            d2 = s2[0].demand
            forecastdemand3 = 0.5 * d1 + 0.5 * d2

        if count3 >= 4:
            s1 = redbean.objects.filter(count=count3 - 1)
            d1 = s1[0].demand
            s2 = redbean.objects.filter(count=count3 - 2)
            d2 = s2[0].demand
            s3 = redbean.objects.filter(count=count3 - 3)
            d3 = s3[0].demand
            forecastdemand3 = 0.5 * d1 + 0.3 * d2 + 0.2 * d3
        list = rn(request,date,forecastdemand3)
        #卡士達麵包
        select4 = cream.objects.filter(date=date)
        count4 = select4[0].count
        demand4 = select4[0].demand
        if count4 == 1:
            forecastdemand4 = demand4

        if count4 == 2:
            s1 = cream.objects.filter(count=count4 - 1)
            d1 = s1[0].demand
            forecastdemand4 = d1

        if count4 == 3:
            s1 = cream.objects.filter(count=count4 - 1)
            d1 = s1[0].demand
            s2 = cream.objects.filter(count=count4 - 2)
            d2 = s2[0].demand
            forecastdemand4 = 0.5 * d1 + 0.5 * d2

        if count4 >= 4:
            s1 = cream.objects.filter(count=count4 - 1)
            d1 = s1[0].demand
            s2 = cream.objects.filter(count=count4 - 2)
            d2 = s2[0].demand
            s3 = cream.objects.filter(count=count4 - 3)
            d3 = s3[0].demand
            forecastdemand4 = 0.5 * d1 + 0.3 * d2 + 0.2 * d3
        list = cm(request,date,forecastdemand4)
        #海苔肉鬆麵包
        select5 = meatfloss.objects.filter(date=date)
        count5 = select5[0].count
        demand5 = select5[0].demand
        if count5 == 1:
            forecastdemand5 = demand5

        if count5 == 2:
            s1 = meatfloss.objects.filter(count=count5 - 1)
            d1 = s1[0].demand
            forecastdemand5 = d1

        if count5 == 3:
            s1 = meatfloss.objects.filter(count=count5 - 1)
            d1 = s1[0].demand
            s2 = meatfloss.objects.filter(count=count5 - 2)
            d2 = s2[0].demand
            forecastdemand5 = 0.5 * d1 + 0.5 * d2

        if count5 >= 4:
            s1 = meatfloss.objects.filter(count=count5 - 1)
            d1 = s1[0].demand
            s2 = meatfloss.objects.filter(count=count5 - 2)
            d2 = s2[0].demand
            s3 = meatfloss.objects.filter(count=count5 - 3)
            d3 = s3[0].demand
            forecastdemand5 = 0.5 * d1 + 0.3 * d2 + 0.2 * d3
        list = porkfiber(request,date,forecastdemand5)
        return render(request, 'f_result.html', locals())
    else:
        return render(request, 'forecast.html', locals())
# Create your views here.
def cho(date,demand):
    r = []
    date=datetime.strptime(date+'-01','%Y-%m-%d')
    select = Product.objects.filter(p_name='巧克力麵包')
    inventory = select[0].p_quantity
    prepare = select[0].preparationtime
    epq = select[0].epq
    if inventory < int(demand) and demand!=None:
        productiondate = date - timedelta(days=prepare)
    m = Material.objects.filter(m_name__contains='巧克力')
    bread = Material.objects.filter(m_name='麵包')
    for mm in m:
        if mm.m_quantity < int(demand):
            orderdate = date - timedelta(days=prepare + mm.preparationtime)
        else:
            orderdate = '不用訂購'
    for b in bread:
        if b.m_quantity < int(demand):
            b_orderdate = date - timedelta(days=prepare + b.preparationtime)
        else:
            b_orderdate = '不用訂購'
    try:
        r.append(productiondate)
    except:
        r.append(orderdate)
        r.append(b_orderdate)
    return r

def rn(request,date,demand):
    r = []
    date=datetime.strptime(date+'-01','%Y-%m-%d')
    select = Product.objects.filter(p_name='紅豆麵包')
    inventory = select[0].p_quantity
    prepare = select[0].preparationtime
    epq = select[0].epq
    if inventory < int(demand) and demand!=None:
        productiondate = date - timedelta(days=prepare)
    m = Material.objects.filter(m_name__contains='紅豆')
    bread = Material.objects.filter(m_name='麵包')
    for mm in m:
        if mm.m_quantity < int(demand):
            orderdate = date - timedelta(days=prepare + mm.preparationtime)
        else:
            orderdate = '不用訂購'
    for b in bread:
        if b.m_quantity < int(demand):
            b_orderdate = date - timedelta(days=prepare + b.preparationtime)
        else:
            b_orderdate = '不用訂購'
    try:
        r.append(productiondate)
    except:
        r.append(orderdate)
        r.append(b_orderdate)
    return r

def cm(request,date,demand):
    r = []
    date=datetime.strptime(date+'-01','%Y-%m-%d')
    select = Product.objects.filter(p_name='卡士達麵包')
    inventory = select[0].p_quantity
    prepare = select[0].preparationtime
    epq = select[0].epq
    if inventory < int(demand) and demand!=None:
        productiondate = date - timedelta(days=prepare)
    m = Material.objects.filter(m_name__contains='卡士達')
    bread = Material.objects.filter(m_name='麵包')
    for mm in m:
        if mm.m_quantity < int(demand) and demand!=None:
            orderdate = date - timedelta(days=prepare + mm.preparationtime)
        else:
            orderdate = '不用訂購'
    for b in bread:
        if b.m_quantity < int(demand) and demand!=None:
            b_orderdate = date - timedelta(days=prepare + b.preparationtime)
        else:
            b_orderdate = '不用訂購'
    try:
        r.append(productiondate)
    except:
        r.append(orderdate)
        r.append(b_orderdate)
    return r

def porkfiber(request,date,demand):
    r = []
    date=datetime.strptime(date+'-01','%Y-%m-%d')
    select = Product.objects.filter(p_name='海苔肉鬆麵包')
    inventory = select[0].p_quantity
    prepare = select[0].preparationtime
    epq = select[0].epq
    if inventory < int(demand) and demand!=None:
        productiondate = date - timedelta(days=prepare)
    m=Material.objects.filter(m_name__contains='海苔')|Material.objects.filter(m_name__contains='肉鬆')
    bread = Material.objects.filter(m_name='麵包')
    for mm in m:
        if mm.m_quantity < int(demand) and demand!=None:
            orderdate = date - timedelta(days=prepare + mm.preparationtime)
        else:
            orderdate = '不用訂購'
    for b in bread:
        if b.m_quantity < int(demand) and demand!=None:
            b_orderdate = date - timedelta(days=prepare + b.preparationtime)
        else:
            b_orderdate = '不用訂購'
    try:
        r.append(productiondate)
    except:
        r.append(orderdate)
        r.append(b_orderdate)
    return r

def garlic(request,date,demand):
    r = []
    date=datetime.strptime(date+'-01','%Y-%m-%d')
    select = Product.objects.filter(p_name='香蒜乳酪麵包')
    inventory = select[0].p_quantity
    prepare = select[0].preparationtime
    epq = select[0].epq
    if inventory < int(demand) and demand!=None:
        productiondate = date - timedelta(days=prepare)
    m=Material.objects.filter(m_name__contains='蒜')|Material.objects.filter(m_name__contains='乳酪')
    bread = Material.objects.filter(m_name='麵包')
    for mm in m:
        if mm.m_quantity < int(demand) and demand!=None:
            orderdate = date - timedelta(days=prepare + mm.preparationtime)
        else:
            orderdate = '不用訂購'
    for b in bread:
        if b.m_quantity < int(demand) and demand!=None:
            b_orderdate = date - timedelta(days=prepare + b.preparationtime)
        else:
            b_orderdate = '不用訂購'
    try:
        r.append(productiondate)
    except:
        r.append(orderdate)
        r.append(b_orderdate)
    return r
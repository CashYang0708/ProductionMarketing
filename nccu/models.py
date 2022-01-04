from django.db import models
from django.db import models
from django.utils import timezone

# Create your models here.
#庫存
class Product(models.Model):
    p_name=models.CharField(max_length=20)
    p_quantity=models.IntegerField()
    preparationtime=models.IntegerField(null=True)
    epq=models.IntegerField(null=True)
    def __str__(self):
        return str(self.p_name)

#庫存
class Material(models.Model):
    m_name=models.CharField(max_length=20)
    m_quantity=models.IntegerField()
    preparationtime=models.IntegerField(null=True)
    best_order_quantity=models.IntegerField(null=True)
    def __str__(self):
        return str(self.m_name)

class Manufacture_Order(models.Model):
    product_name=models.CharField(max_length=20)
    product_quantity=models.IntegerField()
    def __str__(self):
        return str(self.product_name)


#景點貼文
class Customer(models.Model):
    SEX_CHOICES = (
        ('M', '男性'),
        ('F', '女性'),
    )

    AGE_CHOICES = (
        ('under 18', '18歲以下'),
        ('19~30', '19至30歲'),
        ('31~40', '31至40歲'),
        ('41~50', '41至50歲'),
        ('51~65', '51至65歲'),
        ('over 65', '65歲以上'),
    )

    ADDRESS_CHOICES = (
        ('北部', '北部'),
        ('中部', '中部'),
        ('南部', '南部'),
        ('東部', '東部'),
        ('外島', '外島'),
    )

    title = models.CharField(max_length=100)  # 顧客名稱
    sex = models.CharField(max_length=20, choices=SEX_CHOICES)  # 顧客性別
    age = models.CharField(max_length=20, choices=AGE_CHOICES)  # 顧客年齡
    address = models.CharField(max_length=20, choices=ADDRESS_CHOICES)  # 顧客居住區域
    phone = models.CharField(max_length=200)  # 顧客電話
    def __str__(self):
        return str(self.title)

# Create your models here.
class Remaining(models.Model):
    season = models.CharField(max_length=20)
    rr = models.FloatField()
    objects = models.Manager()

    class Meta:
        db_table = 'remaining'

    def __str__(self):
        return str(self.season)

# Create your models here.
class Activity(models.Model):
    date = models.CharField(max_length=20, default='2021-01-01')
    name = models.CharField(max_length=20)
    ta = models.CharField(max_length=20)
    ar = models.FloatField()
    ac = models.IntegerField()

    class Meta:
        db_table = 'activity'
    
    def __str__(self):
        return str(self.name)

#賣出去的
class chocolate(models.Model):
    count = models.IntegerField()
    date = models.CharField(max_length=20, default='2021-01')
    demand = models.IntegerField()

    class Meta:
        db_table = 'chocolate'
    


class cheese(models.Model):
    count = models.IntegerField()
    date = models.CharField(max_length=20, default='2021-01')
    demand = models.IntegerField()

    class Meta:
        db_table = 'cheese'
    



class redbean(models.Model):
    count = models.IntegerField()
    date = models.CharField(max_length=20, default='2021-01')
    demand = models.IntegerField()

    class Meta:
        db_table = 'redbean'


class cream(models.Model):
    count = models.IntegerField()
    date = models.CharField(max_length=20, default='2021-01')
    demand = models.IntegerField()

    class Meta:
        db_table = 'cream'
    



class meatfloss(models.Model):
    count = models.IntegerField()
    date = models.CharField(max_length=20, default='2021-01')
    demand = models.IntegerField()

    class Meta:
        db_table = 'meatfloss'

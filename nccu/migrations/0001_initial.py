# Generated by Django 3.0.3 on 2021-12-28 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='2021-01-01', max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('ta', models.CharField(max_length=20)),
                ('ar', models.FloatField()),
                ('ac', models.IntegerField()),
            ],
            options={
                'db_table': 'activity',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('M', '男性'), ('F', '女性')], max_length=20)),
                ('age', models.CharField(choices=[('under 18', '18歲以下'), ('19~30', '19至30歲'), ('31~40', '31至40歲'), ('41~50', '41至50歲'), ('51~65', '51至65歲'), ('over 65', '65歲以上')], max_length=20)),
                ('address', models.CharField(choices=[('北部', '北部'), ('中部', '中部'), ('南部', '南部'), ('東部', '東部'), ('外島', '外島')], max_length=20)),
                ('phone', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacture_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('product_quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_name', models.CharField(max_length=20)),
                ('m_quantity', models.IntegerField()),
                ('preparationtime', models.IntegerField(null=True)),
                ('best_order_quantity', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=20)),
                ('p_quantity', models.IntegerField()),
                ('preparationtime', models.IntegerField(null=True)),
                ('epq', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Remaining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=20)),
                ('rr', models.FloatField()),
            ],
            options={
                'db_table': 'remaining',
            },
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-20 07:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, null=True, unique=True, verbose_name='商品グループ')),
            ],
        ),
        migrations.CreateModel(
            name='CustomGoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True, verbose_name='商品名')),
                ('management_code', models.CharField(max_length=20, unique=True, verbose_name='管理コード')),
                ('price', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000000000)], verbose_name='価格')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='発売日')),
                ('release_flag', models.BooleanField(default=False, verbose_name='発売済み')),
                ('description', models.CharField(max_length=100000, verbose_name='説明')),
                ('image', models.ImageField(blank=True, null=True, upload_to='goods_images/', verbose_name='画像')),
                ('state_flag', models.BooleanField(default=True, verbose_name='運用状況')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.goodsgroup', verbose_name='商品グループ')),
            ],
        ),
    ]

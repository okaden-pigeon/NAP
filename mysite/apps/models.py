from django.db import models

# Usersテーブルの情報
class Users(models.Model):
  user_name = models.CharField(max_length=20)
  user_email = models.EmailField()
  user_pass = models.CharField(max_length = 30)
  university = models.IntegerField()
  icon = models.ImageField(
    upload_to='../images')
  class Meta:
    db_table = "Users"

# Universitiesテーブルの情報
class Universities(models.Model):
  university_name = models.CharField(max_length=30)
  university_domain = models.URLField()
  class Meta:
    db_table = "Universities"

# Itemsテーブルの情報
class Items(models.Model):
  item_name = models.CharField(max_length = 40)
  item_description = models.CharField(max_length=500)
  created_at = models.DateTimeField()
  item_eval = models.IntegerField(
    default = 0
  )
  is_deal = models.BooleanField(
    default = False
  )
  class Meta:
    db_table = "Items"

# Genresテーブルの情報
class Genres(models.Model):
  genre_name = models.CharField(max_length = 10)
  class Meta:
    db_table = "Genres"

#Imagesテーブルの情報
class Images(models.Model):
  image = models.ImageField()
  class Meta:
    db_table = "Images"

# 商品情報と分類をつなぐためのテーブル
class ItemClassification(models.Model):
  item_id = models.IntegerField()
  genre_id = models.IntegerField()
  class Meta:
    db_table = "ItemClasification"

# 商品情報と画像をつなぐためのテーブル
class ItemImage(models.Model):
  item_id = models.IntegerField()
  image_id = models.IntegerField()
  class Meta:
    db_table = "ItemImage"

# ユーザー情報と商品情報をつなぐためのテーブル
class UserListing(models.Model):
  user_id = models.IntegerField()
  item_id = models.IntegerField()
  class Meta:
    db_table = "UserListing"

# ユーザー情報と商品のお気に入りをつなぐためのテーブル
class Likes(models.Model):
  user_id = models.IntegerField()
  item_id = models.IntegerField()
  class Meta:
    db_table = "Likes"
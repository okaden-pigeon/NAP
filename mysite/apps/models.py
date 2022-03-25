from django.db import models
from django.utils.timezone import now



# Itemsテーブルの情報
class Items(models.Model):
  id = models.AutoField(primary_key=True)
  item_name = models.CharField(max_length = 40)
  item_description = models.CharField(max_length=500)
  created_at = models.DateTimeField(
    default = now
  )
  # 評価をしないといけない場合に備えて項目を設定
  item_eval = models.IntegerField(
    default = 0
  )
  # 取引したかどうかの機能を実装する時のための項目
  is_deal = models.BooleanField(
    default = False
  )
  icon = models.ImageField(
    upload_to='./static/apps/',
    default = "./images/default_user.png"
    )
  def __str__(self):
        return self.item_name
  class Meta:
    db_table = "Items"

# Genresテーブルの情報
class Genres(models.Model):
  id = models.AutoField(primary_key=True)
  genre_name = models.CharField(max_length = 10)
  def __str__(self):
        return self.genre_name
  class Meta:
    db_table = "Genres"

# Imagesテーブルの情報
class Images(models.Model):
  id = models.AutoField(primary_key=True)
  image = models.ImageField(upload_to='./images/')
  first = models.CharField(max_length = 20,default="")
  last = models.CharField(max_length = 20,default = "") 
  def __str__(self):
        return self.first
  class Meta:
    db_table = "Images"




# --------------------今後実装したいmodel-------------------------
# 商品情報と分類をつなぐためのテーブル
# class ItemClassification(models.Model):
#   item_id = models.IntegerField()
#   genre_id = models.IntegerField()
#   class Meta:
#     db_table = "ItemClasification"

# 商品情報と画像をつなぐためのテーブル
# class ItemImage(models.Model):
#   item_id = models.IntegerField()
#   image_id = models.IntegerField()
#   class Meta:
#     db_table = "ItemImage"

# ユーザー情報と商品情報をつなぐためのテーブル
# class UserListing(models.Model):
#   user_id = models.IntegerField()
#   item_id = models.IntegerField()
#   class Meta:
#     db_table = "UserListing"

# ユーザー情報と商品のお気に入りをつなぐためのテーブル
# class Likes(models.Model):
#   user_id = models.IntegerField()
#   item_id = models.IntegerField()
#   class Meta:
#     db_table = "Likes"


# 大学情報を情報を保存するためのテーブル
# class Universities(models.Model):
#   id = models.AutoField(primary_key=True)
#   university_name = models.CharField(max_length=30)
#   university_domain = models.URLField()
#   def __str__(self):
#         return self.university_name
#   class Meta:
#     db_table = "Universities"
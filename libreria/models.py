from django.db import models

# Create your models here.

# class User(models.Model):
#     id_user = models.AutoField(primary_key=True)
#     username= models.CharField(max_length=50,unique=True, null=False, blank=False)
#     password = models.CharField(max_length=50, null=False, blank=False)

# class Category(models.Model):
#     id_category = models.AutoField(primary_key=True)
#     name_category= models.CharField(max_length=100, null=False, blank=False)   
    
# class Position (models.Model):
#     id_position= models.AutoField(primary_key=True)
#     name_position= models.CharField(max_length=100, null=False, blank=False)
# class Employee(models.Model):
#     id_employee = models.AutoField(primary_key=True)
#     first_name= models.CharField(max_length=45, null=False, blank=False)
#     second_name= models.CharField(max_length=45, null=True, blank=True)
#     first_lastname= models.CharField(max_length=45, null=False, blank=False)
#     second_lastname= models.CharField(max_length=45, null=True, blank=True)
#     username= models.ForeignKey(User,on_delete=models.CASCADE)   
#     position= models.ForeignKey(Position, on_delete=models.CASCADE)
#     category= models.ForeignKey(Category,on_delete=models.CASCADE)

# class Menu (models.Model):
#     id_menu = models.AutoField(primary_key=True)
#     category= models.ForeignKey(Category,on_delete=models.CASCADE)
#     name_dish= models.CharField(max_length=100,  null=False, blank=False)
#     price= models.FloatField( null=False, blank=False)


    
        
    
  
    
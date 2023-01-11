from tortoise.models import Model
from tortoise import fields

class user_info(Model):
    Address = fields.CharField(pk=True,max_length=64)
    Password = fields.CharField(max_length=64)
    Name = fields.CharField(max_length=20)
    Phone_Number = fields.CharField(max_length=10)

    def __str__(self):
        return self.Name

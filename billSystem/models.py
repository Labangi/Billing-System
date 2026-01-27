from django.db import models


# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    role=models.CharField(max_length=50)
    pwd=models.CharField(max_length=50)

    class Meta:
        db_table="user"

class billInfo(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bills'
    )
    bill_number = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)




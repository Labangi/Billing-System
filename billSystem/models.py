from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, default="user")
    pwd = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "user"



class Training(models.Model):
    training_name = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    vendor = models.CharField(max_length=200)
    added_by = models.CharField(max_length=200)
    attendance_status = models.CharField(max_length=100, default="Pending Trainer")

    def __str__(self):
        return self.training_name

    class Meta:
        db_table = "training"



class BillInfo(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bills"
    )

    invoice_no = models.CharField(max_length=100)
    training = models.CharField(max_length=200)
    vendor = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    due_date = models.DateField()
    status = models.CharField(max_length=50, default="Pending")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.invoice_no

    class Meta:
        db_table = "billInfo"

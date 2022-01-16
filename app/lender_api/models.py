from django.db import models

# Create your models here.


class Borrower(models.Model):
    first_name = models.CharField(
        max_length=70, blank=False, default='', null=False)
    last_name = models.CharField(
        max_length=70, blank=True, default='', null=True)
    allowed_to_borrow = models.BooleanField(default=False)
    phone = models.CharField(max_length=11, blank=False)

    def __str__(self):
        return self.name + self.last_name


class Item(models.Model):
    title = models.CharField(max_length=70, blank=False, null=False)
    item_type = models.CharField(max_length=70, blank=False, null=False)
    checked_out = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class Transaction(models.Model):
    checked_out_date = models.DateField()
    returned = models.BooleanField(null=True)
    checked_out_by = models.ForeignKey(
        Borrower, blank=False, on_delete=models.CASCADE)
    checked_out_item = models.ForeignKey(
        Item, blank=False, on_delete=models.CASCADE),

    def __str__(self) -> str:
        return self.checked_out_date

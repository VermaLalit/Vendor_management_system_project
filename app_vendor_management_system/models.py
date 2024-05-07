# from django.db import models

# # Create your models here.

# class VendorModel(models.Model):
#     vendor_name = models.CharField(max_length=100)
#     contact_details = models.TextField()
#     address = models.TextField()
#     vendor_code = models.CharField(max_length=100,unique=True)      # code maybe alphanumeric 
#     on_time_delivery_rate = models.FloatField()
#     quality_rating_avg = models.FloatField()
#     average_response_time = models.FloatField()
#     fulfillment_rate = models.FloatField()

#     def __str__(self):
#         return self.vendor_name
    
# class PurchaseOrderModel(models.Model):
#     po_number = models.CharField(max_length=100,unique=True)
#     vendor = models.ForeignKey(VendorModel,on_delete=models.CASCADE)
#     order_date = models.DateTimeField()
#     delivery_date = models.DateTimeField()
#     items = models.JSONField()
#     quantity = models.IntegerField()
#     status = models.CharField(max_length=20)       # pending, completed, canceled
#     quality_rating = models.FloatField(null=True)
#     issue_date = models.DateTimeField()
#     acknowledgment_date = models.DateTimeField(null=True)

#     def __str__(self):
#         return self.po_number

# class HistoricalPerformanceModel(models.Model):
#     vendor = models.ForeignKey(VendorModel,on_delete=models.CASCADE)
#     date = models.DateTimeField()
#     on_time_delivery_rate = models.FloatField()
#     quality_rating_avg = models.FloatField()
#     average_response_time = models.FloatField()
#     fulfillment_rate = models.FloatField()

#     def __str__(self):
#         return self.vendor,self.date





from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class VendorModel(models.Model):
    vendor_name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=100, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    quality_rating_avg = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])

    def __str__(self):
        return self.vendor_name
    
class PurchaseOrderModel(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)
    delivery_date = models.DateTimeField(default=timezone.now)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)  # pending, completed, canceled
    quality_rating = models.FloatField(null=True, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    issue_date = models.DateTimeField(default=timezone.now)
    acknowledgment_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.po_number

class HistoricalPerformanceModel(models.Model):
    vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    on_time_delivery_rate = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    quality_rating_avg = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])

    def __str__(self):
        return f"{self.vendor} - {self.date}"





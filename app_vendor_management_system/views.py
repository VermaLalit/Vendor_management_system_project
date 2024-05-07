from django.shortcuts import render
from .models import VendorModel , PurchaseOrderModel , HistoricalPerformanceModel
from .serializers import VendorSerializer , PurchaseOrderSerializer , HistoricalPerformanceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Avg, Count
from django.db.models import Avg, ExpressionWrapper, F, DurationField

# Create your views here.

class VendorView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request,format = None):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg":"Data inserted successfully","data":serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,id = None,format = None):
        if id != None:
            try:
                vendor = VendorModel.objects.get(id=id)
            except VendorModel.DoesNotExist:
                return Response({"msg":"Vandor not found"},status=status.HTTP_404_NOT_FOUND)
            serializer = VendorSerializer(vendor)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        vendors = VendorModel.objects.all()
        serializer = VendorSerializer(vendors,many = True)
        return Response({"msg":"All data retrived","data":serializer.data},status=status.HTTP_200_OK)

    def put(self,request,id = None,format = None):
        if id != None:
            try:
                vendor = VendorModel.objects.get(id=id)
            except VendorModel.DoesNotExist:
                return Response({"msg":"Vandor not found"},status=status.HTTP_404_NOT_FOUND)
            
            serializer = VendorSerializer(vendor,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"msg":"data updated successfully","data":serializer.data},status=status.HTTP_200_OK)
            
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self,request,id = None,format = None):
        if id != None:
            try:
                vendor = VendorModel.objects.get(id=id)
            except VendorModel.DoesNotExist:
                return Response({"msg":"Vandor not found"},status=status.HTTP_404_NOT_FOUND)

            vendor.delete()
            return Response({"msg":"data deleted successfully"},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)



class PurchaseOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg": "Purchase order created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id = None, format=None):
        if id is not None:
            try:
                order = PurchaseOrderModel.objects.get(id=id)
            except PurchaseOrderModel.DoesNotExist:
                return Response({"msg": "Purchase order not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = PurchaseOrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        orders = PurchaseOrderModel.objects.all()
        serializer = PurchaseOrderSerializer(orders, many=True)
        return Response({"msg": "All purchase orders retrieved", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, id = None, format=None):
        if id is not None:
            try:
                order = PurchaseOrderModel.objects.get(id=id)
            except PurchaseOrderModel.DoesNotExist:
                return Response({"msg": "Purchase order not found"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = PurchaseOrderSerializer(order, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"msg": "Purchase order updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"msg": "Purchase order ID is required"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, format=None):
        if id is not None:
            try:
                order = PurchaseOrderModel.objects.get(id=id)
            except PurchaseOrderModel.DoesNotExist:
                return Response({"msg": "Purchase order not found"}, status=status.HTTP_404_NOT_FOUND)

            order.delete()
            return Response({"msg": "Purchase order deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"msg": "Purchase order ID is required"}, status=status.HTTP_400_BAD_REQUEST)



class VendorPerformanceView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,id = id,format = None):
        try:
            vendor = VendorModel.objects.get(id=id)
        except VendorModel.DoesNotExist:
            return Response({"msg":"Vendor not found"},status=status.HTTP_404_NOT_FOUND)
        
        # Calculate matrix
        on_time_delivery_rate = self.calculate_on_time_delivery_rate(vendor)
        quality_rating_avg = self.calculate_quality_rating_avg(vendor)
        average_response_time = self.calculate_average_response_time(vendor)
        fulfillment_rate = self.calculate_fulfillment_rate(vendor)

        # Prepare response data
        performance_data = {
            "on_time_delivery_rate": on_time_delivery_rate,
            "quality_rating_avg": quality_rating_avg,
            "average_response_time": average_response_time,
            "fulfillment_rate": fulfillment_rate
        }

        return Response(performance_data, status=status.HTTP_200_OK)

    # def calculate_on_time_delivery_rate(self, vendor):
    #     completed_orders = vendor.purchaseordermodel_set.filter(status='completed')
    #     total_completed_orders = completed_orders.count()
    #     on_time_orders = completed_orders.filter(delivery_date__lte=F('acknowledgment_date')).count()
    #     return (on_time_orders / total_completed_orders) * 100 if total_completed_orders > 0 else 0

    def calculate_on_time_delivery_rate(self, vendor):
        # Get all completed orders for the vendor
        completed_orders = vendor.purchaseordermodel_set.filter(status='completed')
        # Count the total number of completed orders
        total_completed_orders = completed_orders.count()
        # Initialize the count of on-time orders
        on_time_orders = 0
        # Loop through each completed order
        for order in completed_orders:
            # Check if the delivery date is on or before the acknowledgment date
            if order.delivery_date <= order.acknowledgment_date:
                # Increment the count of on-time orders
                on_time_orders += 1

        # Calculate the on-time delivery rate
        if total_completed_orders > 0:
            on_time_delivery_rate = (on_time_orders / total_completed_orders) * 100
        else:
            on_time_delivery_rate = 0
        return on_time_delivery_rate


    def calculate_quality_rating_avg(self, vendor):
        # Get all completed orders with non-null quality ratings for the vendor
        completed_orders = vendor.purchaseordermodel_set.filter(status='completed', quality_rating__isnull=False)
        # Calculate the average quality rating using Django's aggregate function
        average_quality_rating = completed_orders.aggregate(Avg('quality_rating'))['quality_rating__avg']    
        # Return the calculated average quality rating or 0 if no completed orders exist
        return average_quality_rating or 0


    # def calculate_average_response_time(self, vendor):
    #     response_times = vendor.purchaseordermodel_set.filter(acknowledgment_date__isnull=False).annotate(
    #         response_time=ExpressionWrapper(F('acknowledgment_date') - F('issue_date'), output_field=DurationField())
    #     )
    #     return response_times.aggregate(Avg('response_time'))['response_time__avg'].total_seconds() if response_times.exists() else 0

    

    def calculate_average_response_time(self, vendor):
        # Filter acknowledged orders
        acknowledged_orders = vendor.purchaseordermodel_set.filter(acknowledgment_date__isnull=False)
        # Calculate response time for each order
        response_times = acknowledged_orders.annotate(response_time=ExpressionWrapper(F('acknowledgment_date') - F('issue_date'),output_field=DurationField()))
        # Calculate the average response time in seconds
        average_response_time = response_times.aggregate(Avg('response_time'))['response_time__avg']
        # Return the calculated average response time in seconds or 0 if no acknowledged orders exist
        return average_response_time.total_seconds() if average_response_time else 0
    


    def calculate_fulfillment_rate(self, vendor):
        # Count total orders
        total_orders = vendor.purchaseordermodel_set.count()
        # If there are no orders, return 0
        if total_orders == 0:
            return 0
        # Count completed orders
        completed_orders = vendor.purchaseordermodel_set.filter(status='completed').count()
        # Calculate fulfillment rate
        fulfillment_rate = (completed_orders / total_orders) * 100
        return fulfillment_rate






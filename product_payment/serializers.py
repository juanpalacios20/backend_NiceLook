from rest_framework import serializers

from client.serializers import clientSerializer
from .models import Product_payment
from product.models import Product
from rest_framework import serializers
from .models import Product_payment
from product.models import Product
from productPaymentDetail.models import ProductPaymentDetail
from productPaymentDetail.serializers import ProductPaymentDetailSerializer
class ProductQuantitySerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.FloatField()

class ProductPaymentSerializer(serializers.ModelSerializer):
    client = clientSerializer(read_only=True)
    products = ProductQuantitySerializer(many=True, write_only=True)
    total_price = serializers.ReadOnlyField()
    total_quantity = serializers.ReadOnlyField()
    details = ProductPaymentDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Product_payment
        fields = ['client', 'establisment', 'date', 'method', 'products', 'discount', 'state', 'details', 'total_price', 'total_quantity']

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        
        # Crear el pago
        payment = Product_payment.objects.create(**validated_data)
        
        # Crear los detalles del pago para cada producto
        for product_data in products_data:
            product_id = product_data['product_id']
            quantity = product_data['quantity']
            
            try:
                product = Product.objects.get(id=product_id)
                ProductPaymentDetail.objects.create(
                    payment=payment,
                    product=product,
                    quantity=quantity
                )
            except Product.DoesNotExist:
                # Puedes manejar el error como prefieras
                raise serializers.ValidationError(f"Product with id {product_id} does not exist")
        
        return payment
from rest_framework import serializers

from products.models import Owner

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['first_name', 'second_name', 'contact']
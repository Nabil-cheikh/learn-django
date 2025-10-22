from .models import Claim
from rest_framework import serializers

class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = '__all__'
        read_only_fields = ['status', 'result', 'created_at']
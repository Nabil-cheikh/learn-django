from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Claim
from .serializers import ClaimSerializer
import random, time

class ClaimViewSet(ModelViewSet):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer

    @action(detail=True, methods=['post'])
    def analyze(self, request, pk=None):
        claim = self.get_object()
        if claim.status == 'done':
            return Response(ClaimSerializer(claim).data)
        claim.status = 'processing'
        claim.save()

        # Simulation
        # Asynchrone avec Celery task
        time.sleep(0.5)
        claim.result = {'damage_level': random.choice(['low','medium','high'])}
        claim.status = 'done'
        claim.save()

        return Response(ClaimSerializer(claim).data)
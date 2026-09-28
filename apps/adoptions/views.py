from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import Visit

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def book_visit(request):
    try:
        visit = Visit.objects.create(
            visitor_name=request.data.get('visitor_name'),
            visitor_email=request.data.get('visitor_email'),
            visitor_phone=request.data.get('visitor_phone'),
            ngo_id=request.data.get('ngo_id'),
            child_id=request.data.get('child_id') or None,
            visit_date=request.data.get('visit_date'),
            visit_time=request.data.get('visit_time'),
            purpose=request.data.get('purpose', 'adoption_inquiry'),
            message=request.data.get('message', '')
        )
        return Response({
            'success': True,
            'visit_id': visit.visit_id,
            'message': 'Visit request submitted.'
        }, status=201)
    except Exception as e:
        return Response({'success': False, 'error': str(e)}, status=400)

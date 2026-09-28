
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Child

@api_view(['GET'])
@permission_classes([AllowAny])
def list_children(request):
    children = Child.objects.all()
    data = []
    for c in children:
        data.append({
            'child_id': c.child_id,
            'name': c.name,
            'age': c.age,
            'gender': c.gender,
            'health_status': c.health_status,
            'education_level': c.education_level,
            'is_sponsored': c.is_sponsored,
            'is_available_for_adoption': c.is_available_for_adoption,
            'story': c.story,
            'needs': c.needs,
            'profile_photo': c.profile_photo.url if c.profile_photo else None,
            'ngo_id': c.ngo.ngo_id,
            'ngo_name': c.ngo.name,
        })
    return Response({'children': data})

@api_view(['GET'])
@permission_classes([AllowAny])
def get_child(request, child_id):
    try:
        c = Child.objects.get(child_id=child_id)
        return Response({
            'child_id': c.child_id,
            'name': c.name,
            'age': c.age,
            'gender': c.gender,
            'health_status': c.health_status,
            'education_level': c.education_level,
            'is_sponsored': c.is_sponsored,
            'is_available_for_adoption': c.is_available_for_adoption,
            'story': c.story,
            'needs': c.needs,
            'profile_photo': c.profile_photo.url if c.profile_photo else None,
            'ngo_id': c.ngo.ngo_id,
            'ngo_name': c.ngo.name,
        })
    except Child.DoesNotExist:
        return Response({'error': 'Child not found'}, status=404)
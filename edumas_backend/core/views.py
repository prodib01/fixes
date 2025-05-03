from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Campus, School
from .serializers import SchoolSerializer, CampusSerializer
from django.shortcuts import get_object_or_404

class SchoolListCreateAPIView(APIView):
    @extend_schema(
        request=SchoolSerializer,
        responses={201: SchoolSerializer},
        summary="Create a new school",
    )
    def post(self, request):
        try:
            profile = request.user.profile
        except Exception:
            return Response({"detail": "User profile not found."}, status=400)

        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        responses={200: SchoolSerializer(many=True)},
        summary="List schools owned by the current user",
    )
    def get(self, request):
        try:
            profile = request.user.profile
        except Exception:
            return Response({"detail": "User profile not found."}, status=400)

        schools = School.objects.filter(owner=profile)
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)

class SchoolDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user):
        try:
            # Ensure the logged-in user owns the school
            return get_object_or_404(School, pk=pk, owner=user.profile)
        except School.DoesNotExist:
            raise PermissionDenied("You do not have permission to access this school.")

    @extend_schema(
        summary="Retrieve a School",
        responses={200: SchoolSerializer},
    )
    def get(self, request, pk):
        try:
            profile = request.user.profile
        except Exception:
            return Response({"detail": "User profile not found."}, status=400)

        # Fetch school for the logged-in user
        school = self.get_object(pk, request.user)
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    @extend_schema(
        summary="Update a School",
        request=SchoolSerializer,
        responses={200: SchoolSerializer},
    )
    def patch(self, request, pk):
        try:
            profile = request.user.profile
        except Exception:
            return Response({"detail": "User profile not found."}, status=400)

        # Fetch school for the logged-in user
        school = self.get_object(pk, request.user)
        serializer = SchoolSerializer(school, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(owner=request.user.profile)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="Delete a School",
        responses={204: None},
    )
    def delete(self, request, pk):
        try:
            profile = request.user.profile
        except Exception:
            return Response({"detail": "User profile not found."}, status=400)

        # Fetch school for the logged-in user
        school = self.get_object(pk, request.user)
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CampusListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=CampusSerializer,
        responses={201: CampusSerializer},
        summary="Create a new campus",
    )
    def post(self, request):
        serializer = CampusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    @extend_schema(
        responses={200: CampusSerializer(many=True)},
        summary="List all campuses",
    )
    def get(self, request):
        campuses = Campus.objects.all()
        serializer = CampusSerializer(campuses, many=True)
        return Response(serializer.data)
    
class CampusDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        campus = campus = get_object_or_404(Campus, pk=pk)
        serializer = CampusSerializer(campus)
        return Response(serializer.data)
    @extend_schema(
        summary="Update a Campus",
        request=CampusSerializer,
        responses={200: CampusSerializer},
    )
    def patch(self, request, pk):
        try:
            profile = request.user.profile
        except Exception:
            return Response({"detail": "User profile not found."}, status=400)

        # Fetch campus for the logged-in user
        campus = self.get_object(pk, request.user)
        serializer = CampusSerializer(campus, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(owner=request.user.profile)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @extend_schema(
        summary="Delete a Campus",
        responses={204: None},
    )
    def delete(self, request, pk):
        try:
            profile = request.user.profile
        except Exception:
            return Response({"detail": "User profile not found."}, status=400)

        # Fetch campus for the logged-in user
        campus = self.get_object(pk, request.user)
        campus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
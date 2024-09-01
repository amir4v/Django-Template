import random

from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import UserModelSerializer
from .models import User


class RoleBasedPermission(permissions.BasePermission):
	def has_permission(self, request, view):
		return True # Just for test.

		# Admins can do anything
		if request.user.role == User.RoleChoice.ADMIN_USER[0]:
			return True

		# Only allow safe methods (GET, HEAD, OPTIONS) for viewers
		if request.user.role == User.RoleChoice.VIEWER_USER[0]:
			return request.method in permissions.SAFE_METHODS

		# Only allow editors to access certain methods
		if request.user.role == User.RoleChoice.EDITOR_USER[0]:
			return request.method in ['GET', 'PUT', 'PATCH', 'HEAD', 'OPTIONS']

		return False


class UserModelViewSet(viewsets.ModelViewSet):
	"""
	User model viewset to provide a CRUD operations for this model.
	"""

	_queryset = User.objects.all()
	serializer_class = UserModelSerializer
	ordering_fields = ('username', 'created_at')
	ordering = ('username',)

	def get_permissions(self):
		return [] # Just for test.

		if self.action == 'create':
			permission_classes = [permissions.IsAuthenticated, RoleBasedPermission]
		elif self.action == 'list':
			permission_classes = [permissions.IsAuthenticatedOrReadOnly]
		else:
			permission_classes = [RoleBasedPermission]

		return [permission() for permission in permission_classes]

	def get_queryset(self):
		return self._queryset # Just for test.

		return self._queryset.filter(username=self.request.user.username)

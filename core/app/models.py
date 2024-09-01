from django.db import models


class User(models.Model):
	"""
	User model for a simple User model to fulfill the minimum amount of a
	standard User model.
	"""

	class Meta:
		ordering = ('username',)

	class RoleChoice(models.TextChoices):
		CONSUMER_USER = 'CS', 'Consumer user'
		VIEWER_USER = 'V', 'Viewer user'
		PREMIUM_USER = 'P', 'Premium user'
		NORMAL_USER = 'N', 'Normal user'
		DEFAULT_USER = 'DF', 'Default user'
		DEVELOPER_USER = 'DV', 'Developer user'
		CREATOR_USER = 'CT', 'Creator user'
		MARKER_USER = 'MK', 'Marker user'
		ADMIN_USER = 'A', 'Admin user'
		SUPER_USER = 'SP', 'Super user'
		MANAGER_USER = 'MG', 'Manager user'
		SUPERVISOR_USER = 'SV', 'Supervisor user'
		WRITER_USER = 'W', 'Writer user'
		EDITOR_USER = 'E', 'Editor user'

	username = models.CharField(max_length=100, unique=True, db_index=True, blank=False, null=False)
	email = models.EmailField(unique=True, db_index=True, blank=False, null=False)
	password = models.CharField(max_length=128, blank=False, null=False)

	role = models.CharField(max_length=2, choices=RoleChoice.choices, default=RoleChoice.NORMAL_USER)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

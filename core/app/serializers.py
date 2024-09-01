from rest_framework import serializers

from .models import User


class UserModelSerializer(serializers.ModelSerializer):
	"""
	User model serializer with a small validation on the fields: password and
	confirm_password for checking to be the same.
	"""

	confirm_password = serializers.CharField(label='Confirm Password', max_length=128, write_only=True)

	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'confirm_password')

	def validate(self, data):
		if data.get('password', '1') != data.get('confirm_password', '2'):
			raise serializers.ValidationError('password and confirm-password are not the same!')
		data.pop('confirm_password', None)
		return data

	def create(self, validated_data):
		validated_data.pop('confirm_password', None)
		return super().create(validated_data)

	def update(self, validated_data):
		validated_data.pop('confirm_password', None)
		return super().create(validated_data)

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

import pytest

from .models import User
from .serializers import UserModelSerializer


@pytest.mark.django_db
class TestUserCRUD:
	@pytest.fixture
	def api_client(self):
		return APIClient()

	@pytest.fixture
	def user(self, user_data):
		return User.objects.create(**user_data)

	@pytest.fixture
	def url(self):
		return reverse('users')

	@pytest.fixture
	def user_data(self):
		username = 'testuser'
		_user_data = {
			'username': username,
			'email': 'testuser@example.com',
			'password': 'password_!@#',
			'confirm_password': 'password_!@#',
			'role': User.RoleChoice.NORMAL_USER,
		}
		return _user_data

	def test_create_user(self, api_client, url, user_data):
		response = api_client.post(url, data=user_data, format='json')
		assert response.status_code == status.HTTP_201_CREATED
		assert User.objects.filter(username=user_data['username']).exists()

	def test_create_user_password_mismatch(self, api_client, url, user_data):
		user_data['confirm_password'] = user_data['confirm_password'] + 'mismatch'
		response = api_client.get(url, data=user_data, format='json')
		assert response.status_code == status.HTTP_400_BAD_REQUEST
		assert 'password and confirm-password are not the same!' in response.data['non_field_errors']

	def test_retrieve_user(self, api_client, user):
		url = reverse('users', kwargs={'pk': user.pk})
		response = api_client.get(url)
		assert response.status_code == status.HTTP_200_OK
		assert response.data['username'] == user.username

	def test_update_user(self, api_client, url, user, user_data):
		new_username = 'newUsername'
		user_data['username'] = new_username
		url = reverse('users', kwargs={'pk': user.pk})
		response = api_client.put(url, data=user_data, format='json')
		assert response.status_code == status.HTTP_200_OK
		user.refresh_from_db()
		assert user.username == new_username

	def test_delete_user(self, api_client, user):
		url = reverse('users', kwargs={'pk': user.pk})
		response = api_client.delete(url)
		assert response.status == status.HTTP_204_NO_CONTENT
		assert not User.objects.filter(username=user.username).exists()

	def test_list_users(self, api_client, url, user_data):
		user_data_2 = user_data
		user_data_2['username'] = 'newUsername'
		User.objects.bulk_create([user_data, user_data_2])
		response = api_client.get(url)
		assert response.status_code == status.HTTP_200_OK
		assert len(response.data) == 2

import pytest

from model_bakery import baker


@pytest.fixture
def key_pair():
	return dict(
		public='...',
		private='...',
	)


@pytest.fixture
def account_sender(key_pair):
	return baker.make(
		'accounts.Account',
		account='username',
		role='admin',
		key_pair=key_pair,
	)

import pytest
from django.test import Client
from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get('/')
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Python Pro</title>')


def test_home_link(resp):
    assert_contains(resp, 'href="/">Python Pro')

import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_index_page(client: Client):
    resp = client.get(reverse("index"))
    assert resp.status_code == 200
    assert "World" in resp.content.decode()
    assert resp.content.decode() == "Hello World"

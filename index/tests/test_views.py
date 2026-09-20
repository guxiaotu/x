import pytest
from django.urls import reverse
from pytest_django.asserts import (
    assertTemplateUsed,
    assertContains,
)


# @pytest.mark.django_db
# def test_index_page(client: Client):

#     from django.test import Client
#     resp = client.get(reverse("index"))
#     assert resp.status_code == 200
#     assert "World" in resp.content.decode()
#     assert resp.content.decode() == "Hello World"


@pytest.mark.django_db
def test_index_view(client):
    response = client.get(reverse("index"))

    # 1. 状态码
    assert response.status_code == 200

    # 2. 使用了哪个模板
    assertTemplateUsed(response, "index.html")

    # 3. context 数据
    # 3. 测「模板变量渲染后的内容」
    assertContains(response, "admin")
    assertContains(response, "Django123456")

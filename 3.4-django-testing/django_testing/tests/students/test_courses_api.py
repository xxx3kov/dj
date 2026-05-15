import pytest

from rest_framework.test import APIClient
from students.models import Course

# Arrange — готовим данные
# Act — совершаем действие, которое хотим протестировать
# Assert — проверяем результат


@pytest.mark.django_db
def test_get_course(client, courses_factory, base_url):
    course = courses_factory()

    response = client.get(f"{base_url}{course.id}/")

    assert response.status_code == 200
    assert response.json()["id"] == course.id


@pytest.mark.django_db
def test_get_courses(client, courses_factory, base_url):
    courses_factory(5)

    response = client.get(base_url)

    assert response.status_code == 200
    assert len(response.json()) == 5


@pytest.mark.django_db
def test_filter_courses_id(client, courses_factory, base_url):
    courses = courses_factory(5)

    response = client.get(base_url, data={"id": courses[0].id})

    data = response.json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["id"] == courses[0].id


@pytest.mark.django_db
def test_filter_courses_name(client, courses_factory, base_url):
    courses = courses_factory(5)

    response = client.get(base_url, data={"name": courses[0].name})

    data = response.json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["name"] == courses[0].name


@pytest.mark.django_db
def test_post_course(client, base_url):
    payload = {"name": "Python разработчик с нуля"}

    response = client.post(base_url, payload)

    assert response.status_code == 201
    assert response.json()["name"] == payload["name"]


@pytest.mark.django_db
def test_update_course(client, courses_factory, base_url):
    course = courses_factory()

    payload = {"name": "Python разработчик с нуля"}

    response = client.patch(f"{base_url}{course.id}/", payload)

    assert response.status_code == 200
    assert response.json()["name"] == payload["name"]


@pytest.mark.django_db
def test_delete_course(client, courses_factory, base_url):
    course = courses_factory()

    response = client.delete(f"{base_url}{course.id}/")

    assert response.status_code == 204
    assert not Course.objects.filter(id=course.id).exists()

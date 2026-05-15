import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def courses_factory():
    def factory(count=None, *args, **kwargs):
        if count is not None:
            return baker.make(Course, _quantity=count, *args, **kwargs)
        return baker.make(Course, *args, **kwargs)

    return factory

@pytest.fixture
def base_url():
    return "/api/v1/courses/"
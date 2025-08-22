import pytest
import random
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course

@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    """Фабрика студентов"""
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.fixture
def сourse_factory():
    """Фабрика курсов"""
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def random_course_from_courses(сourse_factory):
    """Фикстура для создания нескольких курсов и выбора одного из них"""
    courses_qty = random.randint(2, 10)
    courses = сourse_factory(_quantity=courses_qty)
    course_for_check = random.choice(range(courses_qty))
    return courses, course_for_check



@pytest.mark.django_db
def test_get_first_course(client, сourse_factory):
    """Проверка получения первого курса"""
   
    course = сourse_factory()      
    url = f'/api/v1/courses/{course.id}/'
    response = client.get(url)
  
    assert response.status_code == 200
    assert response.data['id'] == course.id
    assert response.data['name'] == course.name

@pytest.mark.django_db
def test_get_courses_list(client, сourse_factory):
    """Проверка получения списка курсов"""
    courses_qty = random.randint(2,10)
    courses = сourse_factory(_quantity=courses_qty)
    
    url = '/api/v1/courses/'
    response = client.get(url)
    data = response.json()
    
    assert response.status_code == 200
    assert len(data) == courses_qty
    
    for i, course in enumerate(data):
        assert course['name'] == courses[i].name



@pytest.mark.django_db
def test_get_course_by_id(client, random_course_from_courses):
    """Проверка получения курсов по фильтру id"""
   
    courses, course_for_check = random_course_from_courses

    url = f'/api/v1/courses/?id={courses[course_for_check].id}'
    response = client.get(url)

    assert response.status_code == 200   
    assert response.data[0]['id'] == courses[course_for_check].id
    assert response.data[0]['name'] == courses[course_for_check].name


@pytest.mark.django_db
def test_get_course_by_name(client, random_course_from_courses):
    """Проверка получения курсов по фильтру name"""

    courses, course_for_check = random_course_from_courses

    url = f'/api/v1/courses/?name={courses[course_for_check].name}'
    response = client.get(url)

    assert response.status_code == 200   
    assert response.data[0]['id'] == courses[course_for_check].id
    assert response.data[0]['name'] == courses[course_for_check].name


@pytest.mark.django_db
def test_create_course(client):
    """Тест создания курса вручную"""
   
    course= {
        'name': 'Test course',
        'students': []  
    }
    count = Course.objects.count()
    url = '/api/v1/courses/'
    response = client.post(url, course, format='json')
   
    assert response.status_code == 201
    assert response.data['name'] == course["name"]
    assert Course.objects.count() == count + 1

@pytest.mark.django_db
def test_update_course(client, сourse_factory):
    """Тест успешного обновления курса"""
    
    course = сourse_factory()
    
    update_course = {
        'name': 'New name',
        'students': []
    }
   
    url = f'/api/v1/courses/{course.id}/'
    response = client.put(url, update_course, format='json')
    
    assert response.status_code == 200
    assert response.data['name'] == update_course["name"]
    
    course_for_check = Course.objects.get(id=course.id)
    assert course_for_check.name == update_course["name"]

@pytest.mark.django_db
def test_delete_course(client, сourse_factory):
    """Тест для проверки удаления курса"""
    
    course = сourse_factory()
    
    url = f'/api/v1/courses/{course.id}/'
    response = client.delete(url)
    
    assert response.status_code == 204
    assert not Course.objects.filter(id=course.id).exists()



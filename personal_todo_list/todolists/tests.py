from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import TodoList
from .views import delete
from . import forms


class TodoListTests(TestCase):

    def setUp(self):
        self.item = TodoList.objects.create(item='Testing')

    def test_content(self):
        items = TodoList.objects.get(pk=1)
        result_item = f'{items.item}'
        assert result_item == 'Testing'

    def test_correct_view_used(self):
        response = self.client.get(reverse('home'))
        assert response.status_code == 200

    def test_delete_views(self):
        self.factory = RequestFactory()
        request = self.factory.get('/delete/')
        request.item = self.item
        response = delete(request, list_id=1)
        assert response.status_code == 302

    def test_post_method(self):
        forms.TodoListForm(data={})
        response = self.client.post(reverse('home'), data={'item': 'test'})
        assert response.status_code == 200

    def test_valid_data(self):
        form = forms.TodoListForm({
            'item': 'Form',
            'completed': 'False'
        },)
        assert form.is_valid() is True
        items = form.save()
        assert items.item == 'Form'
        assert items.completed is False

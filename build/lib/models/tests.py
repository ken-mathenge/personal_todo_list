from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import List
from .views import delete


class ListTests(TestCase):

    def setUp(self):
        self.item = List.objects.create(item='Testing')

    # def create_model(self, item='Testing'):
    #     return List.objects.create(item=item)

    # def create_model2(self, item='Testing delete'):
    #     return List.objects.create(item=item)

    # def create_model3(self, item='Testing cross'):
    #     return List.objects.create(item=item)

    def test_content(self):
        # items = self.create_model()
        items = List.objects.get(pk=1)
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

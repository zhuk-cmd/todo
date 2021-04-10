from django.test import TestCase
from app_name.models import ToDoItem
from django.db.models import QuerySet
# Create your tests here.


class TaskTest(TestCase):
    def setUp(self):
        self.task_1 = ToDoItem.objects.create(content='Task')

    def test_add_to_do(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'to_do_list.html')

    def test_delete_to_do(self):
        response = self.client.post(f'/deletetodo/{self.task_1.pk}')
        self.assertRedirects(response, '/', 302, fetch_redirect_response=False)
        task_list = ToDoItem.objects.all()
        self.assertNotIn(self.task_1, task_list)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'to_do_list.html')
        self.assertIn('data', response.context)
        data = response.context['data']
        self.assertIsInstance(data, QuerySet)
        self.assertNotIn(self.task_1, data)

    def test_edit_task_404(self):
        response = self.client.get('/edit/failure')
        self.assertEqual(response.status_code, 404)



from django.test import Client, TestCase

from .models import Writing


# Create your tests here.
class WritingTest(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass


    def tearDown(self):
        # Clean up run after every test method.
        pass


    def test_writing_index_get_method(self):
        c = Client()
        response = c.get('/board/')
        code = response.status_code
        self.assertEqual(code, 200)


    def test_writing_index_post_method(self):
        c = Client()
        response = c.post('/board/')
        code = response.status_code
        self.assertEqual(code, 405)

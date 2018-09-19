from django.test import TestCase, RequestFactory
from .models import Book
from django.contrib.auth.models import User


class TestBookModel(TestCase):
    def setUp(self):
        # add to db through model
        self.user = User.objects.create(username='test', email='test@example.com')
        # set an encrypted password
        self.user.set_password('hello')
        self.book = Book.objects.create(title='Feed the Kat', author='Your dog', user=self.user)
        Book.objects.create(title='Eat some pie')

    def test_book_titles(self):
        self.assertEqual(self.book.title, 'Feed the Kat')


class TestBookViews(TestCase):
    def setUp(self):
        self.request = RequestFactory()
        self.book1 = Book.objects.create(title='bloop')
        self.book2 = Book.objects.create(title='derp')

    def test_book_detail_view(self):
        from .views import books_detail_view
        request = self.request.get('')
        response = books_detail_view(request, f'{self.book_one.id}')
        self.assertIn(b'bloop', response.content)

    def test_book_detail_status(self):
        from .views import books_detail_view
        request = self.request.get('')
        response = books_detail_view(request, f'{self.book_one.id}')
        self.assertEqual(200, response.status_code)


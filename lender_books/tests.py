from django.test import TestCase, RequestFactory
from .models import Book
from django.contrib.auth.models import User


class TestBookModel(TestCase):
    def setUp(self):
        # add to db through model
        self.user = User.objects.create(username='test', email='test@test.com')
        # set an encrypted password
        self.user.set_password('1234')
        self.book = Book.objects.create(
            title='Feed Kat',
            author='She likes pie',
            user=self.user
        )
        Book.objects.create(title='Sid tha cat', author='Ruby', user=self.user)
        Book.objects.create(title='Ruby the kitty', author='Sid', user=self.user)

    def test_book_titles(self):
        self.assertEqual(self.book.title, 'Feed Kat')

    def test_book_detail(self):
        book = Book.objects.get(title='Sid tha cat')

        self.assertEqual(book.author, 'Ruby')


class TestBookViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test2', email='test2@test.com')
        self.user.set_password('12345')
        self.request = RequestFactory()
        self.book_one = Book.objects.create(title='Rooo', author='Sidward')
        self.book_two = Book.objects.create(title='Sidward', author='Rooo')

    def test_book_detail_view(self):
        from .views import books_detail_view
        request = self.request.get('')
        response = books_detail_view(request, f'{self.book_one.id}')
        self.assertIn(b'Sidward', response.content)

    def test_book_detail_status(self):
        from .views import books_detail_view
        request = self.request.get('')
        response = books_detail_view(request, f'{self.book_one.id}')
        self.assertEqual(200, response.status_code)


# dir(response) find templates

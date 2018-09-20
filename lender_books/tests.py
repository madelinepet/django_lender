from django.test import TestCase, RequestFactory
from .models import Book
from django.contrib.auth.models import User


class TestBookModel(TestCase):
    def setUp(self):
        """ sets up the test for the models with a user
        """
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
        """ Checks to make sure the title of the book set up is correct
        """
        self.assertEqual(self.book.title, 'Feed Kat')

    def test_book_detail(self):
        """ Checks to make sure the author is correct
        """
        book = Book.objects.get(title='Sid tha cat')

        self.assertEqual(book.author, 'Ruby')


class TestBookViews(TestCase):
    def setUp(self):
        """ Sets up the tests for the views with a user and some books
        """
        self.user = User.objects.create(username='test2', email='test2@test.com')
        self.user.set_password('12345')
        self.request = RequestFactory()
        self.book_one = Book.objects.create(title='Rooo', author='Sidward', user=self.user)
        self.book_two = Book.objects.create(title='Sidward', author='Rooo', user=self.user)

    def test_book_detail_view(self):
        """ Test the title is in the content of the repsonse
        """
        from .views import books_detail_view
        # mock request object that can have a path set on it
        request = self.request.get('')
        # need to bind the user to each request
        request.user = self.user
        response = books_detail_view(request, f'{self.book_one.id}')
        # import pdb; pdb.set_trace()
        self.assertIn(b'Sidward', response.content)

    def test_book_detail_status(self):
        """ Test the status code for creating a book with a registered user is 200
        """
        from .views import books_detail_view
        request = self.request.get('')
        request.user = self.user
        response = books_detail_view(request, f'{self.book_one.id}')
        self.assertEqual(200, response.status_code)

    def test_book_list_view(self):
        """ Test the book list view has the title in the response content
        """
        from .views import books_list_view
        request = self.request.get('')
        request.user = self.user
        response = books_list_view(request)
        self.assertIn(b'Sidward', response.content)

    def test_book_detail_date_filtered(self):
        """ Tests the response content for book detail has date added on it
        """
        from .views import books_detail_view
        request = self.request.get('')
        request.user = self.user
        response = books_detail_view(request, f'{self.book_one.id}')
        self.assertIn(b'Added: Today.', response.content)


# dir(response) find templates. They're in response.content
class TestBookTemplates(TestCase):
    def setUp(self):
        """ Sets up the template tests with a registered user
        """
        self.user = User.objects.create(username='test3', email='test3@test.com')
        self.user.set_password('123456')
        self.request = RequestFactory()
        self.book_three = Book.objects.create(title='my cat', author='me', user=self.user)
        self.book_four = Book.objects.create(title='your dog', author='you', user=self.user)

    # def test_book_detail_html(self):
        """Test that the content has specific words on it
        """

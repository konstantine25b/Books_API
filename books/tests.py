from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, RequestsClient, APIRequestFactory , force_authenticate
from django.test import TestCase
from .views import AuthorListCreate
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


import pytest
from django.contrib.auth.models import User
from .models import Book, Author

# # py = tests
# @pytest.mark.django_db
# def test_author_book_relationship():
#     author = Author.objects.create(name = "kio" , nationality = "American")
#     Book.objects.create(title = "bk1" , author = author , publication_date = "2019-02-07")
#     Book.objects.create(title = "bk2" , author = author , publication_date = "2011-04-02")
    
#     assert Book.objects.filter(author = author).count() ==2
    
#     author.delete()
    
#     assert Book.objects.count() == 0


# @pytest.mark.django_db
# def test_book_creation():
#     client = APIClient()
    
#     user = User.objects.create_user(username = "ts1" , password = "ts")
#     url = '/api/books/'
#     url2= '/api/authors/'
    
#     author = client.post(url2,{'name': 'john' , 'nationality':"samtredia" } , format ='json' )
#     assert author.status_code == 201
    
#     response = client.post(url , {'title': 'bk n' , 'publication_date': '2018-03-11' } , format ='json')
    
#     assert response.status_code == 401
    
#     refresh = RefreshToken.for_user(user)
#     client.credentials(HTTP_AUTHORIZATION = f'Bearer {refresh.access_token}')
#     response = client.post(url , {'title': 'bk k' , 'author' :1, 'publication_date': '2018-03-11' } , format ='json')
    
#     assert response.status_code == 201

# @pytest.mark.django_db
# def test_author_pagination():
#     client = APIClient()
    
#     for i in range(23):
#         Author.objects.create(name= f"Author {i}", nationality = f"nationality {i}" )
    
#     response =client.get('/api/authors/')
    
#     assert response.status_code == 200
    
#     assert len(response.json()['results']) == 10
    
#     assert 'next' in response.json()
#     assert response.json()['next'] is not None
     



# @pytest.mark.django_db
# def test_filter_authors():
#     client = APIClient()
    
#     Author.objects.create(name= f"kosarioni", nationality = f"geo3" )
#     Author.objects.create(name= f"kosa", nationality = f"geo" )
#     Author.objects.create(name= f"kotiko", nationality = f"geo" )
#     Author.objects.create(name= f"kosarioaaani", nationality = f"geo2" )
#     Author.objects.create(name= f"kosarfdsgfeioni", nationality = f"geo" )
    
#     response = client.get('/api/authors/', {'nationality' :'georgian'})
#     authors = response.json()['results']
    
#     assert response.status_code == 200
#     assert all(author['nationality'] =='geo' for author in authors)
    
    

    
 
 
 
# ----- new tests

class BookAPITestCase(TestCase):
    def setup(self):
        self.client = APIClient()
        self.author = Author.objects.create(name = 'john' , nationality ='french')
        self.book_date = {
            'title' :'test bk',
            'author': self.author.id,
            'publication_date':"2023-02-03"           
        }
        self.book =Book.objects.create(**self.book_data , author=self.author)
        
    def tets_create_book_with_valid_data(self):
        response = self.client.post(reverse('book-list') ,self.book_date , format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(Book.objects.count() ,1)
        self.assertNotEqual
        
  
  
    

#  django tests
# class AuthorTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()
        
        
#     def test_list_authors(self):
#         response = self.client.get(reverse('author-list'))
#         self.assertEqual(response.status_code , status.HTTP_200_OK)
        
#     def test_create_author(self):
#         response =self.client.post(reverse('author-list') , {'name': 'kosiko' , 'nationality' : 'kai bichi'},format = 'json')
#         self.assertEqual(response.status_code , status.HTTP_201_CREATED)
        
#     def test_create_author_error(self):
#         response =self.client.post(reverse('author-list') , { 'nationality' : 'kai bichi'},format = 'json')
#         self.assertEqual(response.status_code , status.HTTP_400_BAD_REQUEST)
        
# class BookListTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create_user(username='testuser' , password ='testuser123')
#         self.token = RefreshToken.for_user(self.user)
        
#     def test_list_books_unauth(self):
#         response = self.client.get(reverse('book-list'))
#         self.assertEqual(response.status_code , status.HTTP_401_UNAUTHORIZED)
        
#     def test_list_books_auth(self):
#         self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.token.access_token}')
#         response = self.client.get(reverse('book-list'))
#         self.assertEqual(response.status_code,status.HTTP_200_OK)
        
# class BookListTestsWithRequestCLient(TestCase):
#     def setUp(self):
#         self.client = RequestsClient()
#         self.user = User.objects.create_user(username='testuser12' , password ='testuser12')
#         self.token = RefreshToken.for_user(self.user)
#         self.client.headers.update({"Authorization": f"Bearer {self.token.access_token}"})
        
#     def test_list_books(self):
#         response = self.client.get('http://127.0.0.1:8000/api/books/')
#         self.assertEqual(response.status_code, 200)
        
        
# class AuthorCreateTestFactory(TestCase):
#     def setUp(self):
#         self.factory = APIRequestFactory()
#         self.user = User.objects.create_user(username='testuser12', email = "test@gmail.com" , password ='testuser12')
        
#     def test_create_author_with_factory(self):
#         request = self.factory.post('/authors/', {'name': 'kosiko2' , 'nationality' : 'kai bichi2'},format = 'json')
#         force_authenticate(request , user = self.user)
#         response = AuthorListCreate.as_view()(request)
#         self.assertEqual(response.status_code, 201)
        
        

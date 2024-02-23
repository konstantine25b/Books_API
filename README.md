# Books and Authors Django Project

This Django project manages books and authors through a RESTful API. It allows you to create, retrieve, update, and delete authors and books.

## Installation

1. Clone the repository:
git clone https://github.com/konstantine25b/Books_API
cd Books_API

2. pip install -r requirements.txt

Usage
Run Django migrations to set up the database:

python manage.py migrate

Start the development server:

python manage.py runserver

Models
Author
name (CharField): The name of the author.
nationality (CharField): The nationality of the author.
Book
title (CharField): The title of the book.
author (ForeignKey to Author): The author of the book.
publication_date (DateField): The publication date of the book.
Serializers
AuthorSerializer
id: The unique identifier of the author.
name: The name of the author.
nationality: The nationality of the author.
BookSerializer
id: The unique identifier of the book.
title: The title of the book.
author: The author of the book.
publication_date: The publication date of the book.
Tests
The project includes tests to ensure the functionality of the API endpoints. Tests include:

Retrieving a list of authors and books.
Creating new authors and books.
Filtering authors and books based on specific criteria.
Views
AuthorListCreate
GET: Retrieve a list of authors.
POST: Create a new author.
BookListCreate
GET: Retrieve a list of books.
POST: Create a new book.
Permissions
IsAuthenticated: Only authenticated users can create books.
Filter
The API supports filtering for both authors and books based on certain fields:

Authors can be filtered by nationality.
Books can be filtered by publication_date

import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.id, 1)
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.content, "Test Content")
        self.assertEqual(article.author_id, 1)
        self.assertEqual(article.magazine_id, 1)

    def test_instance_from_db(self):
        row = (1, "Test Title", "Test Content", 1, 1)
        article = Article.instance_from_db(row)
        self.assertIsInstance(article, Article)
        self.assertEqual(article.id, 1)
        self.assertEqual(article.content, "Test Content")
        self.assertEqual(article.author_id, 1)
        self.assertEqual(article.magazine_id, 1)

    def test_get_all(self):
        articles = Article.get_all()
        self.assertIsInstance(articles[0], Article)
        self.assertEqual(articles[0].id, 1)
        self.assertEqual(articles[0].author_id, 1)
        self.assertEqual(articles[0].magazine_id, 1)
        self.assertIsInstance(articles[1], Article)
        self.assertEqual(articles[1].id, 2)
        self.assertEqual(articles[1].author_id, 2)
        self.assertEqual(articles[1].magazine_id, 2)

if __name__ == "__main__":
    unittest.main()
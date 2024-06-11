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

    # Magazine class tests.
    def test_id_getter(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.id, 1)

    def test_name_getter(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")

    def test_category_getter(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.category, "Technology")

    def test_id_setter(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        magazine.id = 2
        self.assertEqual(magazine.id, 2)

    def test_name_setter(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        magazine.name = "Science Monthly"
        self.assertEqual(magazine.name, "Science Monthly")

    def test_category_setter(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        magazine.category = "Science"
        self.assertEqual(magazine.category, "Science")

    # Author's class tests.
    def author_test_id_getter(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.id, 1)
        
    def test_id(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.id, 1)


    def test_author_id(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.id, 1)

    def test_author_name(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    # Article class.
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

    
    def test_article_id(self):
        article = Article(1, "article", "article-category", 1, 1)
        self.assertEqual(article.id, 1)
    
    def test_article_title(self):
        article = Article(1, "Article", "Article-category", 1, 1)
        self.assertEqual(article.title, "Article")


    def test_name(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
    

if __name__ == "__main__":
    unittest.main()
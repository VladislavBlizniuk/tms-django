from django.test import TestCase
from django.urls import reverse

from .models import Article


def create_new_article(title, text, author, like_count):
    return Article.objects.create(title=title, text=text, author=author, like_count=like_count)


class ArticleModelTest(TestCase):
    def test_is_this_list_empty(self):
        article = self.client.get(reverse('articles:index'))
        self.assertEquals(article.status_code, 200)
        self.assertContains(article, 'Sorry,there are no articles')

    def test_there_are_articles_in_list(self):
        article = create_new_article('new article', 'long text', 'new author', 3)
        response = self.client.get(reverse('articles:index'))
        self.assertEquals(article.status_code, 200)
        self.assertQuerysetEqual(response.context['articles'], [article])

    def test_is_this_article_popular(self):
        article = Article(like_count=105)
        self.assertTrue(article.is_popular)

    def test_this_article_is_not_popular(self):
        article = Article(like_count=19)
        self.assertTrue(article.is_popular)

    def test_there_is_mistake_404(self):
        create_new_article('new article', 'long text', 'new author', 3)
        response = self.client.get(reverse('articles:detail', args=[10]))
        self.assertEqual(response.status_code, 404)

    def test_there_is_no_mistake_404(self):
        article = create_new_article('new article', 'long text', 'new author', 3)
        response = self.client.get(reverse('articles:detail', args=[article.id]))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, article.text)
from django.test import RequestFactory, TestCase
from django.urls import reverse

from main.models import Word
from main.views import WordDetailView

class WordDetailViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.word = Word.objects.create(title='word', slug='word-slug')

    def test_word_detail_view_get(self):
        # create a GET request to the detail view for the word
        request = self.factory.get(reverse('detail_word', kwargs={'word_slug': self.word.slug}))
        # call the as_view method on the WordDetailView class with the request and word_slug argument
        response = WordDetailView.as_view()(request, word_slug=self.word.slug)
        # check that the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)
        # check that the word object returned in the context is the same as the one created in the setup
        self.assertEqual(response.context_data['detail_word'], self.word)
        # check that the correct template is used
        self.assertTemplateUsed(response, 'main/word.html')

    def test_word_detail_view_post(self):
        # create a POST request to the detail view for the word with permission='granted' in the POST data
        request = self.factory.post(reverse('detail_word', kwargs={'word_slug': self.word.slug}), {'permission': 'granted'})
        # call the as_view method on the WordDetailView class with the request and word_slug argument
        response = WordDetailView.as_view()(request, word_slug=self.word.slug)
        # check that the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)
        # check that the word object returned in the context is the same as the one created in the setup
        self.assertEqual(response.context_data['detail_word'], self.word)
        # check that the correct template is used
        self.assertTemplateUsed(response, 'main/word.html')

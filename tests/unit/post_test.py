from unittest import TestCase
from posts import Post

class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test','Tests Content')

        self.assertEqual('Test',p.title)
        self.assertEqual('Tests Content',p.content)

    def test_json(self):
        p = Post('Test','Tests Content')
        expected = {'title':'Test', 'content': 'Tests Content'}

        self.assertDictEqual(expected, p.json())

    
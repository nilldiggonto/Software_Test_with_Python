from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test','Test Author')

        self.assertEqual('Test',b.title)
        self.assertEqual('Test Author',b.author)
        self.assertListEqual([],b.posts)

    def test_repr(self):
        b = Blog('Test','Test Author')
        b2 = Blog('Test2','Test2 Author')

        self.assertEqual(b.__repr__(),'Test by Test Author (0 Posts)')
        self.assertEqual(b2.__repr__(),'Test2 by Test2 Author (0 Posts)')

    def test_repr_multiple_post(self):
        b = Blog('Test','Test Author')
        b.posts =['Test_post']

        b2 = Blog('Test2','Test2 Author')
        b2.posts = ['one','two']
        self.assertEqual(b.__repr__(),'Test by Test Author (1 Post)')
        self.assertEqual(b2.__repr__(),'Test2 by Test2 Author (2 Posts)')
        
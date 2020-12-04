from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog


class AppTest(TestCase):

    def test_user_menu_promt(self):
        with patch('builtins.input') as mocked_input:
            app.user_menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_user_menu_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input',return_value='q'):
                app.user_menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        blog = Blog('Test','Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('Test by Test Author (0 Posts)')

    
    
MENU_PROMPT = " 'c' to create blog, 'l' to list blogs, 'r' to read, 'p' to create post, 'q' to quit"
POST_TEMPLATE = '''---- {} ---- {}'''

from blog import Blog
blogs = dict()

def user_menu():
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    for key,blog in blogs.items():
        print(f'{blog}')


def ask_create_blog():
    title = input('Blog Title')
    author = input('Blog Author')

    blogs[title] = Blog(title,author)


def ask_read_blog():
    title = input('Blog Title to read')
    print_posts(blogs[title])



def print_posts(blogs):
    for post in blogs.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title,post.content))



        
def ask_create_post():
    blog_name = input('Blog Title')
    title = input('Post Title')
    content = input('Post Content')

    blogs[blog_name].create_post(title,content)
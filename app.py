MENU_PROMPT = " 'c' to create blog, 'l' to list blogs, 'r' to read, 'p' to create post, 'q' to quit"

blogs = dict()

def user_menu():
    print_blogs()
    selection = input(MENU_PROMPT)


def print_blogs():
    for key,blog in blogs.items():
        print(f'{blog}')
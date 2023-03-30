import os
import re
from datetime import datetime
from markdown import markdown
from app.blog.models import Post

def load_posts(directory="app/blog/blog_posts"):
    post_list = []
    for filename in sorted(os.listdir(directory), reverse=True):
        if filename.endswith(".md"):
            with open(os.path.join(directory, filename), "r") as file:
                content = file.read()
                html_content = markdown(content)
                title = re.search(r"<h1>(.+)</h1>", html_content).group(1)
                date_str = re.search(r"(\d{4}-\d{2}-\d{2})", filename).group(1)
                date_posted = datetime.strptime(date_str, "%Y-%m-%d")
                post = Post(title=title, content=html_content, date_posted=date_posted)
                post_list.append(post)
    return post_list

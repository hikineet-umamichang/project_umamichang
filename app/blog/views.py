from flask import render_template, url_for, flash, redirect, request, abort
from . import blog
from app.blog.utils import load_posts
from datetime import datetime

def paginate(posts, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    return posts[start:end]

# 記事一覧表示
@blog.route('/')
@blog.route('/page/<int:page>')
def home(page=1):
    posts = load_posts()
    per_page = 10
    paginated_posts = paginate(posts, page, per_page)
    total_pages = (len(posts) + per_page - 1) // per_page
    return render_template('blog/home.html', posts=paginated_posts, page=page, total_pages=total_pages)

@blog.route('/<string:post_date>-<string:post_title>')
def post_detail(post_date, post_title):
    post_date = datetime.strptime(post_date, "%Y-%m-%d")
    posts = load_posts()

    post = None
    for p in posts:
        if p.date_posted.date() == post_date.date() and p.title == post_title:
            post = p
            break

    if post is None:
        abort(404)

    return render_template('blog/post_detail.html', post=post)

from flask import render_template, request
from flask_paginate import Pagination, get_page_parameter
from . import blog
from . import utils


@blog.route("/")
def index():

    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10
    posts = utils.get_posts_list()
    page_posts = posts[(page - 1) * 10 : page * 10]
    pagination = Pagination(
        page=page,
        total=len(posts),
        search=False,
        display_msg="<b>{total}</b> {record_name}中の <b>{start} - {end}</b> {record_name}",
        record_name="ページ",
        per_page=per_page,
        css_framework="bootstrap5",
    )
    # print(page_posts)

    return render_template(
        "blog/index.html", page_posts=page_posts, pagination=pagination
    )


@blog.route("/<string:filename>")
def post_detail(filename):
    filename=filename+".md"
    metadata = utils.parse_metadata(filename)
    content = utils.load_post(filename)
    # print(metadata)
    # print(content)
    return render_template("blog/post.html", content=content, metadata=metadata)


@blog.route("/tag-<string:tag>")
def tag_filtered(tag):
    target_posts=utils.get_posts_by_tag(tag)
    # print(target_posts)

    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10
    page_posts = target_posts[(page - 1) * 10 : page * 10]
    pagination = Pagination(
        page=page,
        total=len(target_posts),
        search=False,
        display_msg="<b>{total}</b> {record_name}中の <b>{start} - {end}</b> {record_name}",
        record_name="ページ",
        per_page=per_page,
        css_framework="bootstrap5",
    )

    return render_template("blog/tag_filtered.html", tag=tag,posts=page_posts,pagination=pagination)


@blog.context_processor
def inject_recent_posts_and_tags():
    return {
        'recent_posts': utils.get_recent_posts(),
        'tags': utils.get_tags(),
    }


@blog.route("/tags")
def tags():
    tags=utils.get_tags()

    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10
    page_tags = tags[(page - 1) * 10 : page * 10]
    pagination = Pagination(
        page=page,
        total=len(tags),
        search=False,
        display_msg="<b>{total}</b> {record_name}中の <b>{start} - {end}</b> {record_name}",
        record_name="ページ",
        per_page=per_page,
        css_framework="bootstrap5",
    )

    return render_template("blog/tags.html",tags=page_tags,pagination=pagination)


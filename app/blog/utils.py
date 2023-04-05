import os
import re
from datetime import datetime
from markdown import markdown
import yaml
from flask import url_for

posts_directory="blog_posts"

def parse_metadata(filename, directory=posts_directory):
    file_path = os.path.join(directory, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if lines[0].strip() != "---":
        raise ValueError("Metadata not found in the file.")

    metadata_lines = []
    for line in lines[1:]:
        if line.strip() == "---":
            break
        metadata_lines.append(line)

    metadata_str = "".join(metadata_lines)
    metadata = yaml.safe_load(metadata_str)

    metadata["filename"] = filename.replace('.md','')
    return metadata


def get_posts_list(directory=posts_directory):
    post_list = []
    for filename in sorted(os.listdir(directory), reverse=True):
        if filename.endswith(".md"):
            post = parse_metadata(filename, directory)
            post_list.append(post)
    return post_list


def load_post(filename, directory=posts_directory):
    file_path = os.path.join(directory, filename)

    with open(file_path, "r", encoding="utf-8") as f:
        blog_text = f.read()


    reg_delete_metadata = r"^---*[\r\n]*([\s\S]*?)---*[\r\n]"

    blog_text = re.sub(reg_delete_metadata, "", blog_text)



    src_pattern = r'src="images'
    src_replacement = r'src="/images'
    
    closing_tag_pattern = r'\/>'
    closing_tag_replacement = r' class="img-fluid">'

    blog_text = re.sub(src_pattern, src_replacement, blog_text)
    blog_text = re.sub(closing_tag_pattern, closing_tag_replacement, blog_text)



    blog_text_html = markdown(
        blog_text,
        extensions=["extra", "toc", "fenced_code", "codehilite"],
        extension_configs={
            "toc": {"title": "目次"},
            "codehilite": {
                "noclasses": True,
            },
        },  # 目次にタイトルを設ける
    )

    return markdown(blog_text_html)

def get_posts_by_tag(tag_name):
    metadata=get_posts_list()
    # print(metadata)

    target_posts=[]
    for x in metadata:
        if tag_name in x['tags']:
            target_posts.append(x)

    return target_posts

def get_recent_posts():

    recent_posts=get_posts_list()[:5]

    return recent_posts

def get_tags():
    tags=[]

    metadata=get_posts_list()
    for post in metadata:
        tags.extend(post['tags'])    

    tags=list(set(tags))
    return tags
from datetime import datetime

class Post:
    def __init__(self, title, content, date_posted):
        self.title = title
        self.content = content
        self.date_posted = date_posted

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

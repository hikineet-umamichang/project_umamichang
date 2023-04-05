import os
from datetime import date, timedelta
import random

def create_sample_articles(num_articles):
    template = """---
title: サンプル記事{0}
date: {1}
tags: {2}
---
これはサンプル記事{0}です。
"""

    tags_list=['Flask','Python','Mac','Windows','サバ缶','犬','猫','さつまいも','カレー','日常','花']

    # サンプル記事の生成
    start_date = date(2023, 3, 31)
    for i in range(1, num_articles + 1):
        current_date = start_date - timedelta(days=i - 1)
        content = template.format(i, current_date.isoformat(),random.sample(tags_list,3))

        file_name = f"{current_date.strftime('%Y-%m-%d')}_sample{i}.md"
        file_path = file_name

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

# 例：100個のサンプル記事を生成
create_sample_articles(100)

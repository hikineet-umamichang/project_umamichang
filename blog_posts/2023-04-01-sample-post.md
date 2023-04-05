---
title: マークダウンのテスト
date: 2023-04-01
tags: [Flask, Python, ブログ]
---
これはマークダウンのテスト記事です。

# h1 Heading 8-)
## h2 Heading
### h3 Heading
#### h4 Heading
##### h5 Heading
###### h6 Heading

## Horizontal Rules
---

<img alt="picture 1" src="images/sample_image.jpg" />  


* リスト1
* リスト2
* リスト3

> 引用してくれ

本文で **太字にもなるし**、*斜体にもなるはず* 。

```{ python noclasses=True pygments_style='default'}
まさかコードも入れられるんですか？
if (lie):
    return true

def post_detail(filename):
    metadata = utils.parse_metadata(filename:=filename+".md")
    content = utils.load_post(filename:=filename)
    print(metadata)
    print(content)

    return render_template("blog/post.html", content=content, metadata=metadata)
```

| header1 | header2 | header3 |
|:-----------|------------:|:------------:|
| 左寄せ | 右寄せ | 中央寄せ |

すごい！
HTMLタグ。

```{ html noclasses=True pygments_style='default'}
<p>テスト</p>
```

## 言語

* HTML
* JavaScript

### 参考

> 引用

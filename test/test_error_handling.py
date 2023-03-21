def process_input(input_string):
    try:
        word1, word2 = input_string.split()
    except ValueError:
        return "入力エラー: 2つの単語を空白で区切って入力してください。"
    except Exception as e:
        return f"予期せぬエラーが発生しました: {e}"

    return [word1, word2]

# 入力データの例
inputs = [
    "apple orange",  # 正常な入力
    "appleorange",   # 単語が空白で区切られていない
    "apple orange kiwi",  # 3つの単語が入力された
    "",  # 入力が空
]

for input_string in inputs:
    result = process_input(input_string)
    print(f"入力: '{input_string}' → 処理結果: {result}")

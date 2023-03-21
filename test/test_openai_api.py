import os
from dotenv import load_dotenv
import openai
import random

load_dotenv()

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")
# print(openai.api_key)

genre = input("ジャンル：")
difficulty = input("難易度(1~10):")
distance = input("単語の距離；")
num_players=int(input("プレーヤーの人数："))


def generate_themes(genre, difficulty, distance):

    with open(os.path.dirname(__file__)+"/test_openai_api.txt", "r", encoding="utf-8") as file:
        input_text = file.read()

    input_text = (
        input_text.replace("{{genre}}", genre)
        .replace("{{difficulty}}", difficulty)
        .replace("{{distance}}", distance)
    )
    # print(input_text)

    # Call OpenAI API to generate themes
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": input_text}],
    )
    themes = list(response.choices[0]["message"]["content"].strip().split())

    return themes

for _ in range(3):
    themes = generate_themes(genre, difficulty,distance)
    wolf_index = random.randint(0, int(num_players) - 1)
    themes_list = [theme[0] if i == wolf_index else theme[1] for i in range(int(num_players))]
    print(themes_list)


# genre_list=["甘いもの","歴史の偉人","金属製品","小さな動物","歴史用語","赤いもの","アニメキャラ","学校あるある","人間に大切なもの","家具"]
# for i in range(10):
#     genre=genre_list[i]
#     difficulty=str(random.randint(1,10))
#     distance=str(random.randint(1,10))

#     print(f'{i}回目  ジャンル：{genre}、難易度(1~10)：{difficulty}、距離(1~10)：{distance}')
#     print(generate_themes(genre, difficulty, distance))

# # print("ジャンル：",genre_list[0])
# # for i in range(10):
# #     genre=genre_list[0]
# #     difficulty=str(5)
# #     distance=str(i+1)

# #     print(f'{i}回目、難易度：{difficulty}、距離：{distance}')
# #     print(generate_themes(genre, difficulty, distance))

# # print("ジャンル：",genre_list[5])
# # for i in range(10):
# #     genre=genre_list[5]
# #     difficulty=str(i+1)
# #     distance=str(5)

# #     print(f'{i}回目、難易度：{difficulty}、距離：{distance}')
# #     print(generate_themes(genre, difficulty, distance))
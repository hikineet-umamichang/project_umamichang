import os
import random
from flask import render_template, request, redirect, url_for, flash
from . import wordwolf
import openai

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_themes(genre, difficulty, distance):
    # print(os.getcwd())
    if len(genre) > 15:
        return ["生成失敗", "生成失敗"]
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as file:
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

    try:
        themes = list(response.choices[0]["message"]["content"].strip().split())
    except:
        return ["生成失敗", "生成失敗"]
    return themes


@wordwolf.route("/", methods=["GET", "POST"])
def settings():
    return render_template("wordwolf/settings.html")


@wordwolf.route("/reveal", methods=["GET", "POST"])
def reveal():
    if request.method == "POST":
        num_players = int(request.form.get("num_players"))
        difficulty = request.form.get("difficulty")
        distance = request.form.get("distance")
        genre = request.form.get("genre")

        themes = generate_themes(genre, difficulty, distance)
        wolf_index = random.randint(0, int(num_players) - 1)
        themes_list = [
            themes[0] if i == wolf_index else themes[1] for i in range(int(num_players))
        ]

        return render_template(
            "wordwolf/reveal.html",
            themes=themes_list,
            num_players=num_players,
            enumerate=enumerate,
        )

    return redirect(url_for("wordwolf.reveal"))

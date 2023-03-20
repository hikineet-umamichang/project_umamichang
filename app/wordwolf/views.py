import os
import random
from flask import render_template, request, redirect, url_for, flash
from . import wordwolf
import openai

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_themes(genre, difficulty):
    # Call OpenAI API to generate themes
    """response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Generate a pair of related themes for Word Wolf game with genre '{genre}' and difficulty {difficulty}. One theme for citizens and one slightly different theme for the wolf. Separate them with a newline.",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.8,
    )

    themes = response.choices[0].text.strip().split("\n")"""
    themes=["いちご","りんご"]
    return themes


@wordwolf.route("/", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        num_players = int(request.form["num_players"])
        difficulty = int(request.form["difficulty"])
        genre = request.form["genre"]
        themes = generate_themes(genre, difficulty)
        return redirect(
            url_for("wordwolf.reveal", themes=themes, num_players=num_players)
        )
    return render_template("wordwolf/settings.html")


@wordwolf.route("/reveal", methods=["GET", "POST"])
def reveal():
    themes = request.args.get("themes", "").split(",")
    num_players = int(request.args.get("num_players", "4"))

    if request.method == "POST":
        return redirect(url_for("wordwolf.settings"))

    return render_template(
        "wordwolf/reveal.html", themes=themes, num_players=num_players, enumerate=enumerate
    )

"""Flask web app for the FAQ chatbot.

Run:  python app.py   then open http://127.0.0.1:3000
"""

from flask import Flask, jsonify, render_template, request

from chatbot import FAQBot
from faq_data import FAQS

app = Flask(__name__)
bot = FAQBot(FAQS)

MAX_MESSAGE_LENGTH = 500


@app.route("/")
def index():
    # First few FAQs are shown as tappable suggestions.
    suggestions = [faq[0] for faq in FAQS[:5]]
    return render_template("index.html", suggestions=suggestions)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()

    if not message:
        return jsonify(error="Type a question first."), 400
    if len(message) > MAX_MESSAGE_LENGTH:
        return jsonify(error=f"Please keep questions under {MAX_MESSAGE_LENGTH} characters."), 400

    answer, matched, score = bot.ask(message)
    return jsonify(answer=answer, matched=matched, score=round(score, 2))


if __name__ == "__main__":
    app.run(debug=True, port=3000)
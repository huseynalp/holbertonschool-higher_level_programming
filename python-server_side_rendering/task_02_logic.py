#!/usr/bin/python3
"""
Flask app for dynamic Jinja list rendering
"""

from flask import Flask, render_template
import json
import os

app = Flask(__name__)


@app.route("/items")
def items_list():
    """Reads items.json and passes data to template."""

    json_path = os.path.join(os.path.dirname(__file__), "items.json")

    # Read JSON file safely
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            items = data.get("items", [])
    except Exception:
        items = []  # fallback if file error

    return render_template("items.html", items=items)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

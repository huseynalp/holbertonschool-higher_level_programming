#!/usr/bin/python3
"""
Flask app to read product data from JSON or CSV
and render it in an HTML template.
"""

from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)


def read_json(file_path):
    """Reads JSON and returns list of product dictionaries."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def read_csv(file_path):
    """Reads CSV and returns list of product dictionaries."""
    data = []
    try:
        with open(file_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return data
    except Exception:
        return None


@app.route("/products")
def products():
    """Displays products from JSON or CSV depending on query parameter."""
    source = request.args.get("source")
    prod_id = request.args.get("id")

    base_path = os.path.dirname(__file__)
    json_path = os.path.join(base_path, "products.json")
    csv_path = os.path.join(base_path, "products.csv")

    # Determine data source
    if source == "json":
        data = read_json(json_path)
    elif source == "csv":
        data = read_csv(csv_path)
    else:
        return render_template("product_display.html", error="Wrong source")

    # If file could not be read
    if data is None:
        return render_template("product_display.html", error="Could not read data file")

    # Optional filtering by id
    if prod_id:
        try:
            prod_id = int(prod_id)
        except ValueError:
            return render_template("product_display.html", error="Invalid id value")

        filtered = [p for p in data if p["id"] == prod_id]

        if not filtered:
            return render_template("product_display.html", error="Product not found")

        return render_template("product_display.html", products=filtered)

    # No id → return all products
    return render_template("product_display.html", products=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

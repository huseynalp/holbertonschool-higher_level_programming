#!/usr/bin/python3
"""
Flask app that reads product data from JSON, CSV, or SQLite database.
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)


def read_json(file_path):
    """Reads JSON file and returns list of product dictionaries."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def read_csv(file_path):
    """Reads CSV file and returns list of product dictionaries."""
    products = []
    try:
        with open(file_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return products
    except Exception:
        return None


def read_sqlite(db_path, prod_id=None):
    """Reads data from SQLite database and returns products list."""
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row  # Allows dictionary-like access
        cursor = conn.cursor()

        if prod_id:
            cursor.execute("SELECT * FROM Products WHERE id = ?", (prod_id,))
            row = cursor.fetchone()
            conn.close()

            if row:
                return [{
                    "id": row["id"],
                    "name": row["name"],
                    "category": row["category"],
                    "price": row["price"]
                }]
            return []  # id not found

        # No id → return all products
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        conn.close()

        return [
            {
                "id": row["id"],
                "name": row["name"],
                "category": row["category"],
                "price": row["price"]
            } for row in rows
        ]

    except Exception:
        return None


@app.route("/products")
def products():
    """Displays products from JSON, CSV, or SQLite based on query parameter."""
    source = request.args.get("source")
    prod_id = request.args.get("id")

    base_path = os.path.dirname(__file__)
    json_path = os.path.join(base_path, "products.json")
    csv_path = os.path.join(base_path, "products.csv")
    db_path = os.path.join(base_path, "products.db")

    # Handle optional id
    id_value = None
    if prod_id:
        try:
            id_value = int(prod_id)
        except ValueError:
            return render_template("product_display.html", error="Invalid id value")

    # Determine data source
    if source == "json":
        data = read_json(json_path)
    elif source == "csv":
        data = read_csv(csv_path)
    elif source == "sql":
        data = read_sqlite(db_path, id_value)
    else:
        return render_template("product_display.html", error="Wrong source")

    # If file/db could not be read
    if data is None:
        return render_template("product_display.html", error="Could not read data")

    # If id provided but not found
    if prod_id and not data:
        return render_template("product_display.html", error="Product not found")

    return render_template("product_display.html", products=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

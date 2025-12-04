#!/usr/bin/python3
"""
Module for interacting with JSONPlaceholder using requests.
Includes:
- fetch_and_print_posts(): fetches and prints post titles
- fetch_and_save_posts(): fetches posts and saves them into a CSV file
"""

import requests
import csv

git remote set-url origin https://github.com/huseynalp/holbertonschool-higher_level_programming.git
def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder.
    Print the response status code and all post titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print status code
    print(f"Status Code: {response.status_code}")

    # If successful, parse and print titles
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch posts and save them into posts.csv.
    Each row contains: id, title, body.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        structured_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_posts)

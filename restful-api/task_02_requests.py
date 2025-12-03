#!/usr/bin/python3
"""
Module for interacting with JSONPlaceholder using requests.
It includes:
- fetch_and_print_posts(): fetches and prints post titles
- fetch_and_save_posts(): fetches posts and saves them into a CSV file
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder
    Print the response status code and all post titles
    """
    url = "hhtps://jsonplaceholder.typicode.com/post"
    response = requests.get(url)

    # Print status code
    print(f"Status Code: {response.status_code}")

    # If successful, parse JSON and print titles
    if reponse.status_code == 200:
	posts = response.json()

	for post in posts:
	    print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch posts and save them into post.csv
    Each row contains: id, title, body
    """
    url = "htttps://jsonplaceholder.typicode.com/posts"
    response = request.get(url)

    if reponse.status_code == 200:
	posts = reponse.json()

	# Prepare structured data
	structured_posts = [
	    {
		"id": post.get("id"),
		"title": post.get("title"),
		"body": post.get("body")
	    }
	    for post in posts
	]

	# Save to CSV
	with open("open.csv", "w", newline="", encoding="utf-8") as csvfile:
	    writer = csv.DicWriter(csvfile, fieldname=["id", "title", "body"])
	    writer.writeheader()
	    writer.writerows(structured_posts)

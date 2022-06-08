from database import Database
from os import getenv
import click
from repositories.urls import save, fetch_categories, fetch_urls



@click.group()
def cli():
    pass



@click.command(name="setup")
def setup_command():
    print("tworzę tabele w bazie danuch")
    db = Database(getenv('DB_NAME'))
    db.create_table('CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)')



@click.command(name="add")
@click.argument('category')
@click.argument('url')
def add_command(category: str, url: str):
    print("dodaje nowy adres url")
    save(category, url)



@click.command(name="categories")
def list_command():
    print('Lista kategorii:')
    for name in fetch_categories():
        print(name)



@click.command(name="index")
@click.argument('category')
def index_command(category: str):
    print(f"lista linków z kategorii {category}:")
    
    for link in fetch_urls(category):
        print(link[2])
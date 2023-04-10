"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="@dpg-cgpr34gu9tun42u59al0-a.oregon-postgres.render.com",
        database="todolist_fy9k",
        user="todolist_fy9k_user",
        password="DAyeynEROzfDbf2ElsirPNKFI1gdkRZm")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes

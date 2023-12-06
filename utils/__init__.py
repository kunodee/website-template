
from flask import Flask, Blueprint
import datetime
import os
import logging
import colorama
import time

colorama.init(autoreset=True)

log = logging.getLogger('werkzeug')
log.setLevel(logging.CRITICAL)

def getCurrentDate(withDay: bool = False):
    e = datetime.datetime.now()
    if withDay:
        return f"{e.day}/{e.month} {e.hour}:{e.minute}:{e.second}"
    return f"{e.hour}:{e.minute}:{e.second}"


def register_blueprints(app):
    for root, dirs, files in os.walk(config.routes_folder):
        for file in files:
            if file.endswith(".py"):
                route_module = os.path.splitext(file)[0]
                route_module_path = os.path.join(root, route_module).replace(os.path.sep, ".")
                module = __import__(route_module_path, fromlist=["bp"])
                blueprint = getattr(module, "bp", None)
                if blueprint and isinstance(blueprint, Blueprint):
                    print(f"[{getCurrentDate()}] | {colorama.Fore.BLUE}DEBUG{colorama.Fore.RESET} -> {colorama.Fore.CYAN}Loaded route {file}")
                    app.register_blueprint(blueprint)

class config:

    SECRET_KEY = b""
    HOST = "127.0.0.1"
    PORT = 80
    DEBUG = True
    routes_folder = "routes"
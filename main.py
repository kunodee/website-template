
from core import (
    Flask, config, os, getCurrentDate, register_blueprints, colorama
)

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

os.system('cls' if os.name=='nt' else 'clear')
print("")
register_blueprints(app)

print(f"[{getCurrentDate()}] | {colorama.Fore.RED}START{colorama.Fore.RESET} -> {colorama.Fore.GREEN}Website is running on host {config.HOST}:{config.PORT} (debug = {config.DEBUG})")

app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
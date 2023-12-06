
import utils

app = utils.Flask(__name__)
app.secret_key = utils.config.SECRET_KEY

utils.os.system('cls' if utils.os.name=='nt' else 'clear')
print("")
utils.register_blueprints(app)

print(f"[{utils.getCurrentDate()}] | {utils.colorama.Fore.RED}START{utils.colorama.Fore.RESET} -> {utils.colorama.Fore.GREEN}Website is running on host {utils.config.HOST}:{utils.config.PORT} (debug = {utils.config.DEBUG})")

app.run(host=utils.config.HOST, port=utils.config.PORT, debug=utils.config.DEBUG)

from utils import Blueprint

bp = Blueprint("indexBP", __name__)

@bp.route("/")
def indexAPP():

    return "Works!"
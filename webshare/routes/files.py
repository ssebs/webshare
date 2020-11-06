# files.py
import shutil
from flask import Blueprint, request, jsonify
# from webshare.utils import test

files_routes = Blueprint("files", __name__)


@files_routes.route("/api/files_test", methods=["GET"])
def test_files():
    return "Testing files api"
# test_files

# files.py
import shutil
import uuid
from flask import Blueprint, request, jsonify

files_routes = Blueprint("files", __name__)


@files_routes.route("/api/files_test", methods=["GET"])
def test_files():
    return "Testing files api"
# test_files


@files_routes.route("/api/upload/<name>", methods=["POST"])
def upload_file(name):
    # Save the file to memory
    _file_contents = request.get_data()

    # Cleanup the tmp dir
    try:
        shutil.rmtree("files/*")
    except FileNotFoundError:
        pass

    # Save the file
    newname = str(uuid.uuid4())[:6] + "-" + name
    newpath = f"./webshare/files/{newname}"

    with open(newpath, "wb") as f:
        f.write(_file_contents)

    return f"{request.host_url}{newname}", 201  # noqa
# upload_csv

@files_routes.route("/api/download/<name>", methods=["GET"])
def download_file(name):
    _file_contents = b""
    try:
        with open(f"./webshare/files/{name}", "rb") as f:
            _file_contents = f.read()
        return _file_contents
    except Exception as e:
        return e
# download_file

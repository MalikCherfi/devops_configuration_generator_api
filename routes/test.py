from flask import Blueprint, jsonify

test_bp = Blueprint("test", __name__)


import os


@test_bp.route("/api/test", methods=["POST"])
def test():
    try:
        base_path = "/workspace" if os.path.exists("/workspace") else "."
        with open(f"{base_path}/test.txt", "w") as f:
            f.write("test")
        return jsonify({"message": f"Fichier test.txt créé dans {base_path}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

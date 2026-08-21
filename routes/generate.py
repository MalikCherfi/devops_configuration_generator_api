import os
from flask import Blueprint, jsonify, request

generate_bp = Blueprint("generate_bp", __name__)

# Types de fichiers autorisés (doit matcher le front)
ALLOWED_FILE_TYPES = {"ci.yml", "eslint", "pre-commit"}


@generate_bp.route("/api/generate", methods=["POST"])
def generate():
    try:
        print("=== Génération de fichier ===")
        data = request.get_json()

        repo_path = data.get("repoPath")
        file_type = data.get("fileType")
        file_name = data.get("fileName")
        content = data.get("content")
        jobs = data.get("jobs", [])

        # --- Validations ---
        if not repo_path or not os.path.exists(repo_path):
            print(f"Erreur : Le répertoire spécifié n'existe pas : {repo_path}")
            return jsonify({"error": "Le répertoire spécifié n'existe pas"}), 500

        if not os.path.isdir(repo_path):
            print(f"Erreur : Le chemin spécifié n'est pas un répertoire : {repo_path}")
            return jsonify({"error": "Le chemin spécifié n'est pas un répertoire"}), 500

        if file_type not in ALLOWED_FILE_TYPES:
            return jsonify({"error": f"Type de fichier invalide : {file_type}"}), 400

        if not file_name:
            return jsonify({"error": "Nom de fichier manquant"}), 400

        if content is None:
            return jsonify({"error": "Contenu du fichier manquant"}), 400

        print(f"Chemin du répertoire : {repo_path}")
        print(f"Fichier à créer : {file_name}")
        if jobs:
            print(f"Jobs sélectionnés : {jobs}")

        # Chemin complet du fichier (ex: .github/workflows/ci.yml)
        full_path = os.path.join(repo_path, file_name)

        # Empêche d'écrire en dehors du répertoire choisi (../../etc)
        if not os.path.abspath(full_path).startswith(os.path.abspath(repo_path)):
            return jsonify({"error": "Chemin de fichier invalide"}), 400

        # Crée les éventuels sous-dossiers (ex: .github/workflows/)
        parent_dir = os.path.dirname(full_path)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)

        with open(full_path, "w") as f:
            f.write(content)

        return (
            jsonify(
                {
                    "message": f"Fichier {file_name} créé dans {repo_path}",
                    "path": full_path,
                }
            ),
            200,
        )

    except Exception as e:
        print(f"Erreur lors de la génération du fichier : {e}")
        return jsonify({"error": str(e)}), 500

import importlib
import os

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ----------------------------------------------------------
# Chargement automatique de tous les blueprints dans /routes
# Chaque fichier .py doit exposer une variable Blueprint
# nommée <nom_du_fichier>_bp  (ex: test.py → test_bp)
# ----------------------------------------------------------

routes_dir = os.path.join(os.path.dirname(__file__), "routes")

for filename in os.listdir(routes_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]  # retire .py
        module = importlib.import_module(f"routes.{module_name}")
        blueprint = getattr(module, f"{module_name}_bp", None)

        if blueprint:
            app.register_blueprint(blueprint)
            print(f"  ✓ Route chargée : routes/{filename}")
        else:
            print(f"  ✗ Aucun blueprint trouvé dans routes/{filename}")

if __name__ == "__main__":
    print("\n=== Routes enregistrées ===")
    for rule in app.url_map.iter_rules():
        print(f"  {rule.methods} {rule}")
    print()
    app.run(host="0.0.0.0", port=8000, debug=False)

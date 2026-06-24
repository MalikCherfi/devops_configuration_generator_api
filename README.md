# Devops Configuration Generator — API
 
## 🚀 Lancer le projet
 
### Sans Docker
 
```bash
pip install -r requirements.txt
python app.py
```
 
### Avec Docker
 
Remplace le contenu de ton `docker-compose.yml` par ceci en ajoutant le volume pointant vers la racine du projet de ton choix :
 
```yaml
services:
  api:
    build: .
    container_name: devops-configuration-generator-api
    ports:
      - "8000:8000"
    volumes:
      - /chemin/vers/ton/projet:/workspace
```
 
**Exemple :**
 
```yaml
volumes:
  - /Users/john/Projects/monSite:/workspace   # Mac/Linux
  - C:\Users\john\Projects\monSite:/workspace  # Windows
```
 
Puis lance :
 
```bash
docker-compose up -d
```
 
L'API sera accessible sur `http://localhost:8000`.
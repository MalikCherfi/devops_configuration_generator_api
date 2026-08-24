# Devops Configuration Generator — API
 
## 🚀 Lancer l'application complète

### Avec Docker
 
L'application nécessite l'APP ([repo-app](https://github.com/malikcherfi/devops_configuration_generator_app)). 

Pour tout démarrer d'un coup, crée un fichier `docker-compose.yml` avec le contenu suivant puis lancer la commande `docker compose up -d` :

```yaml
services:
  api:
    image: ghcr.io/malikcherfi/devops_configuration_generator_api:latest
    ports:
      - "8000:8000"
    volumes:
      - ${HOME}:/${HOME}
    restart: always

  app:
    image: ghcr.io/malikcherfi/devops_configuration_generator_app:latest
    ports:
      - "3000:3000"
    depends_on:
      - api
    restart: always
```
 
### Sans Docker
 
```bash
pip install -r requirements.txt
python app.py
```
L'API sera accessible sur `http://localhost:8000`.

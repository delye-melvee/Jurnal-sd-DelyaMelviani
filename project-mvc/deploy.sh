docker pull ghcr.io/delye-melvee/mvc-app:v2-prod
docker stop app-v1
docker rm app-v1
docker run -d --name app-v2 -p 8081:5000 ghcr.io/delye-melvee/mvc-app:v2-prod
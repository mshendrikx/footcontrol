docker compose -f /home/mauricio/apps/docker/docker-compose.yml down footdraw
docker rmi mservatius/footdraw
docker build -t footdraw:latest .
docker tag footdraw:latest mservatius/footdraw:latest
docker push mservatius/footdraw:latest
docker rmi footdraw:latest
docker rmi mservatius/footdraw
docker compose -f /home/mauricio/apps/docker/docker-compose.yml up footdraw -d

<!-- git init project -->

git init

<!-- git add . -->

git add .

<!-- git commit -->

git commit -m "init project"

<!-- git push -->

<!--  add pythen rquirements-->

pipreqs .

<!-- if port in use -->

sudo kill -9 $(sudo lsof -t -i:5001)

<!-- buld image -->

docker build -t $DOCKER_HUB_USER/flaskpp:3.0 .

<!-- test docker image -->

docker run -it --rm --name helloflask -p 5001:5001 $DOCKER_HUB_USER/flaskpp:3.0

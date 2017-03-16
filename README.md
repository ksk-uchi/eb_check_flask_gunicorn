# EB_CHECK_FLASK_GUNICORN

This is the boilerplate application with Docker including below combination.

- python 3.6
- Flask
- gunicorn
- mysql 5.7
- Flask-SQLAlchemy

As you can see,\
This repository has a `Dockerrun.aws.json` file.\
However you don't need to care of it for now...

# HOW TO DEVELOP

## Clone repository & cd there
```
git clone [THIS REPOSITORY]
cd [THIS REPOSITORY]
```

## Build this application
```
docker-compose up --build
```

Now the port `3000` is used by `gunicorn` and `3306` is used by `mysql`.

## Check
```
curl -XGET localhost:3000
```

# RUN EACH CONTAINER

## Build each image
```
docker build -t eb_flask_sample ./docker_files/WebApp/
```

## Run the image as container
```
docker run -it --name eb_container -p 3000:8080 -v (THIS_REPOSITORY_PATH)/WebApp/src:/var/app/src --rm eb_flask_sample
```

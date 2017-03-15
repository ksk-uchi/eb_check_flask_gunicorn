# HOW TO DEVELOP

## Clone repository & cd there
```
git clone [THIS REPOSITORY]
cd [THIS REPOSITORY]
```

## Build image
```
docker build -t eb_flask_sample ./docker_files/WebApp/
```

## Run the image as container
```
docker run -it --name eb_con -p 3000:8080 -v C:\Users\LM\Documents\eb_flask_sample\src:/var/app/src --rm eb_flask_sample
```

## Check
```
curl -XGET localhost:3000
```

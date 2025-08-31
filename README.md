# Image Generator Backend

This is an Image Generator FastAPI Backend that connects to a SQLite Database. This service stores the input and output logs of and content of the working model. It is a template that can be used to connect to actual image generator model. 

We have a POST FastAPI endpoint that takes a string as an input and sends it to the server in the ImageRequest Schema. The FastAPI uses uvicorn to handle requests.

The service is 2 Schemas namely ImageRequest and ImageResponse. The request schema consists of a string that holds the prompt to be inouted to the model while the response schema consists of a string as well which holds the link of the image that was generated and uploaded to a cloud service (cloudinary/G-Drive).

We connnect to the SQLite database and store the "id", "timestamp" and "prompt" of the request from the POST endpoint.

After saving the request in the database, we return the url of the generated image via a ImageResponse schema.

Finally we dockerized the Service

Steps to use:
1) Clone the repo
2) run in terminal:
`docker build -t mini-task .`
3) run in terminal:
`docker run --rm -p 8000:80 -v "%cd%\data:/app/data" --name image-gen-app mini-task`
4) Check/Test the API [Here](http://localhost:8000/docs)

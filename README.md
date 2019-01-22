#Overview
  In this repository, covered the following feature:
- Rest App Using Flask Python Framework
- Dockerfile - container enablement
- Make targets for build/run/publish/ing the above
- Helm charts for the app
- For deployment, See docs in (`deploy`)[./deploy/README.md] directory

# How to Install docker in CentOS 7
- sudo groupadd docker
- sudo usermod -aG docker $(whoami)
- sudo service docker start

# How to build docker Image
- git clone https://github.com/ERS-HCL/py-container.git
- cd py-container
- docker build -t py-container .
- docker run -p 80:5000 py-container
- open your browser and check http://127.0.0.1/api/info
- in command prompt, curl http://127.0.0.1/api/info
- You should get "API info text as a response"

# Push Image to docker hub
- docker login
- docker tag py-container jbeginsamuel/py-container
- docker push jbeginsamuel/py-container:latest



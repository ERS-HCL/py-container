# Overview
  In this repository, covered the following feature:
- Rest App Using Flask Python Framework
- Dockerfile - container enablement
- Helm charts enablement for the app
- For deployment, visit docs under deployment folder in (`deploy`)[./deploy/README.md] directory

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

# How to deploy it in Kubernets
- cd deploy
- helm package rest-app --debug
- output: rest-app-0.1.0.tgz file was created
- helm install rest-app-0.1.0.tgz --name rest-app
- kubectl get svc --watch # wait for a IP

# Uninstall or Remove deployed images and Chart
- docker images # list images
- docker rmi py-container
- output:  Remove created helm packages
- helm delete rest-app

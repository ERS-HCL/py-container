from python:3.6

RUN mkdir -p /opt/hcl/webapp/py-container
WORKDIR /opt/hcl/webapp/py-container

RUN pip3 install --upgrade pip
COPY requirements*.txt ./
RUN pip3 install -r requirements.txt

COPY . ./

LABEL maintainer="Begin J Samuel <begin.samuel@hcl.com>"
LABEL source="https://github.com/ERS-HCL/py-container"
ARG commit
LABEL commit="$commit"

ENV PORT 5000
ENV FLASK_APP rest-app/app.py

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

CMD ["flask", "run", "--host=0.0.0.0"]

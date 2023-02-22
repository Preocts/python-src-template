FROM ubuntu:focal

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends software-properties-common
RUN add-apt-repository -y 'ppa:deadsnakes/ppa'
RUN DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends python3.8 python3.8-venv
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /src

ENV PATH=/venv/bin:$PATH
RUN python3.8 -m venv /venv
COPY requirements/ /src/requirements/
RUN python3.8 -m pip install --upgrade -r requirements/requirements-dev.txt -r requirements/requirements-test.txt --no-cache-dir

COPY . /src
RUN python3.8 -m pip install . --no-cache-dir

CMD ["tox", "-r"]

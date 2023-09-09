FROM ubuntu:focal

ENV LANG=C.UTF-8

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends software-properties-common
RUN add-apt-repository -y 'ppa:deadsnakes/ppa'
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends python3.8-distutils python3.8 python3.9 python3.10 python3.11-venv python3.12
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /src

ENV PATH=/venv/bin:$PATH
RUN python3.11 -m venv /venv
RUN python -m pip install --upgrade nox --no-cache-dir

COPY . /src

CMD ["nox"]

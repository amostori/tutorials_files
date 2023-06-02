FROM python:3.7.5-slim-buster
MAINTAINER Marcin Andrzejczak <wtpromise@gmail.com>

ENV INSTALL_PATH /blog

# komenda RUN uruchamiana jest gdy tworzony jest image
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# pierwsza kropka to biezący katalog, druga to WORKDIR, czyli /blog
COPY . .

# komenda CMD uruchamiana jest z poziomu gotowego juz kontenera
CMD ["gunicorn", "--bind", "0.0.0.0:80", "blog.app:create_app()"]

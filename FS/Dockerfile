FROM python:3.5

RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN groupadd -g 799 pan303 && \
    useradd -r -u 999 -g pan303 nyu

# Set up a working folder and install the pre-reqs
WORKDIR /app

RUN pip install Flask
RUN pip install requests
RUN pip install Flask-API

USER nyu

COPY --chown=pan303:nyu . .

CMD [ "python", "./fs.py" ]
FROM tiangolo/uwsgi-nginx-flask:python3.6

ENV LISTEN_PORT 3548
EXPOSE 3548

# RUN git clone https://github.com/docker/docker
COPY ./app /app
RUN pip3 install --no-cache-dir -r requirements.txt
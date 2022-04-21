FROM python:3.10.0b2-alpine3.12

WORKDIR /opt/my-app

COPY  my-app/requirements.txt .
RUN pip install -r requirements.txt

COPY my-app/my-app.py .

ARG FAVORITE_BEER="Westmalle"
ENV FAVORITE_BEER ${FAVORITE_BEER}

ENTRYPOINT [ "./my-app.py" ]
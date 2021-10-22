FROM python:3-alpine

WORKDIR /opt/my-app

COPY  my-app/requirements.txt .
RUN pip install -r requirements.txt

COPY my-app/my-app.py .

ARG FAVORITE_BEER="Westmalle"
ENV FAVORITE_BEER ${FAVORITE_BEER}

ENTRYPOINT [ "./my-app.py" ]
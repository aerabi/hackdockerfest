FROM node:24.13.0-alpine3.23

RUN mkdir /app
COPY . /app

USER node

WORKDIR /app

CMD ["node", "index.js"]

FROM node:20.15.1-alpine3.20

RUN mkdir /app
COPY . /app

USER node

WORKDIR /app

CMD ["node", "index.js"]

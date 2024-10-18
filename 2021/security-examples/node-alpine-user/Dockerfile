FROM node:20.14.0-alpine3.20

RUN mkdir /app
COPY . /app
RUN chown -R node:node /app

USER node

WORKDIR /app

CMD ["node", "index.js"]

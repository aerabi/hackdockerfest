FROM node:lts-alpine

RUN mkdir /app
COPY . /app
RUN chown -R node:node /app

USER node

WORKDIR /app

CMD ["node", "index.js"]

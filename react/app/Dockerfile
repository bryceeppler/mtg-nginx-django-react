FROM node:17-alpine

WORKDIR /react

COPY ./package.json .

RUN npm install

COPY . .

RUN npm run build

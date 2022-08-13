FROM node:16.13.0

WORKDIR /react

COPY ./package.json .

RUN npm install

COPY . .

RUN npm run build

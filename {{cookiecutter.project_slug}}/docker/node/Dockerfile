FROM node
WORKDIR /app
COPY ./package.json /app/
RUN mkdir -p /app/node_modules
RUN npm install

COPY . /app

FROM node:lts-alpine

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install packages
RUN npm install

WORKDIR /app

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

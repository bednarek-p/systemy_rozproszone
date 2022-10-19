#STEP1 BUILD VUE PROJECT
FROM node:lts-alpine AS build
# make the 'app' folder the current working directory
WORKDIR /app
# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./
# install packages
RUN npm install
# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .
# run npm build
RUN npm run build


#STEP2 CREATE NGINX SERVER
FROM nginx:1.19.0-alpine AS prod-stage
COPY --from=build /app/dist /usr/share/nginx/html/
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]

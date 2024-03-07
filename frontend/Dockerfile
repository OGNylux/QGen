FROM node:alpine as builder
WORKDIR /code/
ADD package-lock.json .
ADD package.json .
RUN npm ci
ADD . .
RUN npm run build 

FROM nginx:1.23.1
COPY --from=builder /code/dist/ /dist/
ADD nginx/nginx.conf /etc/nginx/conf.d
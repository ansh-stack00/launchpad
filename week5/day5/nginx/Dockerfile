FROM nginx:1.29.4-alpine-slim

COPY ./ssl/ /etc/nginx/ssl/

COPY default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80 443
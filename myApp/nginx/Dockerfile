FROM nginx:1.26.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
#COPY iplist.conf /etc/nginx/conf.d

#COPY certs/ /etc/certs/
#RUN chmod 644 /etc/certs/server.crt
#RUN chmod 600 /etc/certs/server.key

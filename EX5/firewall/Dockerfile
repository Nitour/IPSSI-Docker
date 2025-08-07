FROM ubuntu:22.04

RUN apt update && \
    apt install -y iptables nginx curl && \
    apt clean

COPY rules.sh /rules.sh
COPY nginx.conf /etc/nginx/nginx.conf

CMD ["sh", "-c", "/rules.sh && nginx -g 'daemon off;'"]

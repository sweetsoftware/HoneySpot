FROM debian:latest

RUN apt-get update

RUN DEBIAN_FRONTEND=noninteractive apt-get -y install dnsmasq

CMD ["dnsmasq", "-k"]


# Setup

## Phishing page

- save a copy of the phishing page in quickfish/src/templates

- replace the target url of the form you want to phish to be "/"

- move all static assets to /static and edit URLs in the page

## Interface

- disable network-manager

- Add an IP to your wireless interface: ip a a 10.0.0.1/24 dev wlan0

## Config

- Edit quickfish/src/config.py to suit your needs

- You can edit the configuration of the AP in hostapd-wpe/conf/ and the DNS settings in dnsmasq/dnsmasq.conf

## Allow internet access

iptables --table nat --append POSTROUTING -s 10.0.0.0/24 -j MASQUERADE

iptables --append FORWARD --in-interface eth0 -j ACCEPT



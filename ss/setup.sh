#!/bin/bash
apt-get update
apt-get install python-pip -y
pip install shadowsocks
pip install --upgrade pip
mkdir -p /etc/shadowsocks

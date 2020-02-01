## Setup a AWS EC2 instance
## Config
Put private IP in config.json
```
vim config.json
```
## Install shadowsocks
```
sudo bash setup.sh
```
## Run
```
sudo ssserver -c /etc/shadowsocks/config.json -d start
```
## Possible issue after ss start
undefined symbol: EVP_CIPHER_CTX_cleanup
```
vim /usr/local/lib/python(3.5 2.7)/dist-packages/shadowsocks/crypto/openssl.py
:%s/cleanup/reset/
:x
```
## References
https://my.oschina.net/u/3163032/blog/1863988
http://celerysoft.github.io/2016-01-15.html

import requests
import requests_unixsocket

# /var/run/docker.sock
# the socket must be mounted to the container
unixsocket = "http+unix://%2Fvar%2Frun%2Fdocker.sock"

# the container have to run with host net
httpsocket = "http://127.0.0.1:2375"

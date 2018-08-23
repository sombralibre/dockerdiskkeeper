## docker run --name docker-cleaner -d -e SCHEME=http -e DISKLIMIT=80 -e INTERVAL=3600 -e TARGETFS="/checkfs" -v /:/checkfs --net=host sombralibre/dockerdiskkeeper:latest

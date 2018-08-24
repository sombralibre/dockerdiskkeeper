
### Docker repository
https://hub.docker.com/r/sombralibre/dockerdiskkeeper/

### Deploying to docker
```
docker run --name docker-cleaner -d -e SCHEME=unix -e DISKLIMIT=70 -e INTERVAL=18000 -e TARGETFS="/checkfs" -v /:/checkfs -v /var/run/docker.sock:/var/run/docker.sock sombralibre/dockerdiskkeeper
```

### Deploying to kubernetes
```
kubectl create -f https://raw.githubusercontent.com/sombralibre/dockerdiskkeeper/master/kubernetes/DaemonSet.yaml
```

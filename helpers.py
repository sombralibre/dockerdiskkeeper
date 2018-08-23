import os
import json
import requests
import requests_unixsocket

# /var/run/docker.sock
# the socket must be mounted to the container
unixsocket = "http+unix://%2Fvar%2Frun%2Fdocker.sock"

# the container have to run with host net
httpsocket = "http://127.0.0.1:2375"

# target fs / must be mounted to container as /target
targetfs = os.environ.get("TARGETFS", "/target")

# Filesystem things


def shouldrun(threshold):
    return True if float(threshold) >= fsusedspace(targetfs) else False


def fsusedspace(path):
    st = os.statvfs(path)
    return (100/st.f_blocks) * (st.f_blocks - st.f_bavail)


# Docker things


api_handler = {
    "http": [requests.Session(), httpsocket],
    "unix": [requests_unixsocket.Session(), unixsocket]
}


def listObjects(handler, obj):
    try:
        return json.loads((handler[0]).get(
            "{}/{}/json?all=1".format(handler[1], obj)).text)
    except Exception as e:
        print(e)


def removeObjects(handler, obj, idf):
    print("Removing -- {} >>> {}".format(obj, idf))
    try:
        return json.loads((handler[0]).delete(
            "{}/{}".format(handler[1], obj)).text)
    except Exception as e:
        print(e)


# The whole thing


def housekeeping(scheme, threshold):
    if shouldrun(threshold):
        # containers states
        states = ['exited', 'dead', 'created']
        objs = ["containers", "images"]
        for ob in objs:
            for it in listObjects(api_handler[scheme], ob):
                if "State" in it and it["State"] in states:
                    removeObjects(api_handler[scheme], ob, it["Id"])
                elif "State" not in it:
                    removeObjects(api_handler[scheme], ob, it["Id"])

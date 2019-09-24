## Deployment on Openshift
Create a .env file. 
Template: 
```
DEBUG=True
MODE=remote # one of local, remote, docker (taken care of, by docker-compose.yaml)
LOCAL_EGL_SERVER=localhost
REMOTE_EGL_SERVER=egl.cern.ch
DOCKER_EGL_SERVER=localhost
REFRESH_INTERVAL=10 #(every x minutes)
DJANGO_ADMIN_EMAIL={CHANGE}
DJANGO_ADMIN_PASSWORD={CHANGE}
```
Run
```
 oc new-app maany/source-s2i-fuleon-egl-django~https://github.com/maany/fuleon_egl_cern --env-file=.env 
```

Create a Persistent Volume on Openshift Web Console. Then create a volume as follows:
```
 oc set volume dc/fuleoneglcern --add --name fuleon-data-mount -t pvc --claim-name {create_a_claim} --path /opt/app-root/src/data
```

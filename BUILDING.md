# Prepare your build environment

There are a few ways you could build this.

A) Docker build - fast and easy
B) Local build - More control
C) Build service - Fancy



## A) Build in a docker (simplifies build setup)
docker run -v $(pwd):/my-snap snapcore/snapcraft sh -c "apt update && cd /my-snap && snapcraft"

## B) Build locally
sudo snap install docker
sudo apt install python3-pip python3-setuptools

# Remove leftovers
rm -rf parts/ prime/ stage/ 
SNAPCRAFT_BUILD_ENVIRONMENT=host snapcraft

## C) Build using snap buildservice
https://build.snapcraft.io


# Trouble-shoot

Missing python3 pip:
   https://forum.snapcraft.io/t/no-module-named-pip/3483


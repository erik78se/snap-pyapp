# Prepare your build environment

There are a few ways you could build this.

A) Docker build - fast and easy
B) Local build - More control
C) Build service - Fancy

## A) Build in a docker (simplifies build setup)
```bash
docker run -v $(pwd):/my-snap snapcore/snapcraft sh -c "apt update && cd /my-snap && snapcraft"
```

## B) Build locally
```bash
sudo snap install docker
sudo apt install python3-pip python3-setuptools
```

## C) Build using snap buildservice
https://build.snapcraft.io


# Remove leftovers
```bash
rm -rf parts/ prime/ stage/ 
SNAPCRAFT_BUILD_ENVIRONMENT=host snapcraft
```

# Trouble-shoot

Missing python3 pip:
   https://forum.snapcraft.io/t/no-module-named-pip/3483

Missing python3 pip:
   https://forum.snapcraft.io/t/no-module-named-pip/3483

Travis
https://tutorials.ubuntu.com/tutorial/continuous-snap-delivery-from-travis-ci#0

sudo snap install docker
sudo apt install python3-pip python3-setuptools

# Remove leftovers
rm -rf parts/ prime/ stage/

# Build in a docker (Travis runs on ubuntu 14.10")
docker run -v $(pwd):/my-snap snapcore/snapcraft sh -c "apt update && cd /my-snap && snapcraft"

# Build locally as such
SNAPCRAFT_BUILD_ENVIRONMENT=host snapcraft

sudo apt install ruby-dev
export GEM_HOME=$HOME/gems
export PATH=$PATH:$GEM_HOME/bin
gem install travis

# Can add these to your bashrc
export GEM_HOME=$HOME/gems
export PATH=$PATH:$GEM_HOME/bin

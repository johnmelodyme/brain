# Docker

## Unit Tests

### Create images

#### Ubuntu 16.04

Build the image for Ubuntu 16.04. By default, the master branch of the Brain.ai project will be cloned.
```
docker build --force-rm=true -t brain-ubuntu1604 -f docker/ubuntu_16_04_python2.dockerfile .
```

To build with TRAVIS env we need to send global variables
```
docker build \
--force-rm=true \
--build-arg TRAVIS_BRANCH=${TRAVIS_BRANCH} \
--build-arg TRAVIS_EVENT_TYPE=${TRAVIS_EVENT_TYPE} \
--build-arg TRAVIS_PULL_REQUEST_SLUG=${TRAVIS_PULL_REQUEST_SLUG} \
--build-arg TRAVIS_PULL_REQUEST_BRANCH=${TRAVIS_PULL_REQUEST_BRANCH} \
-t brain-ubuntu1604 \
-f docker/ubuntu_16_04_python2.dockerfile .
```

#### Debian Jessie

Build the image for Debian Jessie. By default, the master branch of the Brain.ai project will be cloned.
```
docker build --force-rm=true -t brain-debian8 -f docker/debian8_python2.dockerfile .
```

To build with TRAVIS env we need to send global variables
```
docker build \
--force-rm=true \
--build-arg TRAVIS_BRANCH=${TRAVIS_BRANCH} \
--build-arg TRAVIS_EVENT_TYPE=${TRAVIS_EVENT_TYPE} \
--build-arg TRAVIS_PULL_REQUEST_SLUG=${TRAVIS_PULL_REQUEST_SLUG} \
--build-arg TRAVIS_PULL_REQUEST_BRANCH=${TRAVIS_PULL_REQUEST_BRANCH} \
-t brain-debian8 \
-f docker/debian8_python2.dockerfile .
```

### Run the test

Ubuntu image
```
docker run -it --rm brain-ubuntu1604
```

Debian image
```
docker run -it --rm brain-debian8
```

## Compile Snowboy

All Snowboy binaries for x86_64 architecture can be compiled from the docker compose file
```bash
mkdir /tmp/snowboy
docker-compose -f compose_compile_snowboy_all.yml up
```

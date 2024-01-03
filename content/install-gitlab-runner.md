Title: Install gitlab-runner on Ubuntu 20.04
Date: 2024-01-03 14:33
Category: Maintainance
Tags: Maintainance, Gitlab


After install and run gitlab-ce container using docker, you must create self-certification ssl to enable https on your local server.

And gitlab-runner also requires certificated CA to register runner in gitlab-ci server.

The following link [https://gitlab.com/gitlab-org/gitlab-runner/-/issues/28841](https://gitlab.com/gitlab-org/gitlab-runner/-/issues/28841) cotains correct steps which you can take to get rid of x509 cerficate error returns from command `gitlab-runner register`, I have only test it by installing gitlab-runner on local machine(ubuntu20) since I failed to make gitlab-runner docker container to recognize xx.local host name configured using mDNS, but docker uses default DNS(114.114.114.114) I don't know how to make it work yet.
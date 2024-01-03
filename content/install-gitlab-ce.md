Title: Install gitlab-ce on Ubuntu 20.04
Date: 2024-01-03 19:34
Category: Maintainance
Tags: Maintainance, Gitlab

# Introduction

You can quickly set up your own GitLab instance, manage your repositories, and take advantage of its powerful features by installing GitLab CE with Docker. I’ll walk you through the steps of installing GitLab CE with Docker on Ubuntu 22.04, ensuring a smooth installation and configuration. I’ll also go over how to create your first project in GitLab. GitLab is a well-known web-based Git repository manager that offers a full DevOps platform.

# Prerequisites
Before you begin, make sure you have the following:

* An Ubuntu 20.04 server.
* Sufficient system resources, including disk space, RAM, and CPU, to run GitLab CE and Docker containers.

# Step 1: Update the package index

To begin, run the following commands to update your Ubuntu system:

```
sudo apt update
sudo apt upgrade -y
```

# Step 2: Install Docker on Ubuntu 20.04

If your server doesn’t already have Docker installed follow these steps:

## a. Install Docker dependencies:
```
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

## b. Add Docker’s official GPG key:
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

## c. Add the Docker repository:
```
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

## d. Install Docker:
```
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io
```

## e. Check Docker installation by running:
```
sudo docker run hello-world
```

You should see the message of image pulling and "Hello from Docker!".

# Step 3: Install GitLab CE with Docker:

Now, let’s use Docker containers to install GitLab CE:

## a. Pull the latest GitLab CE Docker image:
```
sudo docker pull gitlab/gitlab-ce:latest
```

## b. Create a directory to store GitLab’s configuration and data
```
sudo mkdir -p /srv/gitlab/config /srv/gitlab/logs /srv/gitlab/data
```

## c. Run the GitLab CE Docker container:
```
sudo docker run --detach \
  --hostname YOUR_SERVER_DOMAIN_NAME \
  --publish 443:443 --publish 80:80 --publish 223:22 \
  --name gitlab \
  --restart always \
  --volume /srv/gitlab/config:/etc/gitlab \
  --volume /srv/gitlab/logs:/var/log/gitlab \
  --volume /srv/gitlab/data:/var/opt/gitlab \
  gitlab/gitlab-ce:latest
```

Replace `YOUR_SERVER_DOMAIN_NAME` with your server's domain name. In this tutorial, we have to use a domain name because we will be enabling HTTPS(SSL), which requires a CA certification process, which requires a domain name instead of an IP address.

My server name is `banana.local` so after this point, I use `banana.local` as my domain name. You can get yours too using `mDNS`.

> If you are just deploying your private GitLab server in a private network, I recommend learning `mDNS` which is a very simple protocol to broadcast a domain name for your server. 

You can see that I used `--publish 223:22` to map host machine's port 223 to gitlab-ce's docker container port 22. Because port 22 is used as the `ssh` port of gitlab and is used to transfer data through commands such as `git clone`, so it conflicts with the host's `sshd` service which also uses port 22. And if you don't want to see the port number in git repository's address, you can change the default port of host machine's `sshd` service port to another number.

## d. Change ssh port number in GitLab configuration:
```
sudo vim /srv/gitlab/config/gitlab.rb
```
We open the GitLab configuration file and find line `#gitlab_rails['gitlab_shell_ssh_port'] = 22`, uncomment this line and change the number 22 to 223 which we set earlier in docker run command.

Now we must reconfigure GitLab server and restart it to make it works.
```
sudo docker exec -it gitlab /bin/bash
gitlab-ctl reconfigure
gitlab-ctl restart
exit
```

## (Optional) Change system's SSH port:
Gitlab utilizes the default SSH port, which is in conflict with the system’s SSH port. For the best results, change the system’s default port.

To change the SSH port on your Ubuntu system, you’ll need to modify the SSH server configuration file:

Using a text editor, modify the SSH server configuration file. You can use the vim editor, for example, by running the following command:
```
sudo vim /etc/ssh/sshd_config
```
Look for the line that specifies the SSH port in the sshd_config file. It is usually commented out with a # symbol by default, indicating that the default port (port 22) is used. Remove the # symbol at the beginning of the line to uncomment it and change the default port number (22) with the desired port number. Choose a port number that is not commonly used or assigned to another service. For example, you can use 223.

Restart the SSH service for the changes to take effect. Use the following command:
```
sudo service ssh restart
```

Remember after changing the port number, you have to `ssh` your remote system with the appended `-p` option, for example:
```
ssh username@banana.local -p 223
```

# Step 4: Configure GitLab CE with Docker
## a. Set a new password for your GitLab CE with Docker panel

* Run the following command to access the GitLab container's shell:

```
sudo docker exec -it gitlab /bin/bash
```

* Once inside the container’s shell, run the following command to reset the root user’s password:

```
gitlab-rake "gitlab:password:reset"
```

* You’ll be asked to enter the username for which you’d like to reset the password. Enter root as the username and hit the Enter key.

* Following that, you should receive confirmation that the password reset was successful.

## b. Access GitLab CE with Docker web interface
Open your browser and enter `http://YOUR_DOMAIN_NAME` in my case: `http://banana.local`.


# Step 5: Enables HTTPS (SSL) of GitLab CE server
## a. Create an SSL directory that the GitLab server reads by default:
```
sudo mkdir -p /srv/gitlab/config/ssl
cd /srv/gitlab/config/ssl
```

## b. Generate the CA private key:
```
openssl genrsa -out ca.key 2048
```
This command generates a 2048 bits long RSA private key and save it to `ca.key` file. This private key is used as certificate authority(CA)'s private key.

## c. Generate self-signed CA certification:
```
openssl req -new -x509 -days 365 -key ca.key -subj "/C=CN/ST=GD/L=SZ/O=Acme, Inc./CN=Acme Root CA" -out ca.crt
```
Use CA private key(`ca.key`) generated in previous step to create a self-signed X.509 CA certification(`ca.crt`). This certification is valid in 365 days, and also include subject information.

## d. Generate private key and certification request for `banana.local`:
```
openssl req -newkey rsa:2048 -nodes -keyout banana.local.key -subj "/C=CN/ST=GD/L=SZ/O=Acme, Inc./CN=*.banana.local" -out banana.local.csr
```
Using a new 2048 bits long RSA private key and specified subject information to generate a private key(`banana.local.key`) and a certification request (`banana.local.csr`) for domain `*.banana.local`.

## e. Using CA to sign the certification for `banana.local`:
```
openssl x509 -req -extfile <(printf "subjectAltName=DNS:banana.local") -days 365 -in banana.local.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out banana.local.crt
```
Using CA's private key (`ca.key`) and CA's certification (`ca.crt`) to sign the certification request generated above. This command create a certication (`banana.local.crt`) for site `banana.local` and remains valid in 365 days. In addition, it also add subject additional name(SAN), which ensures certification can be used by `banana.local`.

## f. Configuring self-signed SSL certificate for GitLab server:

Modify settings in `/srv/gitlab/config/gitlab.rb` file:

```
external_url "https://banana.local"

# redirect http to https
nginx['redirect_http_to_https'] = true

# disable letsencrypt
letsencrypt['enable'] = false
```

Then do reconfigure GitLab server and restart it to make it works.
```
sudo docker exec -it gitlab /bin/bash
gitlab-ctl reconfigure
gitlab-ctl restart
exit
```

## g. Check if https works in your favorite browser: 

Open your browser Chrome or Edge to open the GitLab CE in https mode. If you sees the INVALID_CERTIFICATE warning, just ignore it and go to it anyway.


# Step 6: Install GitLab Runner on local machine and register in GitLab CI.

After install and run gitlab-ce container using docker, you must create self-certification ssl to enable https on your local server.

And gitlab-runner also requires certificated CA to register runner in gitlab-ci server.

The following link [https://gitlab.com/gitlab-org/gitlab-runner/-/issues/28841](https://gitlab.com/gitlab-org/gitlab-runner/-/issues/28841) cotains correct steps which you can take to get rid of x509 cerficate error returns from command `gitlab-runner register`, I have only test it by installing gitlab-runner on local machine(ubuntu20) since I failed to make gitlab-runner docker container to recognize xx.local host name configured using mDNS, but docker uses default DNS(114.114.114.114) I don't know how to make it work yet.
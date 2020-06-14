# Installing Sourcehut

This is a guide to getting a working Sourcehut install from these
RPMs. Currently, only FC32 is supported but I hope to build in support
for CentOS 8 in the future.

## Do you really need to do this?

Puppet will do the installation repeatably and reliably; it'll get
it right every time and will be much easier than this. Consider 
using it insead of manually configuring (once I've written the
modules!)

## Components

The following sourcehut services are available.

* `core` -- the core python libraries
* `meta` -- accounts and authenication service
* `git` -- git repositories
* `hub` -- project pages
* `todo` -- ticket management

The rest are in progress:

* `lists` -- mailing lists
* `hg` -- mercurial repositories
* `builds` -- thing-doers

## Database preparation

Sourcehut uses Postgresql. Install the `postgresql-server` package and
create databases for each of the services.  If you create them as
`metasrht`, `gitsrht`, _etc._ and set `trust` authentication from the
local host to the postgres user, you will not need to do any further
configuration. You _must_ enable SSL on the postgresql server.

## Installing the packages

This is simple. The packages and all required dependencies are in
COPR. The `sourcehut` package is a convenient metapackage that 
pulls in a complete installation.

````sh
sudo dnf copr enable tylerjgriffiths/srht
sudo dnf install sourcehut
````

## Configuring

Configuration samples are provided with each of the components,
installed into `/etc/sr.ht/${service}.ini`. You can generate a 
full config file with:

````sh
cat core.ini ${other_components} > config.ini
````

### Generate keys

You need to store three keys: service, network, and webhook.
Generate these and store them in the appropriate slot in 
`config.ini`.

````sh
srht-keygen service
srht-keygen network
srht-keygen webhook
````

### Miscellaneous
Set the hostnames for each service in their appropriate `origin=`
entry. 

### Git

Create the `git` user and a storage directory for repositories.

````sh
adduser git
mkdir -p /var/lib/git
chown -R git:git /var/lib/git
````

Git requires special attention: you will need to modify your 
`sshd_config`. Ensure the following config is present.

````
AuthorizedKeysCommand /usr/bin/gitsrht-dispatch "%u" "%h" "%t" "%k"
AuthorizedKeysCommandUser root
PermitUserEnvironment SRHT_*
AuthenticationMethods publickey
````

At present, `selinux` appears to get in the way of this working.
If it fails for you, try `setenforce 0` and pester me until I
fix it. Sorry!

## Apache

Config fragments for `httpd` are installed into `/etc/httpd/conf.d/`.
Set the appropriate hostname in each of these. 

Generate SSL certificates using `certbot`.

## Starting up

`systemctl start sourcehut-meta sourcehut-todo sourcehut-git sourcehut-hub`

You are now using Sourcehut.



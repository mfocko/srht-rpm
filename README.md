# Sourcehut RPM specfiles

Sourcehut is a powerful Git and Mercurial forge. This repo
represents an attempt to package it sensibly for RPM distros.
Currently this is FC32-only, but will eventually be built for
CentOS too.

## Usage

````sh
sudo dnf copr enable tylerjgriffiths/srht
sudo dnf -y install sourcehut-git
````

Modify /etc/sr.ht/config.ini as appropriate; an example configuration
file is placed into `/etc/sr.ht/conf.d/$service.ini`. Generate keys
with srht-keygen and store in the appropriate locations. You should use a new
Postgres database for _each_ service you are running. Then enable
the appropriate services, which run with Gunicorn.

For each service, run `${service}-initdb`.

````sh
sudo systemctl enable --now sourcehut-meta sourcehut-git
````

You are now using Sourcehut.


## Packages

### Main
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut/) `sourcehut` is a metapackage pulling in all other components
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-srht/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-srht/) `python-srht` is the core Python library for all Sourcehut services
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut-core/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-srht/) `sourcehut-core` covers core functionality and configuration
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-metasrht/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-metasrht/) `python-metasrht` is the Python library for Sourcehut metadata services
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut-meta/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut-meta/) `sourcehut-meta` is the web interface for Sourcehut metadata services
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-hubsrht/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-hubsrht/) `python-hubsrht` is the Python library for Sourcehut project hub
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-scmsrht/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-scmsrht/) `python-scmsrht` is a Python library for SCM 
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-gitsrht/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-gitsrht/) `python-gitsrht` is the Python library for Sourcehut git services
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut-git/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut-git/) `sourcehut-git` is the web interface for Sourcehut git services
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-hgsrht/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-hgsrht/) `python-hgsrht` is the Python library for Sourcehut hg services
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut-hg/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut-hg/) `sourcehut-hg` is the web interface for Sourcehut hg services
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut-hub/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut-hub/) `sourcehut-hub` is the web interface and configuration for Sourcehut project hub
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-todosrht/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-todosrht/) `python-todosrht` is the Python library for Sourcehut tickets
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut-todo/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut-todo/) `sourcehut-todo` is the web interface for Sourcehut tickets
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-pastesrht/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-pastesrht/) `python-pastesrht` is the Python library for Sourcehut pastebin
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut-paste/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut-paste/) `sourcehut-paste` is the web interface for Sourcehut pastebin
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-buildsrht/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-buildsrht/) `python-buildsrht` is the Python library for Sourcehut builds
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut-build/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut-build/) `sourcehut-build` is the web interface for Sourcehut builds
 

### Dependencies
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-pytest-mock/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-pytest-mock/) `python-pytest-mock` is a dependency not packaged by Fedora.
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-pgpy/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-pgpy/) `python-pgpy` is a dependency not packaged by Fedora.
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-stripe/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-stripe/) `python-stripe` is a dependency not packaged by Fedora.
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-zxcvbn/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-zxcvbn/) `python-zxcvbn` is a dependency not packaged by Fedora.
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-misaka/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-misaka/) `python-misaka` is a dependency not packaged by Fedora. 
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-sshpubkeys/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-sshpubkeys/) `python-sshpubkeys` is a dependency not packaged by Fedora.
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-minio/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-minio/) `python-minio` is a dependency not packaged by Fedora.

### Other
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/aerc/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/aerc/) `aerc` is a mailclient. It's not part of sourcehut, but may be useful with it.


# Puppet

Work on a Puppet module to deploy this Sourcehut system is in progress.
A full installation would be achieved with:

````
node "srht.example.com" {
	include sourcehut
}
````

# License

The specfiles are released under GPLv3; the packages built retain the license of
the upstream as indicated in the Specfile.

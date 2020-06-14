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

````sh
sudo systemctl enable --now sourcehut-meta sourcehut-git
````

You are now using Sourcehut.


## Packages

 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-srht/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-srht/) `python-srht` is the core Python library for all Sourcehut services
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut-core/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-srht/) `sourcehut-core` covers core functionality and configuration
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-metasrht/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-metasrht/) `python-metasrht` is the Python library for Sourcehut metadata services
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut-meta/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/sourcehut-meta/) `sourcehut-meta` is the web interface for Sourcehut metadata services
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-pytest-mock/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-pytest-mock/) `python-pytest-mock` is a dependency not packaged by Fedora.
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-pgpy/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-pgpy/) `python-pgpy` is a dependency not packaged by Fedora.
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-stripe/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-stripe/) `python-stripe` is a dependency not packaged by Fedora.
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-zxcvbn/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-zxcvbn/) `python-zxcvbn` is a dependency not packaged by Fedora.
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-misaka/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-misaka/) `python-misaka` is a dependency not packaged by Fedora. 
 * [![Copr build status](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-sshpubkeys/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/tylerjgriffiths/srht/package/python-sshpubkeys/) `python-sshpubkeys` is a dependency not packaged by Fedora.  

 

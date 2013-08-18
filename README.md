elasticsearch-shared-folder
===============

This demo isnt done, probably never will be, just holds some ideas and scripts.

A vagrant virtualbox based elasticsearch server that indexes a directory of files with tika.
As my files are stored on a CIFS share, I didn't want to go the attachment plugin route.


Try it out!
-----------
*Bring up the virtualmachine and provision the server*

    $ vagrant up

_Point your browser at_

    webserver: http://localhost:8080/
    elasticsearch: http://localhost:9020

_Cleaning up_

    $ vagrant destroy

_To manually clean up stray VMs_

    $ VBoxManage list vms
    $ VBoxManage unregistervm elasticsearch-shared-folder –delete

####Requires:
* [Vagrant](http://www.vagrantup.com/) -- `sudo apt-get install vagrant` 1.2.2
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads/) -- `sudo apt-get install virtualbox-4.2`

####Built On:
* [ansible](https://github.com/ansible/ansible/) -- provisioner loaded up first
* [elasticsearch](http://www.elasticsearch.org/) -- flexible and powerfule opensource distributed real-time search and analytics engine
* [tika] (http://tika.apache.org/) -- Extracts metadata from rich documents (e.g. PDF / Word)


####TODO:
* Base vargrant virtualbox install
* Install java7
* Install elasticsearch
* Install tika
* Install python/jnius
* Startup elasticsearch server
* Recursivly index all files in `./files_to_index`
* Provide a web based search bar

####Issues:
* Find Time to work on this!

####Notes:
* bootstrap.sh does a one-time install of ansible to get the ball rolling

####My workflow:
* git config --global user.name 'Your Name'
* git config --global user.email your@email
* git pull
* edit some code
* git add <new files>
* git commit -am 'fixed some bugs'
* git push -u origin master

####Thanks to:
* [Troy Goode](https://github.com/TroyGoode/vagrant-docker-elasticsearch/) -- elasticsearch vagrant docker example
* [owainlewis](https://gist.github.com/owainlewis/6069582) -- Java 7 ansible playbook gist
* [karmi](https://gist.github.com/karmi/5594127) -- test attachments elasticsearch
* [hackzine](http://www.hackzine.org/using-apache-tika-from-python-with-jnius.html) -- python interface to tika with jnius

Contributing
------------

1. Fork it.
2. Create a branch (`git checkout -b my_new_feature`)
3. Commit your changes (`git commit -am "Added Cool Thing"`)
4. Push to the branch (`git push origin my_new_feature`)
5. Open a [Pull Request][1]
6. Enjoy a few plumphelmets while you wait cuz I've never done this before.

[1]: http://github.com/ubergarm/elasticsearch-shared-folder/pulls


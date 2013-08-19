# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.define :es do |es_config|
    es_config.vm.box = "precise32"
    config.vm.box_url = "http://files.vagrantup.com/precise32.box"
    es_config.vm.network :forwarded_port, host: 8080, guest: 5000
    es_config.vm.network :forwarded_port, host: 9200, guest: 9200
    es_config.vm.network :private_network, ip: "192.168.33.103"
    # es_config.vm.synced_folder "./files_to_index", "/files_to_index"

    #the bootstrap script installs ansible in the VM itself    
    es_config.vm.provision :shell, :path => "bootstrap.sh"

    es_config.vm.provider :virtualbox do |vb|
      #vb.gui = true
      vb.customize [
		    "modifyvm", :id,
		    "--name", "elasticsearch-shared-folder",
		    "--memory", "2048"
	 	   ]
    end
  end
end

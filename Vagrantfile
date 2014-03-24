# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "centos6"
  config.vm.box_url = "../boxes/centos6.box"
  config.vm.network "private_network", ip: "192.168.50.01"
  config.vm.provision :shell, :path => "config/bootstrap.sh"
  config.vm.synced_folder ".", "/usr/share/nginx/mindlogs/mindlogs", :mount_options => ["dmode=777","fmode=666"]
end

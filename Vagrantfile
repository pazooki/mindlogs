VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "vagrant-centos-65"
    config.vm.network "private_network", ip: "192.168.50.10"
    config.vm.hostname = "dev01.mindlogs"
    config.hostsupdater.aliases = ["dev01.mindlogs"]
    config.hostsupdater.remove_on_suspend = true
    config.vm.provision :shell, :path => "config/bootstrap.sh"
    config.vm.synced_folder ".", "/srv/mindlogs", :mount_options => ["dmode=777","fmode=666"]
    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "../provlogs/site.yml"
        ansible.extra_vars = { ansible_ssh_user: 'vagrant' }
    end
end
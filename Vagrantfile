VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "vagrant-centos-65"
    config.vm.network "private_network", ip: "192.168.50.10"
    config.vm.hostname = "webapp01"
    config.hostsupdater.aliases = ["webapp01"]
    config.hostsupdater.remove_on_suspend = true
    config.vm.synced_folder ".", "/srv/webapps/mindlogs", :mount_options => ["dmode=777","fmode=666"]
    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "../provlogs/site.yml"
        ansible.inventory_path = "../provlogs/dev"
        ansible.extra_vars = { ansible_ssh_user: 'vagrant', app_name: 'mindlogs' }
        ansible.verbose = 'vv'
        ansible.limit = 'all'
        ansible.raw_arguments  = "--ask-vault-pass"
    end
end
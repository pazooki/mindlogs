#!/bin/sh

echo 'Bootstrap.sh is running......'
#sh [[ `grep dev.mindlogs /etc/hosts` = '' ]]; then
#	echo "192.168.50.1 dev.mindlogs" >> /etc/hosts
#	sudo hostname dev.mindlogs
#fi
#
#rpm -qa | grep -qw epel-release-6-8* || sudo rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
#rpm -qa | grep -qw remi-release-6* || sudo rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm
#rpm -qa | grep -qw webtatic-release-6* || sudo rpm -Uvh http://mirror.webtatic.com/yum/el6/latest.rpm
#
#if [ ! -f /etc/yum.repos.d/hop5.repo ]; then
#	sudo wget "http://www.hop5.in/yum/el6/hop5.repo" -P /etc/yum.repos.d
#fi
#
#echo "--- Yum Update ---"
#sudo yum -y update;
#
#
#echo "--- PostgreSQL configuration ---"
#sudo su - postgres -c /usr/pgsql-9.2/bin/initdb
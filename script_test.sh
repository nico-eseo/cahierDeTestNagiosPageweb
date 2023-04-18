# !/bin/bash

# Afficher le nom de la machine
echo "Nom de la machine : $(hostname)"

# Afficher l'adresse IP
ip=$(hostname -I)
echo "Adresse IP : $ip"

# Afficher le DNS
dns=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}')
echo "DNS : $dns"

# Afficher la sécurité sur les ports
#sudo netstat -tuln | grep LISTEN


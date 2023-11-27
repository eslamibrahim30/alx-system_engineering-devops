# set up your client SSH configuration file
exec { 'echo "PasswordAuthentication no" | sudo tee -a /etc/ssh/ssh_config > /dev/null':
  path => ['/usr/bin', '/usr/sbin',],
}

exec { 'echo "IdentityFile ~/.ssh/school" | sudo tee -a /etc/ssh/ssh_config > /dev/null':
  path => ['/usr/bin', '/usr/sbin',],
}

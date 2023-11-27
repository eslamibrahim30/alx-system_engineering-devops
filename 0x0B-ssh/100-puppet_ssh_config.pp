# set up your client SSH configuration file
file { '/home/$user/.ssh/':
  ensure => directory,
}

file { '/home/$user/.ssh/school':
  ensure => file,
}

file { '/etc':
  ensure => directory,
}

file { '/etc/ssh':
  ensure => directory,
}

file { '/etc/ssh/ssh_config':
  ensure => file,
}

exec { 'echo "PasswordAuthentication no" | sudo tee -a /etc/ssh/ssh_config > /dev/null':
  path => ['/usr/bin', '/usr/sbin',],
}

exec { 'echo "IdentityFile ~/.ssh/school" | sudo tee -a /etc/ssh/ssh_config > /dev/null':
  path => ['/usr/bin', '/usr/sbin',],
}

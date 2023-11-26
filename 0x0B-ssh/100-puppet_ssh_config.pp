# set up your client SSH configuration file
file { '/etc/ssh/ssh_config':
  ensure => file,
}

file_line { 'ssh_key_config':
  path  => '/etc/ssh/ssh_config',
  line  => '    IdentityFile ~/.ssh/school',
  match => '^.*IdentityFile.*$',
}

file_line { 'disable_password_auth':
  path  => '/etc/ssh/ssh_config',
  line  => '    PasswordAuthentication no',
  match => '^.*PasswordAuthentication.*$',
}

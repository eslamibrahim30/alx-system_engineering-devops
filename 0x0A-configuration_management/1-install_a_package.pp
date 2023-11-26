# install flask 2.1.0 from pip3
file { '/opt/graphite/bin/flask-cache.py':
  ensure => 'absent',
}

package { 'flask':
  ensure   => '2.1.0',
  require  => [ Class['graphite::prereqs::install'],
              File['/opt/graphite/bin/flask-cache.py']
              ]
  provider => pip,
}

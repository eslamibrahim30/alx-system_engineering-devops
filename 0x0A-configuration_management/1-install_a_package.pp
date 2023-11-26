# install flask 2.1.0 from pip3
package { 'pip3':
  ensure => installed,
  name   => 'pip3',
}

package { 'flask':
  ensure  => '2.1.0',
  require => Package['pip3'],
  name    => 'flask',
  source  => 'pip3',
}

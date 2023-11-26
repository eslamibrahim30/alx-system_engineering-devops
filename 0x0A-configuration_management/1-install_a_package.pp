# install flask 2.1.0 from pip3
package {' Python3':
  ensure => 'installed',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
}

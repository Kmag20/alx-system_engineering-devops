# Using puppet to install flask from the python packet manager pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}


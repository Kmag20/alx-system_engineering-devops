# create a file in the directory /tmp

file { '/tmp/school':
  ensure  => present,
  mode    => '0744',
  owner   => www-data,
  group   => www-data,
  path    => '/tmp/school',
  content => 'I love Puppet',
}


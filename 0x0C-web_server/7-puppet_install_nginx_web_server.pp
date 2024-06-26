# installs and configures Nginx web server

package { 'nginx':
  ensure => 'installed',
}

file { 'index.html':
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}

exec { 'config':
  command  => 'sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent;/" /etc/nginx/sites-available/default',
  provider => 'shell',
}
exec { 'start':
  command  => 'sudo service nginx restart',
  provider => 'shell',
}

# Install a nginx package

package {'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/default':
  ensure => absent,
  require => Package['nginx'],
  notify => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
  require => Package['nginx'],
  notify => Service['nginx']
}

# Create a new configuration file
file { '/etc/ninx/sites-available/default.conf':
  ensure => file,
  content => @(EOT)
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        add_header X-Served-By ${::hostname};

        location / {
            try_files \$uri \$uri/ =404;
        }

        location /redirect_me {
            return 301 https://google.com;
        }

        error_page 404 /404.html;

        location = /404.html {
            internal;
            add_header Content-Type text/html;
            return 404 "Ceci n'est pas une page";
        }
    }
| EOT
require => Package['nginx'],
  notify  => Service['nginx'],
}

# Enable the new configuration file
file { '/etc/nginx/sites-enabled/default.conf':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default.conf',
  require => File['/etc/nginx/sites-available/default.conf'],
  notify  => Service['nginx'],
}

# Create the /var/www/html directory if it doesn't exist
file { '/var/www/html':
  ensure => directory,
}

# Create the index.html file
file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
  require => File['/var/www/html'],
}

# Ensure the Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

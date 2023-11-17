# adding holberton user limit
exec { 'add-hard-file-limit':
  command => 'sed -i "/holberton hard/s/5/8192/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'add-soft-file-limit':
  command => 'sed -i "/holberton soft/s/4/8192/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

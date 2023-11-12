# Finds the wrong "phpp" extension and replace it by "php" in the "wp-settings.php" file

exec { 'fix-wordpress':
  command => 'sed -i s/\.phpp/\.php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
}

# Killing a process 

exec { 'kill_process':
  path    => '/usr/bin/',
  command => 'pkill killmenow',
  returns => [0, 1]
}

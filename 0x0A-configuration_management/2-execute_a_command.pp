# Manifest that kills a process names killmenow

exec { 'killmenowlol':
  command  => 'pkill -9 killmenow',
  path     => '/usr/bin',
  onlyif   => 'pgrep killmenow',
  provider => shell
}

# This manifest to increase the soft limit
limits::limits{ 'build_nproc':
  ensure     => present,
  user       => 'build',
  limit_type => 'nproc',
  hard       => 512,
  soft       => 256,
}

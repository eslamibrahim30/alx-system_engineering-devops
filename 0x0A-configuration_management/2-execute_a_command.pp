# This manifest kills a process named killmenow
exec { 'pkill_killmenow':
  command => 'pkill killmenow',
}

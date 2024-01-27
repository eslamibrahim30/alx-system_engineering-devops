# This manifest to increase the soft limit
exec {'fix--for-nginx':
        command => '/bin/bash -c "ulimit -c unlimited"',
}

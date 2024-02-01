# This manifest to fix error 'phpp' in the stack
exec {'fix-wordpress':
        command => sed -i 's/phpp/php/g' /var/www/html/wp-settings.php,
}

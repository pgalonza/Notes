# Autocomplete

_rcmail_output_html.php_
```
$user_attrib = $autocomplete > 0 ? array() : array('autocomplete' => 'on');
$host_attrib = $autocomplete > 0 ? array() : array('autocomplete' => 'on');
$pass_attrib = $autocomplete > 1 ? array() : array('autocomplete' => 'on');
```

_config.inc.php_
```
$config['login_autocomplete'] = 2;
```

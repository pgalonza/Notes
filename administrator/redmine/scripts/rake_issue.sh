#!/bin/bash
cd /var/www/redmine
rake -f /var/www/redmine/Rakefile --silent redmine:email:receive_imap RAILS_ENV=production host= username= password= ssl=SSL port=993 project=project_name allow_override=tracker,priority,project unknown_user=create no_permission_check=1
rake -f /var/www/redmine/Rakefile --silent redmine:email:receive_imap RAILS_ENV=production host= username= password= starttls=STARTTLS port=143 project=project_nam allow_override=tracker,priority,project unknown_user=create no_permission_check=1

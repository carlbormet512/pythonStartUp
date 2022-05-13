#errorsalert.py
alert_system = 'console' 
error_severity = 'critical'
error_message = 'OMG! something terrible happened'

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error_severity == 'critical':
        print('admin@example.com', error_message)
    elif error_severity == 'medium':
        print('support.1@example.com', error_message)
    else:
            print('support.2@example.com', error_message)

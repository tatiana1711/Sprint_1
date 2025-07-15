started_time_values = '1h 45m,360s,25m,30m 120s,2h 60s'
separated_time_values = started_time_values.split(',')

minutes = 0

for separated_time_value in separated_time_values:
    for time_value in separated_time_value.split(' '):
        if 'h' in time_value:
            minutes += int(time_value.replace('h',''))* 60
        elif 's' in time_value:
            minutes += int((time_value.replace('s','')))//60
        elif 'm' in time_value:
            minutes += int(time_value.replace('m',''))       
    

print(minutes)

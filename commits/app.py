import os
from random import randint
from datetime import datetime, timedelta
from subprocess import run

def generate_commits(start_date, end_date):
    current_date = start_date
    
    while current_date <= end_date:
        for _ in range(randint(1, 10)):  
            d = current_date.strftime('%Y-%m-%d %H:%M:%S')
            with open('file.txt', 'a') as file:
                file.write(f"{d}\n")
            run(['git', 'add', '.'])
            run(['git', 'commit', '--date', d, '-m', 'commit'])
        
        current_date += timedelta(days=1)
    
    run(['git', 'push', 'origin', 'main'])


start_date = datetime(2024, 6, 9)  
end_date = datetime(2024, 6, 11)   

generate_commits(start_date, end_date)

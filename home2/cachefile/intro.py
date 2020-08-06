import random, time

def intro():
    cur_time = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

    date = cur_time[0:10]
    hour = int(cur_time[11:13])
    greet = 'Good'
    if 5 <= hour < 13:
        greet += ' Morning'
    elif 13 <= hour < 19:
        greet += ' Afternoon'
    else:
        greet += ' Evening'

    return {
        'intro_slide1': random.randint(0, 24),   
        'intro_slide2': random.randint(0, 24),
        'intro_slide3': random.randint(0, 24),
        'intro_greet': greet,
        'intro_date': date,
    }

    
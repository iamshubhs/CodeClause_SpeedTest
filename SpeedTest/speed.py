def calculate_speed(num_words, elapsed_time):
    minutes = elapsed_time / 60
    speed = num_words / minutes
    return round(speed, 2)

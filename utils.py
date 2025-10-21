def calculate_sleep_duration(sleep_time, wake_time):
    """Calculate the duration of sleep in hours and minutes."""
    sleep_duration = wake_time - sleep_time
    hours, minutes = divmod(sleep_duration.total_seconds() // 60, 60)
    return int(hours), int(minutes)

def is_sleep_cycle_good(sleep_duration):
    """Evaluate if the sleep cycle is good based on duration."""
    if sleep_duration < 7:
        return False, "Consider sleeping earlier to achieve at least 7 hours of sleep."
    elif 7 <= sleep_duration <= 9:
        return True, "Your sleep cycle is good. Keep it up!"
    else:
        return False, "You might be oversleeping. Aim for 7-9 hours of sleep."

def format_time_delta(delta):
    """Format a time delta into a readable string."""
    total_seconds = int(delta.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}h {minutes}m {seconds}s"

def send_sleep_alert(current_time):
    """Send an alert message if the current time is after 11:30 PM."""
    if current_time.hour >= 23 and current_time.minute >= 30:
        return "It's time to sleep! Prioritize your rest."
    return None
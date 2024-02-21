from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=5)

formatted_date = new_date.strftime('%Y-%m-%d')

print("Current Date:", current_date.strftime('%Y-%m-%d'))
print("Date Five Days Ago:", formatted_date)

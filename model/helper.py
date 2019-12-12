from datetime import date
from calendar import monthrange

def quarter_of_date(dt):
    month = date.fromisoformat(dt).month
    return 'QTR' + str((month-1)//3 + 1)

def quarter_start(dt):
    d = date.fromisoformat(dt)
    return (d.month - 1) % 3 == 0 and d.day == 1

def quarter_end(dt):
    d = date.fromisoformat(dt)
    return d.month % 3 == 0 and d.day == monthrange(d.year, d.month)[1]

def is_european_country(ctry):
    european_countries = ['AT', 'CL', 'FI', 'FR', 'DE', 'GI', 'HU', 'IE', 'IM', 'IT', 'JE', 'LI', 'LU', 'PE', 'ES', 'SE', 'GB']
    return ctry in european_countries

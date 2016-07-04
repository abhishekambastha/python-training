'Collection of data validation utilities'

def validate_percentage(value):
    if not isinstance(value, (bool, int, float)):
        raise TypeError('Expected int or float')
    if value < 0.0 or value > 100.0:
        raise ValueError('Expected 0 to 100')

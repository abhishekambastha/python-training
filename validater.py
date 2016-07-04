'Collection of data validation utils'

def validate_percentage(value):
    if not isinstance(low, (int, float)):
        raise TypeError('Expected int or float')
    if low < 0.0 or low > 100.0:
        raise ValueError('Expected 0 to 100')

def clean_amount(value):
    """Convert text like '$1,200.50' into the number 1200.50"""
    return float(value.replace("$", "").replace(",", ""))
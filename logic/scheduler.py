import urllib.parse
import pandas as pd
from datetime import datetime

COMPATIBILITY = {
    'O+': ['O+', 'O-'], 'O-': ['O-'], 'A+': ['A+', 'A-', 'O+', 'O-'],
    'A-': ['A-', 'O-'], 'B+': ['B+', 'B-', 'O+', 'O-'], 'B-': ['B-', 'O-'],
    'AB+': ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'], 'AB-': ['AB-', 'A-', 'B-', 'O-']
}

def get_matches(bg, donor_df):
    # Convert dates to ensure comparison works
    donor_df['LastDonationDate'] = pd.to_datetime(donor_df['LastDonationDate'])
    
    # Filter 1: Eligibility (90-day rule)
    eligible = donor_df[(datetime.now() - donor_df['LastDonationDate']).dt.days >= 90]
    
    # Filter 2: Strict Blood Group Match
    # This ensures A+ patients only find A+ donors
    if isinstance(bg, (list, pd.Series, pd.Index)):
        bg = bg[0] # Extract string from list if necessary
        
    strict_matches = eligible[eligible['BloodGroup'] == bg]
    return strict_matches

def get_wa_link(phone, p_name, bg):
    msg = f"Hi! Patient {p_name} needs exactly {bg} blood. You are eligible and a perfect match. Can you donate today?"
    return f"https://wa.me{phone}?text={urllib.parse.quote(msg)}"
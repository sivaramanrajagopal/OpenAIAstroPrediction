#!/usr/bin/env python3
"""
Global timezone utilities for astrology calculations
Simplified version based on working AstrologyResearchDatabase
"""

try:
    from timezonefinder import TimezoneFinder
    TIMEZONEFINDER_AVAILABLE = True
except ImportError:
    TIMEZONEFINDER_AVAILABLE = False

import pytz
from datetime import datetime, date

# Initialize timezone finder if available
tf = TimezoneFinder() if TIMEZONEFINDER_AVAILABLE else None

def get_timezone_from_coordinates(lat, lon):
    """
    Automatically detect timezone from coordinates
    """
    if not TIMEZONEFINDER_AVAILABLE or not tf:
        return estimate_timezone_from_longitude(lon)
    
    try:
        timezone_name = tf.timezone_at(lng=lon, lat=lat)
        if timezone_name:
            # Validate timezone name with pytz
            try:
                pytz.timezone(timezone_name)
                return timezone_name
            except pytz.exceptions.UnknownTimeZoneError:
                print(f"Invalid timezone detected: {timezone_name}")
                return estimate_timezone_from_longitude(lon)
        else:
            return estimate_timezone_from_longitude(lon)
    except Exception as e:
        print(f"Error detecting timezone: {e}")
        return estimate_timezone_from_longitude(lon)

def estimate_timezone_from_longitude(lon):
    """
    Estimate timezone from longitude as fallback
    """
    # Rough estimation based on longitude
    hours_from_utc = int(round(lon / 15))
    
    # Map to common timezone names
    timezone_map = {
        -12: 'Pacific/Kwajalein', -11: 'Pacific/Midway', -10: 'Pacific/Honolulu',
        -9: 'America/Anchorage', -8: 'America/Los_Angeles', -7: 'America/Denver',
        -6: 'America/Chicago', -5: 'America/New_York', -4: 'America/Halifax',
        -3: 'America/Sao_Paulo', -2: 'Atlantic/South_Georgia', -1: 'Atlantic/Azores',
        0: 'Europe/London', 1: 'Europe/Paris', 2: 'Europe/Kiev', 3: 'Europe/Moscow',
        4: 'Asia/Dubai', 5: 'Asia/Kolkata', 6: 'Asia/Dhaka', 7: 'Asia/Bangkok',
        8: 'Asia/Shanghai', 9: 'Asia/Tokyo', 10: 'Australia/Sydney',
        11: 'Pacific/Guadalcanal', 12: 'Pacific/Auckland'
    }
    
    return timezone_map.get(hours_from_utc, 'UTC')

def get_timezone_offset(lat, lon, birth_date):
    """
    Get timezone offset for specific date (handles DST)
    """
    try:
        timezone_name = get_timezone_from_coordinates(lat, lon)
        tz = pytz.timezone(timezone_name)
        
        # Create datetime at noon to avoid DST transition issues
        dt = datetime.combine(birth_date, datetime.min.time().replace(hour=12))
        local_dt = tz.localize(dt)
        
        return local_dt.utcoffset().total_seconds() / 3600
    except Exception as e:
        print(f"Error calculating timezone offset: {e}")
        return 0

def get_timezone_info(lat, lon, birth_date=None):
    """
    Get comprehensive timezone information
    """
    try:
        timezone_name = get_timezone_from_coordinates(lat, lon)
        tz = pytz.timezone(timezone_name)
        
        # Get offset for birth date if provided
        birth_offset = None
        if birth_date:
            birth_offset = get_timezone_offset(lat, lon, birth_date)
        
        return {
            'timezone_name': timezone_name,
            'birth_offset': birth_offset,
        }
    except Exception as e:
        print(f"Error getting timezone info: {e}")
        return {
            'timezone_name': 'UTC',
            'birth_offset': 0,
        }
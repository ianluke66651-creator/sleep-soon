from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class UserProfile:
    user_id: str
    email: str
    sleep_time: Optional[datetime] = None
    wake_time: Optional[datetime] = None
    spotify_usage: Optional[float] = 0.0  # in hours
    youtube_usage: Optional[float] = 0.0  # in hours

@dataclass
class SleepData:
    user_id: str
    sleep_start: datetime
    sleep_end: datetime
    sleep_quality: str  # e.g., "Good", "Bad"
    sleep_duration: float  # in hours

@dataclass
class UsageStats:
    user_id: str
    spotify_hours: float  # in hours
    youtube_hours: float  # in hours
    total_usage: float  # in hours

def calculate_sleep_duration(sleep_data: SleepData) -> float:
    duration = (sleep_data.sleep_end - sleep_data.sleep_start).total_seconds() / 3600.0
    return duration if duration > 0 else 0.0

def evaluate_sleep_quality(sleep_duration: float) -> str:
    if sleep_duration >= 7:
        return "Good"
    elif 5 <= sleep_duration < 7:
        return "Average"
    else:
        return "Bad"
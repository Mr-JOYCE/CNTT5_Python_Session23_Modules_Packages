from datetime import datetime, timedelta


def predict_eta(departure_str, distance_km, speed=60):
    """
    Tính ETA dựa trên khoảng cách và vận tốc
    """

    departure_time = datetime.strptime(
        departure_str,
        "%Y-%m-%d %H:%M:%S"
    )

    travel_hours = distance_km / speed

    eta = departure_time + timedelta(hours=travel_hours)

    return eta
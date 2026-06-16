import math


def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Tính khoảng cách giữa 2 tọa độ GPS bằng công thức Haversine
    Đơn vị trả về: km
    """

    R = 6371

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)

    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1_rad)
        * math.cos(lat2_rad)
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c

    return distance
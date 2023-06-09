import carla
import numpy as np
import typing

def location_from_carla(location : carla.Location) -> np.ndarray:
    # coordinate frame of CARLA is left-handed, z-up, x-right, y-backward
    # coordinate frame of ROAR is right-handed, z-up, x-forward, y-left
    return np.array([location.x, -location.y, location.z])

def location_to_carla(location : np.ndarray) -> carla.Location:
    return carla.Location(x=location[0], y=-location[1], z=location[2])

def rotation_from_carla(rotation : carla.Rotation) -> np.ndarray:
    rot_deg = np.array([
        rotation.roll, -rotation.pitch, -rotation.yaw
    ])
    return np.deg2rad(rot_deg)

def rotation_to_carla(rotation : np.ndarray) -> carla.Rotation:
    rot_deg = np.rad2deg(rotation)
    return carla.Rotation(roll=rot_deg[0], pitch=-rot_deg[1], yaw=-rot_deg[2])

def transform_from_carla(transform : carla.Transform) -> typing.Tuple[np.ndarray, np.ndarray]:
    location = location_from_carla(transform.location)
    rotation = rotation_from_carla(transform.rotation)
    return location, rotation

def transform_to_carla(location : np.ndarray, rotation : np.ndarray) -> carla.Transform:
    location = location_to_carla(location)
    rotation = rotation_to_carla(rotation)
    return carla.Transform(location=location, rotation=rotation)
    
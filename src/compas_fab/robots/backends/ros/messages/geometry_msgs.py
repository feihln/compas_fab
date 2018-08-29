from __future__ import absolute_import

from .std_msgs import ROSmsg
from .std_msgs import Header
from .std_msgs import Time

from compas.geometry import Frame


class Point(ROSmsg):
    """http://docs.ros.org/kinetic/api/geometry_msgs/html/msg/Point.html
    """
    def __init__(self, x ,y, z):
        self.x = x
        self.y = y
        self.z = z

class Quaternion(ROSmsg):
    """http://docs.ros.org/kinetic/api/geometry_msgs/html/msg/Quaternion.html
    """
    def __init__(self, x ,y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

class Pose(ROSmsg):
    """http://docs.ros.org/kinetic/api/geometry_msgs/html/msg/Pose.html
    """

    def __init__(self, position=Point(0,0,0), orientation=Quaternion(0,0,0,1)):
        self.position = position
        self.orientation = orientation

    @classmethod
    def from_frame(cls, frame):
        point = frame.point
        qw, qx, qy, qz = frame.quaternion
        return cls(Point(*list(point)), Quaternion(qx, qy, qz, qw))

    @property
    def frame(self):
        point = [self.position.x, self.position.y, self.position.z]
        quaternion = [self.orientation.w, self.orientation.x, self.orientation.y, self.orientation.z]
        return Frame.from_quaternion(quaternion, point=point)

    @classmethod
    def from_msg(cls, msg):
        position = Point.from_msg(msg['position'])
        orientation = Quaternion.from_msg(msg['orientation'])
        return cls(position, orientation)

class PoseStamped(ROSmsg):
    """http://docs.ros.org/melodic/api/geometry_msgs/html/msg/PoseStamped.html
    """

    def __init__(self, header=Header(), pose=Pose()):
        self.header = header
        self.pose = pose

class Vector3(ROSmsg):
    """http://docs.ros.org/api/geometry_msgs/html/msg/Vector3.html
    """
    def __init__(self, x=0., y=0., z=0.):
        self.x = x
        self.y = y
        self.z = z

class Quaternion(ROSmsg):
    """http://docs.ros.org/api/geometry_msgs/html/msg/Quaternion.html
    """
    def __init__(self, x=0., y=0., z=0., w=1.):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

class Transform(ROSmsg):
    """http://docs.ros.org/api/geometry_msgs/html/msg/Transform.html
    """
    def __init__(self, translation=Vector3(), rotation=Quaternion()):
        self.translation = translation
        self.rotation = rotation



class Twist(ROSmsg):
    """http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html
    """
    def __init__(self, linear=Vector3(), angular=Vector3()):
        self.linear = linear
        self.angular = angular
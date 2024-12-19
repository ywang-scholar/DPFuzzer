import pcl
import numpy as np
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2, PointField
import rospy
import threading
import json


class MapGenerator:
    def __init__(self, resolution, size, height, z_global, topic="map_generator/global_cloud", ns = None):
        self.node_name = "cylinder_point_cloud_generator"
        if not rospy.core.is_initialized():
            if ns != None:
                rospy.init_node(ns + '_' + self.node_name)
            else:
                rospy.init_node(self.node_name)
        if ns != None:
            topic = ns + "/" + top

        self.pub = rospy.Publisher(topic, PointCloud2, queue_size=10)
        self.resolution = resolution
        self.size = size
        self.height = height
        self.z_global = z_global
        self.global_map = None
        self.publish_thread = None
        self.publish_flag = False
        self.lock = threading.Lock()


    def save_map(self, name):
        pass #delete in this version

    def read_map(self, name):
        if not isinstance(name, type("string")):
            raise TypeError('Need a file name')

        points = np.load(name + ".npy")

        cloud = pcl.PointCloud()
        cloud.from_list(points)

        msg = PointCloud2()
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = "world"
        msg.height = 1
        msg.width = len(points)
        msg.fields.append(PointField(name="x", offset=0, datatype=PointField.FLOAT32, count=1))
        msg.fields.append(PointField(name="y", offset=4, datatype=PointField.FLOAT32, count=1))
        msg.fields.append(PointField(name="z", offset=8, datatype=PointField.FLOAT32, count=1))
        msg.is_bigendian = False
        msg.point_step = 12
        msg.row_step = msg.point_step * len(points)
        msg.is_dense = True
        msg.data = np.asarray(cloud, dtype=np.float32).tostring()

        self.global_map = msg

        

    def map_pub(self):
        self.publish_flag = True
        self.publish_thread = threading.Thread(target=self.publish_loop)
        self.publish_thread.start()

    def publish_loop(self):
        rate = rospy.Rate(1)  # 发布频率为1Hz
        while self.publish_flag and not rospy.is_shutdown():
            with self.lock:
                if self.global_map is not None:
                    self.global_map.header.stamp = rospy.Time.now()
                    self.pub.publish(self.global_map)
            rate.sleep()

    def map_pub_stop(self):
        self.publish_flag = False
        if self.publish_thread is not None:
            self.publish_thread.join()

    def __del__(self):
        self.map_pub_stop()


if __name__ == "__main__":
    resolution = 0.1
    height = 3.2
    size = 0.2
    z = -0.2

    map_generator = MapGenerator(resolution, size, height, z)

    obstacle_type = "cylinder"
    xy_positions = [[0.0, 0.0], [2.0, 0.0]]
    map_generator.generate_map(obstacle_type, xy_positions)

    obstacle_type = "square_cylinder"
    size = 0.3
    xy_positions = [[4.0, 0.0]]
    map_generator.size = size
    map_generator.generate_map(obstacle_type, xy_positions)
    map_generator.map_pub()
    rospy.sleep(5)
    map_generator.map_pub_stop()

#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class MyNode(Node):
    def __init__(self):
        super().__init__("first_node")
        self.create_timer(2.0, self.timer_callback)
        self.counter_=0

    def timer_callback(self):
        self.get_logger().info("Hello from ROS2 " + str(self.counter_))
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args)
    node= MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__== "__main__":
    main()

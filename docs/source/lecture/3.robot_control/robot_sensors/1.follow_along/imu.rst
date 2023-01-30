IMU
===

Open the following jupyter notebook:

- 01_03_imu.ipynb
- To run the cells within the notebook use *Ctrl + Enter*

.. thumbnail:: /_images/content_control/sensor1.jpg

|

Import the necessary python libraries and modules

.. code-block:: python

    import rospy
    from sensor_msgs.msg import Imu
    from tf.transformations import quaternion_from_euler


- Create zetabot Node
- Subscribe to the "imu" Topic
- Check message by dividing it into x, y, z, w values


.. code-block:: python

    def process_imu(msg):
        rospy.loginfo("x: {},y: {},z: {},w: {}".format(msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w))

    def start_node():
        rospy.init_node('zetabot')
        rospy.Subscriber("imu", Imu, process_imu)
        rospy.spin()

    try:
        start_node()
    except rospy.ROSInterruptException as err:
        print(err)



LIDAR
=====

Open the following jupyter notebook:

- 04_scan.ipynb
- To run the cells within the notebook use *Ctrl + Enter*

.. thumbnail:: /_images/content_control/sensor5.png

|

Import the necessary python libraries and modules

.. code-block:: python

    import rospy
    from sensor_msgs.msg import LaserScan



-   Create zetabot Node
-   Subscribe to the "scan" topic, and display the published information. 

.. code-block:: python

    def process_scan(msg):
        rospy.loginfo("data: {}".format(msg))

    def start_node():
        rospy.init_node('zetabot')
        rospy.Subscriber("scan", LaserScan, process_scan)
        rospy.spin()

    try:
        start_node()
    except rospy.ROSInterruptException as err:
        print(err)




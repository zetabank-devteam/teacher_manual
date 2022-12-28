===================
ROS Command Example
===================

-   01_ros.ipynbipynb
-   Running the cell code
    `Ctrl + Enter`

.. image:: ../images/comm3.png

.. code-block:: bash

    $ !rosnode list

-   Outputs a list of currently running ROS Nodes

.. image:: ../images/comm4.webp

.. code-block:: bash

    $ !rosnode info /joy_node

-   Outputs joy_node Print Node information

.. image:: ../images/comm5.png

.. code-block:: bash

    $ !rostopic list

-   Prints a list of currently running ROS topics

.. image:: ../images/comm6.png

.. code-block:: bash

    $ !rostopic info /imu

-   Output information of imu Topic

.. image:: ../images/comm7.png

.. code-block:: bash

    $ !rostopic echo /imu

-   Print imu Topic Message


.. image:: ../images/comm8.webp

.. code-block:: bash

    $ pm2 list

-   Check process list using pm2

.. image:: ../images/comm9.png

.. code-block:: bash

    $ !rosnode info /zetasound

-   Output information of zetasound Node

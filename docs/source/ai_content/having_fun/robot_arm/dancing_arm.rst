==========================
Dancing with the Robot Arm
==========================

-   05_04_dance.ipynb
-   | Running the cell code
    | `Ctrl + Enter`

.. thumbnail:: /_images/having_fun/dance1.png

.. code-block:: python

    #!/usr/bin/env python3
    #coding=utf-8
    import time
    from Arm_Lib import Arm_Device


    Arm = Arm_Device()
    time.sleep(.1)

    time_1 = 500
    time_2 = 1000
    time_sleep = 0.5

-   Load Arm_Lib module and register the robot arm as an object


.. code-block:: python

    # Dancing Robot arm in repeat
    def main():
        # 서보를 중심으로 만든다.
        Arm.Arm_serial_servo_write6(90, 90, 90, 90, 90, 90, 500)
        time.sleep(1)
        
        while True:
            Arm.Arm_serial_servo_write(2, 180-120, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(3, 120, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(4, 60, time_1)
            time.sleep(time_sleep)

            Arm.Arm_serial_servo_write(2, 180-135, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(3, 135, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(4, 45, time_1)
            time.sleep(time_sleep)

            Arm.Arm_serial_servo_write(2, 180-120, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(3, 120, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(4, 60, time_1)
            time.sleep(time_sleep)

            Arm.Arm_serial_servo_write(2, 90, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(3, 90, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(4, 90, time_1)
            time.sleep(time_sleep)

            Arm.Arm_serial_servo_write(2, 180-80, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(3, 80, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(4, 80, time_1)
            time.sleep(time_sleep)



            Arm.Arm_serial_servo_write(2, 180-60, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(3, 60, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(4, 60, time_1)
            time.sleep(time_sleep)

            Arm.Arm_serial_servo_write(2, 180-45, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(3, 45, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(4, 45, time_1)
            time.sleep(time_sleep)

            Arm.Arm_serial_servo_write(2, 90, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(3, 90, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(4, 90, time_1)
            time.sleep(.001)
            time.sleep(time_sleep)



            Arm.Arm_serial_servo_write(4, 20, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(6, 150, time_1)
            time.sleep(.001)
            time.sleep(time_sleep)

            Arm.Arm_serial_servo_write(4, 90, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(6, 90, time_1)
            time.sleep(time_sleep)

            Arm.Arm_serial_servo_write(4, 20, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(6, 150, time_1)
            time.sleep(time_sleep)

            Arm.Arm_serial_servo_write(4, 90, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(6, 90, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(1, 0, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(5, 0, time_1)
            time.sleep(time_sleep)



            Arm.Arm_serial_servo_write(3, 180, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(4, 0, time_1)
            time.sleep(time_sleep)

            Arm.Arm_serial_servo_write(6, 180, time_1)
            time.sleep(time_sleep)

            Arm.Arm_serial_servo_write(6, 0, time_2)
            time.sleep(time_sleep)



            Arm.Arm_serial_servo_write(6, 90, time_2)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(1, 90, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(5, 90, time_1)
            time.sleep(time_sleep)

            Arm.Arm_serial_servo_write(3, 90, time_1)
            time.sleep(.001)
            Arm.Arm_serial_servo_write(4, 90, time_1)
            time.sleep(time_sleep)

            print(" END OF LINE! ")

    try :
        main()
    except KeyboardInterrupt:
        print(" Program closed! ")
        pass


-   Arm_serial_servo_write (motor number, angle, time)
-   Dance motion using servo motor angle control and while statement



.. code-block:: python

    del Arm  # Remove robot arm object


-   Remove object (Robot arm)
from macimu import IMU

def main():
    try:
        imu = IMU(accel=True, gyro=True, lid=True)
        imu.start()  
        print("Lid angle reader")
        # Read data
        while True:
            # read lid
            lid_angle = imu.read_lid()
            if lid_angle is not None:
                print("\033[A                             \033[A")
                print(f"Lid angle: {lid_angle:.1f}°")

    except KeyboardInterrupt:
        print("\nbye bud")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        imu.stop()



if __name__ == '__main__':
    main()
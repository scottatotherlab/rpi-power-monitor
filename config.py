import logging
import sys

# Create basic logger
logger = logging.getLogger('power_monitor')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s : %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)
logger.addHandler(ch)


# Using a multimeter, measure the voltage of the receptacle where your 9V AC transformer will plug into. Enter the measured value below.
GRID_VOLTAGE = 120.7 # 124.2
# Using a multimeter, measure the output voltage of your AC transformer. Using the value on the label is not ideal and will lead to greater accuracy in the calculations.
AC_TRANSFORMER_OUTPUT_VOLTAGE = 10.3 # 10.2

BATT_VOLTAGE = 10.83

DC_VOLTAGE_DIVIDER_OUTPUT_VOLTAGE = 2.75

# InfluxDB Settings
db_settings = {
    'host' : 'localhost',
    'port' : 8086,
    'username' : 'root',
    'password' : 'password',
    'database' : 'power_monitor'
}


# Define Variables
ct0_channel = 0             # Orange Pair           | House main (leg 1 - left)  (orange pair)
ct1_channel = 1             # Green Pair            | House main (leg 2 - right) (green pair)
ct2_channel = 2             # Blue Pair             | Subpanel main (leg 1 - top)
ct3_channel = 3             # Brown Pair            | Solar Power 
ct4_channel = 6             # 3.5mm Input #1        | Subpanel main (leg 2 - bottom)
board_voltage_channel =  4  # Board voltage ~3.3V
v_sensor_channel = 5        # 9V AC Voltage channel
vbatt_sensor_channel = 7    # battery output voltage channel

# The values from running the software in "phase" mode should go below!
ct_phase_correction = {
    'ct0' : 1.71340443,
    'ct1' : 1,
    'ct2' : 1,
    'ct3' : 1,
    'ct4' : 1,
}

# AFTER phase correction is completed, these values are used in the final calibration for accuracy. See the documentation for more information.
accuracy_calibration = {
    'ct0' : 0.16819,
    'ct1' : 1,
    'ct2' : 1,
    'ct3' : 1,
    'ct4' : 1,
    'AC'  : 1.07346,
    'DC'  : 1, # battery output voltage channel calibration 
}
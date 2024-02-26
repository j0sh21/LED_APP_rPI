import configparser

config = configparser.ConfigParser()

# Attempt to read the config file
try:
    config.read(r'cfg.ini')
except Exception as e:
    print(f"Error reading the config file: {e}")

# Helper function to get configuration values with error handling
def get_config_value(section, key):
    try:
        return config.get(section, key)
    except configparser.NoSectionError:
        print(f"Missing section '{section}' in config file.")
    except configparser.NoOptionError:
        print(f"Missing key '{key}' in section '{section}' in config file.")
    except Exception as e:
        print(f"Error retrieving configuration value: {e}")

# GPIO PINS for LED
red_pin = config.getint('GPIO', 'red_pin')
green_pin = config.getint('GPIO', 'green_pin')
blue_pin = config.getint('GPIO', 'blue_pin')

# LED effects
on_time = config.getfloat('GPIO', 'on_time')
off_time = config.getfloat('GPIO', 'off_time')
fade_steps = config.getfloat('GPIO', 'fade_steps')
brightness_steps = config.getfloat('GPIO', 'brightness_steps')

BREATH_SPEED = config.getfloat('GPIO', 'BREATH_SPEED')
BREATH_STEPS = config.getint('GPIO', 'BREATH_STEPS')

#DEBUG MODE
DEBUG_MODE = config.getint('DEV', 'DEBUG')

print("Config successfully loaded!")

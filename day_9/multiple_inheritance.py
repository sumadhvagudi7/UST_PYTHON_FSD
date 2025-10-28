# ============================================================
# SMART HOME DEVICE MANAGEMENT SYSTEM  (Starter Code)
# Demonstrates Multiple Inheritance in Python
# ============================================================

class Device:
    """Base class representing a generic device."""

    def __init__(self, device_name):
        self.device_name = device_name
        self.status = "off"

    def turn_on(self):
        self.status = "on"
        return f"{self.device_name} turned on."

    def turn_off(self):
        self.status = "off"
        return f"{self.device_name} turned off."
    
    def __str__(self):
        return f"{self.device_name} (Status: {self.status})"



class Connectable:
    """Base class for connectivity features."""

    def __init__(self):
        self.wifi_connected = False

    def connect_wifi(self):
        self.wifi_connected = True
        return "Conected to wifi!"

    def disconnect_wifi(self):
        self.wifi_connected = False
        return "Disconnected wifi!"


# ------------------------------------------------------------
# Derived Classes using Multiple Inheritance
# ------------------------------------------------------------

class SmartLight(Device, Connectable):
    """Derived class combining Device and Connectable"""

    def __init__(self, device_name, brightness=50):
        Device.__init__(self, device_name)
        Connectable.__init__(self)
        self.brightness = brightness

    def set_brightness(self, level):
        self.brightness = level
        return f"{self.device_name} brightness set to {level}%."

    def turn_on(self):  # Overridden
        super().turn_on()
        return f"{self.device_name} light is shining bright!"

    def __str__(self):
        return f"{self.device_name} (Light - {self.brightness}%, Wi-Fi: {'Connected' if self.wifi_connected else 'Disconnected'})"



class SmartSpeaker(Device, Connectable):
    """Derived class combining Device and Connectable"""

    def __init__(self, device_name, volume=5):
        Device.__init__(self, device_name)
        Connectable.__init__(self)
        self.volume = volume

    def set_volume(self, level):
        self.volume = level
        return f"{self.device_name} Speaker's volume is set to :{level}"


class SmartThermostat(Device, Connectable):
    """Derived class combining Device and Connectable"""

    def __init__(self, device_name, temperature=24):
        Device.__init__(self, device_name)
        Connectable.__init__(self)
        self.temperature = temperature

    def set_temperature(self, temp):
        self.temperature = temp
        return f"{self.device_name} temperature is set to : {temp}"


# ------------------------------------------------------------
# Smart Home Manager Class
# ------------------------------------------------------------

class SmartHome:
    """Manages multiple smart devices."""

    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        return f"Successfully added {device} device to smarthome!"

    

    def turn_all_on(self):
        return "\n".join(device.turn_on() for device in self.devices)

    def connect_all_wifi(self):
        return "\n".join(device.connect_wifi() for device in self.devices)
    
    def show_all_devices(self):
        for device in self.devices:
            print(device)


# ------------------------------------------------------------
# DEMONSTRATION AREA
# ------------------------------------------------------------

if __name__ == "__main__":
    # Create sample devices
    light = SmartLight("Living Room Light")
    speaker = SmartSpeaker("Home Speaker")
    thermostat = SmartThermostat("Bedroom Thermostat")

    # Add to SmartHome and perform basic operations
    home = SmartHome()
    home.add_device(light)
    home.add_device(speaker)
    home.add_device(thermostat)

    # Example: turn all devices on and connect Wi-Fi
    
    print(home.turn_all_on())
    print(home.connect_all_wifi())
    
    print("mro", SmartLight.mro())

    # Students can extend this to show all device details, etc.
#This script that advertises a bluetooth low energy beacon for 15 seconds

#importing from libr
from bluetooth.ble import BeaconService #<-- importing a third party module

#Create an instance of the object from the 3rd party class

service = BeaconService()

#start advertizing the signal
service.start_advertising ("11111111-2222-3333-4444-555555555555", 1, 1,1,200)
#setting a 15 timer
time.sleep(15)
#stop it after 15 seconds
service.stop_advertizing
#display Done
print("Done.")
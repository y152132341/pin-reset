# Pin Reset

Pin Reset is an automation script written in Python using the Appium library for resetting the 4 digit PIN number on a Panasonic Viera TV, in case you forgot completely forgot it.

This script will basically try every code possible until it finds the forgotten PIN.

It is meant to go at human speed because that's the speed the testing TV was able to respond to. Going faster would just result on the TV not being process all commands on the sequence.

## Requirements

1. Python3 
1. Appium-Python-Client 1.0.2
1. Android Debug Bridge (adb)
1. Android Device on Debug mode
    1. Must have IR Blaster
    1. USB cable
    1. [AnyMote Universal Remote](https://play.google.com/store/apps/details?id=com.remotefairy4&hl=en_US&gl=US) app installed
    1. if `platformVersion` is not `7` you will need to edit the config file.  


## Usage

```
$ python3 brute_force_pin_reset.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
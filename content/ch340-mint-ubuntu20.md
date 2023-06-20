Title: You must manually install CH340 driver on Mint 21.1/Ubuntu 22.04 
Date: 2023-06-20 14:1
Category: Embeded
Tags: Embeded

Most linux have built in driver for ch340, except for Mint 21.1/Ubuntu 22.04.

## Install Driver 

Go to [https://github.com/juliagoda/CH341SER](https://github.com/juliagoda/CH341SER), and follow the instruction. Basically all you need to do is to clone the repo and run make and make load. You might want to sudo them if you get permission denied.

![embeded_man](./images/embeded_man.png)

## /dev/ttyUSB0
In order to make /dev/ttyUSB0 accesible, you have to `sudo apt autoremove brltty`.

## Set proper permission to `/dev/ttyUSB0`
Depending on your root permissions, you might want to run `sudo chmod a+rw /dev/ttyUSB0`.

## Load kernel module at boostrap

Copy kernel module to the drivers directory.

`$ sudo cp ch34x.ko /lib/modules/$(uname -r)/kernel/drivers//usb/serial/`

Add the simple name of module to the file /etc/modules. You can edit the file or just append to it as shown here.

`$ echo 'ch34x' | sudo tee -a /etc/modules`

Update the list of module dependencies.

`$ sudo depmod`

Reboot the computer and voila, it worked.



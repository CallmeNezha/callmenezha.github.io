Title: You must manually install CH340 driver on Mint 21.1/Ubuntu 22.04 
Date: 2023-06-20 14:1
Category: Embeded
Tags: Embeded

Most linux have built in driver for ch340, except for Mint 21.1/Ubuntu 22.04.

## Install Driver 

Go to https://github.com/juliagoda/CH341SER, and follow the instruction. Basically all you need to do is to clone the repo and run make and make load. You might want to sudo them if you get permission denied.

![embeded_man](./images/embeded_man.png)
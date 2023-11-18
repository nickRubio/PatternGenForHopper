# Patterning Hopper Addresses for Frida

## Purpose

I wrote this little helper script to assist in creating patterns for use in Frida's Memory Scanning APIs to assist in further script writing. The upsides to generating patterns this way mainly is it's a time saver, in addition to guaranteeing that our pattern will be correct and typo free. This can save a lot of time with trouble shooting. 

A note about this script to be aware of if you choose to use it is that by default I am only doing little endian pattern output. If for some reason you need big endian, you need to change the `hex_encoding_of_current_instruction = hex(doc.readUInt32LE(current_instruction_address))[2:]
` to use the `readUInt32BE()` function instead. Down the road I might add some functionality to specify this if it comes up more but currently all my use cases are LE focused. 

## How to "install" to Hopper

1. Pull this repo down:

```
$ git clone <repo name>
```

2. Open/Navigate to Hopper.

3. In the top bar which appears when Hopper is open, select "Scripts".

![SS1](https://github.com/nickRubio/PatternGenForHopper/assets/124838061/95212fb0-c878-4e1e-b22e-ad2547b39365)

4. Select the "Open Script Editor" option. 

![SS2](https://github.com/nickRubio/PatternGenForHopper/assets/124838061/4b9c6c07-328a-4dfc-8cc1-55755a5448be)

5. Press the + button on the bottom left of the new window.

![SS3](https://github.com/nickRubio/PatternGenForHopper/assets/124838061/575e3e7e-7ec4-4dd4-8c70-1426b92f4df9)

6. Copy the contents of the PatternGen.py script into a new script file here.

![SS4](https://github.com/nickRubio/PatternGenForHopper/assets/124838061/fab8a8a2-a0f1-46e3-b0cf-e570e113323b)

7. Close the script editor, select the "Scripts" drop down again and observe the hot key for PatternGen. (Control + CMD + #)

![SS5](https://github.com/nickRubio/PatternGenForHopper/assets/124838061/321e2714-acf7-4f11-a70a-30f4d4149fd5)


## How to use

1. In an open project place your cursor at the address which will be the target address.

2. Press the script hotkey buttons, it will reload the Assembly View and place a new label "target" at the address selected.

![SS6](https://github.com/nickRubio/PatternGenForHopper/assets/124838061/dc40556c-d1f2-4ded-a57b-925133d53b7e)

3. Select a range of addresses now for which you would like a pattern generated, including your target address. Press the script hotkey buttons again. Observe in the Hopper log that a pattern was emitted. Copy and use in your Frida script. 

![SS7](https://github.com/nickRubio/PatternGenForHopper/assets/124838061/4ae1f5f2-02a3-4ed0-9f28-8146f5775b22)

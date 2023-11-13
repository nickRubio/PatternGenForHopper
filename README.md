# Patterning Hopper Addresses for Frida

## Purpose

I wrote this little helper script to assist in creating patterns for use in Frida's Memory Scanning APIs to assist in further script writing. The upsides to generating patterns this way mainly is a time saver, in addition to guaranteeing that our pattern will be correct and typo free. This can save a lot of time with trouble shooting. 

A note about this script to be aware of if you choose to use it is that by default I am only doing little endian pattern output. If for some reason you need big endian, you need to change the `			hex_encoding_of_current_instruction = hex(doc.readUInt32LE(current_instruction_address))[2:]
` to use the `readUInt32BE()` function instead. Down the road I might add some functionality to specify this if it comes up more but currently all my use cases are LE focused. 

## How to "install" to Hopper

1. Pull this repo down:

```
$ git clone <repo name>
```

2. Open/Navigate to Hopper.

3. In the top bar which appears when Hopper is open, select "Scripts".

<img src="data:image/png;base64,"/>

4. Select the "Open Script Editor" option. Press the + button on the bottom left

<img src="data:image/png;base64,"/>

5. Copy the contents of the PatternGen.py script into a new script file here.

<img src="data:image/png;base64,"/>

6. Close the script editor, select the "Scripts" drop down again and observe the hot key for PatternGen. (Control + CMD + #)

<img src="data:image/png;base64,"/>


## How to use

1. In an open project place your cursor at the address which will be the target address.

2. Press the script hotkey buttons, it will reload the Assembly View and place a new label "target" at the address selected.

<img src="data:image/png;base64,"/>

3. Select a range of addresses now for which you would like a pattern generated, including your target address. Press the script hotkey buttons again. Observe in the Hopper log that a pattern was emitted. Copy and use in your Frida script. 

<img src="data:image/png;base64,"/>
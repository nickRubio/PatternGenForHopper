# Setting a variable for interacting with our current hopper document
doc = Document.getCurrentDocument()

# Get our selection from the assembly view
instruction_selection_list = doc.getRawSelectedLines()
sanitized_instruction_list = []

for instruction in instruction_selection_list:
	if instruction[:16].isspace() or not instruction[:16]:
		continue
	else:
		sanitized_instruction_list.append(instruction)

# Some error checking to see if our selection contains non-valid addresses
if (sanitized_instruction_list[0][:16].isspace() or not sanitized_instruction_list[0][:16])or\
	 (sanitized_instruction_list[-1][:16].isspace() or not sanitized_instruction_list[-1][:16]):
	doc.log("The current selection is not correct, please select a proper address range and try again.")

# Select only a single address if we want to mark our current selection as the target.
elif len(sanitized_instruction_list) == 1:
	cursor_at = doc.getCurrentAddress()

	# If our current cursor is already labeled "target" then remove it
	if doc.getNameAtAddress(cursor_at) == "target":
		doc.setNameAtAddress(cursor_at,"")

	# Otherwise label it as our "target"
	else:
		doc.setNameAtAddress(cursor_at,"target")

# Start the part of our script which emits a pattern for use in Frida's memory scanning tooling
else:

	# Convert our addresses from raw strings to addresses which can be used with Hoppers API
	instruction_start = int("0x"+sanitized_instruction_list[0][:16],16)
	instruction_end = int("0x"+sanitized_instruction_list[-1][:16],16)

	doc.log("Starting Instuction addr is " + hex(instruction_start))
	doc.log("Ending Instruction addr is " + hex(instruction_end))

	final_string = ""

	# Loop through our instruction range
	for current_instruction_line in sanitized_instruction_list:

		# Some more error checking here in case my top level if fails for some reason
		if "target" not in current_instruction_line and current_instruction_line:

			# Converts the current instruction line into an address the API can read
			current_instruction_address = int("0x"+current_instruction_line[:16],16)

			# This reads the int value of the current instruction as Little Endian
			# and then hex encodes it, like 0x012345AB, then slices off the 0x part 
			# via the array indexing of [2:]
			hex_encoding_of_current_instruction = hex(doc.readUInt32LE(current_instruction_address))[2:]

			# If the address range contains a "target" label log the offset which we need to
			# provide to Frida so our script will properly hook the correct address
			if doc.getNameAtAddress(current_instruction_address) == "target":
				doc.log("Target address is at offset %s" % (hex(current_instruction_address-instruction_start-0x3)))

			# Loop through our instruction hex char by char 
			# and only record the first two characters, we want
			# ? for every thing besides those two values.
			count = 0
			for hex_char in hex_encoding_of_current_instruction: 
				if count <= 1:
					final_string = final_string + hex_char
				else:
				 	final_string = final_string + "?"
					
				count = count + 1

	# Print out our pattern string to Hopper's console.
	doc.log("Final pattern string is:\n" + final_string[:-6])



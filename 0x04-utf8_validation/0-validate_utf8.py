#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Function to determine if a given data set is a valid UTF-8 encoding.
    Parameters:
    data (list of int): The data set, where each integer represents a byte
    (8 least significant bits).

    Returns:
    bool: True if the data set is a valid UTF-8 encoding, otherwise
    False.
    """

    # Number of bytes in the current UTF-8 character being processed
    remaining_bytes = 0

    # Masks to check the two most significant bits of a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Iterate over each byte in the data
    for byte in data:
        # Mask to check the most significant bit of the byte
        current_mask = 1 << 7  # 10000000

        if remaining_bytes == 0:
            # If we are not currently processing a multi-byte character
            while current_mask & byte:
                # Count how many consecutive 1s are at the start of d byte
                remaining_bytes += 1
                current_mask >>= 1  # Shift the mask to the right

            # If the byte is a single byte character (0xxxxxxx), continue
            if remaining_bytes == 0:
                continue

            # UTF-8 characters can only be 1 to 4 bytes long
            if remaining_bytes == 1 or remaining_bytes > 4:
                return False

        else:
            # If we are in the middle of processing a multi-byte character
            # The byte should be of the form 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrease the number of bytes remaining to be processed for the
        # current character
        remaining_bytes -= 1

    # If all characters were processed correctly, remaining_bytes should be 0
    return remaining_bytes == 0

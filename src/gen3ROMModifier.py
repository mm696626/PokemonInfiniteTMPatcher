def modify_byte_in_file(file_path, offset, old_byte, new_byte):
    try:
        with open(file_path, 'r+b') as file:
            file.seek(offset)
            current_byte = file.read(1)
            if current_byte == bytes([old_byte]):
                file.seek(offset)
                file.write(bytes([new_byte]))
                print(f"Byte at {hex(offset)} replaced from {hex(old_byte)} to {hex(new_byte)}.")
    except Exception as e:
        print(f"Error: {e}")
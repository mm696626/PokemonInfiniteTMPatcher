def modify_byte_in_file(file_path, offset, old_byte, new_byte):
    try:
        with open(file_path, 'r+b') as file:
            file.seek(offset)
            current_byte = file.read(1)
            if current_byte == bytes([old_byte]):
                file.seek(offset)
                file.write(bytes([new_byte]))
    except Exception as e:
        print(f"Error: {e}")


def firered_leafgreen_downgrade_modify_bytes(file_data, offset, old_byte, new_byte):
    current_byte = file_data[offset]
    if current_byte == old_byte:
        file_data[offset] = new_byte
    else:
        pass

def firered_leafgreen_downgrade(file_path, differences_file):
    try:
        with open(differences_file, 'r') as diff_file:
            lines = diff_file.readlines()

        with open(file_path, 'rb') as file:
            file_data = bytearray(file.read())

        for line in lines:
            if not line.strip():
                continue

            parts = line.strip().split()
            if len(parts) == 3:
                offset_str, old_byte_str, new_byte_str = parts

                offset = int(offset_str, 16)
                old_byte = int(old_byte_str, 16)
                new_byte = int(new_byte_str, 16)

                firered_leafgreen_downgrade_modify_bytes(file_data, offset, old_byte, new_byte)

        with open(file_path, 'wb') as file:
            file.write(file_data)

    except Exception as e:
        print(f"Error: {e}")


import socket
import os

def send_file(s, file_path):
    file_size = os.path.getsize(file_path)
    s.sendall(f'UPLOAD {file_path} {file_size}'.encode())
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            s.sendall(chunk)
    print(s.recv(1024).decode())  # Receive and print the server response

def get_file(s, file_name):
    s.sendall(f'DOWNLOAD {file_name}'.encode())
    data = s.recv(1024).decode()
    if data.isdigit():
        file_size = int(data)
        with open(f"downloaded_{file_name}", 'wb') as f:
            remaining = file_size
            while remaining > 0:
                chunk = s.recv(min(4096, remaining))
                if not chunk:
                    break
                f.write(chunk)
                remaining -= len(chunk)
        print("File downloaded successfully")
    else:
        print(data)  # If the file does not exist, print the error message from the server

def list_files(s):
    s.sendall('LIST'.encode())
    files = s.recv(1024).decode()
    print("Files on server:", files)

def delete_file(s, file_name):
    s.sendall(f'DELETE {file_name}'.encode())
    response = s.recv(1024).decode()
    print(response)

def main():
    host = '127.0.0.1'
    port = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            action = input("Enter 'upload <file_path>', 'download <file_name>', 'list', 'delete <file_name>', or 'exit': ")
            if action == 'exit':
                break
            if action == 'list':
                list_files(s)
            else:
                command, path = action.split(maxsplit=1)
                if command == 'upload':
                    send_file(s, path)
                elif command == 'download':
                    get_file(s, path)
                elif command == 'delete':
                    delete_file(s, path)

if __name__ == "__main__":
    main()

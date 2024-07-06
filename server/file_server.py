import socket
import os

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            command, *args = data.split()
            if command == 'UPLOAD':
                file_name = args[0]
                file_size = int(args[1])
                with open(file_name, 'wb') as f:
                    remaining = file_size
                    while remaining > 0:
                        chunk = conn.recv(min(4096, remaining))
                        if not chunk:
                            break
                        f.write(chunk)
                        remaining -= len(chunk)
                conn.sendall(b'File uploaded successfully')
            elif command == 'DOWNLOAD':
                file_name = args[0]
                if os.path.isfile(file_name):
                    file_size = os.path.getsize(file_name)
                    conn.sendall(f"{file_size}".encode())
                    with open(file_name, 'rb') as f:
                        chunk = f.read(4096)
                        while chunk:
                            conn.sendall(chunk)
                            chunk = f.read(4096)
                else:
                    conn.sendall(b'File not found')
            elif command == 'LIST':
                files = os.listdir('.')
                conn.sendall(" ".join(files).encode())
            elif command == 'DELETE':
                file_name = args[0]
                if os.path.isfile(file_name):
                    os.remove(file_name)
                    conn.sendall(b'File deleted successfully')
                else:
                    conn.sendall(b'File not found')
            else:
                conn.sendall(b'Invalid command')
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        conn.close()

def main():
    host = '127.0.0.1'
    port = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        while True:
            conn, addr = s.accept()
            handle_client(conn, addr)

if __name__ == "__main__":
    main()

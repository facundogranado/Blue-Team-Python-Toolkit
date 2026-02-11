import sys
from collections import Counter

def parse_log(file_path):
    dts_ips = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()  # Split the line into parts based on whitespace
            if len(parts) < 5:
                continue  # Skip lines that don't have enough parts

            dts_ip = parts[3]  # Assuming the IP address is the 5th element (index 4)
            dts_ips.append(dts_ip)
    return dts_ips



def main():
    if len(sys.argv) != 2:
        print("Usage: python Prueba.py <filename>")
        sys.exit(1)

    log_file = sys.argv[1]
    dts_ips = parse_log(log_file)

    counter = Counter(dts_ips)

    print("DTS IP Address Counts:")
    for ip, count in counter.items():
        print(f"{ip}: {count}")

    print("Analysis complete.")

if __name__ == "__main__":    main()
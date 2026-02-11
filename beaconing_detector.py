import sys
from datetime import datetime
from collections import defaultdict

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
INTERVAL_TOLERANCE = 5  # segundos de margen
MIN_CONNECTIONS = 4     # mínimo para analizar beaconing


def parse_log(file_path):
    connections = defaultdict(list)

    with open(file_path, "r") as f:
        for line in f:
            parts = line.strip().split()

            if len(parts) < 6:
                continue

            timestamp = f"{parts[0]} {parts[1]}"
            src_ip = parts[2]
            dst_ip = parts[3]
            dst_port = parts[4]
            protocol = parts[5]

            if dst_port == "443" and protocol.upper() == "TLS":
                dt = datetime.strptime(timestamp, TIME_FORMAT)
                key = (src_ip, dst_ip)
                connections[key].append(dt)

    return connections


def detect_beaconing(connections):
    alerts = []

    for (src_ip, dst_ip), timestamps in connections.items():
        if len(timestamps) < MIN_CONNECTIONS:
            continue

        timestamps.sort()
        intervals = []

        for i in range(1, len(timestamps)):
            diff = (timestamps[i] - timestamps[i - 1]).seconds
            intervals.append(diff)

        avg_interval = sum(intervals) / len(intervals)

        consistent = all(
            abs(interval - avg_interval) <= INTERVAL_TOLERANCE
            for interval in intervals
        )

        if consistent:
            alerts.append({
                "src_ip": src_ip,
                "dst_ip": dst_ip,
                "connections": len(timestamps),
                "avg_interval": round(avg_interval, 2)
            })

    return alerts


def main():
    if len(sys.argv) != 2:
        print("Uso: python beaconing_detector.py firewall.log")
        sys.exit(1)

    log_file = sys.argv[1]
    connections = parse_log(log_file)
    alerts = detect_beaconing(connections)

    if alerts:
        print("\n Posible TLS Beaconing Detectado:\n")
        for alert in alerts:
            print(f"Host interno: {alert['src_ip']}")
            print(f"Destino externo: {alert['dst_ip']}")
            print(f"Conexiones: {alert['connections']}")
            print(f"Intervalo promedio: {alert['avg_interval']} segundos")
            print("-" * 40)
    else:
        print("No se detectaron patrones claros de beaconing.")


if __name__ == "__main__":
    main()





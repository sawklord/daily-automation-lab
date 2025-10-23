#!/usr/bin/env python3
"""
port_check.py
-------------
Quick utility to check if specific network ports are open on a host.
Useful for verifying firewall rules or server availability.
"""

import socket
import argparse

def check_port(host, port, timeout=2):
    """Check if a TCP port is open."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((host, port))
            return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False

def main():
    parser = argparse.ArgumentParser(description="Check open TCP ports on a host.")
    parser.add_argument("host", help="Hostname or IP address to scan")
    parser.add_argument(
        "-p", "--ports", nargs="+", type=int, default=[22, 80, 443],
        help="Ports to check (default: 22 80 443)"
    )
    args = parser.parse_args()

    print(f"🔍 Checking ports on {args.host}...\n")
    for port in args.ports:
        status = "OPEN ✅" if check_port(args.host, port) else "CLOSED ❌"
        print(f"{args.host}:{port:<5} {status}")

if __name__ == "__main__":
    main()

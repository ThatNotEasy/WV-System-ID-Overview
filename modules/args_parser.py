import argparse

def args_parser():
    parser = argparse.ArgumentParser(description="Add a new Widevine device entry.")
    parser.add_argument('-b', '--brand', type=str, required=True, help='Device brand/manufacturer')
    parser.add_argument('-m', '--model', type=str, required=True, help='Device model name')
    parser.add_argument('-si', '--system-id', type=str, required=True, help='Widevine system ID')
    parser.add_argument('-sl', '--security-level', type=str, choices=['1', '2', '3'], required=True, help='Security level (1, 2, or 3)')
    return parser.parse_args()
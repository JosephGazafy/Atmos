import argparse
import sys
from atmos.core import calculate_pressure

def main():
    # Setup the argument parser for a professional CLI feel
    parser = argparse.ArgumentParser(
        description="Atmos: Peerless Atmospheric Calculations for Termux",
        epilog="Example: atmos --altitude 1000"
    )
    
    # Add an argument for altitude
    parser.add_argument(
        "-a", "--altitude", 
        type=float, 
        help="Altitude in meters above sea level",
        required=True
    )

    # Parse arguments
    args = parser.parse_args()

    try:
        # Execute the core logic
        pressure = calculate_pressure(args.altitude)
        
        # Finer output formatting
        print(f"\n--- Atmos Results ---")
        print(f"Altitude: {args.altitude:>10} m")
        print(f"Pressure: {pressure:>10.2f} Pa")
        print(f"---------------------\n")
        
    except Exception as e:
        print(f"Error in calculation: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()


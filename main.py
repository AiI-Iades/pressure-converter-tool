import argparse

def convert_pressure(value, from_unit, to_unit):
    # Conversion logic for pressure units (Pa, atm, bar, psi)
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert between pressure units')
    parser.add_argument('value', type=float, help='Value to convert')
    parser.add_argument('--from', required=True, choices=['Pa', 'atm', 'bar', 'psi'], help='Source unit')
    parser.add_argument('--to', required=True, choices=['Pa', 'atm', 'bar', 'psi'], help='Target unit')
    args = parser.parse_args()
    result = convert_pressure(args.value, args.from, args.to)
    print(f'{args.value} {args.from} = {result:.4f} {args.to}')
"""Lightyear Frontier Desktop — A local helper for Lightyear Frontier homestead folders, mech notes, and valley photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='lightyear_frontier_desktop',
        description='A local helper for Lightyear Frontier homestead folders, mech notes, and valley photos.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Lightyear Frontier Desktop')
    print('Keep the homestead on disk before a frontier patch.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

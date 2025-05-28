#!/usr/bin/python3

"""output a ICS file for holidays in a given region"""

import argparse
from datetime import date
import logging
import os
import os.path

from ..registry import registry


args = argparse.Namespace(subregions=True)


def get_region_keys():
    """convert get_calendars into a generator so our usage reflects the --subregions argument"""
    yield from registry.get_calendars(include_subregions=args.subregions).keys()


def main():
    logging.basicConfig(level="INFO", format="%(levelname)s: %(message)s")

    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-r",
        "--region-code",
        choices=get_region_keys(),
        metavar="REGION",
        help="output holidays calendar for REGION to stdout",
    )
    group.add_argument(
        "--all-regions",
        action="store_true",
    )
    group.add_argument(
        "--list", action="store_true", help="list all available region codes"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--directory",
        "-d",
        help="store generated calendars in DIRECTORY, default: %(default)s",
    )
    group.add_argument(
        "--file",
        "-f",
        dest="path",
        type=argparse.FileType('w'),
        help="store generated calendars in FILE, default: standard output",
    )
    parser.add_argument(
        "--subregions",
        default=args.subregions,
        action=argparse.BooleanOptionalAction,
        help="include ISO 3166-2 subregions, default is ISO 3166-1 countries",
    )
    parser.add_argument(
        "--start-year",
        help="start year, default: %(default)s",
        default=date.today().year,
    )
    parser.add_argument(
        "--end-year",
        help="end year (inclusive), default: %(default)s",
        default=date.today().year,
    )
    parser.parse_args(namespace=args)

    all_regions = registry.get_calendars(include_subregions=args.subregions)
    if args.list:
        for l, c in sorted(all_regions.items()):
            print(l, c.name)
        return

    if args.region_code:
        regions = { args.region_code: all_regions[args.region_code] }
    else:
        assert args.all_regions, "logic error: we *are* doing all regions here"
        regions = all_regions

    if args.directory:
        os.makedirs(args.directory, exist_ok=True)

    for region, cal in regions.items():
        try:
            ical_blob = cal().export_to_ical(period=[args.start_year, args.end_year])
        except Exception as e:
            logging.warning("failed to generate calendar for region %s: %s", region, e)
            continue
        if args.directory:
            with open(os.path.join(args.directory, region + ".ics"), "w") as fp:
                print(ical_blob, file=fp)
        else:
            print(ical_blob, file=args.path)


if __name__ == "__main__":
    main()

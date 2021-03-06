import argparse
import ConfigParser
import datetime
import os
import pymongo
import sys
import scripts.tools as tools
from scripts.settings import settings
from scripts.settings import alternative_keys


api_files_root_path = '/home/kgontarz/prywatne/projekt_dyplomowy/data/test_data/'

def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--country", required=True, action="store")
    parser.add_argument("--date", required=True, type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d'),
                        help="proper format is YYYY-MM-DD")
    parser.add_argument("--periodType", required=True)
    parser.add_argument("--gem_id", default=None)
    parser.add_argument("--override", action='store_true')
    return parser

if __name__ == '__main__':
    parser = init_args()
    arguments = parser.parse_args()

    year = arguments.date.strftime('%Y')
    month = arguments.date.strftime('%m')
    day = arguments.date.strftime('%d')
    instance_type = settings['instance_type']
    current_path = os.path.join(api_files_root_path, instance_type,
                                arguments.country, arguments.periodType, year, month, day)

    gem_id = arguments.gem_id

    main_key = {"gem_id": gem_id, "country": arguments.country, "date": arguments.date,
                "period_type": arguments.periodType}
    files_list = tools.get_full_paths(current_path, settings['files_to_db_update'])
    if tools.is_files_exists(files_list):
        print "all files exists"
        for file_path in files_list:
            file_name = os.path.basename(file_path)
            data_to_insert = tools.csv_to_list_of_dict(file_path, main_key)
            tools.insert_many(file_name, data_to_insert, instance_type, override=arguments.override, key=main_key)
            print "data inserted", file_name


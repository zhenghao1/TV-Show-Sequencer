#!/usr/bin/env python

#Date Modified:   Today
#Author:  Huang Zhenghao
#Email:   zhenghao1@me.com

import optparse
import os

DESC = "This script renames TV shows by providing: show, season, episode,"

USAGE = "Usage: %prog <options> FILE1 (FILE2 FILE3 FILE 4...)"

VERSION = "%prog version 1.0"

def run_options_parser():
    parser = optparse.OptionParser(description=DESC,
                                   usage=USAGE,
                                   version=VERSION)
    parser.add_option('-s', '--show',
            help='Name of the show that you want to rename.  Please use quotes to wrap the show name.',
            dest='show',
            action='store',
            type='string')
    parser.add_option('-n', '--season',
            help='Which season does the show belong?  This is a number',
            dest='season',
            action='store',
            type='string')
    parser.add_option('-e', '--episode',
            help='Which episode does the first FILE belong to? This is a number',
            dest='episode',
            action='store',
            type='int')
    (options, args) = parser.parse_args()

    if len(args) < 1:
        parser.error("You must have at least 1 FILE specified")
        parser.print_help()
        exit(-1)
    return options, args

def convert_episode_number(episode, increment=False):
    """
    If given episode is "2", then the output has to be:
        02
    However, if episode was "14" then the output will just be:
        14
    """
    if increment and type(episode) == int:
        episode = episode + 1
    if len(episode.__str__()) == 1:
        return '0' + episode.__str__()
    else:
        return episode.__str__()e

def main():
    options, args = run_options_parser()
    show = options.show.strip().title()
    season = options.season.strip()
    episode = convert_episode_number(options.episode)

    print options.show
    print options.season
    print options.episode
    print '-------------------'
    print args

if __name__ == '__main__':
    main()

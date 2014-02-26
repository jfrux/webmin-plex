#!/usr/bin/perl
#
#    Plex Media Server Webmin Module
#    Copyright (C) 2014 by Joshua F. Rountree
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    This module inherited from the Webmin Module Template 0.79.1 by tn

do '../web-lib.pl';
$|=1;
&init_config("plexmediaserver");

%access=&get_module_acl;


&header($text{'index_title'}, "", "intro", 1, 1, undef,
        "Written by<BR><A HREF=mailto:joshua@swodev.com>Joshua F. Rountree</A><BR><A HREF=http://www.joshuairl.com/>Home://page</A>");


print "<hr>\n";
## Insert Output code here

&footer("/", $text{'index'});
# uses the index entry in /lang/en



## if subroutines are not in an extra file put them here


### END of index.cgi ###.

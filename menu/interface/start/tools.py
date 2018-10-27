#!/usr/bin/python
#
# GitHub:   https://github.com/Admin9705/PlexGuide.com-The-Awesome-Plex-Server
# Author:   Admin9705
# URL:      https://plexguide.com
#
# PlexGuide Copyright (C) 2018 PlexGuide.com
# Licensed under GNU General Public License v3.0 GPL-3 (in short)
#
#   You may copy, distribute and modify the software as long as you track
#   changes/dates in source files. Any modifications to our software
#   including (via compiler) GPL-licensed code must also be made available
#   under the GPL along with build & install instructions.
#
#################################################################################
# https://pypi.org/project/console-menu/

# Import for Menu Interface
from consolemenu import *
from consolemenu.format import *
from consolemenu.items import *

# Import for Bash Ending
from subprocess import call

def main():
    # Change some menu formatting
    menu_format = MenuFormatBuilder().set_border_style_type(MenuBorderStyleType.HEAVY_BORDER)\
        .set_prompt("SELECT>")\
        .set_title_align('center')\
        .set_subtitle_align('left')\
        .set_left_margin(2)\
        .set_right_margin(2)\
        .show_header_bottom_border(True)

    menu = ConsoleMenu(edition + " - " + pgversion, "Server ID: " + serverid + " | Domain: " + domain, formatter=menu_format)
    item1 = MenuItem("Item 1", menu)

    # A CommandItem runs a console command
    command_item1 = CommandItem("Backup & Restore", "bash /opt/plexguide/roles/b-control/scripts/main.sh")
    command_item2 = CommandItem("Deploy GCE Feeder Instance", "bash /opt/plexguide/menu/interface/traefik/main.sh")
    command_item3 = CommandItem("PGTrak - Fills Up Radarr & Sonarr", "bash /opt/plexguide/roles/menu-transport/scripts/main.sh")
    command_item4 = CommandItem("Server VPN Service Installer", "bash /opt/plexguide/roles/menu-ports/scripts/main.sh")
    command_item5 = CommandItem("System & Network Auditor", "bash /opt/plexguide/roles/menu-appguard/scripts/main.sh")
    command_item6 = CommandItem("TroubleShoot - Pre & UnInstaller", "echo 'tshoot' > /var/plexguide/type.choice && bash /opt/plexguide/menu/core/scripts/main.sh")
    command_item7 = CommandItem("Backup & Restore", "bash /opt/plexguide/roles/b-control/scripts/main.sh")
    # Once we're done creating them, we just add the items to the menu
    menu.append_item(command_item1)
    menu.append_item(command_item2)
    menu.append_item(command_item3)
    menu.append_item(command_item4)
    menu.append_item(command_item5)
    # Finally, we call show to show the menu and allow the user to interact
    menu.show()

if __name__ == "__main__":
    main()
# When User Exits Menu; Displays PG Ending
rc = call("/opt/plexguide/roles/ending/ending.sh", shell=True)

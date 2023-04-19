#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.colors import colors
import os
def banner():

    picture =  """
############################
############################
## ########      ######## ##
## #####            ##### ##
## ###                ### ##
## #                    # ##
## ## #####      ##### ## ##
## ###   ####  ###    ### ##
## #       ##  ##       # ##
## # #      #  #      # # ##
##   # ####      #### #   ##
##   # #### #  # #### #   ##
##    #     #  #     #    ##
##          #  #          ##
##   #     #    #     #   ##
##  ##     #    #     ##  ##
## ###   ####  ####   ### ##
## ###################### ##
##  ####################  ##
## #  ################  # ##
## ##     #########    ## ##
## ##      ######      ## ##
## ###                ### ##
## ####              #### ##
## #####            ##### ##
############################
############################
Author: @MrTuxx
DISCLAIMER: Use for educational/testing purposes and at your own risk! The devs hold no responsibility for your actions, so don't be an asshole, skid.
"""

    pic = picture.split("\n")
    for line in pic:
        centered = line.center(os.get_terminal_size().columns)
        print(colors.BOLD + centered + colors.end)

import random
import re

from errbot import BotPlugin, re_botcmd


class Ship_it(BotPlugin):
    """
    Show motivational ship it squirrel images.
    """

    # start ignoring LineLengthBear PyCodeStyleBear
    IMAGES = [
        'https://i.imgur.com/DPVM1.png',
        'https://d2f8dzk2mhcqts.cloudfront.net/0772_PEW_Roundup/09_Squirrel.jpg',
        'https://www.cybersalt.org/images/funnypictures/s/supersquirrel.jpg',
        'https://www.zmescience.com/wp-content/uploads/2010/09/squirrel.jpg',
        'https://qph.ec.quoracdn.net/main-qimg-c8781a4bb1f17e330b50cb35f851da05-c',
        'https://shipitsquirrel.github.io/images/squirrel.png',
        'https://1.bp.blogspot.com/_v0neUj-VDa4/TFBEbqFQcII/AAAAAAAAFBU/E8kPNmF1h1E/s640/squirrelbacca-thumb.jpg',
    ]
    # stop ignoring LineLengthBear PyCodeStyleBear

    @re_botcmd(pattern=r'ship\s*it',
               re_cmd_name_help='ship it',
               flags=re.IGNORECASE)
    def ship_it(self, msg, match):
        """
        Show motivational ship it squirrel images.
        """
        return '![ship it!]({})'.format(
            self.IMAGES[random.randint(0, len(self.IMAGES) - 1)]
        )

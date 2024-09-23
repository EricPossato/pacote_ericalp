#!/usr/bin/env python3
from dev_aberto import hello
import babel.dates as dates
from datetime import datetime
from datetime import date

import gettext
gettext.bindtextdomain('cli', 'locale')
gettext.textdomain('cli')
_ = gettext.gettext

if __name__ == '__main__':
    try:
        data, name = hello()
        data = datetime.strptime(data, '%Y-%m-%dT%H:%M:%S%z')
    except:
        data, name = date.today(), '???'
    
    data = dates.format_datetime(data)
    print(_('Último commit feito em: {} por {}').format(data, name))

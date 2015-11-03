#! /usr/bin/env python3

import funtool.api
import sys

if sys.argv[1:]:
    for arg in sys.argv[1:]:
        funtool.api.run_analysis(arg)
else:
    funtool.api.run_analyses()

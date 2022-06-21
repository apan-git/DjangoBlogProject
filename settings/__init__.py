#!/usr/bin/env python
# -*- coding: utf-8 -*-

# DateTime:2022/06/20 18:42:28

import os


if os.getenv("ENV"):
    from settings.pro import *
else:
    from settings.dev import *



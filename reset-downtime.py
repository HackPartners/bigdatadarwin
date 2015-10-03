#!/usr/bin/env python3

import pickle
import datetime

if __name__ == "__main__":
    with open("downtime.pickle", "wb") as f:
        pickle.dump(datetime.datetime.now(), f)


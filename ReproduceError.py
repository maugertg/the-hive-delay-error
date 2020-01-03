#!/usr/bin/env python
import time
import requests

from simplejson.errors import JSONDecodeError
from cortexutils.analyzer import Analyzer


class DelayError(Analyzer):
    def __init__(self):
        Analyzer.__init__(self)

    def run(self):

        # Delay value of 420 causes The Hive to fail to retrieve the report from Cortex 
        delay = 420

        results = {str(delay):'info'}

        time.sleep(delay)

        self.report(results)

    def summary(self, raw):
        taxonomies = []
        namespace = "Error"
        predicate = "Reproduce"

        for value, level in raw.items():
            taxonomies.append(self.build_taxonomy(level, namespace, predicate, value))

        return {"taxonomies": taxonomies}

if __name__ == '__main__':
    DelayError().run()

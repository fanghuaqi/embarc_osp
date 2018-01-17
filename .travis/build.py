#! /usr/bin/env python
import json
import os
import sys

example = {"arc_feature_cache":"baremetal/arc_feature/cache",
            "arc_feature_timer_interrupt":"baremetal/arc_feature/timer_interrupt"}

result = {"arc_feature_cache":0,
            "arc_feature_timer_interrupt":0}
folder = ".test"

if __name__ == '__main__':
print(example)
for (k,v) in example.items():
    print("example[%s]=" %k,v)
    pathin = "../example/"+v
    os.chdir(pathin)
    os.system('make distclean')
    if os.system('make TOOLCHAIN=gnu -k') != 0:
        result[k] = 1
    pathout = pathin.count('/')*"../"+".test"
    os.chdir(pathout)
print(result)

for (k,v) in result.items():
    if v == 1:
        sys.exit(1)

sys.exit(0)
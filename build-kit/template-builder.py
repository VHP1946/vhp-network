import yaml
import sys

from anyyml import Loader, Dumper, Tagged, Pairs

print('File to Read ->>>>',sys.argv[1])
print('File to Write ->>>>',sys.argv[2])

with open('../staging/vhp-net-launch.yml','r') as f:
    data = yaml.load(f,Loader=Loader)

print('Build Data >>>>>',data)

with open('../staging/builds/new-build.yml','w+') as wf:
    write = yaml.dump(data,wf,Dumper = Dumper)

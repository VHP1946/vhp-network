import yaml
import os
import sys

print('File to Read ->>>>',sys.argv[1])
print('File to Write ->>>>',sys.argv[2])

class Loader(yaml.SafeLoader):

    def __init__(self, stream):

        self._root = os.path.split(stream.name)[0]

        super(Loader, self).__init__(stream)

    def include(self, node):

        filename = os.path.join(self._root, self.construct_scalar(node))

        with open(filename, 'r') as f:
            return yaml.load(f, Loader)


Loader.add_constructor('!include', Loader.include)

with open('../staging/testfile.yml','r') as f:
    data = yaml.load(f,Loader)

print('Build Data >>>>>',data)

with open('../staging/builds/new-build.yml','w+') as wf:
    write = yaml.dump(data,wf)

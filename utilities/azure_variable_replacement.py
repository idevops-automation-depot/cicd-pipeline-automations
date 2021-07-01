#!/usr/bin/env python
import os.path

env_vars = dict(os.environ)

#f_path = "C:/Users/Erran/PycharmProjects/deployment.template.yml"
f_path = os.environ["APPLICATION_PATH"] + "/manifests/deployment.template.yml"
f = open(f_path, 'r')
new_lines = []
for line in f:
    for json_var in env_vars:
        json_with_extra_stuff = "-=" + json_var + "=-"
        line = line.replace(json_with_extra_stuff, env_vars[json_var])
    new_lines.append(line)
new_lines = "".join(new_lines)
#f_path = "C:/Users/Erran/PycharmProjects/deployment.yml"
f_path = os.environ["APPLICATION_PATH"] + "/manifests/deployment.yml"
test = open(f_path, "w")
test.write(new_lines)
test.close()
#!/usr/bin/env python
# This scripts sets default entry in grub.cfg to the entry specified by name.
# It works only for grub2 (should work with Ubuntu 10.04)
# Backup of config file is created as grub.cfg.bak
import re
conf_file='/boot/grub/grub.cfg'
default_menuentry='Microsoft Windows XP'  #should match begining of text in cfg

f = open(conf_file, 'r')
data = f.read()
f.close()
p = '\s*set\s*default\s*=\D*(\d)\D*'
default = re.search(p, data).groups()
if not default:
  print 'not found default'
  exit(1)
else:
  default=default[0]

count=0
for i in re.findall('\s*menuentry\s"(.*)"', data):
  if i.find(default_menuentry) > -1:
    break
  count += 1
if count == len(re.findall('\s*menuentry\s"(.*)"', data)):
  print 'default menuentry not found'
  exit(1)
if int(count) != int(default):
  g = open(conf_file+'.bak', 'w')
  g.write(data)
  g.close()
  p = '(\s*set\s*default\s*=\D*)(\d)(\D*)'
  g = open(conf_file, 'w')
  g.write(re.sub(p, '\g<1>%s\g<3>' % str(count), data))
  g.close()

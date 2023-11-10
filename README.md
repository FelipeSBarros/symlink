# symlink

```python
python3 exemplo_erro.py
#texto:  config de nvim
#Traceback (most recent call last):
#  File "/home/felipe/repos/symlink/exemplo_erro.py", line 10, in <module>
#    dest_config.symlink_to(original)
#  File "/usr/lib/python3.10/pathlib.py", line 1255, in symlink_to
#    self._accessor.symlink(target, self, target_is_directory)
#FileNotFoundError: [Errno 2] No such file or directory: 'original.txt' -> '~/.config/linked.txt'
```
Contudo, ao executar:
```
ln -s original.txt ~/.config/linked.txt
```
o link é criado sem problemas.

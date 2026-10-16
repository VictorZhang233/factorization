import sys, os, runpy
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
script = sys.argv[1]
sys.argv = [script]
runpy.run_path(script, run_name='__main__')

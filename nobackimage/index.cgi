#!/home/xs255212/anaconda3/bin/python　    
# coding: utf-8
import sys, os
import cgitb  #cgitbでトレースバックを生成する
cgitb.enable(display=0, logdir='.') #cgitbでトレースバックをカレントディレクトリにファイルとして生成する
sys.path.insert(0, '/home/xs255212/.local/shere/virtualenvs/nobackimage.com/bin')
os.environ['DJANGO_SETTINGS_MODULE'] = 'nobackimage.settings'    #settingsの読み込み先を記載
from wsgiref.handlers import CGIHandler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
CGIHandler().run(application)
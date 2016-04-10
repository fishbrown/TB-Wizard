import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,base64,sys,xbmcvfs
from addon.common.addon import Addon
import urllib2,urllib
import extract
import downloader
import re
import time
addon_id = 'plugin.video.tdbadvanced'
ADDON = xbmcaddon.Addon(id=addon_id)
AddonID='plugin.video.tdbadvanced'
USERDATA     =  xbmc.translatePath(os.path.join('special://home/userdata',''))
my_addon = xbmcaddon.Addon()
dp = xbmcgui.DialogProgress()
# Addon starts here


try: addon_handle=int(sys.argv[1])
except: addon_handle=0
try: addon=Addon(addon_id,sys.argv)
except: addon=Addon(addon_id,0)





def KillKodi():
	if xbmc.getCondVisibility('system.platform.osx'): # OSX
			print "############   try osx force close  #################"
			try: os.system('killall -9 XBMC')
			except: pass
			try: os.system('killall -9 Kodi')
			except: pass
			dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
	elif xbmc.getCondVisibility('system.platform.linux'): #Linux
			print "############   try linux force close  #################"
			try: os.system('killall XBMC')
			except: pass
			try: os.system('killall Kodi')
			except: pass
			try: os.system('killall -9 xbmc.bin')
			except: pass
			try: os.system('killall -9 kodi.bin')
			except: pass
			dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
	elif xbmc.getCondVisibility('system.platform.android'): # Android  
			print "############   try android force close  #################"
			try: os.system('adb shell am force-stop org.xbmc.kodi')
			except: pass
			try: os.system('adb shell am force-stop org.kodi')
			except: pass
			try: os.system('adb shell am force-stop org.xbmc.xbmc')
			except: pass
			try: os.system('adb shell am force-stop org.xbmc')
			except: pass        
			dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "Your system has been detected as Android, you ", "[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.","Pulling the power cable is the simplest method to force close.")
	elif xbmc.getCondVisibility('system.platform.windows'): # Windows
			print "############   try windows force close  #################"
			try:
				os.system('@ECHO off')
				os.system('tskill XBMC.exe')
			except: pass
			try:
				os.system('@ECHO off')
				os.system('tskill Kodi.exe')
			except: pass
			try:
				os.system('@ECHO off')
				os.system('TASKKILL /im Kodi.exe /f')
			except: pass
			try:
				os.system('@ECHO off')
				os.system('TASKKILL /im XBMC.exe /f')
			except: pass
			dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.","Use task manager and NOT ALT F4")
	else: #ATV
			print "############   try atv force close  #################"
			try: os.system('killall AppleTV')
			except: pass
			print "############   try raspbmc force close  #################" #OSMC / Raspbmc
			try: os.system('sudo initctl stop kodi')
			except: pass
			try: os.system('sudo initctl stop xbmc')
			except: pass
			dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu.","Your platform could not be detected so just pull the power cable.")

import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,base64,sys,xbmcvfs
from addon.common.addon import Addon
import urllib2,urllib
import extract
import downloader
import re
import time
import common as Common
USERDATA     =  xbmc.translatePath(os.path.join('special://home/userdata',''))
CHECKVERSION  =  os.path.join(USERDATA,'version.txt')
my_addon = xbmcaddon.Addon()
dp = xbmcgui.DialogProgress()
checkver=my_addon.getSetting('checkupdates')
dialog = xbmcgui.Dialog()
if not os.path.exists(CHECKVERSION):
		file = open(CHECKVERSION,'w') 
		file.write("<version>0</version>")
		file.close()
checkurl = "https://archive.org/download/wizard_rel_201604/version_check.txt"
vers = open(CHECKVERSION, "r")
regex = re.compile(r'<build>(.+?)</build><version>(.+?)</version>')
for line in vers:
	if checkver!='false':
		currversion = regex.findall(line)
		for build,vernumber in currversion:
			if vernumber > 0:
				req = urllib2.Request(checkurl)
				req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
				response = urllib2.urlopen(req)
				link=response.read()
				response.close()
				match = re.compile('<build>'+build+'</build><version>(.+?)</version><fresh>(.+?)</fresh>').findall(link)
				for newversion,fresh in match:
					if newversion > vernumber:
						choice = xbmcgui.Dialog().yesno("NEW UPDATE AVAILABLE", 'Found a new update for the Build', build + " ver: "+newversion, 'Do you want to install it now?', yeslabel='YES',nolabel='NO')
						if choice == 1: 
							if fresh =='false': # TRUE
								updateurl = "https://archive.org/download/wizard_rel_201604/update_wiz.txt"
								req = urllib2.Request(updateurl)
								req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
								response = urllib2.urlopen(req)
								link=response.read()
								response.close()
								match = re.compile('<build>'+build+'</build><url>(.+?)</url>').findall(link)
								for url in match:
								
									path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
									name = "build"
									dp = xbmcgui.DialogProgress()

									dp.create("[COLOR=orange][B]Thomas Begley[/B][/COLOR][COLOR=white] Wizard[/COLOR]","Downloading ",'', 'Please Wait')
									lib=os.path.join(path, name+'.zip')
									try:
									   os.remove(lib)
									except:
									   pass
									
									downloader.download(url, lib, dp)
									addonfolder = xbmc.translatePath(os.path.join('special://','home'))
									time.sleep(2)
									dp.update(0,"", "Extracting Zip Please Wait")
									print '======================================='
									print addonfolder
									print '======================================='
									extract.all(lib,addonfolder,dp)
									dialog = xbmcgui.Dialog()
									dialog.ok("[COLOR=orange][B]Thomas Begley[/B][/COLOR][COLOR=white] Wizard[/COLOR]", "To save changes you now need to force close Kodi, Press OK to force close Kodi")
									
									Common.KillKodi()
									
							else:
								dialog.ok('[COLOR=orange][B]Thomas Begley[/B][/COLOR][COLOR=white] Wizard[/COLOR]','A FRESH START is required for the update... Run the WIPE option in the NEXT WINDOW then INSTALL the new build version','','')
								xbmc.executebuiltin("RunAddon(plugin.video.tdbwizard)")
							
								
## ################################################## ##
## ################################################## ##

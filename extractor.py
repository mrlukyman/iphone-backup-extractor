import os
from pathlib import Path
from iOSbackup import iOSbackup
from simple_term_menu import TerminalMenu
dynamicPath = Path('') # change this to your desired path

destination = str(dynamicPath)
backupName = ''

def slectBackup():
  backups = iOSbackup.getDeviceList()
  options = []
  udids = []
  if backups:
    global backupName
    for i in range(len(backups)):
      if backups[i] == None:
        options.append(None)
      else:
        options.append(backups[i]['name'] + " - " + backups[i]['udid'])
        udids.append(backups[i]['udid'])
        backupName = backups[i]['name']
    terminalMenu = TerminalMenu(options)
    menuEntryIndex = terminalMenu.show()
    print(f"You have selected {options[menuEntryIndex]}!")
    return udids[menuEntryIndex]
  else:
    print("No backups found :(")
    return None

def domainsToExtract():
  options = ['WirelessDomain', 'HomeDomain', 'CameraRollDomain', 'MediaDomain']
  selectedOptions = []
  terminalMenu = TerminalMenu(
    options, 
    multi_select=True,
    show_multi_select_hint=True
  )
  menuEntryIndex = terminalMenu.show()
  for i in menuEntryIndex:
    selectedOptions.append(options[i])
  return selectedOptions

def getListOfBackedUpFiles(backup):
  global loading
  fileList = backup.getBackupFilesList()
  loading = False
  return fileList 

def extractWirelessDomain(backup):
  backup.getFolderDecryptedCopy(
    'Library',
    targetFolder=destination+backupName,
    includeDomains='WirelessDomain',
  )

def extractHomeDomain(backup):
  backup.getFolderDecryptedCopy(
    'Library',
    targetFolder=destination+backupName,
    includeDomains='HomeDomain',
  )

def extractCameraRollDomain(backup):
  backup.getFolderDecryptedCopy(
    'Media',
    targetFolder=destination+backupName,
    includeDomains='CameraRollDomain',
  )

def extractMediaDomain(backup):
  backup.getFolderDecryptedCopy(
    'Library',
    targetFolder=destination+backupName,
    includeDomains='MediaDomain',
  )

def extract(backup):
  for domain in selectedDomains:
    if domain == 'WirelessDomain':
      extractWirelessDomain(backup)
    elif domain == 'HomeDomain':
      extractHomeDomain(backup)
    elif domain == 'CameraRollDomain':
      extractCameraRollDomain(backup)
    elif domain == 'MediaDomain':
      extractMediaDomain(backup)
    else:
      print(f"Domain {domain} not supported yet")

udid = slectBackup()
domains = []

if udid:
  backup = iOSbackup(
    udid=udid
  )
  selectedDomains = domainsToExtract()
  if selectedDomains:
    if os.path.exists(destination+backupName):
      extract(backup)
    else:
      os.mkdir(destination+backupName)
      extract(backup)
  else:
    print("No domains selected")
else:
  print("No backups found")

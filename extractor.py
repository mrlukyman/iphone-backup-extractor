import iOSbackup

backup_folder = "~/Library/Application Support/MobileSync/Backup" # backup folder (macOs)

destination = '' # destination folder

backups = iOSbackup.iOSbackup.getDeviceList()
print("Available backups:")

for i in range(len(backups)):
  if backups[i] == None:
    print(str(i) + " - " + "No backup")
  else:
    print(str(i) + " - " + backups[i]['name'] + " - " + backups[i]['udid'])

backup_id = int(input("Select a backup: "))

udid = backups[backup_id]['udid']

backup = iOSbackup.iOSbackup(
  udid=udid
)

# extract backup photos
# change arguments to extract domains you want
backup.getFolderDecryptedCopy(
	'Media',
	targetFolder=destination,
	includeDomains='CameraRollDomain',
)

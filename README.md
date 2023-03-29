# iphone-backup-extractor

The extractor works for extracting all domains in iOS backups. Please keep in mind that this is just a simple implementation of the iOSbackup library and I do not take any reponsibility for the loss of your data (though I tested it multiple times and I didn't experience any data loss).

<p>Domain list</p>
<table>
<thead>
<tr>
<th>Backup file</th>
<th>Domain</th>
<th>File name</th>
<th>Contains</th>
</tr>
</thead>
<tbody>
<tr>
<td>ed1f8fb5a948b40504c19580a458c384659a605e</td>
<td>WirelessDomain</td>
<td>Library/Databases/CellularUsage.db</td>
<td>Table <code>subscriber_info</code> apparently contains all SIM phone numbers ever inserted in the phone since about iOS 11 or 12. Data here is related to <code>Library/Preferences/com.apple.commcenter.plist</code>.</td>
</tr>
<tr>
<td>0d609c54856a9bb2d56729df1d68f2958a88426b</td>
<td>WirelessDomain</td>
<td>Library/Databases/DataUsage.sqlite</td>
<td>A rich database that apparently contains app WWAN usage through time. Chack tables <code>ZPROCESS</code> and <code>ZLIVEUSAGE</code>.</td>
</tr>
<tr>
<td>1570a95f5dc7f4cd6b54bc17c427eda95288b8fa</td>
<td>HomeDomain</td>
<td>Library/SpringBoard/LockVideo.mov</td>
<td>Video used as background on lock screen</td>
</tr>
<tr>
<td>.</td>
<td>HomeDomain</td>
<td>Library/Passes/Cards/*</td>
<td>Wallet passes and items</td>
</tr>
<tr>
<td>8d0167b67f664a3816b4c00115c2dfa6a8f81388</td>
<td>WirelessDomain</td>
<td>Library/Preferences/com.apple.AppleBasebandManager.Statistics.plist</td>
<td>Apparently contains times of last boot and restores.</td>
</tr>
<tr>
<td>dafec408e48be2700704dd3e763014c39f6de6b3</td>
<td>WirelessDomain</td>
<td>Library/Preferences/com.apple.AppleBasebandManager.plist</td>
<td></td>
</tr>
<tr>
<td>9329979c8298f9cd3fb110fa387570a8b957e912</td>
<td>WirelessDomain</td>
<td>Library/Preferences/com.apple.CommCenter.counts.plist</td>
<td>Has <code>CellularBytesRecved</code> and <code>CellularBytesSent</code></td>
</tr>
<tr>
<td>3dec38ca46c9e37ffebacf2611463eb47a65eb09</td>
<td>WirelessDomain</td>
<td>Library/Preferences/com.apple.commcenter.audio.plist</td>
<td></td>
</tr>
<tr>
<td>7e5f642f6da5e2345c0893bdf944da9c53902756</td>
<td>WirelessDomain</td>
<td>Library/Preferences/com.apple.commcenter.callservices.plist</td>
<td></td>
</tr>
<tr>
<td>bfecaa9c467e3acb085a5b312bd27bdd5cd7579a</td>
<td>WirelessDomain</td>
<td>Library/Preferences/com.apple.commcenter.plist</td>
<td>Cellular network informations and configurations, including all ever inserted SIM and eSIM cards, their phone numbers and nicknames as configured under Settings➔Celular. Data here is related to <code>Library/Databases/CellularUsage.db</code></td>
</tr>
<tr>
<td>160600e9c2e408c69e4193d325813a2a885bce2a</td>
<td>WirelessDomain</td>
<td>Library/Preferences/com.apple.ipTelephony.plist</td>
<td></td>
</tr>
<tr>
<td>12b144c0bd44f2b3dffd9186d3f9c05b917cee25</td>
<td>CameraRollDomain</td>
<td>Media/PhotoData/Photos.sqlite</td>
<td>Photo library data, albums, tagged faces, moments, places, geolocations, date and times, formats etc.</td>
</tr>
<tr>
<td>.</td>
<td>CameraRollDomain</td>
<td>Media/DCIM/*APPLE</td>
<td>Original master photos/videos taken by your camera or imported through AirDrop etc</td>
</tr>
<tr>
<td>.</td>
<td>CameraRollDomain</td>
<td>Media/PhotoData/Mutations/DCIM/*APPLE</td>
<td>Edited version of photos/videos</td>
</tr>
<tr>
<td>.</td>
<td>HomeDomain</td>
<td>Library/Mobile Documents/iCloud~...</td>
<td>Apps documents on iCloud</td>
</tr>
<tr>
<td>.</td>
<td>HomeDomain</td>
<td>Library/Mobile Documents/com~apple~CloudDocs/...</td>
<td>Documents folder on iCloud</td>
</tr>
<tr>
<td>5a4935c78a5255723f707230a451d79c540d2741</td>
<td>HomeDomain</td>
<td>Library/CallHistoryDB/CallHistory.storedata</td>
<td>Call History database with only the last 600 calls</td>
</tr>
<tr>
<td>31bb7ba8914766d4ba40d6dfb6113c8b614be442</td>
<td>HomeDomain</td>
<td>Library/AddressBook/AddressBook.sqlitedb</td>
<td>User contacts and address book. Table <code>ABPerson</code> is the central one with facts about contact creation and modification, while <code>ABMultiValue*</code> tables contain contact details.</td>
</tr>
<tr>
<td>cd6702cea29fe89cf280a76794405adb17f9a0ee</td>
<td>HomeDomain</td>
<td>Library/AddressBook/AddressBookImages.sqlitedb</td>
<td>Contact photos</td>
</tr>
<tr>
<td>9db3e5a6f1672cc306cd785809811e79cc43a2f8</td>
<td>HomeDomain</td>
<td>Library/AddressBook/backup/AddressBook.sqlitedb</td>
<td></td>
</tr>
<tr>
<td>2a87d5bcdb9753f1462dd1e929b17e6a971c5b01</td>
<td>HomeDomain</td>
<td>Library/AddressBook/backup/AddressBookImages.sqlitedb</td>
<td></td>
</tr>
<tr>
<td>1a0e7afc19d307da602ccdcece51af33afe92c53</td>
<td>HomeDomain</td>
<td>Library/Safari/History.db</td>
<td></td>
</tr>
<tr>
<td>.</td>
<td>MediaDomain</td>
<td>Library/SMS/Attachments/*</td>
<td></td>
</tr>
<tr>
<td>.</td>
<td>MediaDomain</td>
<td>Library/SMS/StickerCache/*</td>
<td></td>
</tr>
<tr>
<td>.</td>
<td>.</td>
<td>Library/Caches/locationd/consolidated.db</td>
<td>Apparently list of known iBeacons</td>
</tr>
</tbody>
</table>

If you have any suggestions for better a experience with extracting backups don't hesitate to make a PR or contact me on my socials.

Enjoy!

# iphone-backup-extractor
[![MIT-LICENCE](https://img.shields.io/github/license/mrlukyman/iphone-backup-extractor?style=flat-square)](https://github.com/mrlukyman/iphone-backup-extractor/blob/main/LICENSE)

The extractor works for extracting all domains in iOS backups. Please keep in mind that this is just a simple implementation of the iOSbackup library and I do not take any reponsibility for the loss of your data (though I tested it multiple times and I didn't experience any data loss).

For more information check: https://pypi.org/project/iOSbackup/

### How to use:
You will need to install following packages:

    pip install iOSbackup
    simple_term_menu
     
After installing you need to change the destination path for the extraction

    ...
    
    dynamicPath = Path('<destination>') # change this to your desired path
    
    ...
Now you can run:

    python3 extractor.py

If you have any suggestions for better a experience with extracting backups don't hesitate to make a PR or contact me on my socials.

Enjoy!

# Manage Axes Save File

Once you have selected the path to save the file, you can save the current axes list configured in the inspector, so it will be loaded when the game starts, using as the default configuration.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F9nHxGUakAnDB9RfQmd2c%2F0?alt=media)

There are different options in the **Input Scheme Options**:

* **Default -** Removes the current axes list and configures it with the controls by default (this is created inside the code, so the default list is always the same, but it can be changed, in the **inputManager** script, go to the function **setToDefault** and change the list configured). This function also set the touch buttons.
* **Save To File** - Save the current axes list in a file with the name and path configured previously in the Save Settings.
* **Load From File** - It removes the current axes list and configures it with the controls created in the last save file created.

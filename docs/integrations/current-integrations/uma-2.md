# UMA 2

Integration with the UMA 2 system.

## What is UMA 2 - Unity Multipurpose Avatar?

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-McLLp9jDL-LIuzRrSTQ%2F-McQr0HehxWZQ3LQRcqD%2F-McQtvnDSOC2rdEpGZQg%2Fgkc-doc-integration-uma-header.png?alt=media\&token=82ccd0fe-bfe5-439c-a1d1-85efaff79ca1)

The **Unity Multipurpose Avatar (aka UMA)** system lets you create customizable characters. Whether you need a hero, a villain, or an entire village of NPCs this package is for you!

UMA includes all of the code necessary to build a huge variety of unique characters at runtime from simple recipes. By merging the meshes, textures and bones of a character and its equipment UMA builds efficient customizable characters with a minimum number of draw calls.

The included Human meshes can be used as is with some of the stunning clothing assets available on the Asset Store or you can create brand new creatures specific to your game and use UMA to customize those as well.

Import UMA 2 from the store.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FYAx5l2uDdFIBabc6mdFr%2F0?alt=media)Open the scene “How to Load and Save a DCA to a string” Drop the prefab called “UMADynamicCharacterAvatar” into the scene:

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FHMKKTF0qjr00J428PKoV%2F1?alt=media)

Assign that object here:

Drop the main player prefab “Player and Game Management” into the scene and use the manual character creator, selecting the UMA character as the new model and replace the model of that player with this UMA character.

Go here and press this button:

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FEZeQBuo1DTd1tKsmc9dD%2F2?alt=media)

You can see the field Number Of Childs will change its value from 0 to a certain number.

Replace the scripts on UMA with the two provided on this zip (CapsuleColliderSlotScript and UMASkeleton) directly the window explorer and not in unity.

UMASkeleton is located here:

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FGk6NBXPMZavoyyW4xr8W%2F3?alt=media)

And CapsuleColliderSlotScript here:

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FjpqL7uE16SWOj8EXEKOq%2F4?alt=media)

Move the scripts UMAIgnoreTransformAndChilds and UMAIgnoreTransformAndChildsEditor from GKC folder to this folder:

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FeKOcW9YFXMS3RTqgrg5w%2F5?alt=media)

Hit play and try it.

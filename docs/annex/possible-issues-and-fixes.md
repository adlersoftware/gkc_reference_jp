# Possible Issues and Fixes

### Change from .NET 3.5 to 4.0 in Unity 2019 <a href="#toc93306" id="toc93306"></a>

If you are using unity 2019, maybe you can see this message on the console:

This issue is happening to most assets which haven't used 2019 as starting version, so when importing the asset, the default configuration of .NET is 3.5 when Unity needs 4.0 to work properly, causing these errors on screen in any project/asset from a lower version.

To fix this, follow these steps: Go to Edit --> Project Settings --> Player --> Other Settings --> Configuration --> Scripting Runtime Version --> .NET 4.x Equivalent

You can see more info in this link:

{% embed url="<https://www.corrosionhour.com/change-net-version-to-4-in-unity/>" %}

### Unity 2018 Collision Error

If you use 2018 unity version or higher and when you fire a weapon, it shows an error message, it is due to the new collision detection on unity 2018 and higher.

To fix this, search the projectile prefabs in the project and configure the collision detection to deterministic in those projectiles which uses a different collision detection from discrete.

If the collision detection is discrete, there is no need to change the setting.

This is a bug from unity itself, in other versions like 2017, this won't happen.

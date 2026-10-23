# Tutorial - Configure Armor-Clothe for New Model

How to configure the Armor-Cloth component on a new model in GKC

## Overview

First thing, make sure to drop in the scene the **Main Inventory List Manager** prefab, as it will contain the inventory info from the new armor set created.

Before creating a new character, create a prefab of the new model and attach the component **Character Customization Manager**

{% hint style="warning" %}
Configure the settings of the component as shown below.
{% endhint %}

<figure><img src="https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FCxFeZr5HErAA4SRQDyTT%2Fimage.png?alt=media&amp;token=b0b7cfab-1f21-47ae-a6c5-2829c40ee37a" alt=""><figcaption><p>Intial Settings for the Character Customization Manager</p></figcaption></figure>

### Configure Mesh List

Then, on the main character base info, configure the list of meshes of the base model (usually the one that is "naked/underwear", avoid configuring their hair or any body accessory.

For each part, make sure to use a unique name, like Head, Chest, Hips, Feet, Hands, Upper Arms, Lower Arms, Upper Legs, Lower Legs, etc... as this will be used for each category of equipment in the next settings.

Make sure to have the base model meshes as the only active meshes on the character, so the rest of the meshes are disabled on the hierarchy.

### Create Set Name and Settings

On **Character Set Settings**, create a new element, set a unique name for the Set, and configure the meshes used on that set, using the same Type Name for each body part, for example, Helmet on Name and Head on Type Name on that object.

Once all the parts of that set are configured, go to the **Game Kit Controller top bar settings**, and press **Create Armor-Cloth Set** button.

### Configure Armor Parts

Configure the same amount of elements as you did in the previous step, set the same unique names for each armor part and its Category Name (same as the Type Name that you configured previously, Head, Hips, Hands, Feet, ....), and the mesh used on the inventory pickup (this can be a regular pickup mesh or any other), set the icon capture used for that inventory object, the description and any extra info that you consider.

Make sure to set the same set name on the **Full Armor Cloth Set Name** field.

Select the scriptable objects which contain the full list of pieces of the character and the full armor lists (you can create new scriptable objects for those in the project).

### Finish Creating Set

Once all is configured, press **Create New Set**, which will take a few seconds to complete. This will create all the info related to the new set, including the inventory object's info and prefabs.

Locate on the hierarchy where you dropped the **Main Inventory List Manager**, you can see the new set is added into the armor-cloth category, press the button apply on the above part of the inspector on the prefab section, to update the main inventory info on the prefab, so all is updated properly.

### Update Character Prefab

Finally, with the model on the hierarchy with its **Character Customization Component** configured, update its prefab, so that info is updated on the model, which is the one that you will use to create a new player with it (or AI).

# Prefabs Manager

## Overview

There is a system called **Prefabs Manager**, which allows to manage, instantiate and add prefabs to the scene easily, avoiding the need to search between folders.

For this follow these steps:

Go to the upper part of unity, in the options of the top, **Game Kit Controller->Create Prefabs Manager**.

If there was a Prefabs Manager previously in the scene, it will select in the editor, else a new one will be placed on the scene and selected in the editor.

Inside the **Prefab Type Info List**, you can find the current prefab categories configured and the different prefabs configured in each one along an explanation of what each category does.

This list is mostly used to configure the prefabs of the project, where you can add your own, so you can use this system as well to place your new prefabs into the scene.

Once you have your prefabs configured here (using the buttons to configure a path for the prefabs folder and using the buttons to get the prefabs objects in those folders), you can use the next list, **Prefab Type Info List To Place On Scene**, which is the one used to place the prefabs in the scene, being a more simplified version, with only the needed elements to make it simpler to use.

In this list, you can select any category and press the button **Add: “Name of the prefab”**, to place in on the scene, placing the prefab in the position of the level where the current camera editor in the window Scene is looking at, using a raycast to detect the surface:

Also, if you add new prefabs or remove others from the first list, make sure to press the button **Update Prefab List To Place On Scene**, so the main second list used to place prefabs in scene contains the same elements

You can also use a searcher to filter the categories and prefabs objects by name, so you can easily find the prefab you need to use. For this, press the button **Show Prefabs Searcher**:

And in the field Prefab Name To Search, type the name (or part of the name) of the prefab you are searching and press the button **Search Prefab By Name**, to get a list of similar results:

So for the results found, you can press the button below each results to place them in the scene.

You can also search by categories, instead of by prefab name, with the other text field and pressing **Search Prefab By Category:**

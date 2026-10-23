# Configure the Main Mission Manager

This system allows to configure the whole mission system and is used to set some settings automatically on it.

For this, go to the upper toolbar of unity, select **Game Kit Controller->Main Managers->Add Main Mission Manager**.

Then, this system is placed on the level, which is the main mission manager, and it contains a list of all the station systems in each level. These station systems can be used as a physical mission board or just an invisible to configure different missions which are maybe activate by dialog or trigger.

Each station has a list of missions, which are the one which contains the missions to achieve, task, and rewards, and events to activate.

Also, it allows to place different mission elements on the level with just a click.

One of them is the **Mission Station**, which can be used as a physical mission board or just an invisible to configure different missions which are maybe activate by dialog or trigger.

Each station has a list of missions, which are the one which contains the missions to achieve, task, and rewards and events to activate.

Other element is the **Mission System.** which is the component where each mission itself is configured and managed.

And finally the **Character Mission System**, used to place missions on NPC, giving them to the player directly when the player uses the interaction button, showing the mission panel on characters. To trigger missions with dialog, other way (which will be explained later in videos and on this doc) is used, and which you can already see in the advanced mission demo.

The process to configure missions in the main mission manager is the next:

Configure all the missions that you need in the **Objective Event System** components:

Them, in the **Station System or the Empty Station System** (Objective Station System component), assign these missions according to where you want them to be found by the player, like a mission board, with a character, by trigger, etc...so you assign these missions to one Objective Station System component or other.

Then, go to the **Main Mission Manager** (Objective Manager component), assign the Scene number of the level assigned in the unity Build Settings panel and press the button **Get All Station Systems On The Level And Assign Info**. You will see how all the Station System appear on the

**Objective Station System List**.

With it, all **Objective Event System** (each mission configured), gets a Mission Id and the same Mission Scene value than in the main manager.

This also allows the system to save the info of the missions found by the player, with those already complete and those to finish yet.

# Tutorial - Create a Generic Character

How to create a Generic Character in Game Kit Controller

## Video Tutorial

{% embed url="<https://www.youtube.com/watch?v=XABt9LvzRaY>" %}
Creating a Generic in 3.03-2
{% endembed %}

## Written Tutorial

### The Generic Model Wizard

Search for **AI Main Template Prefab** and drag it into your scene. Next, go to *Game Kit Controller Menu / Generic Models / Add new generic model to controller*.&#x20;

Fill in the name of your new AI and drag its generic model to your scene, then drag it from there to the generic model slot in the wizard.&#x20;

Select the generic character's avatar, then search your project for **Generic Model Animator Template** duplicate and rename it, and put it in whatever folder you want.&#x20;

Drag it into the animator slot to assign it and check the **Character Is AI** box. Then click **Create**.

### Set up the Prefab

Now go to your AI Player Controller gameObject and expand **Other AI Systems**. Click on **Custom Character Controller Manager**.

Check the box **Start Game with Custom Character Type** in the name that you used in the wizard for your character Scroll to the bottom and click "Enable Current Generic Model"

Now search for the animator controller you duplicated and double click on it to open it. Double click on **Locomotion** then double click on **Grounded** and then double click **Locomotion** again. Select **Locomotion Tree** and drag your animations to the slots on the right side.

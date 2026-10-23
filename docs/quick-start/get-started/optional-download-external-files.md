# (Optional) Download External Files

### Mixamo Animations <a href="#toc93303" id="toc93303"></a>

The action system can be used with any type of humanoid animation. To work on this system, example animations from Mixamo were used as placeholders to configure multiple examples of the action system. Due to Mixamo animations can’t be included on asset, you can find the animations used on these examples on the public repository of **Game Kit Controller** on **Github.**

<https://github.com/sr3888/GKC-Public-Repository>

These animations are already with the regular settings applied to work on root motion properly (like rotation based on current pose, loop time, adjust speed, etc…). No extra setting is needed to try these examples.

All those animations and copyrights belong to Mixamo. You can get those animations and more at the official website of Mixamo: <https://www.mixamo.com/#/>

Of course, on this action system, you can use your own animations, from the asset store or any other store or web.

### **Slice System** <a href="#toc93304" id="toc93304"></a>

There are a couple of systems in the asset that uses a slice system for 3d meshes and skinned mesh renders, for the melee weapon system, allowing to cut surfaces and characters, similar to games like metal gear rising. Those systems can be found in the public repository of GKC, which is the same limb from a few lines above.

You only need to import those 2 packages and open the script file called sliceSystemUtils.cs and uncomment all the commented lines on that script, in order to use the slice system. This is not mandatory to be done if you won’t use the slice system in any part of your project.

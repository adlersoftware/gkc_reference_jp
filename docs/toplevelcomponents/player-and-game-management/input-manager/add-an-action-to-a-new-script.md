# Add an Action to a New Script

How to add a Player Action to a New Unity Script

#### Add an action to a new script <a href="#toc72415" id="toc72415"></a>

* Add a new Axe in the Axes list, by pressing the button Add New Axe or Add Action.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FUlIqVCgai3Q081FFnRvd%2F0?alt=media)![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FAoWgOK0yrYPZyxYlHsbE%2F1?alt=media)

* Set the name that you want for that action and a keyboard button.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F4zK322WbGTXbnrPAdB22%2F2?alt=media)

* Declare an inputManager variable type (if the script doesn’t contain it yet), get the main inputManager in the scene, and add the above functions to the script, setting the type of press button and the action that you want to check. In this example you can see it better:

![Just add this basic code](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FuEmbi5zGDwKVdJRHqJQV%2F3?alt=media)

```
if (input.checkInputButton ("newAction", inputManager.buttonType.getKeyDown)){
//KeyDown, key pressed, call the need function
}
if (input.checkInputButton ("newAction", inputManager.buttonType.getKey)){
//Key, key held call the need function
}
if (input.checkInputButton ("newAction", inputManager.buttonType.getKeyUp)){
//KeyUp, key released, call the need function
}
```

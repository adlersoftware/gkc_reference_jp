# Assign a Touch Button to an Action

Once you have created an action in the axes list, you can assign a touch button to it:

* Go to the Touch Panel gameObject, inside the Canvas component of the player.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FqyPltvJTAdj6zTmgoWJg%2F0?alt=media)

* Copy and paste any **Touch Button** inside of the **Touch Panel**. Also, you can add a new empty object, add a Raw Image component, configure its texture and add a **Touch Button Listener**. Here's how the button inspector looks:

![In the Touch Button Listener, it can be configured if the button changes its color on press and release.](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2Fn0GYUtbXCGI3x5dqSQTA%2F1?alt=media)

* Also, you have to configure the name of that button with the same name that the action which uses it. For example, if the action is called “Jump”, the touch button needs to be called “Jump” too (this is used in the code to identify better every touch button). Finally, assign that object in the Touch Button element of the action configured.

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FryqoQnROKfCVxYNbItJe%2F2?alt=media)

* When a touch button is added, the option **Show Touch Button Scale** is shown.

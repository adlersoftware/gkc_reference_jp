# Universal AI

This page covers the integration of Universal AI and Game Kit Controller

## What is Universal AI?

<figure><img src="https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2F7pN4cmbgJislEL4onc3X%2Fimage.png?alt=media&amp;token=eac46a1c-6a06-4b29-ac18-43135e749a16" alt=""><figcaption></figcaption></figure>

**Universal AI** allows game developers to create **AAA**-quality AI characters in a few minutes. The system allows users to extend the system, understand the code; add features, disable features, and **much** more.

**Customizable -** Easy to add custom actions, behaviors & animations with examples.

**Animation Wizard -** Easily set up animations for your AI, with our custom animator creator wizard.

**Setup Manager -** With a few clicks, create your AI with our advanced AI setup wizard.

{% hint style="info" %}
You can find more information about **Universal AI** and its documentation and also download it over on [**Github**](https://github.com/darkingassetsof/universalai20)**.**
{% endhint %}

## Integration Steps

Open the script health.cs from Game Kit Controller and add this code:

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FRCEIxvKUs3H26nTSZ7KS%2F0?alt=media)

using **UniversalAI**; and , **universalDamageable**.

Rename the file **GKCUniversalAIDamageDetectionInterface**.txt as .cs and attach it to the Universal AI objects:

![](https://3552900959-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-McLLp9jDL-LIuzRrSTQ%2Fuploads%2FxrJvG4fmQlBOETaStlpF%2F1?alt=media)

And that is all needed, the damage detection will be applied between both characters, GKC player and Universal AI objects.

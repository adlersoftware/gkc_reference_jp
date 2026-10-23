# Remote Event System Component

## Overview

This system which allows to configure a list of events and assign a name to each element of the list. Each one of these elements can be triggered remotely by another object through an effect area, on trigger or by certain components or other events, as the system is made in order to avoid having direct references to the object with the event to trigger, so each object can be different prefabs without any relation.

### Example Usage

An example of this is that the player can activate their sleep spell ability which basically uses a sphere cast to detect objects inside a radius and trigger their remote event system, searching for the element with the name “Activate Sleep Spell Cast”. That has an event configured on each AI to call to the ragdoll state to make them fall and be in that state x amount of time.

So that type of reaction is triggered without any direct reference to any specific component or object of the AI and the player, even if the AI is spawned dynamically at run time.&#x20;

This can be used in a multitude of situations, for example, an ability hack which basically detects an object by raycast and calls its remote event system component to call the event called “Hack”, to unlock a door, make a device explode, disable the energy of a generator, make a vehicle to activate its self destruct function, etc.

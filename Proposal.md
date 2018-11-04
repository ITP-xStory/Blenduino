# Open Source Studio Final Project Proposal

## Title: Blenduino

Blender 3D is an open source 3D creation tool, and Arduino is an open source electronics prototyping platform. They should be friends!

I aim to create 2 libraries - an arduino library and a blender add-on - that facilitate serial communication between the two platforms.
Blender includes python scripting and can read serial, but the actual implementation of getting serial data into blender in a useful way can be clunky and not beginner friendly. I hope to create a way to easily bring physical data into blender, and send useful data out into the physical world.

Whether you're looking to design a new 3D modelling interface, or experiment with animations involving real-time physical data, or anything in between, this system could be for you.


## Team Members

James Hosken

## Define the problem.

_What is the current state of things? What issue do you wish to solve and why? Who is the audience?_

Getting physical data into a 3D creation tool doesn't exactly solve a *problem*, but it does open up a lot of new possibilities. 
In the current state of things, one can use Blender's python integration to read serial data from an arduino. In this case, however, one must be familiar with both arduino and python, and blender's specific python libraries, as well as how to get data from the python script into the 3D environment. All said that's a lot of barriers to entry.  
Hopefully this proposed system will allow quick experimentation without having to know the intricacies of each stage of the process.

Potential use cases are:
* Control a game within the blender game engine using an arduino-based controller.
* Control elements of an interactive installation running on Blender using an Arduino
* Design & build new modelling or animation interfaces (e.g. a physical doll to help animate a virtual character)

## Address Greater Landscape

_Please address how the open source project you are creating or contributing to fits into a greater field or tech landscape. Who has done similar work before? How are you building off this? What sets your project apart from your colleagues?_

This system could be thought of as similar in concept to the Processing(/p5)/Arduino relationship, in that physical data can be sent from the Arduino to a more powerful processor so that something interesting can be done with it. The more powerful processor in this case is the Blender engine, which specialises in all things 3D. So, where in Processing/p5 the physical data coming in could alter parameters of your code, in this system the physical data coming in could alter parameters of objects in your 3D enivonment (PSR\*, light intensity, colour)

\* Position, Scale, Rotation

Individuals have connected [arduino to blender](http://forum.arduino.cc/index.php?topic=17797.0) [before](https://www.youtube.com/watch?v=sVtZPQGt5PM), but as mentioned above in a way that requires a decent amount of understanding of all different parts involved. I'm hoping to remove some of those barriers to entry by creating a sort of "plug and play" system where the user can simply choose the data they wish to send and not have to worry about how to implement python or Arduino serial, or how to navigate Blender's python library.

## Deliverables

* A protocol to send/receive serial data between Arduino & Blender
* A Blender add-on that processes incoming serial data and outputs data in a user-friendly window of customisable drivers
  * "Driver/Driven" is a relationship where one parameter can directly chage another. It's a way to centralise control of many different parameters.
* [Potential] An Arduino library that standardises the way data is sent/received from Blender
  * I've put this as optional because maybe it is irrelevant - perhaps serial IO will be enough.

## Implementation

_Describe the technical details about your implementation and development process._

## Timeline

### Week 1 
* Get data from Arduino to Blender
* Start thinking about a standardisation of data (ints? bytes? how much data? )
* Update Documentation

### Week 2
* Implement data standardisation so that sending/receiving is easily repeatable
* Start preparing how to implement blender Addon
* [Optional] Start preparing how to implement Arduino library
* Update Documentation

### Week 3
* Link data coming in from serial to blender drivers
  *This may involve a bit of translation, e.g. from bytes to degrees/floats?
* Start wrapping blender system in Addon template
* [Optional] Start wrapping Arduino library
* Update Documentation

### Week 4
* Finish wrapping blender-side Addon
* Start Preparing presentation
* Update Documentation

### Week 5
* Prepare presentation 
* Contingency bugfix time
* Update Documentation

## Documentation

The code and development documentation will live on GitHub, and I'll post informal updates on [my ITP blog](https://generallyplayful.com)

## Accessibility

I shall strive to follow WCAG in all documentation materials.

## Mentoring

I think my two main technical challenges will be thinking through how data is structured and sent, and implementing the blender-side code as an Addon. 

In terms of the latter, I'm not sure of anyone who has experience specifically with blender Addons, and it seems that there's enough documentation that the process will mostly involve rigorous research and reading the documentation.

In terms of the former, pretty much anyone who has experience reliably sending/receiving data between two systems could be helpful to me. Luckily there's a vast pool of the very such people at ITP! Off the top of my head two (very busy) people I could learn a lot from are:
- Shawn van Every (networking and data streaming seem a good match)
- Tom Igoe (networking and connection to Arduino development)


## More about you

*Todo*

_What are your interests and experience? Have you contributed to other open source projects? What barriers or concerns have kept you from contributing to free and open source software? If you have an online portfolio, github account, or other relevant documentation of your work, please include links. If the project is a collaboration, a section should be included for each collaborator._

## References

This proposal template was created with material and advice from:

- [How to write a proposal for GSoC](http://teom.org/blog/kde/how-to-write-a-kick-ass-proposal-for-google-summer-of-code/)
- [Processing Foundation GSoC application template](https://docs.google.com/document/d/1UFcWh2IWqhICh4YIFNwtKUaWWXifaBB67rjPxbYzjbE/edit)
- [Getting into Summer of Code programs](http://exploreshaifali.github.io/2015/06/08/getting-into-summer-of-code-programs/)

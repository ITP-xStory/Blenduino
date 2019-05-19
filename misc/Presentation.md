# Blendiuno Presentation Documentation 

## Blenduino

Blenduino is an almost-plug-and-play addon for Blender that facilitates easy access to a serial data stream. Bringing information from the physical world into a virtual 3D environment has many potential applications, from experimental new interfaces for 3D modelling and animation to immersive interactive experiences that blend the real and the virtual. Blenduino is not intended to be a robust production system, rather an easy way to get started experimenting!

## People
Project Creator: James Hosken

Project Mentor: Michael Shiloh

## The Deliverable

Within this repo (blender > addon) there is a file [blenduino.py](https://github.com/jameshosken/Blenduino/blob/master/blender/addon/blenduino.py). This is the entirety of the addon as it currently stands. 

Though I did not end up creating an Arduino library, there are a few example sketches in the Arduino > Examples folder.

The **User Guide** is a basic run through of how to install and use Blenduino.

## The problem and greater landscape

Connecting a 3D virtual world to the physical world does not necessariy solve a problem in itself, but it does open up a lot of creative possibilities, some of which may solve other problems. 

For example, a designer experimenting with new ways to interact with the 3D modelling process could use this tool to quickly sketch ideas. Or an animator with a uniquely structured model could 3D print the model, attach some sensors, and have a physical doll to manipulate the virtual model on screen. Or an ITP student could use Blender's new real time rendering capabilities to build an interactive escape room that blends reality and photorealistic CGI.

As mentioned above, Blenduino is not necessarily a robust system. I wanted to make something that was beginner friendly, and would allow someone with a bit of Blender experience but not too much Arduino experience (or vice versa) to get started as soon as possible. All the pieces - pySerial, threading, blender's API - are already there, but require time and effort to get used to. Hopefully Blenduino takes out that middle person.

A mantra I hear at ITP a lot is 'build something you would use.' Blenduino allows me to explore ways to bring in camera information into Blender in real time, hopefully adding a new tool to the Visual Effects pipeline.

Processing's Serial library and Chris Coleman's Maxduino project do similar things to Blenduino, although on a larger and more robust scale. 

## Implementation
1. **Relevant Content:** The weeks covering version control and licensing stand out as the most relevant to how I've structured my project. The licensing around Blender is such a core part of the tool that I wanted to stay in the spirit of things with the addon.

2. **Technicals:** The Blenderside add-on is written in python, Blender's scripting language
The first hurdle to overcome was Serial being a blocking function and causing Blender to freeze. I found that python's **threading library** is a good solution to this problem, although it took me some time to wrap my head around what was going on. <br/><br/>The python thread that handles Serial is activated and deactivated within the Blender User Interface, which is made possible by blender's python API. Using the API I can create new panels based off the UI theme. There was some discussion with Michael about how the user would interact with the data - in a UI panel, within a new blender object, using nodes - and I settled on a separate discreet panel. Michael suggest I look at what others have done, so I drew on the UI for the OSC addon in Blender.

3. **Challenges:** Learning the structure of Blender's API took a while; even though there is abundant documentation the leap from beginner example to what I wanted to do felt a bit steep. Getting python threading to play nice with Blender's API was a bit of a technical challenge, since the API restricts certain behaviours on initialisation.

4. **Timeline:** Wrapping my head around Blender's API took a bit longer than I expected, which pushed my timeline back a bit. I had hoped to get started on an Arduino library as well, but that has been taken off the immediate todo list. Since the process simply involves sending some data out via serial on the Arduino side, I don't think it's necessary to have a library for that - in fact it might be restrictive.

5. The biggest personal success for me surprisingly was becoming familiar with the Blender API. I feel like I am much more comfortable with the inner workings of the program now, which is a huge surprise bonus from this project.<br/><br/>What I regret is not more actively searching out for a community in the very early stages. I felt restricted by lack of any sort of viable product; I find it difficult to express what I'm doing without immediately sounding like I'm justifying the project.

## Accessibility

I do not yet have a website for the project, but I can imagine that there are going to be a few challenges in creating an accessible framework around this project which is inherently very visual.

## Mentoring

Michael, the mentor for this project, was very helpful in a few significant ways:

1. UI: I was struggling with how to present the incoming data to the user in a meaningful way. Mishael and I had a conversation about several different options and he suggested finding similar Blender addons and seeing how they handle this issue. This conversation led to the way that Blenduino is currently presented, as a tool in the Blender tool shelf.
2. Documentation: Michael had a great suggestion of structuring my documentation as if I were leading a workshop. Not only would this give me a solid place to start, but if I ever do present Blenduino to a group I'll already have an outline!
3. Marketing: Very forward looking, Michael suggested some conferences and workshops to think about as I continue with Blenduino.

I also met with Shawn van Every who gave some great suggestions regarding serial communication, and how I could implement a more efficient data stream. For this version I've decided to stick with the current implementation (it works as a prototype), but they are good notes for moving forward. 

## Longer-Term Goals

The original inception of this idea came about from a Visual Effects problem: How can you replicate real camera movement in a virtual environment. Since Avatar there have been a few physical and expensive solutions, but the most common low budget solution is algorithmic; take the video data and try to extract camera position info based on parallax shift in the scene. This solution is error prone and slow. The original idea behind Blenduino was to strap a few sensors onto a camera and bring live position and rotation tracking into Blender.

I hope to eventually use Blenduino to experiment with this Visual Effects project. As I do I intend to keep Blenduino open source, and if along the way anyone wants to contribute I'd be more than happy to have outside involvement!
AtomSplitter

Written by: Justin Israel
      justinisrael@gmail.com
      justinfx.com




Description
============================================

This FREE desktop application allows you to convert nuke Camera.chan files into 
either Autodesk FBX or Autodesk Flame .action files with the simplest of controls. 
It was designed for Chris Maynard of cmiVFX based on the research for the NukeX tracking system. 
Justin Israel and George Nahkl sorted out the code in python then ported it into individual 
desktop applications for convenient use. This is a python based solution that will provide 
extensibility to those interested in expanding its features. cmiVFX supports the open source 
growth of this application and is willing to share its source code to participating members 
of this community. The Autodesk FBX plug-in allows all types of data to be packaged into one 
file format that can be used by most of today's 3D authoring software.


Pre-built Binary
============================================

Older binary builds hosted here:  
http://justinfx.com/public/files/AtomSplitter/1.6.2/binary/

Binary builds are no longer maintained as of v1.6.2
The current way to use AtomSplitter is to download the source, and either running
directly from the AtomSplitter.py script, or follow the directions below and build
into a stand-alone executable.


Dependancies
============================================

AtomSplitter is a python application that requires the following:
  * Python 2.5+
  * PyQt 4.6+
  * PIL 


Usage
============================================

The tool has both a command line interface, and a GUI.
Running the script with no arguments will launch in GUI mode.

The following is the usage for command-line mode:

> python AtomSplitter.py -h
Usage: AtomSplitter.py <chan file> [out fbx file]

Options:
  -h, --help            show this help message and exit
  -o OBJ, --obj=OBJ     Optional nuke-exported pointCloud .obj file
  -f FPS, --fps=FPS     Set FPS rate (default 24)
  -x WIDTH, --width=WIDTH
                        Set frame width (default 2048)
  -y HEIGHT, --height=HEIGHT
                        Set frame height (default 1556)
  --filmwidth=FILMWIDTH
                        Set film aperature width in mm (default 24.576)
  --filmheight=FILMHEIGHT
                        Set film aperature height in mm (default 18.672)
  -s SCALE, --scale=SCALE
                        Scale the translation values by this amount
  -F FORMAT, --format=FORMAT
                        Output format (fbx, action, terragen)
  -a, --action          Export a Flame .action file instead of FBX
                        (DEPRECATED)


Building AtomSplitter into stand-alone apps
============================================

For your convenience, I have also included the setup files used
with py2app (for osx), and py2exe (win32)

Usage (osx):
  > cd build
  > python setup.py py2app   
  
For windows you can just run the bat script.

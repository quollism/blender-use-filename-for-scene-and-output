# blender-use-filename-for-scene-and-output

A quick Blender add-on which uses the filename for the scene's render output file and current scene name.

Usage:
- Install and enable it
- Every time you save a Blender file, the scene name and file output will change to the name of the file without the .blend extension (doesn't always work, looking into it)
- Disable the add-on to stop it from changing the scene and render settings

NB: The name change is made after the file is saved, so if it does something undesirable you can disable the add-on and Revert the file to get your render settings and scene name back.

As of 31 July 2016, it doesn't always work automatically, but you can Spacebar search for "Use Filename For Scene And Output" and run that to fire it off manually.

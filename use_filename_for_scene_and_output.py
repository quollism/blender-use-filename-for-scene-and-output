# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# todo:
# - automation for switching assets
# --- sombrero -> sombrero 278
# --- pointy -> pointy blocking 278
# -- read unwanted proxy for action, create new proxy and apply new action

bl_info = {
    "name": "Use Filename For Scene And Output",
    "author": "QUOLLISM",
    "version": (0,10),
    "blender": (2, 77, 0),
    "description": "Adds button which copies current filename to scene and render output after saving",
    "category": "User Interface" }

import ntpath
import bpy
import re

def get_base_filename():
    base_filename = ntpath.basename(bpy.data.filepath)
    # strip .blend off the end
    fn_re = re.compile('(.*?)\.blend')
    return fn_re.findall(base_filename)[0]

class FilenameToSceneAndOutput(bpy.types.Operator):
    """Copies filename to scene name and render output of current scene"""
    bl_idname = "scene.filename_to_scene_output"
    bl_label = "Use Filename For Scene And Output"

    @classmethod
    def poll(cls, context):
        return bpy.data.filepath != ''

    def execute(self, context):
        do_the_thing(bpy.context.scene)
        return {'FINISHED'}

def do_the_thing(scene):
    fn = get_base_filename()
    bpy.context.scene.render.filepath = "//"+fn
    bpy.context.scene.name = fn

def view3d_fn2sao(self, context):
    row = self.layout.row(align=True)
    row.operator("scene.filename_to_scene_output", text="Force Use Filename")

def register():
    bpy.utils.register_class(FilenameToSceneAndOutput)
    ### uncomment for button
    # bpy.types.VIEW3D_HT_header.append(view3d_fn2sao)
    bpy.app.handlers.save_post.append(do_the_thing)

def unregister():
    bpy.utils.unregister_class(FilenameToSceneAndOutput)
    ### uncomment for button
    # bpy.types.VIEW3D_HT_header.remove(view3d_fn2sao)
    bpy.app.handlers.save_post.remove(do_the_thing)

if __name__ == "__main__":
    register()

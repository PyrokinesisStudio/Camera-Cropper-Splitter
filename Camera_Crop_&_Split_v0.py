######################################################################################################


############# Add-on description (used by Blender)

bl_info = {
    "name": "Camera crop & split",
    "description": 'Allows to crop the camera view using the render borders or split the frame',
    "author": "Caetano Veyssières",
    "version": (0, 1),
    "blender": (2, 77, 0),
    "location": "Properties > Render > Camera crop & split",
    "warning": "", # used for warning icon and text in addons panel
    "tracker_url": "Not yet",
    "category": "Render"}

##############


import bpy
 
class OBJECT_PT_borderconvert(bpy.types.Panel):
	bl_label = "Camera Crop & Split"
	bl_space_type = "PROPERTIES"
	bl_region_type = "WINDOW"
	bl_context = "render"

	def draw_header(self, context):
		layout = self.layout
		layout.label(text="", icon="RENDER_REGION")
 
	def draw(self, context):
		layout = self.layout
 
		row = layout.row()
		split = row.split(percentage=0.5)
		col_left = split.column()
		col_right = split.column()
 
		col_left.operator("object.borderconvert", text="Crop using borders")
		col_right.operator("object.borderconvert", text="Split")
 
 
class OBJECT_OT_borderconvert(bpy.types.Operator):
	bl_label = "Border Converter Operator"
	bl_idname = "object.borderconvert"
	bl_description = "Converts render borders to camera view"
 
	def execute(self, context):
		C = bpy.context
		X = C.scene.render.resolution_x
		Y = C.scene.render.resolution_y
		f = C.scene.camera.data.lens
		bXmin = C.scene.render.border_min_x
		bXMAX = C.scene.render.border_max_x
		bYmin = C.scene.render.border_min_y
		bYMAX = C.scene.render.border_max_y
		
		# Focal length change :
		if (X>Y):
			if ((X*(bXMAX-bXmin))>((Y*(bYMAX-bYmin)))):
				C.scene.camera.data.lens = f * (1/(bXMAX-bXmin))
			else:
				C.scene.camera.data.lens = f * (X/(Y * (bYMAX - bYmin)))
		else:
			if ((X*(bXMAX-bXmin))>((Y*(bYMAX-bYmin)))):
				C.scene.camera.data.lens = f * (Y/(X * (bXMAX - bXmin)))
			else :
				C.scene.camera.data.lens = f * (1/(bYMAX-bYmin))
		
		# Resolution change :
		C.scene.render.resolution_x = round(X * (bXMAX - bXmin))
		C.scene.render.resolution_y = round(Y * (bYMAX - bYmin))
		
		# Shift X:
		if ((X * (bXMAX - bXmin))>(Y * (bYMAX - bYmin))):
			C.scene.camera.data.shift_x = (0.5 * (bXMAX + bXmin - 1)) / (bXMAX - bXmin)
		else :
			C.scene.camera.data.shift_x = (0.5 * (X * (bXMAX - bXmin)) * (bXMAX + bXmin - 1))/((Y * (bYMAX - bYmin)) * (bXMAX - bXmin))
		
		# Shift Y:
		if ((X * (bXMAX - bXmin))>(Y * (bYMAX - bYmin))):
			C.scene.camera.data.shift_y = (0.5 * (Y * (bYMAX - bYmin)) * (bYMAX + bYmin - 1))/((X * (bXMAX - bXmin)) * (bYMAX - bYmin))
			
		else :
			C.scene.camera.data.shift_y = (0.5 * (bYMAX + bYmin - 1)) / (bYMAX - bYmin)
		
		# Info report :
		self.report({'INFO'}, "Converted render borders to camera view")
		return {'FINISHED'}
 
def register():
	bpy.utils.register_module(__name__)
 
def unregister():
	bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
	register()
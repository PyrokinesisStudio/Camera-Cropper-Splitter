# Camera Cropper & Splitter

This Blender addon allows you to convert your render borders to the actual camera view or split the camera view in multiple tiles over time.

![alt text](https://caetanoveyssieres.files.wordpress.com/2016/04/crop-atom-demo.png)

My [5 min Blender conference 2016 talk](https://youtu.be/pBhRXLuI4FY?t=296) about it :
[![alt text](https://caetanoveyssieres.files.wordpress.com/2016/04/bcon.png?w=169&h=172)](https://youtu.be/pBhRXLuI4FY?t=296)


## Why would I need this ?

If you use a renderfarm or any network rendering setting to render your projects, chances are you need to split your frames in parts. Some renderfarms already do that, but even so, you can still face 2 problems :
* in most cases, if you want to render a region (with ctrl+B) and still want to split your job, the farm won’t take in account your region and will render the entire frame (since it needs to use its own regions to split the job)
* also, if you want to render very high-res images (4k, 8k or more) at a decent sampling quality, you may need to split the frames more than the farm allows you to.

With this addon, you can use the splitting feature of any renderfarm while rendering a region (since the region is converted to become the actual camera), or you can increase the number of tiles by splitting the frame directly within Blender, thus multiplying your number of tiles by the number you set on the farm. You can even combine the cropping and splitting features ! (which I did for a project), though for the moment this scenario requires an little extra step to reposition the frame.

## Installing (regular python addon) :

* Save the raw .py file of the latest version anywhere on your computer
* In Blender, open the User Preferences and go in the “Addons” tab
* Click on “Install from file” at the bottom
* Find the addon you downloaded
* Enable it by checking the box in the Addons list (the addon’s name is “Camera crop & split”)
* Now you should find it in the Render Properties

## All current features :

* **Crop using borders :** after defining a region with Ctrl+B in your active camera, this button changes the resolution, focal length and X-Y shift values of the camera to match the region you defined. The red rectangle you drew is now useless and most likely deformed. You can therefore disable it by unchecking "Border" in the render settings.
* **Split :** will split your camera view in multiple tiles by dividing the render resolution, changing the focal length and animating the X-Y camera shift values, depending on the number of tiles and tiling order you defined
* **Number of tiles :** allows you to chose by how many tiles you want your frame to be divided
* **Tiling order :** allows you to chose how the tiles should be animated. The indicated direction is the general movement, i.e. "Top to bottom" means "from Top left to top right, then once the line is finished go down". In the future I would like to use big icons with arrows to make this much easier to read and much more informative at the same time.

## Using the splitting feature :

* Select the number of tiles and tiling order and click on “Split”
* Set the keyframe interpolation of the generated keyframes to “Constant”
* Render the number of frames corresponding to the number of tiles

To use it on animations, put your animation in a track in the NLA editor and make it repeat as many times as your number of tiles (you have to do it on each animated object). Add one frame in the “End frame” value under “Action extents”, then scale the camera Shift keyframes (those generated by the “Split” button) by the same value as the animation length (one loop). This way the animation will play once for each tile, and each tile will last as long as one animation loop.

You can test the cropping and splitting features with this simple test file.

## Combining the result :

After trying a bunch of “Contact Sheet” programs and such, the Best way to have a perfect result was to use Blender’s compositor.
Contact sheets usually stick images together from edge to edge instead of positioning their center, which is what you should do to avoid a possible offset of 1 pixel per tile (in some situations).
The good news is, once you make a node group to arrange your tiles, you can plug any other image sequence with the same configuration and the node group will arrange the tiles instantly. I will soon make a full tutorial which includes this process (hopefully in november 2016).

I also plan on adding a feature that combines the tiles automatically in either the Compositor or the Video editor, but I can’t tell yet when that will come.

##Troubleshooting :

- Ensure your camera shifts X and Y are set to zero before using the cropping or splitting feature
- Ensure the camera sensor fit is set to "auto" (under the camera settings) as it is by default.
- Although it is very unlikely that your use case would go this far, remember that the Shift X and Y properties have a maximum value of 10. Splitting in 256 tiles generates a maximum shift of 7.5, so you can still add 2.5 to that.

Tell me if you’re interested in getting more features, it will motivate me !

This addon was made on Blender 2.77a and was tested on 2.78

![](https://caetanoveyssieres.files.wordpress.com/2016/05/with-logo-composited.png?w=391&h=391)

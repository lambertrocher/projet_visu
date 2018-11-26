# state file generated using paraview version 4.4.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1181, 758]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [1.999999999987267, 46.45, 0.0]
renderView1.RotationFactor = 0.96
renderView1.StereoType = 0
renderView1.CameraPosition = [1.999999999987267, 46.45, 64.20057813121173]
renderView1.CameraFocalPoint = [1.999999999987267, 46.45, 0.0]
renderView1.CameraParallelScale = 9.001510194202217
renderView1.Background = [0.32, 0.34, 0.43]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
sortienc = NetCDFReader(FileName=['/user/6/rocherl/Documents/visu/projet/sortie.nc'])
sortienc.Dimensions = '(latitude, longitude)'
sortienc.SphericalCoordinates = 0
sortienc.ReplaceFillValueWithNan = 1

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'TMP2maboveground'
tMP2mabovegroundLUT = GetColorTransferFunction('TMP2maboveground')
tMP2mabovegroundLUT.RGBPoints = [260.7394714355469, 0.231373, 0.298039, 0.752941, 282.451904296875, 0.865003, 0.865003, 0.865003, 297.1105651855469, 0.705882, 0.0156863, 0.14902]
tMP2mabovegroundLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'TMP2maboveground'
tMP2mabovegroundPWF = GetOpacityTransferFunction('TMP2maboveground')
tMP2mabovegroundPWF.Points = [260.7394714355469, 0.0, 0.5, 0.0, 297.1105651855469, 1.0, 0.5, 0.0]
tMP2mabovegroundPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from sortienc
sortiencDisplay = Show(sortienc, renderView1)
# trace defaults for the display properties.
sortiencDisplay.Representation = 'Slice'
sortiencDisplay.ColorArrayName = ['POINTS', 'TMP_2maboveground']
sortiencDisplay.LookupTable = tMP2mabovegroundLUT
sortiencDisplay.ScalarOpacityUnitDistance = 0.1941905735298652

# show color legend
sortiencDisplay.SetScalarBarVisibility(renderView1, True)

# setup the color legend parameters for each legend in this view

# get color legend/bar for tMP2mabovegroundLUT in view renderView1
tMP2mabovegroundLUTColorBar = GetScalarBar(tMP2mabovegroundLUT, renderView1)
tMP2mabovegroundLUTColorBar.Title = 'TMP_2maboveground'
tMP2mabovegroundLUTColorBar.ComponentTitle = ''
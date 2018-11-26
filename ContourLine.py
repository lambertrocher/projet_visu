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
renderView1.StereoType = 0
renderView1.CameraPosition = [1.9823518066045052, 46.45217026390131, 10000.0]
renderView1.CameraFocalPoint = [1.9823518066045052, 46.45217026390131, 0.0]
renderView1.CameraParallelScale = 8.993971239837444
renderView1.Background = [0.32, 0.34, 0.43]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
previsionPour = NetCDFReader(FileName=['/user/4/.base/jolivelm/home/Documents/3A/Visualisation/Scripts/PrevisionPour08h.nc', '/user/4/.base/jolivelm/home/Documents/3A/Visualisation/Scripts/PrevisionPour14h.nc', '/user/4/.base/jolivelm/home/Documents/3A/Visualisation/Scripts/PrevisionPour20h.nc'])
previsionPour.Dimensions = '(latitude, longitude)'
previsionPour.SphericalCoordinates = 0
previsionPour.ReplaceFillValueWithNan = 1

# create a new 'Extract Subset'
extractSubset1 = ExtractSubset(Input=previsionPour)
extractSubset1.VOI = [0, 2800, 0, 1790, 0, 0]
extractSubset1.SampleRateI = 10
extractSubset1.SampleRateJ = 10

# create a new 'Contour'
contour1 = Contour(Input=extractSubset1)
contour1.ContourBy = ['POINTS', 'TMP_2maboveground']
contour1.Isosurfaces = [280.0]
contour1.PointMergeMethod = 'Uniform Binning'

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'TMP2maboveground'
tMP2mabovegroundLUT = GetColorTransferFunction('TMP2maboveground')
tMP2mabovegroundLUT.EnableOpacityMapping = 1
tMP2mabovegroundLUT.RGBPoints = [255.67230224609375, 0.231373, 0.298039, 0.752941, 277.32952880859375, 0.865003, 0.865003, 0.865003, 298.98675537109375, 0.705882, 0.0156863, 0.14902]
tMP2mabovegroundLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'TMP2maboveground'
tMP2mabovegroundPWF = GetOpacityTransferFunction('TMP2maboveground')
tMP2mabovegroundPWF.Points = [255.67230224609375, 0.0, 0.5, 0.0, 298.98675537109375, 1.0, 0.5, 0.0]
tMP2mabovegroundPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from previsionPour
previsionPourDisplay = Show(previsionPour, renderView1)
# trace defaults for the display properties.
previsionPourDisplay.Representation = 'Slice'
previsionPourDisplay.ColorArrayName = ['POINTS', 'TMP_2maboveground']
previsionPourDisplay.LookupTable = tMP2mabovegroundLUT
previsionPourDisplay.ScalarOpacityUnitDistance = 0.1941905735298652

# show color legend
previsionPourDisplay.SetScalarBarVisibility(renderView1, True)

# show data from extractSubset1
extractSubset1Display = Show(extractSubset1, renderView1)
# trace defaults for the display properties.
extractSubset1Display.Representation = 'Slice'
extractSubset1Display.ColorArrayName = ['POINTS', 'TMP_2maboveground']
extractSubset1Display.LookupTable = tMP2mabovegroundLUT
extractSubset1Display.ScalarOpacityUnitDistance = 0.9013527976890835

# show color legend
extractSubset1Display.SetScalarBarVisibility(renderView1, True)

# show data from contour1
contour1Display = Show(contour1, renderView1)
# trace defaults for the display properties.
contour1Display.ColorArrayName = [None, '']

# setup the color legend parameters for each legend in this view

# get color legend/bar for tMP2mabovegroundLUT in view renderView1
tMP2mabovegroundLUTColorBar = GetScalarBar(tMP2mabovegroundLUT, renderView1)
tMP2mabovegroundLUTColorBar.Position = [0.554830508474576, 0.025099075297225895]
tMP2mabovegroundLUTColorBar.Position2 = [0.4299999999999997, 0.1199999999999997]
tMP2mabovegroundLUTColorBar.Orientation = 'Horizontal'
tMP2mabovegroundLUTColorBar.Title = 'TMP_2maboveground'
tMP2mabovegroundLUTColorBar.ComponentTitle = ''
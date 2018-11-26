# state file generated using paraview version 4.4.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

import sys


def main():

    """
    main
    """

    if len(sys.argv) != 4 or sys.argv[0] == "-h" or sys.argv[0] == "--help":
        print("utilisation: pvpython "+sys.argv[0]+" nc_file temperature image_name")
        sys.exit(1)

    # Create a new 'Render View'
    renderView1 = CreateView('RenderView')
    renderView1.ViewSize = [1187, 758]
    renderView1.InteractionMode = '2D'
    renderView1.AxesGrid = 'GridAxes3DActor'
    renderView1.CenterOfRotation = [1.99999999998727, 46.45, 0.0]
    renderView1.StereoType = 0
    renderView1.CameraPosition = [1.98235180660451, 46.4521702639013, 10000.0]
    renderView1.CameraFocalPoint = [1.98235180660451, 46.4521702639013, 0.0]
    renderView1.CameraParallelScale = 8.99397123983744
    renderView1.Background = [0.32, 0.34, 0.43]

    # ----------------------------------------------------------------
    # setup the data processing pipelines
    # ----------------------------------------------------------------

    # create a new 'NetCDF Reader'
    previsionPour = NetCDFReader(FileName=sys.argv[1])
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
    contour1.Isosurfaces = [float(sys.argv[2])]
    contour1.PointMergeMethod = 'Uniform Binning'

    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------

    # get color transfer function/color map for 'TMP2maboveground'
    tMP2mabovegroundLUT = GetColorTransferFunction('TMP2maboveground')
    tMP2mabovegroundLUT.EnableOpacityMapping = 1
    tMP2mabovegroundLUT.RGBPoints = [255.672302246094, 0.231373, 0.298039, 0.752941, 280.3642883300781, 0.8627450980392157, 0.8666666666666667, 0.8666666666666667, 298.986755371094, 0.705882, 0.0156863, 0.14902]
    tMP2mabovegroundLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'TMP2maboveground'
    tMP2mabovegroundPWF = GetOpacityTransferFunction('TMP2maboveground')
    tMP2mabovegroundPWF.Points = [255.672302246094, 0.0, 0.5, 0.0, 258.98297119140625, 0.9276315569877625, 0.5, 0.0, 298.986755371094, 1.0, 0.5, 0.0]
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
    previsionPourDisplay.ScalarOpacityUnitDistance = 0.194190573529865

    # show color legend
    previsionPourDisplay.SetScalarBarVisibility(renderView1, True)

    # show data from contour1
    contour1Display = Show(contour1, renderView1)
    # trace defaults for the display properties.
    contour1Display.ColorArrayName = [None, '']

    # setup the color legend parameters for each legend in this view

    # get color legend/bar for tMP2mabovegroundLUT in view renderView1
    tMP2mabovegroundLUTColorBar = GetScalarBar(tMP2mabovegroundLUT, renderView1)
    tMP2mabovegroundLUTColorBar.Position = [0.554830508474576, 0.0250990752972259]
    tMP2mabovegroundLUTColorBar.Position2 = [0.43, 0.12]
    tMP2mabovegroundLUTColorBar.Orientation = 'Horizontal'
    tMP2mabovegroundLUTColorBar.Title = 'TMP_2maboveground'
    tMP2mabovegroundLUTColorBar.ComponentTitle = ''

    WriteImage(sys.argv[3])

    print(sys.argv[3]+" generated")

main()

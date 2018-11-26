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

    if len(sys.argv) != 3 or sys.argv[0] == "-h" or sys.argv[0] == "--help":
        print("utilisation: pvpython "+sys.argv[0]+" nc_file image_name")
        sys.exit(1)


    # Create a new 'Render View'
    renderView1 = CreateView('RenderView')
    renderView1.ViewSize = [1184, 758]
    renderView1.InteractionMode = '2D'
    renderView1.AxesGrid = 'GridAxes3DActor'
    renderView1.CenterOfRotation = [1.99999999998727, 46.45, 0.0]
    renderView1.StereoType = 0
    renderView1.CameraPosition = [1.9422626695178127, 46.43398743808001, 10000.0]
    renderView1.CameraFocalPoint = [1.9422626695178127, 46.43398743808001, 0.0]
    renderView1.CameraParallelScale = 8.992676317018041
    renderView1.Background = [0.32, 0.34, 0.43]

    # ----------------------------------------------------------------
    # setup the data processing pipelines
    # ----------------------------------------------------------------

    # create a new 'NetCDF Reader'
    previsionPour = NetCDFReader(FileName=sys.argv[1])
    previsionPour.Dimensions = '(latitude, longitude)'
    previsionPour.SphericalCoordinates = 0
    previsionPour.ReplaceFillValueWithNan = 1

    # create a new 'Calculator'
    calculator1 = Calculator(Input=previsionPour)
    calculator1.ResultArrayName = 'WindSpeed'
    calculator1.Function = 'UGRD_10maboveground*iHat+VGRD_10maboveground*jHat'

    # create a new 'Stream Tracer'
    streamTracer1 = StreamTracer(Input=calculator1,
        SeedType='Point Source')
    streamTracer1.Vectors = ['POINTS', 'WindSpeed']
    streamTracer1.MaximumStreamlineLength = 27.159999999975298

    # init the 'Point Source' selected for 'SeedType'
    streamTracer1.SeedType.Center = [2.024961986126652, 46.49992397227883, 0.0]
    streamTracer1.SeedType.NumberOfPoints = 400000
    streamTracer1.SeedType.Radius = 10.0

    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------

    # get color transfer function/color map for 'TMP2maboveground'
    tMP2mabovegroundLUT = GetColorTransferFunction('TMP2maboveground')
    tMP2mabovegroundLUT.EnableOpacityMapping = 1
    tMP2mabovegroundLUT.RGBPoints = [261.0631103515625, 0.231373, 0.298039, 0.752941, 262.284912109375, 0.26666666666666666, 0.35294117647058826, 0.8, 278.5015869140625, 0.865003, 0.865003, 0.865003, 295.9400634765625, 0.705882, 0.0156863, 0.14902]
    tMP2mabovegroundLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'TMP2maboveground'
    tMP2mabovegroundPWF = GetOpacityTransferFunction('TMP2maboveground')
    tMP2mabovegroundPWF.Points = [261.0631103515625, 0.0, 0.5, 0.0, 262.0627746582031, 1.0, 0.5, 0.0, 295.9400634765625, 1.0, 0.5, 0.0]
    tMP2mabovegroundPWF.ScalarRangeInitialized = 1

    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView1'
    # ----------------------------------------------------------------

    # show data from calculator1
    calculator1Display = Show(calculator1, renderView1)
    # trace defaults for the display properties.
    calculator1Display.Representation = 'Slice'
    calculator1Display.ColorArrayName = ['POINTS', 'TMP_2maboveground']
    calculator1Display.LookupTable = tMP2mabovegroundLUT
    calculator1Display.ScalarOpacityUnitDistance = 0.194190573529865

    # show color legend
    calculator1Display.SetScalarBarVisibility(renderView1, True)

    # show data from streamTracer1
    streamTracer1Display = Show(streamTracer1, renderView1)
    # trace defaults for the display properties.
    streamTracer1Display.ColorArrayName = [None, '']

    # setup the color legend parameters for each legend in this view

    # get color legend/bar for tMP2mabovegroundLUT in view renderView1
    tMP2mabovegroundLUTColorBar = GetScalarBar(tMP2mabovegroundLUT, renderView1)
    tMP2mabovegroundLUTColorBar.Position = [0.560159105277418, 0.154557463672391]
    tMP2mabovegroundLUTColorBar.Position2 = [0.43, 0.12]
    tMP2mabovegroundLUTColorBar.Orientation = 'Horizontal'
    tMP2mabovegroundLUTColorBar.Title = 'TMP_2maboveground'
    tMP2mabovegroundLUTColorBar.ComponentTitle = ''

    WriteImage(sys.argv[2])

    print(sys.argv[2]+" generated")

main()

# yaq-labview 

This repository contains VIs, test VIs, and python scripts for interfacing the yaq library 
with LabVIEW.


### Installation

To install, either copy the volume of and run the installer.exe or `git clone` the repository to a folder of
your choice.  The installer will automatically install the VIs + python script components of yaq
into the default LabVIEW `instr.lib` folder.


### Requirements

You will likely need to create a specific conda environment with the following Python packages installed:

* `pip install numpy==1.21.6` or less
* `conda install yaqc`
* `conda install yaqd-core`
* (optional) `conda install yaqd-control`

The filepath to the Python executable associated with this environment will be needed to start using the
yaq-labview library.

Then, you will need a separate environment in which yaqd-core and the yaqd daemons from this repository
are installed.  You will need yaqd-control to run the yaqd VIs but it can be associated with this
2nd environment if needed.

It was found that conda installed NumPy packages would not work with LabVIEW's Python Node
VIs.  Also, many conda packages attempt to overwrite the PyPi package with a conda-forge version of NumPy...
these versions also will not work with the Python Node VIs and uninstalls may break the environment.  It is
therefore recommended that no other packages be installed into this specific environment.


### About the Library

Information about the yaq project may be found at http://yaq.fyi  .  The yaq protocol works by instancing Client objects
to daemons installed on a host computer.   The yaq-labview code sets and gets public properties from these objects,
including measuring and setting positions on devices to which the daemons are connected.   The yaq-labview library of VIs is 
hierarchically arranged by traits, some of which the object may have inherited.  


### Tutorial:  test_yaqc_measure

Let's look at a test VI utilizing the yaq project, called test_yaqc_measure.  The two images refer to the LabVIEW front panel
and wire diagram of test_yaqc_measure.vi.

![test_yaqc_measure front panel](/test_yaqc_measure_frontpanel.png)

![test_yaqc_measure wire diagram](/test_yaqc_measure_wire_diagram.png)

This test VI makes use of the yaqd-seabreeze daemon (https://github.com/yaq-project/yaqd-seabreeze) associated with the
Ocean Optics USB2000 spectrometer.  

For the front panel, the port and paths at top need to be filled in before the VI is run.  It is presumed that the
USB2000 is installed on the local computer.  If you have a USB2000 and installed the necessary drivers and yaqd daemon, the port
is that found on configuring the daemon or by performing `yaqd list` at an Anaconda prompt with yaqd-control installed.
The path marked "python path" is the path to the Python executable mentioned above.  The Python Module Path is the path to
yaqc_labview.py, which is the python script found as part of this repository.    

The wire diagram starts at left by opening a Python session, then instantiating a USB2000 Client object at the seabreeze port.  This
client object (as well as the session, module path, and error cluster) is passed to yaq's Get Channel Names, which is 
essentially the LabVIEW version of `Client.get_channel_names()`.   The first element of the channel names is taken out and used in
the next VI,  Get Channel Map.   This VI returns the mapping of a measured data associated with the first channel, i.e. it 
provides the user the "X-axis" of information related to the data.   An uninitialized 1D array is fed into the input to tell LabVIEW
that the expected output of the map is 1-dimensional, which is the case for the USB2000 as it is a 1D-array spectrometer. This
information is fed into the continuous data acquisition loop.

The loop simply requests a start of measurement through the yaqc_measure.vi.  Then an internal loop polls the busy aspect of the 
daemon (yaqc_busy.vi).  When False it is presumed it has completed measurement, and so the loop ends and a yaqc_get_measured.vim is
called to obtain the resulting data.  Again, the uninitialized 1D array is fed into the VI to tell LabVIEW that the resulting data
(the "Y" values) is 1-D.  Finally, the two arrays are combined and plotted. The loop restarts until Stop is pressed.

The final two VIs close the object and python session cleanly.


### Customization

The yaq library does not contain specific Client properties to specialized daemons.   These daemons may have additional features
for modifying the behavior of a device connected to it.  Should you wish to make such specialized yaq VIs, it is hoped that the 
examination of the python script and VIs in this library will provide the insight necessary to develop them.

The LabVIEW Python Node framework is currently unable to support Python dictionary (LabVIEW map) inputs and outputs, and so
yaq VIs developed so far are limited to returning values of a specific key.  Also, some of the yaq python returns consist
of arrays of arbitrary dimension.   In order to best utilize these methods, the VIs associated with them may need to adapt to the
dimensionality of an input and pass an error if an inappropriate dimensionality is used.  See LabVIEW discussions on malleable
VIs to determine if this adaptation method can be utilized in your specific project or if you need VIs for each dimension.
(For example, malleable VIs cannot be integrated into packed libraries.)   


## Author

@kameyer226

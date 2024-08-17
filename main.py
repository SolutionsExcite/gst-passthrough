import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib

# Initialize GStreamer
Gst.init(None)

# Create the pipeline
pipeline = Gst.Pipeline()

# Create the elements
src = Gst.ElementFactory.make("v4l2src", "source")
capsfilter1 = Gst.ElementFactory.make("capsfilter", "capsfilter1")
videoscale = Gst.ElementFactory.make("videoscale", "videoscale")
capsfilter2 = Gst.ElementFactory.make("capsfilter", "capsfilter2")
sink = Gst.ElementFactory.make("glimagesink", "sink")

# Set the device property on the source element
src.set_property("device", "/dev/video0")

# Set the caps for the first capsfilter
caps1 = Gst.Caps.from_string("video/x-raw,width=1920,height=1080")
capsfilter1.set_property("caps", caps1)

# Set the caps for the second capsfilter
caps2 = Gst.Caps.from_string("video/x-raw,width=1920,height=1080")
capsfilter2.set_property("caps", caps2)

# Add all elements to the pipeline
pipeline.add(src)
pipeline.add(capsfilter1)
pipeline.add(videoscale)
pipeline.add(capsfilter2)
pipeline.add(sink)

# Link the elements
src.link(capsfilter1)
capsfilter1.link(videoscale)
videoscale.link(capsfilter2)
capsfilter2.link(sink)

# Start playing
pipeline.set_state(Gst.State.PLAYING)

# Run the main loop
loop = GLib.MainLoop()
try:
    loop.run()
except KeyboardInterrupt:
    pass

# Stop playing and release resources
pipeline.set_state(Gst.State.NULL)
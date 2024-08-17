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
tee = Gst.ElementFactory.make("tee", "tee")
queue1 = Gst.ElementFactory.make("queue", "queue1")
queue2 = Gst.ElementFactory.make("queue", "queue2")
sink = Gst.ElementFactory.make("glimagesink", "sink")
encoder = Gst.ElementFactory.make("mpph265enc", "encoder")
parser = Gst.ElementFactory.make("h265parse", "parser")
muxer = Gst.ElementFactory.make("matroskamux", "muxer")
filesink = Gst.ElementFactory.make("filesink", "filesink")

# Set properties
src.set_property("device", "/dev/video0")
caps1 = Gst.Caps.from_string("video/x-raw,width=1920,height=1080")
capsfilter1.set_property("caps", caps1)
caps2 = Gst.Caps.from_string("video/x-raw,width=1920,height=1080")
capsfilter2.set_property("caps", caps2)
filesink.set_property("location", "output.mkv")

# Add all elements to the pipeline
elements = [src, capsfilter1, videoscale, capsfilter2, tee, queue1, queue2, 
            sink, encoder, parser, muxer, filesink]
for element in elements:
    pipeline.add(element)

# Link the elements
src.link(capsfilter1)
capsfilter1.link(videoscale)
videoscale.link(capsfilter2)
capsfilter2.link(tee)

# Link one branch of the tee to the display sink
tee.link(queue1)
queue1.link(sink)

# Link the other branch of the tee to the encoder, parser, muxer, and file output
tee.link(queue2)
queue2.link(encoder)
encoder.link(parser)
parser.link(muxer)
muxer.link(filesink)

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
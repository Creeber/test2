from __future__ import annotations
from typing import List, Tuple, Union, Any, Optional
"""
<h3>image - BINARY</h3><p>BINARY (bitmap) pixel format. Each pixel is 1-bit.</p>
"""
BINARY: int = None
"""
<h3>image - GRAYSCALE</h3><p>GRAYSCALE pixel format. Each pixel is 8-bits, 1-byte.</p>
"""
GRAYSCALE: int = None
"""
<h3>image - RGB565</h3><p>RGB565 pixel format. Each pixel is 16-bits, 2-bytes. 5-bits are used for red, 6-bits are used for green, and 5-bits are used for blue.</p>
"""
RGB565: int = None
"""
<h3>image - BAYER</h3><p>RAW BAYER image pixel format. If you try to make the frame size too big to fit in the frame buffer your OpenMV Cam will set the pixel format to BAYER so that you can capture images but no image processing methods will be operational.</p>
"""
BAYER: int = None
"""
<h3>image - YUV422</h3><p>A pixel format that is very easy to jpeg compress. Each pixel is stored as a grayscale 8-bit Y value followed by alternating 8-bit U/V color values that are shared between two Y values (8-bits Y1, 8-bits U, 8-bits Y2, 8-bits V, etc.). Only some image processing methods work with YUV422.</p>
"""
YUV422: int = None
"""
<h3>image - JPEG</h3><p>A JPEG image.</p>
"""
JPEG: int = None
"""
<h3>image - PNG</h3><p>A PNG image.</p>
"""
PNG: int = None
"""
<h3>image - PALETTE_RAINBOW</h3><p>Default OpenMV Cam color palette for thermal images using a smooth color wheel.</p>
"""
PALETTE_RAINBOW: int = None
"""
<h3>image - PALETTE_IRONBOW</h3><p>Makes images look like the FLIR Lepton thermal images using a very non-linear color palette.</p>
"""
PALETTE_IRONBOW: int = None
"""
<h3>image - PALETTE_DEPTH</h3><p>Depth color palette for depth images.</p>
"""
PALETTE_DEPTH: int = None
"""
<h3>image - PALETTE_EVT_DARK</h3><p>Dark background color palette for event images.</p>
"""
PALETTE_EVT_DARK: int = None
"""
<h3>image - PALETTE_EVT_LIGHT</h3><p>Light background color palette for event images.</p>
"""
PALETTE_EVT_LIGHT: int = None
"""
<h3>image - AREA</h3><p>Use area scaling when downscaling an image (Nearest Neighbor is used for upscaling).</p><p>You should use area scaling when downscaling for the highest visual quality.</p>
"""
AREA: int = None
"""
<h3>image - BILINEAR</h3><p>Use bilinear scaling when upscaling an image. This produces a good quality scaled image output and is fast.</p><p>When downscaling an image this method will subsample the input image to produce the downscaled image. Use <code>image.AREA</code> for the higest quality downscaling if speed is not an issue.</p>
"""
BILINEAR: int = None
"""
<h3>image - BICUBIC</h3><p>Use bicubic scaling when upscaling an image. This produces a high quality scaled image output, but is slow.</p><p>When downscaling an image this method will subsample the input image to produce the downscaled image. Use <code>image.AREA</code> for the higest quality downscaling if speed is not an issue.</p>
"""
BICUBIC: int = None
"""
<h3>image - VFLIP</h3><p>Vertically flip the image being drawn by <code>draw_image</code>.</p>
"""
VFLIP: int = None
"""
<h3>image - HMIRROR</h3><p>Horizontally mirror the image being drawn by <code>draw_image</code>.</p>
"""
HMIRROR: int = None
"""
<h3>image - TRANSPOSE</h3><p>Transpose (swap x/y) the image being draw by <code>draw_image</code>.</p>
"""
TRANSPOSE: int = None
"""
<h3>image - CENTER</h3><p>Center the image being drawn to the center of the image/canvas it’s being drawn on. Any x/y offsets passed will move the image being drawn from the center by that amount.</p>
"""
CENTER: int = None
"""
<h3>image - EXTRACT_RGB_CHANNEL_FIRST</h3><p>When extracting an RGB channel from an RGB image using <code>draw_image</code> extract the channel first before scaling versus afterwards to prevent any artifacts.</p>
"""
EXTRACT_RGB_CHANNEL_FIRST: int = None
"""
<h3>image - APPLY_COLOR_PALETTE_FIRST</h3><p>When applying a color lookup table to an image using <code>draw_image</code> apply the color look table first before scaling versus afterwards to prevent any artifacts.</p>
"""
APPLY_COLOR_PALETTE_FIRST: int = None
"""
<h3>image - SCALE_ASPECT_KEEP</h3><p>Scale the image being drawn to fit inside of the image/canvas being drawn on while maintaining the aspect ratio. Unless the image aspect ratios match the image being drawn will not completley cover the image/canvas being drawn on. Any x_scale/y_scale values passed will additionally scale the scaled image.</p>
"""
SCALE_ASPECT_KEEP: int = None
"""
<h3>image - SCALE_ASPECT_EXPAND</h3><p>Scale the image being drawn to fill image/canvas being drawn on while maintaining the aspect ratio. Unless the image aspect ratios match the image being drawn will be cropped. Any x_scale/y_scale values passed will additionally scale the scaled image.</p>
"""
SCALE_ASPECT_EXPAND: int = None
"""
<h3>image - SCALE_ASPECT_IGNORE</h3><p>Scale the image being drawn to fill the image/canvas being drawn on. This does not maintain the aspect ratio of the image being drawn. Any x_scale/y_scale values passed will additionally scale the scaled image.</p>
"""
SCALE_ASPECT_IGNORE: int = None
"""
<h3>image - BLACK_BACKGROUND</h3><p>Speeds up <code>draw_image</code> when drawing on a black destination image when using alpha effects that require reading both source and destination pixels. This skips reading the destination pixel.</p>
"""
BLACK_BACKGROUND: int = None
"""
<h3>image - ROTATE_90</h3><p>Rotate the image by 90 degrees (this is just <code>image.VFLIP</code> ORed with <code>image.TRANSPOSE</code>).</p>
"""
ROTATE_90: int = None
"""
<h3>image - ROTATE_180</h3><p>Rotate the image by 180 degrees (this is just <code>image.HMIRROR</code> ORed with <code>image.VFLIP</code>).</p>
"""
ROTATE_180: int = None
"""
<h3>image - ROTATE_270</h3><p>Rotate the image by 270 degrees (this is just <code>image.HMIRROR</code> ORed with <code>image.TRANSPOSE</code>).</p>
"""
ROTATE_270: int = None
"""
<h3>image - JPEG_SUBSAMPLING_AUTO</h3><p>Automatically select the best JPEG subsampling based on the image quality parameter.</p>
"""
JPEG_SUBSAMPLING_AUTO: int = None
"""
<h3>image - JPEG_SUBSAMPLING_444</h3><p>Use 4:4:4 JPEG subsampling.</p>
"""
JPEG_SUBSAMPLING_444: int = None
"""
<h3>image - JPEG_SUBSAMPLING_422</h3><p>Use 4:2:2 JPEG subsampling. Note, you should force the jpeg subsampling to be 4:2:2 if you are streaming video via MJPEG for the best compatibility with third-party video players.</p>
"""
JPEG_SUBSAMPLING_422: int = None
"""
<h3>image - JPEG_SUBSAMPLING_420</h3><p>Use 4:2:0 JPEG subsampling.</p>
"""
JPEG_SUBSAMPLING_420: int = None
"""
<h3>image - SEARCH_EX</h3><p>Exhaustive template matching search.</p>
"""
SEARCH_EX: int = None
"""
<h3>image - SEARCH_DS</h3><p>Faster template matching search.</p>
"""
SEARCH_DS: int = None
"""
<h3>image - EDGE_CANNY</h3><p>Use the canny edge detection algorithm for doing edge detection on an image.</p>
"""
EDGE_CANNY: int = None
"""
<h3>image - EDGE_SIMPLE</h3><p>Use a simple thresholded high pass filter algorithm for doing edge detection on an image.</p>
"""
EDGE_SIMPLE: int = None
"""
<h3>image - CORNER_FAST</h3><p>Faster and less accurate corner detection algorithm for ORB keypoints.</p>
"""
CORNER_FAST: int = None
"""
<h3>image - CORNER_AGAST</h3><p>Slower and more accurate corner detection algorithm for ORB keypoints.</p>
"""
CORNER_AGAST: int = None
"""
<h3>image - TAG16H5</h3><p>TAG1H5 tag family bit mask enum. Used for AprilTags.</p>
"""
TAG16H5: int = None
"""
<h3>image - TAG25H7</h3><p>TAG25H7 tag family bit mask enum. Used for AprilTags.</p>
"""
TAG25H7: int = None
"""
<h3>image - TAG25H9</h3><p>TAG25H9 tag family bit mask enum. Used for AprilTags.</p>
"""
TAG25H9: int = None
"""
<h3>image - TAG36H10</h3><p>TAG36H10 tag family bit mask enum. Used for AprilTags.</p>
"""
TAG36H10: int = None
"""
<h3>image - TAG36H11</h3><p>TAG36H11 tag family bit mask enum. Used for AprilTags.</p>
"""
TAG36H11: int = None
"""
<h3>image - ARTOOLKIT</h3><p>ARTOOLKIT tag family bit mask enum. Used for AprilTags.</p>
"""
ARTOOLKIT: int = None
"""
<h3>image - EAN2</h3><p>EAN2 barcode type enum.</p>
"""
EAN2: int = None
"""
<h3>image - EAN5</h3><p>EAN5 barcode type enum.</p>
"""
EAN5: int = None
"""
<h3>image - EAN8</h3><p>EAN8 barcode type enum.</p>
"""
EAN8: int = None
"""
<h3>image - UPCE</h3><p>UPCE barcode type enum.</p>
"""
UPCE: int = None
"""
<h3>image - ISBN10</h3><p>ISBN10 barcode type enum.</p>
"""
ISBN10: int = None
"""
<h3>image - UPCA</h3><p>UPCA barcode type enum.</p>
"""
UPCA: int = None
"""
<h3>image - EAN13</h3><p>EAN13 barcode type enum.</p>
"""
EAN13: int = None
"""
<h3>image - ISBN13</h3><p>ISBN13 barcode type enum.</p>
"""
ISBN13: int = None
"""
<h3>image - I25</h3><p>I25 barcode type enum.</p>
"""
I25: int = None
"""
<h3>image - DATABAR</h3><p>DATABAR barcode type enum.</p>
"""
DATABAR: int = None
"""
<h3>image - DATABAR_EXP</h3><p>DATABAR_EXP barcode type enum.</p>
"""
DATABAR_EXP: int = None
"""
<h3>image - CODABAR</h3><p>CODABAR barcode type enum.</p>
"""
CODABAR: int = None
"""
<h3>image - CODE39</h3><p>CODE39 barcode type enum.</p>
"""
CODE39: int = None
"""
<h3>image - PDF417</h3><p>PDF417 barcode type enum - Future (e.g. doesn’t work right now).</p>
"""
PDF417: int = None
"""
<h3>image - CODE93</h3><p>CODE93 barcode type enum.</p>
"""
CODE93: int = None
"""
<h3>image - CODE128</h3><p>CODE128 barcode type enum.</p>
"""
CODE128: int = None
def binary_to_grayscale(binary_image_value:0|1) -> int:
	"""
	<h3>image - binary_to_grayscale(binary_image_value: 0 | 1)</h3><p>Returns a converted binary value (0-1) to a grayscale value (0-255).</p>
	"""
	pass
def binary_to_rgb(binary_image_value:0|1) -> Tuple[int,int,int]:
	"""
	<h3>image - binary_to_rgb(binary_image_value: 0 | 1)</h3><p>Returns a converted binary value (0-1) to a 3 value RGB888 tuple.</p>
	"""
	pass
def binary_to_lab(binary_image_value:0|1) -> Tuple[int,int,int]:
	"""
	<h3>image - binary_to_lab(binary_image_value: 0 | 1)</h3><p>Returns a converted binary value (0-1) to a 3 value LAB tuple.</p><p>L goes between 0 and 100 and A/B go from -128 to 128.</p>
	"""
	pass
def binary_to_yuv(binary_image_value:0|1) -> Tuple[int,int,int]:
	"""
	<h3>image - binary_to_yuv(binary_image_value: 0 | 1)</h3><p>Returns a converted binary value (0-1) to a 3 value YUV tuple.</p><p>Y goes between 0 and 255 and U/V go from -128 to 128.</p>
	"""
	pass
def grayscale_to_binary(grayscale_value:int) -> 0|1:
	"""
	<h3>image - grayscale_to_binary(grayscale_value: int)</h3><p>Returns a converted grayscale value (0-255) to a binary value (0-1).</p>
	"""
	pass
def grayscale_to_rgb(grayscale_value:int) -> Tuple[int,int,int]:
	"""
	<h3>image - grayscale_to_rgb(grayscale_value: int)</h3><p>Returns a converted grayscale value to a 3 value RGB888 tuple.</p><div><p>Note</p><p>The OpenMV Cam firmware does the conversion using a RGB565-&gt;RGB888 process so this method won’t return the exact values as a pure RGB888 system would. However, it’s true to how the image lib works internally.</p></div>
	"""
	pass
def grayscale_to_lab(grayscale_value:int) -> Tuple[int,int,int]:
	"""
	<h3>image - grayscale_to_lab(grayscale_value: int)</h3><p>Returns a converted grayscale value to a 3 value LAB tuple.</p><p>L goes between 0 and 100 and A/B go from -128 to 128.</p><div><p>Note</p><p>The OpenMV Cam firmware does the conversion using a RGB565-&gt;LAB process so this method won’t return the exact values as a pure LAB system would. However, it’s true to how the image lib works internally.</p></div>
	"""
	pass
def grayscale_to_yuv(grayscale_value:int) -> Tuple[int,int,int]:
	"""
	<h3>image - grayscale_to_yuv(grayscale_value: int)</h3><p>Returns a converted grayscale value to a 3 value YUV tuple.</p><p>Y goes between 0 and 255 and U/V go from -128 to 128.</p><div><p>Note</p><p>The OpenMV Cam firmware does the conversion using a RGB565-&gt;YUV process so this method won’t return the exact values as a pure YUV system would. However, it’s true to how the image lib works internally.</p></div>
	"""
	pass
def rgb_to_binary(rgb_tuple:Tuple[int,int,int]) -> 0|1:
	"""
	<h3>image - rgb_to_binary(rgb_tuple: Tuple[int, int, int])</h3><p>Returns a converted 3 value RGB888 tuple to a center range thresholded binary value (0-1).</p><div><p>Note</p><p>The OpenMV Cam firmware does the conversion using a RGB888-&gt;RGB565 process so this method won’t return the exact values as a pure RGB888 system would. However, it’s true to how the image lib works internally.</p></div>
	"""
	pass
def rgb_to_grayscale(rgb_tuple:Tuple[int,int,int]) -> int:
	"""
	<h3>image - rgb_to_grayscale(rgb_tuple: Tuple[int, int, int])</h3><p>Returns a converted 3 value RGB888 tuple to a grayscale value (0-255).</p><div><p>Note</p><p>The OpenMV Cam firmware does the conversion using a RGB888-&gt;RGB565 process so this method won’t return the exact values as a pure RGB888 system would. However, it’s true to how the image lib works internally.</p></div>
	"""
	pass
def rgb_to_lab(rgb_tuple:Tuple[int,int,int]) -> Tuple[int,int,int]:
	"""
	<h3>image - rgb_to_lab(rgb_tuple: Tuple[int, int, int])</h3><p>Returns a converted 3 value RGB888 tuple to a 3 value LAB tuple.</p><p>L goes between 0 and 100 and A/B go from -128 to 128.</p><div><p>Note</p><p>The OpenMV Cam firmware does the conversion using a RGB888-&gt;RGB565 process so this method won’t return the exact values as a pure RGB888 system would. However, it’s true to how the image lib works internally.</p></div>
	"""
	pass
def rgb_to_yuv(rgb_tuple:Tuple[int,int,int]) -> Tuple[int,int,int]:
	"""
	<h3>image - rgb_to_yuv(rgb_tuple: Tuple[int, int, int])</h3><p>Returns a converted 3 value RGB888 tuple to a 3 value YUV tuple.</p><p>Y goes between 0 and 255 and U/V go from -128 to 128.</p><div><p>Note</p><p>The OpenMV Cam firmware does the conversion using a RGB888-&gt;RGB565 process so this method won’t return the exact values as a pure RGB888 system would. However, it’s true to how the image lib works internally.</p></div>
	"""
	pass
def lab_to_binary(lab_tuple:Tuple[int,int,int]) -> 0|1:
	"""
	<h3>image - lab_to_binary(lab_tuple: Tuple[int, int, int])</h3><p>Returns a converted 3 value LAB tuple to a center range thresholded binary value (0-1).</p><div><p>Note</p><p>The OpenMV Cam firmware does the conversion using a LAB-&gt;RGB565 process so this method won’t return the exact values as a pure LAB system would. However, it’s true to how the image lib works internally.</p></div>
	"""
	pass
def lab_to_grayscale(lab_tuple:Tuple[int,int,int]) -> int:
	"""
	<h3>image - lab_to_grayscale(lab_tuple: Tuple[int, int, int])</h3><p>Returns a converted 3 value LAB tuple to a grayscale value (0-255).</p><div><p>Note</p><p>The OpenMV Cam firmware does the conversion using a LAB-&gt;RGB565 process so this method won’t return the exact values as a pure LAB system would. However, it’s true to how the image lib works internally.</p></div>
	"""
	pass
def lab_to_rgb(lab_tuple:Tuple[int,int,int]) -> Tuple[int,int,int]:
	"""
	<h3>image - lab_to_rgb(lab_tuple: Tuple[int, int, int])</h3><p>Returns a converted 3 value LAB tuple to a 3 value RGB888 tuple.</p><div><p>Note</p><p>The OpenMV Cam firmware does the conversion using a LAB-&gt;RGB565 process so this method won’t return the exact values as a pure LAB system would. However, it’s true to how the image lib works internally.</p></div>
	"""
	pass
def lab_to_yuv(lab_tuple:Tuple[int,int,int]) -> Tuple[int,int,int]:
	"""
	<h3>image - lab_to_yuv(lab_tuple: Tuple[int, int, int])</h3><p>Returns a converted 3 value LAB tuple to a 3 value YUV tuple.</p><p>Y goes between 0 and 255 and U/V go from -128 to 128.</p><div><p>Note</p><p>The OpenMV Cam firmware does the conversion using a LAB-&gt;RGB565 process so this method won’t return the exact values as a pure LAB system would. However, it’s true to how the image lib works internally.</p></div>
	"""
	pass
def yuv_to_binary(yuv_tuple:Tuple[int,int,int]) -> 0|1:
	"""
	<h3>image - yuv_to_binary(yuv_tuple: Tuple[int, int, int])</h3><p>Returns a converted 3 value YUV tuple to a center range thresholded binary value (0-1).</p><div><p>Note</p><p>The OpenMV Cam firmware does the conversion using a YUV-&gt;RGB565 process so this method won’t return the exact values as a pure YUV system would. However, it’s true to how the image lib works internally.</p></div>
	"""
	pass
def yuv_to_grayscale(yuv_tuple:Tuple[int,int,int]) -> int:
	"""
	<h3>image - yuv_to_grayscale(yuv_tuple: Tuple[int, int, int])</h3><p>Returns a converted 3 value YUV tuple to a grayscale value (0-255).</p><div><p>Note</p><p>The OpenMV Cam firmware does the conversion using a YUV-&gt;RGB565 process so this method won’t return the exact values as a pure YUV system would. However, it’s true to how the image lib works internally.</p></div>
	"""
	pass
def yuv_to_rgb(lab_tuple:Tuple[int,int,int]) -> Tuple[int,int,int]:
	"""
	<h3>image - yuv_to_rgb(lab_tuple: Tuple[int, int, int])</h3><p>Returns a converted 3 value YUV tuple to a 3 value RGB888 tuple.</p><div><p>Note</p><p>The OpenMV Cam firmware does the conversion using a YUV-&gt;RGB565 process so this method won’t return the exact values as a pure YUV system would. However, it’s true to how the image lib works internally.</p></div>
	"""
	pass
def yuv_to_lab(yuv_tuple:Tuple[int,int,int]) -> Tuple[int,int,int]:
	"""
	<h3>image - yuv_to_lab(yuv_tuple: Tuple[int, int, int])</h3><p>Returns a converted 3 value YUV tuple to a 3 value LAB tuple.</p><p>L goes between 0 and 100 and A/B go from -128 to 128.</p><div><p>Note</p><p>The OpenMV Cam firmware does the conversion using a YUV-&gt;RGB565 process so this method won’t return the exact values as a pure YUV system would. However, it’s true to how the image lib works internally.</p></div>
	"""
	pass
def load_decriptor(path:str):
	"""
	<h3>image - load_decriptor(path: str)</h3><p>Loads a descriptor object from disk.</p><p><code>path</code> is the path to the descriptor file to load.</p>
	"""
	pass
def save_descriptor(path:str, descriptor):
	"""
	<h3>image - save_descriptor(path: str, descriptor)</h3><p>Saves the descriptor object <code>descriptor</code> to disk.</p><p><code>path</code> is the path to the descriptor file to save.</p>
	"""
	pass
def match_descriptor(descritor0, descriptor1, threshold=70, filter_outliers=False):
	"""
	<h3>image - match_descriptor(descritor0, descriptor1, threshold=70, filter_outliers=False)</h3><p>For LBP descriptors this function returns an integer representing the difference between the two descriptors. You may then threshold/compare this distance metric as necessary. The distance is a measure of similarity. The closer it is to zero the better the LBP keypoint match.</p><p>For ORB descriptors this function returns the <code>kptmatch</code> object. See above.</p><p><code>threshold</code> is used for ORB keypoints to filter ambiguous matches. A lower <code>threshold</code> value tightens the keypoint matching algorithm. <code>threshold</code> may be between 0-100 (int). Defaults to 70.</p><p><code>filter_outliers</code> is used for ORB keypoints to filter out outlier keypoints allow you to raise the <code>threshold</code>. Defaults to False.</p>
	"""
	pass
class HaarCascade:
	def __init__(self, path:str, stages:int|None=None):
		"""
		<h3>image - HaarCascade(path: str, stages: int | None = None)</h3><p>Loads a Haar Cascade into memory from a Haar Cascade binary file formatted for your OpenMV Cam. If you pass “frontalface” instead of a path then this constructor will load the built-in frontal face Haar Cascade into memory. Additionally, you can also pass “eye” to load a Haar Cascade for eyes into memory. Finally, this method returns the loaded Haar Cascade object for use with <code>Image.find_features()</code>.</p><p><code>stages</code> defaults to the number of stages in the Haar Cascade. However, you can specify a lower number of stages to speed up processing the feature detector at the cost of a higher rate of false positives.</p><div><p>Note</p><p>You can make your own Haar Cascades to use with your OpenMV Cam. First, Google for “&lt;thing&gt; Haar Cascade” to see if someone already made an OpenCV Haar Cascade for an object you want to detect. If not… then you’ll have to generate your own (which is a lot of work). See here for how to make your own Haar Cascade. Then see this script for converting OpenCV Haar Cascades into a format your OpenMV Cam can read.</p></div><p>Q: What is a Haar Cascade?</p><p>A: A Haar Cascade is a series of contrast checks that are used to determine if an object is present in the image. The contrast checks are split of into stages where a stage is only run if previous stages have already passed. The contrast checks are simple things like checking if the center vertical of the image is lighter than the edges. Large area checks are performed first in the earlier stages followed by more numerous and smaller area checks in later stages.</p><p>Q: How are Haar Cascades made?</p><p>A: Haar Cascades are made by training the generator algorithm against positive and negative labeled images. For example, you’d train the generator algorithm against hundreds of pictures with cats in them that have been labeled as images with cats and against hundreds of images with not cat like things labeled differently. The generator algorithm will then produce a Haar Cascade that detects cats.</p>
		"""
		pass
class Similarity:
	def __init__(self):
		"""
		<h3>image - Similarity</h3><p>Please call <code>Image.get_similarity()</code> to create this object.</p>
		"""
		pass
	def mean(self) -> float:
		"""
		<h3>image - Similarity.mean()</h3><p>Returns the mean of the similarity values computed across the image (float).</p><p>You may also get this value doing <code>[0]</code> on the object.</p>
		"""
		pass
	def stdev(self) -> float:
		"""
		<h3>image - Similarity.stdev()</h3><p>Returns the standard deviation of the similarity values computed across the image ( (float).</p><p>You may also get this value doing <code>[1]</code> on the object.</p>
		"""
		pass
	def min(self) -> float:
		"""
		<h3>image - Similarity.min()</h3><p>Returns the min of the similarity values computed across the image ( (float).</p><p>Generally, for the SSIM you want to threshold the min value to determine if two images are different.</p><p>You may also get this value doing <code>[2]</code> on the object.</p>
		"""
		pass
	def max(self) -> float:
		"""
		<h3>image - Similarity.max()</h3><p>Returns the max of the similarity values computed across the image ( (float).</p><p>Generally, for the DSIM you want to threshold the max value to determine if two images are different.</p><p>You may also get this value doing <code>[3]</code> on the object.</p>
		"""
		pass
class histogram:
	def __init__(self):
		"""
		<h3>image - histogram</h3><p>Please call <code>Image.get_histogram()</code> to create this object.</p>
		"""
		pass
	def bins(self) -> List[float]:
		"""
		<h3>image - histogram.bins()</h3><p>Returns a list of floats for the grayscale histogram.</p><p>You may also get this value doing <code>[0]</code> on the object.</p>
		"""
		pass
	def l_bins(self) -> List[float]:
		"""
		<h3>image - histogram.l_bins()</h3><p>Returns a list of floats for the RGB565 histogram LAB L channel.</p><p>You may also get this value doing <code>[0]</code> on the object.</p>
		"""
		pass
	def a_bins(self) -> List[float]:
		"""
		<h3>image - histogram.a_bins()</h3><p>Returns a list of floats for the RGB565 histogram LAB A channel.</p><p>You may also get this value doing <code>[1]</code> on the object.</p>
		"""
		pass
	def b_bins(self) -> List[float]:
		"""
		<h3>image - histogram.b_bins()</h3><p>Returns a list of floats for the RGB565 histogram LAB B channel.</p><p>You may also get this value doing <code>[2]</code> on the object.</p>
		"""
		pass
	def get_percentile(self, percentile) -> percentile:
		"""
		<h3>image - histogram.get_percentile(percentile)</h3><p>Computes the CDF of the histogram channels and returns a <code>image.percentile</code> object with the values of the histogram at the passed in <code>percentile</code> (0.0 - 1.0) (float). So, if you pass in 0.1 this method will tell you (going from left-to-right in the histogram) what bin when summed into an accumulator caused the accumulator to cross 0.1. This is useful to determine min (with 0.1) and max (with 0.9) of a color distribution without outlier effects ruining your results for adaptive color tracking.</p>
		"""
		pass
	def get_threshold(self) -> threshold:
		"""
		<h3>image - histogram.get_threshold()</h3><p>Uses Otsu’s Method to compute the optimal threshold values that split the histogram into two halves for each channel of the histogram. This method returns a <code>image.threshold</code> object. This method is particularly useful for determining optimal <code>Image.binary()</code> thresholds.</p>
		"""
		pass
	def get_statistics(self) -> statistics:
		"""
		<h3>image - histogram.get_statistics()</h3><p>Computes the mean, median, mode, standard deviation, min, max, lower quartile, and upper quartile of each color channel in the histogram and returns a <code>statistics</code> object.</p><p>You may also use <code>histogram.statistics()</code> and <code>histogram.get_stats()</code> as aliases for this method.</p>
		"""
		pass
class percentile:
	def __init__(self):
		"""
		<h3>image - percentile</h3><p>Please call <code>histogram.get_percentile()</code> to create this object.</p>
		"""
		pass
	def value(self) -> int:
		"""
		<h3>image - percentile.value()</h3><p>Return the grayscale percentile value (between 0 and 255).</p><p>You may also get this value doing <code>[0]</code> on the object.</p>
		"""
		pass
	def l_value(self) -> int:
		"""
		<h3>image - percentile.l_value()</h3><p>Return the RGB565 LAB L channel percentile value (between 0 and 100).</p><p>You may also get this value doing <code>[0]</code> on the object.</p>
		"""
		pass
	def a_value(self) -> int:
		"""
		<h3>image - percentile.a_value()</h3><p>Return the RGB565 LAB A channel percentile value (between -128 and 127).</p><p>You may also get this value doing <code>[1]</code> on the object.</p>
		"""
		pass
	def b_value(self) -> int:
		"""
		<h3>image - percentile.b_value()</h3><p>Return the RGB565 LAB B channel percentile value (between -128 and 127).</p><p>You may also get this value doing <code>[2]</code> on the object.</p>
		"""
		pass
class threshold:
	def __init__(self):
		"""
		<h3>image - threshold</h3><p>Please call <code>histogram.get_threshold()</code> to create this object.</p>
		"""
		pass
	def value(self) -> int:
		"""
		<h3>image - threshold.value()</h3><p>Return the grayscale threshold value (between 0 and 255).</p><p>You may also get this value doing <code>[0]</code> on the object.</p>
		"""
		pass
	def l_value(self) -> int:
		"""
		<h3>image - threshold.l_value()</h3><p>Return the RGB565 LAB L channel threshold value (between 0 and 100).</p><p>You may also get this value doing <code>[0]</code> on the object.</p>
		"""
		pass
	def a_value(self) -> int:
		"""
		<h3>image - threshold.a_value()</h3><p>Return the RGB565 LAB A channel threshold value (between -128 and 127).</p><p>You may also get this value doing <code>[1]</code> on the object.</p>
		"""
		pass
	def b_value(self) -> int:
		"""
		<h3>image - threshold.b_value()</h3><p>Return the RGB565 LAB B channel threshold value (between -128 and 127).</p><p>You may also get this value doing <code>[2]</code> on the object.</p>
		"""
		pass
class statistics:
	def __init__(self):
		"""
		<h3>image - statistics</h3><p>Please call <code>histogram.get_statistics()</code> or <code>Image.get_statistics()</code> to create this object.</p>
		"""
		pass
	def mean(self) -> int:
		"""
		<h3>image - statistics.mean()</h3><p>Returns the grayscale mean (0-255) (int).</p><p>You may also get this value doing <code>[0]</code> on the object.</p>
		"""
		pass
	def median(self) -> int:
		"""
		<h3>image - statistics.median()</h3><p>Returns the grayscale median (0-255) (int).</p><p>You may also get this value doing <code>[1]</code> on the object.</p>
		"""
		pass
	def mode(self) -> int:
		"""
		<h3>image - statistics.mode()</h3><p>Returns the grayscale mode (0-255) (int).</p><p>You may also get this value doing <code>[2]</code> on the object.</p>
		"""
		pass
	def stdev(self) -> int:
		"""
		<h3>image - statistics.stdev()</h3><p>Returns the grayscale standard deviation (0-255) (int).</p><p>You may also get this value doing <code>[3]</code> on the object.</p>
		"""
		pass
	def min(self) -> int:
		"""
		<h3>image - statistics.min()</h3><p>Returns the grayscale min (0-255) (int).</p><p>You may also get this value doing <code>[4]</code> on the object.</p>
		"""
		pass
	def max(self) -> int:
		"""
		<h3>image - statistics.max()</h3><p>Returns the grayscale max (0-255) (int).</p><p>You may also get this value doing <code>[5]</code> on the object.</p>
		"""
		pass
	def lq(self) -> int:
		"""
		<h3>image - statistics.lq()</h3><p>Returns the grayscale lower quartile (0-255) (int).</p><p>You may also get this value doing <code>[6]</code> on the object.</p>
		"""
		pass
	def uq(self) -> int:
		"""
		<h3>image - statistics.uq()</h3><p>Returns the grayscale upper quartile (0-255) (int).</p><p>You may also get this value doing <code>[7]</code> on the object.</p>
		"""
		pass
	def l_mean(self) -> int:
		"""
		<h3>image - statistics.l_mean()</h3><p>Returns the RGB565 LAB L mean (0-255) (int).</p><p>You may also get this value doing <code>[0]</code> on the object.</p>
		"""
		pass
	def l_median(self) -> int:
		"""
		<h3>image - statistics.l_median()</h3><p>Returns the RGB565 LAB L median (0-255) (int).</p><p>You may also get this value doing <code>[1]</code> on the object.</p>
		"""
		pass
	def l_mode(self) -> int:
		"""
		<h3>image - statistics.l_mode()</h3><p>Returns the RGB565 LAB L mode (0-255) (int).</p><p>You may also get this value doing <code>[2]</code> on the object.</p>
		"""
		pass
	def l_stdev(self) -> int:
		"""
		<h3>image - statistics.l_stdev()</h3><p>Returns the RGB565 LAB L standard deviation (0-255) (int).</p><p>You may also get this value doing <code>[3]</code> on the object.</p>
		"""
		pass
	def l_min(self) -> int:
		"""
		<h3>image - statistics.l_min()</h3><p>Returns the RGB565 LAB L min (0-255) (int).</p><p>You may also get this value doing <code>[4]</code> on the object.</p>
		"""
		pass
	def l_max(self) -> int:
		"""
		<h3>image - statistics.l_max()</h3><p>Returns the RGB565 LAB L max (0-255) (int).</p><p>You may also get this value doing <code>[5]</code> on the object.</p>
		"""
		pass
	def l_lq(self) -> int:
		"""
		<h3>image - statistics.l_lq()</h3><p>Returns the RGB565 LAB L lower quartile (0-255) (int).</p><p>You may also get this value doing <code>[6]</code> on the object.</p>
		"""
		pass
	def l_uq(self) -> int:
		"""
		<h3>image - statistics.l_uq()</h3><p>Returns the RGB565 LAB L upper quartile (0-255) (int).</p><p>You may also get this value doing <code>[7]</code> on the object.</p>
		"""
		pass
	def a_mean(self) -> int:
		"""
		<h3>image - statistics.a_mean()</h3><p>Returns the RGB565 LAB A mean (0-255) (int).</p><p>You may also get this value doing <code>[8]</code> on the object.</p>
		"""
		pass
	def a_median(self) -> int:
		"""
		<h3>image - statistics.a_median()</h3><p>Returns the RGB565 LAB A median (0-255) (int).</p><p>You may also get this value doing <code>[9]</code> on the object.</p>
		"""
		pass
	def a_mode(self) -> int:
		"""
		<h3>image - statistics.a_mode()</h3><p>Returns the RGB565 LAB A mode (0-255) (int).</p><p>You may also get this value doing <code>[10]</code> on the object.</p>
		"""
		pass
	def a_stdev(self) -> int:
		"""
		<h3>image - statistics.a_stdev()</h3><p>Returns the RGB565 LAB A standard deviation (0-255) (int).</p><p>You may also get this value doing <code>[11]</code> on the object.</p>
		"""
		pass
	def a_min(self) -> int:
		"""
		<h3>image - statistics.a_min()</h3><p>Returns the RGB565 LAB A min (0-255) (int).</p><p>You may also get this value doing <code>[12]</code> on the object.</p>
		"""
		pass
	def a_max(self) -> int:
		"""
		<h3>image - statistics.a_max()</h3><p>Returns the RGB565 LAB A max (0-255) (int).</p><p>You may also get this value doing <code>[13]</code> on the object.</p>
		"""
		pass
	def a_lq(self) -> int:
		"""
		<h3>image - statistics.a_lq()</h3><p>Returns the RGB565 LAB A lower quartile (0-255) (int).</p><p>You may also get this value doing <code>[14]</code> on the object.</p>
		"""
		pass
	def a_uq(self) -> int:
		"""
		<h3>image - statistics.a_uq()</h3><p>Returns the RGB565 LAB A upper quartile (0-255) (int).</p><p>You may also get this value doing <code>[15]</code> on the object.</p>
		"""
		pass
	def b_mean(self) -> int:
		"""
		<h3>image - statistics.b_mean()</h3><p>Returns the RGB565 LAB B mean (0-255) (int).</p><p>You may also get this value doing <code>[16]</code> on the object.</p>
		"""
		pass
	def b_median(self) -> int:
		"""
		<h3>image - statistics.b_median()</h3><p>Returns the RGB565 LAB B median (0-255) (int).</p><p>You may also get this value doing <code>[17]</code> on the object.</p>
		"""
		pass
	def b_mode(self) -> int:
		"""
		<h3>image - statistics.b_mode()</h3><p>Returns the RGB565 LAB B mode (0-255) (int).</p><p>You may also get this value doing <code>[18]</code> on the object.</p>
		"""
		pass
	def b_stdev(self) -> int:
		"""
		<h3>image - statistics.b_stdev()</h3><p>Returns the RGB565 LAB B standard deviation (0-255) (int).</p><p>You may also get this value doing <code>[19]</code> on the object.</p>
		"""
		pass
	def b_min(self) -> int:
		"""
		<h3>image - statistics.b_min()</h3><p>Returns the RGB565 LAB B min (0-255) (int).</p><p>You may also get this value doing <code>[20]</code> on the object.</p>
		"""
		pass
	def b_max(self) -> int:
		"""
		<h3>image - statistics.b_max()</h3><p>Returns the RGB565 LAB B max (0-255) (int).</p><p>You may also get this value doing <code>[21]</code> on the object.</p>
		"""
		pass
	def b_lq(self) -> int:
		"""
		<h3>image - statistics.b_lq()</h3><p>Returns the RGB565 LAB B lower quartile (0-255) (int).</p><p>You may also get this value doing <code>[22]</code> on the object.</p>
		"""
		pass
	def b_uq(self) -> int:
		"""
		<h3>image - statistics.b_uq()</h3><p>Returns the RGB565 LAB B upper quartile (0-255) (int).</p><p>You may also get this value doing <code>[23]</code> on the object.</p>
		"""
		pass
class blob:
	def __init__(self):
		"""
		<h3>image - blob</h3><p>Please call <code>Image.find_blobs()</code> to create this object.</p>
		"""
		pass
	def corners(self) -> List[Tuple[int,int]]:
		"""
		<h3>image - blob.corners()</h3><p>Returns a list of 4 (x,y) tuples of the 4 corners of the object. Corners are always returned in sorted clock-wise order starting from the top left.</p>
		"""
		pass
	def min_corners(self) -> List[Tuple[int,int]]:
		"""
		<h3>image - blob.min_corners()</h3><p>Returns a list of 4 (x,y) tuples of the 4 corners than bound the min area rectangle of the blob. Unlike <code>blob.corners()</code> the min area rectangle corners do not necessarily lie on the blob.</p>
		"""
		pass
	def rect(self) -> Tuple[int,int,int,int]:
		"""
		<h3>image - blob.rect()</h3><p>Returns a rectangle tuple (x, y, w, h) for use with other <code>image</code> methods like <code>Image.draw_rectangle()</code> of the blob’s bounding box.</p>
		"""
		pass
	def x(self) -> int:
		"""
		<h3>image - blob.x()</h3><p>Returns the blob’s bounding box x coordinate (int).</p><p>You may also get this value doing <code>[0]</code> on the object.</p>
		"""
		pass
	def y(self) -> int:
		"""
		<h3>image - blob.y()</h3><p>Returns the blob’s bounding box y coordinate (int).</p><p>You may also get this value doing <code>[1]</code> on the object.</p>
		"""
		pass
	def w(self) -> int:
		"""
		<h3>image - blob.w()</h3><p>Returns the blob’s bounding box w coordinate (int).</p><p>You may also get this value doing <code>[2]</code> on the object.</p>
		"""
		pass
	def h(self) -> int:
		"""
		<h3>image - blob.h()</h3><p>Returns the blob’s bounding box h coordinate (int).</p><p>You may also get this value doing <code>[3]</code> on the object.</p>
		"""
		pass
	def pixels(self) -> int:
		"""
		<h3>image - blob.pixels()</h3><p>Returns the number of pixels that are part of this blob (int).</p><p>You may also get this value doing <code>[4]</code> on the object.</p>
		"""
		pass
	def cx(self) -> int:
		"""
		<h3>image - blob.cx()</h3><p>Returns the centroid x position of the blob (int).</p><p>You may also get this value doing <code>[5]</code> on the object.</p>
		"""
		pass
	def cxf(self) -> int:
		"""
		<h3>image - blob.cxf()</h3><p>Returns the centroid x position of the blob (float).</p>
		"""
		pass
	def cy(self) -> int:
		"""
		<h3>image - blob.cy()</h3><p>Returns the centroid y position of the blob (int).</p><p>You may also get this value doing <code>[6]</code> on the object.</p>
		"""
		pass
	def cyf(self) -> int:
		"""
		<h3>image - blob.cyf()</h3><p>Returns the centroid y position of the blob (float).</p>
		"""
		pass
	def rotation(self) -> float:
		"""
		<h3>image - blob.rotation()</h3><p>Returns the rotation of the blob in radians (float). If the blob is like a pencil or pen this value will be unique for 0-180 degrees. If the blob is round this value is not useful.</p><p>You may also get this value doing <code>[7]</code> on the object.</p>
		"""
		pass
	def rotation_deg(self) -> float:
		"""
		<h3>image - blob.rotation_deg()</h3><p>Returns the rotation of the blob in degrees.</p>
		"""
		pass
	def rotation_rad(self) -> float:
		"""
		<h3>image - blob.rotation_rad()</h3><p>Returns the rotation of the blob in radians. This method is more descriptive than just <code>blob.rotation()</code>.</p>
		"""
		pass
	def code(self) -> int:
		"""
		<h3>image - blob.code()</h3><p>Returns a 32-bit binary number with a bit set in it for each color threshold that’s part of this blob. For example, if you passed <code>Image.find_blobs()</code> three color thresholds to look for then bits 0/1/2 may be set for this blob. Note that only one bit will be set for each blob unless <code>Image.find_blobs()</code> was called with <code>merge=True</code>. Then its possible for multiple blobs with different color thresholds to be merged together. You can use this method along with multiple thresholds to implement color code tracking.</p><p>You may also get this value doing <code>[8]</code> on the object.</p>
		"""
		pass
	def count(self) -> int:
		"""
		<h3>image - blob.count()</h3><p>Returns the number of blobs merged into this blob. This is 1 unless you called <code>Image.find_blobs()</code> with <code>merge=True</code>.</p><p>You may also get this value doing <code>[9]</code> on the object.</p>
		"""
		pass
	def perimeter(self) -> int:
		"""
		<h3>image - blob.perimeter()</h3><p>Returns the number of pixels on this blob’s perimeter.</p>
		"""
		pass
	def roundness(self) -> float:
		"""
		<h3>image - blob.roundness()</h3><p>Returns a value between 0 and 1 representing how round the object is. A circle would be a 1.</p>
		"""
		pass
	def elongation(self) -> float:
		"""
		<h3>image - blob.elongation()</h3><p>Returns a value between 0 and 1 representing how long (not round) the object is. A line would be a 1.</p>
		"""
		pass
	def area(self) -> int:
		"""
		<h3>image - blob.area()</h3><p>Returns the area of the bounding box around the blob. (w * h).</p>
		"""
		pass
	def density(self) -> float:
		"""
		<h3>image - blob.density()</h3><p>Returns the density ratio of the blob. This is the number of pixels in the blob over its bounding box area. A low density ratio means in general that the lock on the object isn’t very good. The result is between 0 and 1.</p>
		"""
		pass
	def extent(self) -> float:
		"""
		<h3>image - blob.extent()</h3><p>Alias for <code>blob.density()</code>.</p>
		"""
		pass
	def compactness(self) -> float:
		"""
		<h3>image - blob.compactness()</h3><p>Like <code>blob.density()</code>, but, uses the perimeter of the blob instead to measure the objects density and is thus more accurate. The result is between 0 and 1.</p>
		"""
		pass
	def solidity(self) -> float:
		"""
		<h3>image - blob.solidity()</h3><p>Like <code>blob.density()</code> but, uses the minimum area rotated rectangle versus the bounding rectangle to measure density. The result is between 0 and 1.</p>
		"""
		pass
	def convexity(self) -> float:
		"""
		<h3>image - blob.convexity()</h3><p>Returns a value between 0 and 1 representing how convex the object is. A square would be 1.</p>
		"""
		pass
	def x_hist_bins(self) -> List[float]:
		"""
		<h3>image - blob.x_hist_bins()</h3><p>Returns a histogram of the x axis of all columns in a blob. Bin values are scaled between 0 and 1.</p>
		"""
		pass
	def y_hist_bins(self) -> List[float]:
		"""
		<h3>image - blob.y_hist_bins()</h3><p>Returns a histogram of the y axis of all the rows in a blob. Bin values are scaled between 0 and 1.</p>
		"""
		pass
	def major_axis_line(self) -> Tuple[int,int,int,int]:
		"""
		<h3>image - blob.major_axis_line()</h3><p>Returns a line tuple (x1, y1, x2, y2) that can be drawn with <code>Image.draw_line()</code> of the major axis of the blob (the line going through the longest side of the min area rectangle).</p>
		"""
		pass
	def minor_axis_line(self) -> Tuple[int,int,int,int]:
		"""
		<h3>image - blob.minor_axis_line()</h3><p>Returns a line tuple (x1, y1, x2, y2) that can be drawn with <code>Image.draw_line()</code> of the minor axis of the blob (the line going through the shortest side of the min area rectangle).</p>
		"""
		pass
	def enclosing_circle(self) -> Tuple[int,int,int]:
		"""
		<h3>image - blob.enclosing_circle()</h3><p>Returns a circle tuple (x, y, r) that can be drawn with <code>Image.draw_circle()</code> of the circle that encloses the min area rectangle of a blob.</p>
		"""
		pass
	def enclosed_ellipse(self) -> Tuple[int,int,int,int,float]:
		"""
		<h3>image - blob.enclosed_ellipse()</h3><p>Returns an ellipse tuple (x, y, rx, ry, rotation) that can be drawn with <code>Image.draw_ellipse()</code> of the ellipse that fits inside of the min area rectangle of a blob.</p>
		"""
		pass
class line:
	def __init__(self):
		"""
		<h3>image - line</h3><p>Please call <code>Image.find_lines()</code>, <code>Image.find_line_segments()</code>, or <code>Image.get_regression()</code> to create this object.</p>
		"""
		pass
	def line(self) -> Tuple[int,int,int,int]:
		"""
		<h3>image - line.line()</h3><p>Returns a line tuple (x1, y1, x2, y2) for use with other <code>image</code> methods like <code>Image.draw_line()</code>.</p>
		"""
		pass
	def x1(self) -> int:
		"""
		<h3>image - line.x1()</h3><p>Returns the line’s p1 x component.</p><p>You may also get this value doing <code>[0]</code> on the object.</p>
		"""
		pass
	def y1(self) -> int:
		"""
		<h3>image - line.y1()</h3><p>Returns the line’s p1 y component.</p><p>You may also get this value doing <code>[1]</code> on the object.</p>
		"""
		pass
	def x2(self) -> int:
		"""
		<h3>image - line.x2()</h3><p>Returns the line’s p2 x component.</p><p>You may also get this value doing <code>[2]</code> on the object.</p>
		"""
		pass
	def y2(self) -> int:
		"""
		<h3>image - line.y2()</h3><p>Returns the line’s p2 y component.</p><p>You may also get this value doing <code>[3]</code> on the object.</p>
		"""
		pass
	def length(self) -> int:
		"""
		<h3>image - line.length()</h3><p>Returns the line’s length: sqrt(((x2-x1)^2) + ((y2-y1)^2).</p><p>You may also get this value doing <code>[4]</code> on the object.</p>
		"""
		pass
	def magnitude(self) -> int:
		"""
		<h3>image - line.magnitude()</h3><p>Returns the magnitude of the line from the hough transform.</p><p>You may also get this value doing <code>[5]</code> on the object.</p>
		"""
		pass
	def theta(self) -> int:
		"""
		<h3>image - line.theta()</h3><p>Returns the angle of the line from the hough transform - (0 - 179) degrees.</p><p>You may also get this value doing <code>[7]</code> on the object.</p>
		"""
		pass
	def rho(self) -> int:
		"""
		<h3>image - line.rho()</h3><p>Returns the the rho value for the line from the hough transform.</p><p>You may also get this value doing <code>[8]</code> on the object.</p>
		"""
		pass
class circle:
	def __init__(self):
		"""
		<h3>image - circle</h3><p>Please call <code>Image.find_circles()</code> to create this object.</p>
		"""
		pass
	def x(self) -> int:
		"""
		<h3>image - circle.x()</h3><p>Returns the circle’s x position.</p><p>You may also get this value doing <code>[0]</code> on the object.</p>
		"""
		pass
	def y(self) -> int:
		"""
		<h3>image - circle.y()</h3><p>Returns the circle’s y position.</p><p>You may also get this value doing <code>[1]</code> on the object.</p>
		"""
		pass
	def r(self) -> int:
		"""
		<h3>image - circle.r()</h3><p>Returns the circle’s radius.</p><p>You may also get this value doing <code>[2]</code> on the object.</p>
		"""
		pass
	def magnitude(self) -> int:
		"""
		<h3>image - circle.magnitude()</h3><p>Returns the circle’s magnitude.</p><p>You may also get this value doing <code>[3]</code> on the object.</p>
		"""
		pass
class rect:
	def __init__(self):
		"""
		<h3>image - rect</h3><p>Please call <code>Image.find_rects()</code> to create this object.</p>
		"""
		pass
	def corners(self) -> List[Tuple[int,int]]:
		"""
		<h3>image - rect.corners()</h3><p>Returns a list of 4 (x,y) tuples of the 4 corners of the object. Corners are always returned in sorted clock-wise order starting from the top left.</p>
		"""
		pass
	def rect(self) -> Tuple[int,int,int,int]:
		"""
		<h3>image - rect.rect()</h3><p>Returns a rectangle tuple (x, y, w, h) for use with other <code>image</code> methods like <code>Image.draw_rectangle()</code> of the rect’s bounding box.</p>
		"""
		pass
	def x(self) -> int:
		"""
		<h3>image - rect.x()</h3><p>Returns the rectangle’s top left corner’s x position.</p><p>You may also get this value doing <code>[0]</code> on the object.</p>
		"""
		pass
	def y(self) -> int:
		"""
		<h3>image - rect.y()</h3><p>Returns the rectangle’s top left corner’s y position.</p><p>You may also get this value doing <code>[1]</code> on the object.</p>
		"""
		pass
	def w(self) -> int:
		"""
		<h3>image - rect.w()</h3><p>Returns the rectangle’s width.</p><p>You may also get this value doing <code>[2]</code> on the object.</p>
		"""
		pass
	def h(self) -> int:
		"""
		<h3>image - rect.h()</h3><p>Returns the rectangle’s height.</p><p>You may also get this value doing <code>[3]</code> on the object.</p>
		"""
		pass
	def magnitude(self) -> int:
		"""
		<h3>image - rect.magnitude()</h3><p>Returns the rectangle’s magnitude.</p><p>You may also get this value doing <code>[4]</code> on the object.</p>
		"""
		pass
class qrcode:
	def __init__(self):
		"""
		<h3>image - qrcode</h3><p>Please call <code>Image.find_qrcodes()</code> to create this object.</p>
		"""
		pass
	def corners(self) -> List[Tuple[int,int]]:
		"""
		<h3>image - qrcode.corners()</h3><p>Returns a list of 4 (x,y) tuples of the 4 corners of the object. Corners are always returned in sorted clock-wise order starting from the top left.</p>
		"""
		pass
	def rect(self) -> Tuple[int,int,int,int]:
		"""
		<h3>image - qrcode.rect()</h3><p>Returns a rectangle tuple (x, y, w, h) for use with other <code>image</code> methods like <code>Image.draw_rectangle()</code> of the qrcode’s bounding box.</p>
		"""
		pass
	def x(self) -> int:
		"""
		<h3>image - qrcode.x()</h3><p>Returns the qrcode’s bounding box x coordinate (int).</p><p>You may also get this value doing <code>[0]</code> on the object.</p>
		"""
		pass
	def y(self) -> int:
		"""
		<h3>image - qrcode.y()</h3><p>Returns the qrcode’s bounding box y coordinate (int).</p><p>You may also get this value doing <code>[1]</code> on the object.</p>
		"""
		pass
	def w(self) -> int:
		"""
		<h3>image - qrcode.w()</h3><p>Returns the qrcode’s bounding box w coordinate (int).</p><p>You may also get this value doing <code>[2]</code> on the object.</p>
		"""
		pass
	def h(self) -> int:
		"""
		<h3>image - qrcode.h()</h3><p>Returns the qrcode’s bounding box h coordinate (int).</p><p>You may also get this value doing <code>[3]</code> on the object.</p>
		"""
		pass
	def payload(self) -> str:
		"""
		<h3>image - qrcode.payload()</h3><p>Returns the payload string of the qrcode. E.g. the URL.</p><p>You may also get this value doing <code>[4]</code> on the object.</p>
		"""
		pass
	def version(self) -> int:
		"""
		<h3>image - qrcode.version()</h3><p>Returns the version number of the qrcode (int).</p><p>You may also get this value doing <code>[5]</code> on the object.</p>
		"""
		pass
	def ecc_level(self) -> int:
		"""
		<h3>image - qrcode.ecc_level()</h3><p>Returns the ecc_level of the qrcode (int).</p><p>You may also get this value doing <code>[6]</code> on the object.</p>
		"""
		pass
	def mask(self) -> int:
		"""
		<h3>image - qrcode.mask()</h3><p>Returns the mask of the qrcode (int).</p><p>You may also get this value doing <code>[7]</code> on the object.</p>
		"""
		pass
	def data_type(self) -> int:
		"""
		<h3>image - qrcode.data_type()</h3><p>Returns the data type of the qrcode (int).</p><p>You may also get this value doing <code>[8]</code> on the object.</p>
		"""
		pass
	def eci(self) -> int:
		"""
		<h3>image - qrcode.eci()</h3><p>Returns the eci of the qrcode (int). The eci stores the encoding of data bytes in the QR Code. If you plan to handling QR Codes that contain more than just standard ASCII text you will need to look at this value.</p><p>You may also get this value doing <code>[9]</code> on the object.</p>
		"""
		pass
	def is_numeric(self) -> bool:
		"""
		<h3>image - qrcode.is_numeric()</h3><p>Returns True if the data_type of the qrcode is numeric.</p>
		"""
		pass
	def is_alphanumeric(self) -> bool:
		"""
		<h3>image - qrcode.is_alphanumeric()</h3><p>Returns True if the data_type of the qrcode is alpha numeric.</p>
		"""
		pass
	def is_binary(self) -> bool:
		"""
		<h3>image - qrcode.is_binary()</h3><p>Returns True if the data_type of the qrcode is binary. If you are serious about handling all types of text you need to check the eci if this is True to determine the text encoding of the data. Usually, it’s just standard ASCII, but, it could be UTF8 that has some 2-byte characters in it.</p>
		"""
		pass
	def is_kanji(self) -> bool:
		"""
		<h3>image - qrcode.is_kanji()</h3><p>Returns True if the data_type of the qrcode is alpha Kanji. If this is True then you’ll need to decode the string yourself as Kanji symbols are 10-bits per character and MicroPython has no support to parse this kind of text. The payload in this case must be treated as just a large byte array.</p>
		"""
		pass
class apriltag:
	def __init__(self):
		"""
		<h3>image - apriltag</h3><p>Please call <code>Image.find_apriltags()</code> to create this object.</p>
		"""
		pass
	def corners(self) -> List[Tuple[int,int]]:
		"""
		<h3>image - apriltag.corners()</h3><p>Returns a list of 4 (x,y) tuples of the 4 corners of the object. Corners are always returned in sorted clock-wise order starting from the top left.</p>
		"""
		pass
	def rect(self) -> Tuple[int,int,int,int]:
		"""
		<h3>image - apriltag.rect()</h3><p>Returns a rectangle tuple (x, y, w, h) for use with other <code>image</code> methods like <code>Image.draw_rectangle()</code> of the apriltag’s bounding box.</p>
		"""
		pass
	def x(self) -> int:
		"""
		<h3>image - apriltag.x()</h3><p>Returns the apriltag’s bounding box x coordinate (int).</p><p>You may also get this value doing <code>[0]</code> on the object.</p>
		"""
		pass
	def y(self) -> int:
		"""
		<h3>image - apriltag.y()</h3><p>Returns the apriltag’s bounding box y coordinate (int).</p><p>You may also get this value doing <code>[1]</code> on the object.</p>
		"""
		pass
	def w(self) -> int:
		"""
		<h3>image - apriltag.w()</h3><p>Returns the apriltag’s bounding box w coordinate (int).</p><p>You may also get this value doing <code>[2]</code> on the object.</p>
		"""
		pass
	def h(self) -> int:
		"""
		<h3>image - apriltag.h()</h3><p>Returns the apriltag’s bounding box h coordinate (int).</p><p>You may also get this value doing <code>[3]</code> on the object.</p>
		"""
		pass
	def id(self) -> int:
		"""
		<h3>image - apriltag.id()</h3><p>Returns the numeric id of the apriltag.</p><div><ul><li>TAG16H5 -&gt; 0 to 29</li><li>TAG25H7 -&gt; 0 to 241</li><li>TAG25H9 -&gt; 0 to 34</li><li>TAG36H10 -&gt; 0 to 2319</li><li>TAG36H11 -&gt; 0 to 586</li><li>ARTOOLKIT -&gt; 0 to 511</li></ul></div><p>You may also get this value doing <code>[4]</code> on the object.</p>
		"""
		pass
	def family(self) -> int:
		"""
		<h3>image - apriltag.family()</h3><p>Returns the numeric family of the apriltag.</p><div><ul><li>image.TAG16H5</li><li>image.TAG25H7</li><li>image.TAG25H9</li><li>image.TAG36H10</li><li>image.TAG36H11</li><li>image.ARTOOLKIT</li></ul></div><p>You may also get this value doing <code>[5]</code> on the object.</p>
		"""
		pass
	def cx(self) -> int:
		"""
		<h3>image - apriltag.cx()</h3><p>Returns the centroid x position of the apriltag (int).</p>
		"""
		pass
	def cxf(self) -> float:
		"""
		<h3>image - apriltag.cxf()</h3><p>Returns the centroid x position of the apriltag (float).</p><p>You may also get this value doing <code>[6]</code> on the object.</p>
		"""
		pass
	def cy(self) -> int:
		"""
		<h3>image - apriltag.cy()</h3><p>Returns the centroid y position of the apriltag (int).</p>
		"""
		pass
	def cyf(self) -> float:
		"""
		<h3>image - apriltag.cyf()</h3><p>Returns the centroid y position of the apriltag (float).</p><p>You may also get this value doing <code>[7]</code> on the object.</p>
		"""
		pass
	def rotation(self) -> float:
		"""
		<h3>image - apriltag.rotation()</h3><p>Returns the rotation of the apriltag in radians (float).</p><p>You may also get this value doing <code>[8]</code> on the object.</p>
		"""
		pass
	def decision_margin(self) -> float:
		"""
		<h3>image - apriltag.decision_margin()</h3><p>Returns the quality of the apriltag match (0.0 - 1.0) where 1.0 is the best.</p><p>You may also get this value doing <code>[9]</code> on the object.</p>
		"""
		pass
	def hamming(self) -> int:
		"""
		<h3>image - apriltag.hamming()</h3><p>Returns the number of accepted bit errors for this tag.</p><div><ul><li>TAG16H5 -&gt; 0 bit errors will be accepted</li><li>TAG25H7 -&gt; up to 1 bit error may be accepted</li><li>TAG25H9 -&gt; up to 3 bit errors may be accepted</li><li>TAG36H10 -&gt; up to 3 bit errors may be accepted</li><li>TAG36H11 -&gt; up to 4 bit errors may be accepted</li><li>ARTOOLKIT -&gt; 0 bit errors will be accepted</li></ul></div><p>You may also get this value doing <code>[10]</code> on the object.</p>
		"""
		pass
	def goodness(self) -> float:
		"""
		<h3>image - apriltag.goodness()</h3><p>Returns the quality of the apriltag image (0.0 - 1.0) where 1.0 is the best.</p><div><p>Note</p><p>This value is always 0.0 for now. We may enable a feature called “tag refinement” in the future which will allow detection of small apriltags. However, this feature currently drops the frame rate to less than 1 FPS.</p></div><p>You may also get this value doing <code>[11]</code> on the object.</p>
		"""
		pass
	def x_translation(self) -> float:
		"""
		<h3>image - apriltag.x_translation()</h3><p>Returns the translation in unknown units from the camera in the X direction.</p><p>This method is useful for determining the apriltag’s location away from the camera. However, the size of the apriltag, the lens you are using, etc. all come into play as to actually determining what the X units are in. For ease of use we recommend you use a lookup table to convert the output of this method to something useful for your application.</p><p>Note that this is the left-to-right direction.</p><p>You may also get this value doing <code>[12]</code> on the object.</p>
		"""
		pass
	def y_translation(self) -> float:
		"""
		<h3>image - apriltag.y_translation()</h3><p>Returns the translation in unknown units from the camera in the Y direction.</p><p>This method is useful for determining the apriltag’s location away from the camera. However, the size of the apriltag, the lens you are using, etc. all come into play as to actually determining what the Y units are in. For ease of use we recommend you use a lookup table to convert the output of this method to something useful for your application.</p><p>Note that this is the up-to-down direction.</p><p>You may also get this value doing <code>[13]</code> on the object.</p>
		"""
		pass
	def z_translation(self) -> float:
		"""
		<h3>image - apriltag.z_translation()</h3><p>Returns the translation in unknown units from the camera in the Z direction.</p><p>This method is useful for determining the apriltag’s location away from the camera. However, the size of the apriltag, the lens you are using, etc. all come into play as to actually determining what the Z units are in. For ease of use we recommend you use a lookup table to convert the output of this method to something useful for your application.</p><p>Note that this is the front-to-back direction.</p><p>You may also get this value doing <code>[14]</code> on the object.</p>
		"""
		pass
	def x_rotation(self) -> float:
		"""
		<h3>image - apriltag.x_rotation()</h3><p>Returns the rotation in radians of the apriltag in the X plane. E.g. moving the camera left-to-right while looking at the tag.</p><p>You may also get this value doing <code>[15]</code> on the object.</p>
		"""
		pass
	def y_rotation(self) -> float:
		"""
		<h3>image - apriltag.y_rotation()</h3><p>Returns the rotation in radians of the apriltag in the Y plane. E.g. moving the camera up-to-down while looking at the tag.</p><p>You may also get this value doing <code>[16]</code> on the object.</p>
		"""
		pass
	def z_rotation(self) -> float:
		"""
		<h3>image - apriltag.z_rotation()</h3><p>Returns the rotation in radians of the apriltag in the Z plane. E.g. rotating the camera while looking directly at the tag.</p><p>Note that this is just a renamed version of <code>apriltag.rotation()</code>.</p><p>You may also get this value doing <code>[17]</code> on the object.</p>
		"""
		pass
class datamatrix:
	def __init__(self):
		"""
		<h3>image - datamatrix</h3><p>Please call <code>Image.find_datamatrices()</code> to create this object.</p>
		"""
		pass
	def corners(self) -> List[Tuple[int,int]]:
		"""
		<h3>image - datamatrix.corners()</h3><p>Returns a list of 4 (x,y) tuples of the 4 corners of the object. Corners are always returned in sorted clock-wise order starting from the top left.</p>
		"""
		pass
	def rect(self) -> Tuple[int,int,int,int]:
		"""
		<h3>image - datamatrix.rect()</h3><p>Returns a rectangle tuple (x, y, w, h) for use with other <code>image</code> methods like <code>Image.draw_rectangle()</code> of the datamatrix’s bounding box.</p>
		"""
		pass
	def x(self) -> int:
		"""
		<h3>image - datamatrix.x()</h3><p>Returns the datamatrix’s bounding box x coordinate (int).</p><p>You may also get this value doing <code>[0]</code> on the object.</p>
		"""
		pass
	def y(self) -> int:
		"""
		<h3>image - datamatrix.y()</h3><p>Returns the datamatrix’s bounding box y coordinate (int).</p><p>You may also get this value doing <code>[1]</code> on the object.</p>
		"""
		pass
	def w(self) -> int:
		"""
		<h3>image - datamatrix.w()</h3><p>Returns the datamatrix’s bounding box w coordinate (int).</p><p>You may also get this value doing <code>[2]</code> on the object.</p>
		"""
		pass
	def h(self) -> int:
		"""
		<h3>image - datamatrix.h()</h3><p>Returns the datamatrix’s bounding box h coordinate (int).</p><p>You may also get this value doing <code>[3]</code> on the object.</p>
		"""
		pass
	def payload(self) -> str:
		"""
		<h3>image - datamatrix.payload()</h3><p>Returns the payload string of the datamatrix. E.g. The string.</p><p>You may also get this value doing <code>[4]</code> on the object.</p>
		"""
		pass
	def rotation(self) -> float:
		"""
		<h3>image - datamatrix.rotation()</h3><p>Returns the rotation of the datamatrix in radians (float).</p><p>You may also get this value doing <code>[5]</code> on the object.</p>
		"""
		pass
	def rows(self) -> int:
		"""
		<h3>image - datamatrix.rows()</h3><p>Returns the number of rows in the data matrix (int).</p><p>You may also get this value doing <code>[6]</code> on the object.</p>
		"""
		pass
	def columns(self) -> int:
		"""
		<h3>image - datamatrix.columns()</h3><p>Returns the number of columns in the data matrix (int).</p><p>You may also get this value doing <code>[7]</code> on the object.</p>
		"""
		pass
	def capacity(self) -> int:
		"""
		<h3>image - datamatrix.capacity()</h3><p>Returns how many characters could fit in this data matrix.</p><p>You may also get this value doing <code>[8]</code> on the object.</p>
		"""
		pass
	def padding(self) -> int:
		"""
		<h3>image - datamatrix.padding()</h3><p>Returns how many unused characters are in this data matrix.</p><p>You may also get this value doing <code>[9]</code> on the object.</p>
		"""
		pass
class barcode:
	def __init__(self):
		"""
		<h3>image - barcode</h3><p>Please call <code>Image.find_barcodes()</code> to create this object.</p>
		"""
		pass
	def corners(self) -> List[Tuple[int,int]]:
		"""
		<h3>image - barcode.corners()</h3><p>Returns a list of 4 (x,y) tuples of the 4 corners of the object. Corners are always returned in sorted clock-wise order starting from the top left.</p>
		"""
		pass
	def rect(self) -> Tuple[int,int,int,int]:
		"""
		<h3>image - barcode.rect()</h3><p>Returns a rectangle tuple (x, y, w, h) for use with other <code>image</code> methods like <code>Image.draw_rectangle()</code> of the barcode’s bounding box.</p>
		"""
		pass
	def x(self) -> int:
		"""
		<h3>image - barcode.x()</h3><p>Returns the barcode’s bounding box x coordinate (int).</p><p>You may also get this value doing <code>[0]</code> on the object.</p>
		"""
		pass
	def y(self) -> int:
		"""
		<h3>image - barcode.y()</h3><p>Returns the barcode’s bounding box y coordinate (int).</p><p>You may also get this value doing <code>[1]</code> on the object.</p>
		"""
		pass
	def w(self) -> int:
		"""
		<h3>image - barcode.w()</h3><p>Returns the barcode’s bounding box w coordinate (int).</p><p>You may also get this value doing <code>[2]</code> on the object.</p>
		"""
		pass
	def h(self) -> int:
		"""
		<h3>image - barcode.h()</h3><p>Returns the barcode’s bounding box h coordinate (int).</p><p>You may also get this value doing <code>[3]</code> on the object.</p>
		"""
		pass
	def payload(self) -> str:
		"""
		<h3>image - barcode.payload()</h3><p>Returns the payload string of the barcode. E.g. The number.</p><p>You may also get this value doing <code>[4]</code> on the object.</p>
		"""
		pass
	def type(self) -> int:
		"""
		<h3>image - barcode.type()</h3><p>Returns the type enumeration of the barcode (int).</p><p>You may also get this value doing <code>[5]</code> on the object.</p><div><ul><li>image.EAN2</li><li>image.EAN5</li><li>image.EAN8</li><li>image.UPCE</li><li>image.ISBN10</li><li>image.UPCA</li><li>image.EAN13</li><li>image.ISBN13</li><li>image.I25</li><li>image.DATABAR</li><li>image.DATABAR_EXP</li><li>image.CODABAR</li><li>image.CODE39</li><li>image.PDF417 - Future (e.g. doesn’t work right now).</li><li>image.CODE93</li><li>image.CODE128</li></ul></div>
		"""
		pass
	def rotation(self) -> float:
		"""
		<h3>image - barcode.rotation()</h3><p>Returns the rotation of the barcode in radians (float).</p><p>You may also get this value doing <code>[6]</code> on the object.</p>
		"""
		pass
	def quality(self) -> int:
		"""
		<h3>image - barcode.quality()</h3><p>Returns the number of times this barcode was detected in the image (int).</p><p>When scanning a barcode each new scanline can decode the same barcode. This value increments for a barcode each time that happens…</p><p>You may also get this value doing <code>[7]</code> on the object.</p>
		"""
		pass
class displacement:
	def __init__(self):
		"""
		<h3>image - displacement</h3><p>Please call <code>Image.find_displacement()</code> to create this object.</p>
		"""
		pass
	def x_translation(self) -> float:
		"""
		<h3>image - displacement.x_translation()</h3><p>Returns the x translation in pixels between two images. This is sub pixel accurate so it’s a float.</p><p>You may also get this value doing <code>[0]</code> on the object.</p>
		"""
		pass
	def y_translation(self) -> float:
		"""
		<h3>image - displacement.y_translation()</h3><p>Returns the y translation in pixels between two images. This is sub pixel accurate so it’s a float.</p><p>You may also get this value doing <code>[1]</code> on the object.</p>
		"""
		pass
	def rotation(self) -> float:
		"""
		<h3>image - displacement.rotation()</h3><p>Returns the rotation in radians between two images.</p><p>You may also get this value doing <code>[2]</code> on the object.</p>
		"""
		pass
	def scale(self) -> float:
		"""
		<h3>image - displacement.scale()</h3><p>Returns the scale change between two images.</p><p>You may also get this value doing <code>[3]</code> on the object.</p>
		"""
		pass
	def response(self) -> float:
		"""
		<h3>image - displacement.response()</h3><p>Returns the quality of the results of displacement matching between two images. Between 0-1. A <code>displacement</code> object with a response less than 0.1 is likely noise.</p><p>You may also get this value doing <code>[4]</code> on the object.</p>
		"""
		pass
class kptmatch:
	def __init__(self):
		"""
		<h3>image - kptmatch</h3><p>Please call <code>image.match_descriptor()</code> to create this object.</p>
		"""
		pass
	def rect(self) -> Tuple[int,int,int,int]:
		"""
		<h3>image - kptmatch.rect()</h3><p>Returns a rectangle tuple (x, y, w, h) for use with other <code>image</code> methods like <code>Image.draw_rectangle()</code> of the kptmatch’s bounding box.</p>
		"""
		pass
	def cx(self) -> int:
		"""
		<h3>image - kptmatch.cx()</h3><p>Returns the centroid x position of the kptmatch (int).</p><p>You may also get this value doing <code>[0]</code> on the object.</p>
		"""
		pass
	def cy(self) -> int:
		"""
		<h3>image - kptmatch.cy()</h3><p>Returns the centroid y position of the kptmatch (int).</p><p>You may also get this value doing <code>[1]</code> on the object.</p>
		"""
		pass
	def x(self) -> int:
		"""
		<h3>image - kptmatch.x()</h3><p>Returns the kptmatch’s bounding box x coordinate (int).</p><p>You may also get this value doing <code>[2]</code> on the object.</p>
		"""
		pass
	def y(self) -> int:
		"""
		<h3>image - kptmatch.y()</h3><p>Returns the kptmatch’s bounding box y coordinate (int).</p><p>You may also get this value doing <code>[3]</code> on the object.</p>
		"""
		pass
	def w(self) -> int:
		"""
		<h3>image - kptmatch.w()</h3><p>Returns the kptmatch’s bounding box w coordinate (int).</p><p>You may also get this value doing <code>[4]</code> on the object.</p>
		"""
		pass
	def h(self) -> int:
		"""
		<h3>image - kptmatch.h()</h3><p>Returns the kptmatch’s bounding box h coordinate (int).</p><p>You may also get this value doing <code>[5]</code> on the object.</p>
		"""
		pass
	def count(self) -> int:
		"""
		<h3>image - kptmatch.count()</h3><p>Returns the number of keypoints matched (int).</p><p>You may also get this value doing <code>[6]</code> on the object.</p>
		"""
		pass
	def theta(self) -> int:
		"""
		<h3>image - kptmatch.theta()</h3><p>Returns the estimated angle of rotation for the keypoint (int).</p><p>You may also get this value doing <code>[7]</code> on the object.</p>
		"""
		pass
	def match(self) -> List[Tuple[int,int]]:
		"""
		<h3>image - kptmatch.match()</h3><p>Returns the list of (x,y) tuples of matching keypoints.</p><p>You may also get this value doing <code>[8]</code> on the object.</p>
		"""
		pass
class ImageIO:
	def __init__(self, path:str, mode):
		"""
		<h3>image - ImageIO(path: str, mode)</h3><p>Creates an ImageIO object.</p><p>If <code>path</code> is a file name on disk then that file will be opened for reading if <code>mode</code> is <code>'r'</code> or writing if <code>mode</code> is <code>'w'</code>.</p><p><code>path</code> may also be a 3-value tuple (w, h, bpp) for in-memory storage of images. <code>mode</code> in this case is then the number of image buffers to store in memory. Note that the in-memory storage buffer is not allowed to grow in size after being allocated. Use a <code>bpp</code> value of 0 for binary images, 1 for grayscale images, and 2 for rgb565 images.</p>
		"""
		pass
	def type(self) -> int:
		"""
		<h3>image - ImageIO.type()</h3><p>Returns if the <code>ImageIO</code> object is a <code>FILE_STREAM</code> or <code>MEMORY_STREAM</code>.</p>
		"""
		pass
	def is_closed(self) -> bool:
		"""
		<h3>image - ImageIO.is_closed()</h3><p>Returns if the <code>ImageIO</code> object is closed and can no longer be used.</p>
		"""
		pass
	def count(self) -> int:
		"""
		<h3>image - ImageIO.count()</h3><p>Returns the number of frames stored.</p>
		"""
		pass
	def offset(self) -> int:
		"""
		<h3>image - ImageIO.offset()</h3><p>Returns the image index offset.</p>
		"""
		pass
	def version(self) -> int|None:
		"""
		<h3>image - ImageIO.version()</h3><p>Returns the version of the object if it’s <code>FILE_STREAM</code>. <code>MEMORY_STREAM</code> versions are <code>none</code>.</p>
		"""
		pass
	def buffer_size(self) -> int:
		"""
		<h3>image - ImageIO.buffer_size()</h3><p>Returns the size allocated by the object for a frame in a single buffer.</p><p><code>buffer_size() * count() == size()</code></p>
		"""
		pass
	def size(self) -> int:
		"""
		<h3>image - ImageIO.size()</h3><p>Returns the number of bytes on disk or memory used by the ImageIO object.</p>
		"""
		pass
	def write(self, img:Image) -> ImageIO:
		"""
		<h3>image - ImageIO.write(img: Image)</h3><p>Writes a new image <code>img</code> to the ImageIO object. For on disk ImageIO objects the file will grow as new images are added. For in-memory ImageIO objects this just writes an image to the current pre-allocated slot before advancing to the next slot.</p><p>Returns the ImageIO object.</p>
		"""
		pass
	def read(self, copy_to_fb=True, loop=True, pause=True) -> Image:
		"""
		<h3>image - ImageIO.read(copy_to_fb=True, loop=True, pause=True)</h3><p>Returns an image object from the ImageIO object. If <code>copy_to_fb</code> is False then the new image is allocated on the MicroPython heap. However, the MicroPython heap is limited and may not have space to store the new image if exhausted. Instead, set <code>copy_to_fb</code> to True to set the frame buffer to the new image making this function work just like <code>sensor.snapshot()</code>.</p><p><code>loop</code> if True automatically causes the ImageIO object to seek to the beginning at the end of the stream of images.</p><p><code>pause</code> if True causes this method to pause for a previously recorded number of milliseconds by write in-order to match the original frame rate that captured the image data.</p>
		"""
		pass
	def seek(self, offset) -> None:
		"""
		<h3>image - ImageIO.seek(offset)</h3><p>Seeks to the image slot number <code>offset</code> in the ImageIO object.</p><p>Works for on disk or in-memory objects.</p>
		"""
		pass
	def sync(self) -> None:
		"""
		<h3>image - ImageIO.sync()</h3><p>Writes out all data pending for on-disk ImageIO objects.</p>
		"""
		pass
	def close(self) -> None:
		"""
		<h3>image - ImageIO.close()</h3><p>Closes the ImageIO object. For in-memory objects this free’s the allocated space and for on-disk files this closes the file and writes out all meta-data.</p>
		"""
		pass
class Image:
	def __init__(self, arg, buffer:bytes|bytearray|memoryview|None=None, copy_to_fb:bool=False):
		"""
		<h3>image - Image(arg, buffer: bytes | bytearray | memoryview | None = None, copy_to_fb: bool = False)</h3><p>If <code>arg</code> is a string then this creates a new image object from a file at <code>arg</code> path. Supports loading bmp/pgm/ppm/jpg/jpeg/png image files from disk. If <code>copy_to_fb</code> is true the image is copied to the frame buffer verus being allocated on the heap.</p><p>If <code>arg</code> is an <code>ndarray</code> then this creates a new image object from the <code>ndarray</code>. <code>ndarray</code> objects with a shape of <code>(w, h)</code> are treated as grayscale images, <code>(w, h, 3)</code> are treated as RGB565 images. Only float32 point <code>ndarrays</code> are supported at this time. When creating an image this way if you pass a <code>buffer</code> argument it will be used to store the image data versus allocating space on the heap. If <code>copy_to_fb</code> is true the image is copied to the frame buffer verus being allocated on the heap or using the <code>buffer</code>.</p><p>If <code>arg</code> is an <code>int</code> it is then considered the width of a new image and a <code>height</code> value and a <code>format</code> value must follow to create a new blank image object. <code>format</code> can be be any image pixformat value like <code>image.GRAYSCALE</code>. The image will be initialized to all zeros. Note that a <code>buffer</code> value is expected for compressed image formats. <code>buffer</code> is considered as the source of image data for creating images this way. If used with <code>copy_to_fb</code> the data from <code>buffer</code> is copied to the frame buffer. If you’d like to create a JPEG image from a JPEG <code>bytes()</code> or <code>bytearray()</code> object you can pass the <code>width</code>, <code>height</code>, <code>image.JPEG</code> for the JPEG along with setting <code>buffer</code> to the JPEG byte stream to create a JPEG image.</p><p>Images support “[]” notation. Do <code>image[index] = 8/16-bit value</code> to assign an image pixel or <code>image[index]</code> to get an image pixel which will be either an 8-bit value for grayscale/bayer images of a 16-bit value for RGB565/YUV images. Binary images return a 1-bit value.</p><p>For JPEG images the “[]” allows you to access the compressed JPEG image blob as a byte-array. Reading and writing to the data array is opaque however as JPEG images are compressed byte streams.</p><p>Images also support read buffer operations. You can pass images to all sorts of MicroPython functions like as if the image were a byte-array object. In particular, if you’d like to transmit an image you can just pass it to the UART/SPI/I2C write functions to be transmitted automatically.</p>
		"""
		pass
	def width(self) -> int:
		"""
		<h3>image - Image.width()</h3><p>Returns the image width in pixels.</p>
		"""
		pass
	def height(self) -> int:
		"""
		<h3>image - Image.height()</h3><p>Returns the image height in pixels.</p>
		"""
		pass
	def format(self) -> int:
		"""
		<h3>image - Image.format()</h3><p>Returns <code>image.GRAYSCALE</code> for grayscale images, <code>image.RGB565</code> for RGB565 images, <code>image.BAYER</code> for bayer pattern images, and <code>image.JPEG</code> for JPEG images.</p>
		"""
		pass
	def size(self) -> int:
		"""
		<h3>image - Image.size()</h3><p>Returns the image size in bytes.</p>
		"""
		pass
	def bytearray(self) -> bytearray:
		"""
		<h3>image - Image.bytearray()</h3><p>Returns a <code>bytearray</code> object that points to the image data for byte-level read/write access.</p><div><p>Note</p><p>Image objects are automatically cast as <code>bytes</code> objects when passed to MicroPython driver that requires a <code>bytes</code> like object. This is read-only access. Call <code>bytearray()</code> to get read/write access.</p></div>
		"""
		pass
	def get_pixel(self, x:int, y:int, rgbtuple:bool|None=None) -> int|Tuple[int,int,int]:
		"""
		<h3>image - Image.get_pixel(x: int, y: int, rgbtuple: bool | None = None)</h3><p>For grayscale images: Returns the grayscale pixel value at location (x, y). For RGB565 images: Returns the RGB888 pixel tuple (r, g, b) at location (x, y). For bayer pattern images: Returns the the pixel value at the location (x, y).</p><p>Returns None if <code>x</code> or <code>y</code> is outside of the image.</p><p><code>x</code> and <code>y</code> may either be passed independently or as a tuple.</p><p><code>rgbtuple</code> if True causes this method to return an RGB888 tuple. Otherwise, this method returns the integer value of the underlying pixel. I.e. for RGB565 images this method returns a RGB565 value. Defaults to True for RGB565 images and False otherwise.</p><p>Not supported on compressed images.</p><div><p>Note</p><p><code>Image.get_pixel()</code> and <code>Image.set_pixel()</code> are the only methods that allow you to manipulate bayer pattern images. Bayer pattern images are literal images where pixels in the image are R/G/R/G/etc. for even rows and G/B/G/B/etc. for odd rows. Each pixel is 8-bits. If you call this method with <code>rgbtuple</code> set then <code>Image.get_pixel()</code> will debayer the source image at that pixel location and return a valid RGB888 tuple for the pixel location.</p></div>
		"""
		pass
	def set_pixel(self, x:int, y:int, pixel:int|Tuple[int,int,int]) -> Image:
		"""
		<h3>image - Image.set_pixel(x: int, y: int, pixel: int | Tuple[int, int, int])</h3><p>For grayscale images: Sets the pixel at location (x, y) to the grayscale value <code>pixel</code>. For RGB565 images: Sets the pixel at location (x, y) to the RGB888 tuple (r, g, b) <code>pixel</code>. For bayer pattern images: Sets the pixel value at the location (x, y) to the value <code>pixel</code>.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p><code>x</code> and <code>y</code> may either be passed independently or as a tuple.</p><p><code>pixel</code> may either be an RGB888 tuple (r, g, b) or the underlying pixel value (i.e. a RGB565 value for RGB565 images or an 8-bit value for grayscale images.</p><p>Not supported on compressed images.</p><div><p>Note</p><p><code>Image.get_pixel()</code> and <code>Image.set_pixel()</code> are the only methods that allow you to manipulate bayer pattern images. Bayer pattern images are literal images where pixels in the image are R/G/R/G/etc. for even rows and G/B/G/B/etc. for odd rows. Each pixel is 8-bits. If you call this method with an RGB888 tuple the grayscale value of that RGB888 tuple is extracted and set to the pixel location.</p></div>
		"""
		pass
	def to_ndarray(self, dtype:str, buffer:bytes|bytearray|memoryview|None=None) -> ndarray:
		"""
		<h3>image - Image.to_ndarray(dtype: str, buffer: bytes | bytearray | memoryview | None = None)</h3><p>Returns a <code>ndarray</code> object created from the image. This only works for GRAYSCALE or RGB565 images currently.</p><p><code>dtype</code> can be <code>b</code>, <code>B</code>, or <code>f</code> for creating a signed 8-bit, unsigned 8-bit, or 32-bit floating point <code>ndarray</code>. GRAYSCALE images are directly converted to unsigned 8-bit <code>ndarray</code> objects. For signed 8-bit <code>ndarray</code> objects the values (0:255) are mapped to (-127:128). For float 32-bit <code>ndarray</code> objects the values are mapped to (0.0:255.0). RGB565 images are converted to 3-channel <code>ndarray</code> objects and the same process described above for GRAYSCALE images is applied to each channel depending on <code>dtype</code>. Note that <code>dtype</code> also accepts the integer values (e.g. <code>ord()</code>) of <code>b</code>, <code>B</code>, and <code>f</code> respectively.</p><p><code>buffer</code> if not <code>None</code> is a <code>bytearray</code> object to use as the buffer for the <code>ndarray</code>. If <code>None</code> a new buffer is allocated on the heap to store the <code>ndarray</code> image data. You can use the <code>buffer</code> argument to directly allocate the <code>ndarray</code> in a pre-allocated buffer saving a heap allocation and a copy operation.</p><p>The <code>ndarray</code> returned has the shape of <code>(height, width)</code> for GRAYSCALE images and <code>(height, width, 3)</code> for RGB565 images.</p>
		"""
		pass
	def to_bitmap(self, x_scale:float=1.0, y_scale:float=1.0, roi:Tuple[int,int,int,int]|None=None, rgb_channel:int=-1, alpha:int=256, color_palette=None, alpha_palette=None, hint:int=0, copy:bool=False, copy_to_fb:bool=False) -> Image:
		"""
		<h3>image - Image.to_bitmap(x_scale: float = 1.0, y_scale: float = 1.0, roi: Tuple[int, int, int, int] | None = None, rgb_channel: int = -1, alpha: int = 256, color_palette=None, alpha_palette=None, hint: int = 0, copy: bool = False, copy_to_fb: bool = False)</h3><p>Converts an image to a bitmap image (1 bit per pixel).</p><p><code>x_scale</code> controls how much the displayed image is scaled by in the x direction (float). If this value is negative the image will be flipped horizontally. Note that if <code>y_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>y_scale</code> controls how much the displayed image is scaled by in the y direction (float). If this value is negative the image will be flipped vertically. Note that if <code>x_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This allows you to extract just the pixels in the ROI to scale and draw on the destination image.</p><p><code>rgb_channel</code> is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed) and to render onto the destination image. For example, if you pass <code>rgb_channel=1</code> this will extract the green channel of the source RGB565 image and draw that in grayscale on the destination image.</p><p><code>alpha</code> controls how much of the source image to blend into the destination image. A value of 255 draws an opaque source image while a value lower than 255 produces a blend between the source and destination image. 0 results in no modification to the destination image.</p><p><code>color_palette</code> if not <code>None</code> can be an a color palette enum or a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of whatever the source image is. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>alpha_palette</code> if not <code>None</code> can be a 256 pixel in total GRAYSCALE image to use as a alpha palette which modulates the <code>alpha</code> value of the source image being drawn at a pixel pixel level allowing you to precisely control the alpha value of pixels based on their grayscale value. A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes more transparent until 0. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>hint</code> can be a logical OR of the flags:</p><div><ul><li><code>image.AREA</code>: Use area scaling when downscaling versus the default of nearest neighbor.</li><li><code>image.BILINEAR</code>: Use bilinear scaling versus the default of nearest neighbor scaling.</li><li><code>image.BICUBIC</code>: Use bicubic scaling versus the default of nearest neighbor scaling.</li><li><code>image.CENTER</code>: Center the image being drawn on the display. This is applied after scaling.</li><li><code>image.HMIRROR</code>: Horizontally mirror the image.</li><li><code>image.VFLIP</code>: Vertically flip the image.</li><li><code>image.TRANSPOSE</code>: Transpose the image (swap x/y).</li><li><code>image.EXTRACT_RGB_CHANNEL_FIRST</code>: Do rgb_channel extraction before scaling.</li><li><code>image.APPLY_COLOR_PALETTE_FIRST</code>: Apply color palette before scaling.</li><li><code>image.SCALE_ASPECT_KEEP</code>: Scale the image being drawn to fit inside the display.</li><li><code>image.SCALE_ASPECT_EXPAND</code>: Scale the image being drawn to fill the display (results in cropping)</li><li><code>image.SCALE_ASPECT_IGNORE</code>: Scale the image being drawn to fill the display (results in stretching).</li><li><code>image.ROTATE_90</code>: Rotate the image by 90 degrees (this is just VFLIP | TRANSPOSE).</li><li><code>image.ROTATE_180</code>: Rotate the image by 180 degrees (this is just HMIRROR | VFLIP).</li><li><code>image.ROTATE_270</code>: Rotate the image by 270 degrees (this is just HMIRROR | TRANSPOSE).</li></ul></div><p><code>copy</code> if True create a deep-copy on the heap of the image that’s been converted versus converting the original image in-place.</p><p><code>copy_to_fb</code> if True the image is loaded directly into the frame buffer. <code>copy_to_fb</code> has priority over <code>copy</code>. This has no special effect if the image is already in the frame buffer.</p><div><p>Note</p><p>Bitmap images are like grayscale images with only two pixels values - 0 and 1. Additionally, bitmap images are packed such that they only store 1 bit per pixel making them very small. The OpenMV image library allows bitmap images to be used in all places <code>sensor.GRAYSCALE</code> and <code>sensor.RGB565</code> images can be used. However, many operations when applied on bitmap images don’t make any sense becuase bitmap images only have 2 values. OpenMV recommends using bitmap images for <code>mask</code> values in operations and such as they fit on the MicroPython heap quite easily. Finally, bitmap image pixel values 0 and 1 are interpreted as black and white when being applied to <code>sensor.GRAYSCALE</code> or <code>sensor.RGB565</code> images. The library automatically handles conversion.</p></div><p>Returns the image object so you can call another method using <code>.</code> notation.</p>
		"""
		pass
	def to_grayscale(self, x_scale:float=1.0, y_scale:float=1.0, roi:Tuple[int,int,int,int]|None=None, rgb_channel:int=-1, alpha:int=256, color_palette=None, alpha_palette=None, copy:bool=False, copy_to_fb:bool=False) -> Image:
		"""
		<h3>image - Image.to_grayscale(x_scale: float = 1.0, y_scale: float = 1.0, roi: Tuple[int, int, int, int] | None = None, rgb_channel: int = -1, alpha: int = 256, color_palette=None, alpha_palette=None, copy: bool = False, copy_to_fb: bool = False)</h3><p>Converts an image to a grayscale image (8-bits per pixel).</p><p><code>x_scale</code> controls how much the displayed image is scaled by in the x direction (float). If this value is negative the image will be flipped horizontally. Note that if <code>y_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>y_scale</code> controls how much the displayed image is scaled by in the y direction (float). If this value is negative the image will be flipped vertically. Note that if <code>x_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This allows you to extract just the pixels in the ROI to scale and draw on the destination image.</p><p><code>rgb_channel</code> is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed) and to render onto the destination image. For example, if you pass <code>rgb_channel=1</code> this will extract the green channel of the source RGB565 image and draw that in grayscale on the destination image.</p><p><code>alpha</code> controls how much of the source image to blend into the destination image. A value of 255 draws an opaque source image while a value lower than 255 produces a blend between the source and destination image. 0 results in no modification to the destination image.</p><p><code>color_palette</code> if not <code>None</code> can be an a color palette enum or a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of whatever the source image is. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>alpha_palette</code> if not <code>None</code> can be a 256 pixel in total GRAYSCALE image to use as a alpha palette which modulates the <code>alpha</code> value of the source image being drawn at a pixel pixel level allowing you to precisely control the alpha value of pixels based on their grayscale value. A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes more transparent until 0. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>hint</code> can be a logical OR of the flags:</p><div><ul><li><code>image.AREA</code>: Use area scaling when downscaling versus the default of nearest neighbor.</li><li><code>image.BILINEAR</code>: Use bilinear scaling versus the default of nearest neighbor scaling.</li><li><code>image.BICUBIC</code>: Use bicubic scaling versus the default of nearest neighbor scaling.</li><li><code>image.CENTER</code>: Center the image being drawn on the display. This is applied after scaling.</li><li><code>image.HMIRROR</code>: Horizontally mirror the image.</li><li><code>image.VFLIP</code>: Vertically flip the image.</li><li><code>image.TRANSPOSE</code>: Transpose the image (swap x/y).</li><li><code>image.EXTRACT_RGB_CHANNEL_FIRST</code>: Do rgb_channel extraction before scaling.</li><li><code>image.APPLY_COLOR_PALETTE_FIRST</code>: Apply color palette before scaling.</li><li><code>image.SCALE_ASPECT_KEEP</code>: Scale the image being drawn to fit inside the display.</li><li><code>image.SCALE_ASPECT_EXPAND</code>: Scale the image being drawn to fill the display (results in cropping)</li><li><code>image.SCALE_ASPECT_IGNORE</code>: Scale the image being drawn to fill the display (results in stretching).</li><li><code>image.ROTATE_90</code>: Rotate the image by 90 degrees (this is just VFLIP | TRANSPOSE).</li><li><code>image.ROTATE_180</code>: Rotate the image by 180 degrees (this is just HMIRROR | VFLIP).</li><li><code>image.ROTATE_270</code>: Rotate the image by 270 degrees (this is just HMIRROR | TRANSPOSE).</li></ul></div><p><code>copy</code> if True create a deep-copy on the heap of the image that’s been converted versus converting the original image in-place.</p><p><code>copy_to_fb</code> if True the image is loaded directly into the frame buffer. <code>copy_to_fb</code> has priority over <code>copy</code>. This has no special effect if the image is already in the frame buffer.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p>
		"""
		pass
	def to_rgb565(self, x_scale:float=1.0, y_scale:float=1.0, roi:Tuple[int,int,int,int]|None=None, rgb_channel:int=-1, alpha:int=256, color_palette=None, alpha_palette=None, hint:int=0, copy:bool=False, copy_to_fb:bool=False) -> Image:
		"""
		<h3>image - Image.to_rgb565(x_scale: float = 1.0, y_scale: float = 1.0, roi: Tuple[int, int, int, int] | None = None, rgb_channel: int = -1, alpha: int = 256, color_palette=None, alpha_palette=None, hint: int = 0, copy: bool = False, copy_to_fb: bool = False)</h3><p>Converts an image to an RGB565 image (16-bits per pixel).</p><p><code>x_scale</code> controls how much the displayed image is scaled by in the x direction (float). If this value is negative the image will be flipped horizontally. Note that if <code>y_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>y_scale</code> controls how much the displayed image is scaled by in the y direction (float). If this value is negative the image will be flipped vertically. Note that if <code>x_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This allows you to extract just the pixels in the ROI to scale and draw on the destination image.</p><p><code>rgb_channel</code> is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed) and to render onto the destination image. For example, if you pass <code>rgb_channel=1</code> this will extract the green channel of the source RGB565 image and draw that in grayscale on the destination image.</p><p><code>alpha</code> controls how much of the source image to blend into the destination image. A value of 255 draws an opaque source image while a value lower than 255 produces a blend between the source and destination image. 0 results in no modification to the destination image.</p><p><code>color_palette</code> if not <code>None</code> can be an a color palette enum or a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of whatever the source image is. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>alpha_palette</code> if not <code>None</code> can be a 256 pixel in total GRAYSCALE image to use as a alpha palette which modulates the <code>alpha</code> value of the source image being drawn at a pixel pixel level allowing you to precisely control the alpha value of pixels based on their grayscale value. A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes more transparent until 0. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>hint</code> can be a logical OR of the flags:</p><div><ul><li><code>image.AREA</code>: Use area scaling when downscaling versus the default of nearest neighbor.</li><li><code>image.BILINEAR</code>: Use bilinear scaling versus the default of nearest neighbor scaling.</li><li><code>image.BICUBIC</code>: Use bicubic scaling versus the default of nearest neighbor scaling.</li><li><code>image.CENTER</code>: Center the image being drawn on the display. This is applied after scaling.</li><li><code>image.HMIRROR</code>: Horizontally mirror the image.</li><li><code>image.VFLIP</code>: Vertically flip the image.</li><li><code>image.TRANSPOSE</code>: Transpose the image (swap x/y).</li><li><code>image.EXTRACT_RGB_CHANNEL_FIRST</code>: Do rgb_channel extraction before scaling.</li><li><code>image.APPLY_COLOR_PALETTE_FIRST</code>: Apply color palette before scaling.</li><li><code>image.SCALE_ASPECT_KEEP</code>: Scale the image being drawn to fit inside the display.</li><li><code>image.SCALE_ASPECT_EXPAND</code>: Scale the image being drawn to fill the display (results in cropping)</li><li><code>image.SCALE_ASPECT_IGNORE</code>: Scale the image being drawn to fill the display (results in stretching).</li><li><code>image.ROTATE_90</code>: Rotate the image by 90 degrees (this is just VFLIP | TRANSPOSE).</li><li><code>image.ROTATE_180</code>: Rotate the image by 180 degrees (this is just HMIRROR | VFLIP).</li><li><code>image.ROTATE_270</code>: Rotate the image by 270 degrees (this is just HMIRROR | TRANSPOSE).</li></ul></div><p><code>copy</code> if True create a deep-copy on the heap of the image that’s been converted versus converting the original image in-place.</p><p><code>copy_to_fb</code> if True the image is loaded directly into the frame buffer. <code>copy_to_fb</code> has priority over <code>copy</code>. This has no special effect if the image is already in the frame buffer.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p>
		"""
		pass
	def to_rainbow(self, x_scale:float=1.0, y_scale:float=1.0, roi:Tuple[int,int,int,int]|None=None, rgb_channel:int=-1, alpha:int=256, color_palette=PALETTE_RAINBOW, alpha_palette=None, hint:int=0, copy:bool=False, copy_to_fb:bool=False) -> Image:
		"""
		<h3>image - Image.to_rainbow(x_scale: float = 1.0, y_scale: float = 1.0, roi: Tuple[int, int, int, int] | None = None, rgb_channel: int = -1, alpha: int = 256, color_palette=PALETTE_RAINBOW, alpha_palette=None, hint: int = 0, copy: bool = False, copy_to_fb: bool = False)</h3><p>Converts an image to an RGB565 rainbow image (16-bits per pixel).</p><p><code>x_scale</code> controls how much the displayed image is scaled by in the x direction (float). If this value is negative the image will be flipped horizontally. Note that if <code>y_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>y_scale</code> controls how much the displayed image is scaled by in the y direction (float). If this value is negative the image will be flipped vertically. Note that if <code>x_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This allows you to extract just the pixels in the ROI to scale and draw on the destination image.</p><p><code>rgb_channel</code> is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed) and to render onto the destination image. For example, if you pass <code>rgb_channel=1</code> this will extract the green channel of the source RGB565 image and draw that in grayscale on the destination image.</p><p><code>alpha</code> controls how much of the source image to blend into the destination image. A value of 255 draws an opaque source image while a value lower than 255 produces a blend between the source and destination image. 0 results in no modification to the destination image.</p><p><code>color_palette</code> if not <code>None</code> can be an a color palette enum or a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of whatever the source image is. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>alpha_palette</code> if not <code>None</code> can be a 256 pixel in total GRAYSCALE image to use as a alpha palette which modulates the <code>alpha</code> value of the source image being drawn at a pixel pixel level allowing you to precisely control the alpha value of pixels based on their grayscale value. A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes more transparent until 0. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>hint</code> can be a logical OR of the flags:</p><div><ul><li><code>image.AREA</code>: Use area scaling when downscaling versus the default of nearest neighbor.</li><li><code>image.BILINEAR</code>: Use bilinear scaling versus the default of nearest neighbor scaling.</li><li><code>image.BICUBIC</code>: Use bicubic scaling versus the default of nearest neighbor scaling.</li><li><code>image.CENTER</code>: Center the image being drawn on the display. This is applied after scaling.</li><li><code>image.HMIRROR</code>: Horizontally mirror the image.</li><li><code>image.VFLIP</code>: Vertically flip the image.</li><li><code>image.TRANSPOSE</code>: Transpose the image (swap x/y).</li><li><code>image.EXTRACT_RGB_CHANNEL_FIRST</code>: Do rgb_channel extraction before scaling.</li><li><code>image.APPLY_COLOR_PALETTE_FIRST</code>: Apply color palette before scaling.</li><li><code>image.SCALE_ASPECT_KEEP</code>: Scale the image being drawn to fit inside the display.</li><li><code>image.SCALE_ASPECT_EXPAND</code>: Scale the image being drawn to fill the display (results in cropping)</li><li><code>image.SCALE_ASPECT_IGNORE</code>: Scale the image being drawn to fill the display (results in stretching).</li><li><code>image.ROTATE_90</code>: Rotate the image by 90 degrees (this is just VFLIP | TRANSPOSE).</li><li><code>image.ROTATE_180</code>: Rotate the image by 180 degrees (this is just HMIRROR | VFLIP).</li><li><code>image.ROTATE_270</code>: Rotate the image by 270 degrees (this is just HMIRROR | TRANSPOSE).</li></ul></div><p><code>copy</code> if True create a deep-copy on the heap of the image that’s been converted versus converting the original image in-place.</p><p><code>copy_to_fb</code> if True the image is loaded directly into the frame buffer. <code>copy_to_fb</code> has priority over <code>copy</code>. This has no special effect if the image is already in the frame buffer.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p>
		"""
		pass
	def to_ironbow(self, x_scale:float=1.0, y_scale:float=1.0, roi:Tuple[int,int,int,int]|None=None, rgb_channel:int=-1, alpha:int=256, color_palette=PALETTE_IRONBOW, alpha_palette=None, hint:int=0, copy:bool=False, copy_to_fb:bool=False) -> Image:
		"""
		<h3>image - Image.to_ironbow(x_scale: float = 1.0, y_scale: float = 1.0, roi: Tuple[int, int, int, int] | None = None, rgb_channel: int = -1, alpha: int = 256, color_palette=PALETTE_IRONBOW, alpha_palette=None, hint: int = 0, copy: bool = False, copy_to_fb: bool = False)</h3><p>Converts an image to an RGB565 ironbow image (16-bits per pixel).</p><p><code>x_scale</code> controls how much the displayed image is scaled by in the x direction (float). If this value is negative the image will be flipped horizontally. Note that if <code>y_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>y_scale</code> controls how much the displayed image is scaled by in the y direction (float). If this value is negative the image will be flipped vertically. Note that if <code>x_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This allows you to extract just the pixels in the ROI to scale and draw on the destination image.</p><p><code>rgb_channel</code> is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed) and to render onto the destination image. For example, if you pass <code>rgb_channel=1</code> this will extract the green channel of the source RGB565 image and draw that in grayscale on the destination image.</p><p><code>alpha</code> controls how much of the source image to blend into the destination image. A value of 255 draws an opaque source image while a value lower than 255 produces a blend between the source and destination image. 0 results in no modification to the destination image.</p><p><code>color_palette</code> if not <code>None</code> can be an a color palette enum or a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of whatever the source image is. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>alpha_palette</code> if not <code>None</code> can be a 256 pixel in total GRAYSCALE image to use as a alpha palette which modulates the <code>alpha</code> value of the source image being drawn at a pixel pixel level allowing you to precisely control the alpha value of pixels based on their grayscale value. A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes more transparent until 0. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>hint</code> can be a logical OR of the flags:</p><div><ul><li><code>image.AREA</code>: Use area scaling when downscaling versus the default of nearest neighbor.</li><li><code>image.BILINEAR</code>: Use bilinear scaling versus the default of nearest neighbor scaling.</li><li><code>image.BICUBIC</code>: Use bicubic scaling versus the default of nearest neighbor scaling.</li><li><code>image.CENTER</code>: Center the image being drawn on the display. This is applied after scaling.</li><li><code>image.HMIRROR</code>: Horizontally mirror the image.</li><li><code>image.VFLIP</code>: Vertically flip the image.</li><li><code>image.TRANSPOSE</code>: Transpose the image (swap x/y).</li><li><code>image.EXTRACT_RGB_CHANNEL_FIRST</code>: Do rgb_channel extraction before scaling.</li><li><code>image.APPLY_COLOR_PALETTE_FIRST</code>: Apply color palette before scaling.</li><li><code>image.SCALE_ASPECT_KEEP</code>: Scale the image being drawn to fit inside the display.</li><li><code>image.SCALE_ASPECT_EXPAND</code>: Scale the image being drawn to fill the display (results in cropping)</li><li><code>image.SCALE_ASPECT_IGNORE</code>: Scale the image being drawn to fill the display (results in stretching).</li><li><code>image.ROTATE_90</code>: Rotate the image by 90 degrees (this is just VFLIP | TRANSPOSE).</li><li><code>image.ROTATE_180</code>: Rotate the image by 180 degrees (this is just HMIRROR | VFLIP).</li><li><code>image.ROTATE_270</code>: Rotate the image by 270 degrees (this is just HMIRROR | TRANSPOSE).</li></ul></div><p><code>copy</code> if True create a deep-copy on the heap of the image that’s been converted versus converting the original image in-place.</p><p><code>copy_to_fb</code> if True the image is loaded directly into the frame buffer. <code>copy_to_fb</code> has priority over <code>copy</code>. This has no special effect if the image is already in the frame buffer.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p>
		"""
		pass
	def to_depth(self, x_scale:float=1.0, y_scale:float=1.0, roi:Tuple[int,int,int,int]|None=None, rgb_channel:int=-1, alpha:int=256, color_palette=PALETTE_IRONBOW, alpha_palette=None, hint:int=0, copy:bool=False, copy_to_fb:bool=False) -> Image:
		"""
		<h3>image - Image.to_depth(x_scale: float = 1.0, y_scale: float = 1.0, roi: Tuple[int, int, int, int] | None = None, rgb_channel: int = -1, alpha: int = 256, color_palette=PALETTE_IRONBOW, alpha_palette=None, hint: int = 0, copy: bool = False, copy_to_fb: bool = False)</h3><p>Converts an image to an RGB565 Depth Image (16-bits per pixel).</p><p><code>x_scale</code> controls how much the displayed image is scaled by in the x direction (float). If this value is negative the image will be flipped horizontally. Note that if <code>y_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>y_scale</code> controls how much the displayed image is scaled by in the y direction (float). If this value is negative the image will be flipped vertically. Note that if <code>x_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This allows you to extract just the pixels in the ROI to scale and draw on the destination image.</p><p><code>rgb_channel</code> is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed) and to render onto the destination image. For example, if you pass <code>rgb_channel=1</code> this will extract the green channel of the source RGB565 image and draw that in grayscale on the destination image.</p><p><code>alpha</code> controls how much of the source image to blend into the destination image. A value of 255 draws an opaque source image while a value lower than 255 produces a blend between the source and destination image. 0 results in no modification to the destination image.</p><p><code>color_palette</code> if not <code>None</code> can be <code>image.PALETTE_DEPTH</code> or a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of whatever the source image is. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>alpha_palette</code> if not <code>None</code> can be a 256 pixel in total GRAYSCALE image to use as a alpha palette which modulates the <code>alpha</code> value of the source image being drawn at a pixel pixel level allowing you to precisely control the alpha value of pixels based on their grayscale value. A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes more transparent until 0. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>hint</code> can be a logical OR of the flags:</p><div><ul><li><code>image.AREA</code>: Use area scaling when downscaling versus the default of nearest neighbor.</li><li><code>image.BILINEAR</code>: Use bilinear scaling versus the default of nearest neighbor scaling.</li><li><code>image.BICUBIC</code>: Use bicubic scaling versus the default of nearest neighbor scaling.</li><li><code>image.CENTER</code>: Center the image being drawn on the display. This is applied after scaling.</li><li><code>image.HMIRROR</code>: Horizontally mirror the image.</li><li><code>image.VFLIP</code>: Vertically flip the image.</li><li><code>image.TRANSPOSE</code>: Transpose the image (swap x/y).</li><li><code>image.EXTRACT_RGB_CHANNEL_FIRST</code>: Do rgb_channel extraction before scaling.</li><li><code>image.APPLY_COLOR_PALETTE_FIRST</code>: Apply color palette before scaling.</li><li><code>image.SCALE_ASPECT_KEEP</code>: Scale the image being drawn to fit inside the display.</li><li><code>image.SCALE_ASPECT_EXPAND</code>: Scale the image being drawn to fill the display (results in cropping)</li><li><code>image.SCALE_ASPECT_IGNORE</code>: Scale the image being drawn to fill the display (results in stretching).</li><li><code>image.ROTATE_90</code>: Rotate the image by 90 degrees (this is just VFLIP | TRANSPOSE).</li><li><code>image.ROTATE_180</code>: Rotate the image by 180 degrees (this is just HMIRROR | VFLIP).</li><li><code>image.ROTATE_270</code>: Rotate the image by 270 degrees (this is just HMIRROR | TRANSPOSE).</li></ul></div><p><code>copy</code> if True create a deep-copy on the heap of the image that’s been converted versus converting the original image in-place.</p><p><code>copy_to_fb</code> if True the image is loaded directly into the frame buffer. <code>copy_to_fb</code> has priority over <code>copy</code>. This has no special effect if the image is already in the frame buffer.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p>
		"""
		pass
	def to_evt_dark(self, x_scale:float=1.0, y_scale:float=1.0, roi:Tuple[int,int,int,int]|None=None, rgb_channel:int=-1, alpha:int=256, color_palette=PALETTE_IRONBOW, alpha_palette=None, hint:int=0, copy:bool=False, copy_to_fb:bool=False) -> Image:
		"""
		<h3>image - Image.to_evt_dark(x_scale: float = 1.0, y_scale: float = 1.0, roi: Tuple[int, int, int, int] | None = None, rgb_channel: int = -1, alpha: int = 256, color_palette=PALETTE_IRONBOW, alpha_palette=None, hint: int = 0, copy: bool = False, copy_to_fb: bool = False)</h3><p>Converts an image to an RGB565 Dark Event Image (16-bits per pixel).</p><p><code>x_scale</code> controls how much the displayed image is scaled by in the x direction (float). If this value is negative the image will be flipped horizontally. Note that if <code>y_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>y_scale</code> controls how much the displayed image is scaled by in the y direction (float). If this value is negative the image will be flipped vertically. Note that if <code>x_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This allows you to extract just the pixels in the ROI to scale and draw on the destination image.</p><p><code>rgb_channel</code> is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed) and to render onto the destination image. For example, if you pass <code>rgb_channel=1</code> this will extract the green channel of the source RGB565 image and draw that in grayscale on the destination image.</p><p><code>alpha</code> controls how much of the source image to blend into the destination image. A value of 255 draws an opaque source image while a value lower than 255 produces a blend between the source and destination image. 0 results in no modification to the destination image.</p><p><code>color_palette</code> if not <code>None</code> can be an a color palette enum or a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of whatever the source image is. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>alpha_palette</code> if not <code>None</code> can be a 256 pixel in total GRAYSCALE image to use as a alpha palette which modulates the <code>alpha</code> value of the source image being drawn at a pixel pixel level allowing you to precisely control the alpha value of pixels based on their grayscale value. A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes more transparent until 0. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>hint</code> can be a logical OR of the flags:</p><div><ul><li><code>image.AREA</code>: Use area scaling when downscaling versus the default of nearest neighbor.</li><li><code>image.BILINEAR</code>: Use bilinear scaling versus the default of nearest neighbor scaling.</li><li><code>image.BICUBIC</code>: Use bicubic scaling versus the default of nearest neighbor scaling.</li><li><code>image.CENTER</code>: Center the image being drawn on the display. This is applied after scaling.</li><li><code>image.HMIRROR</code>: Horizontally mirror the image.</li><li><code>image.VFLIP</code>: Vertically flip the image.</li><li><code>image.TRANSPOSE</code>: Transpose the image (swap x/y).</li><li><code>image.EXTRACT_RGB_CHANNEL_FIRST</code>: Do rgb_channel extraction before scaling.</li><li><code>image.APPLY_COLOR_PALETTE_FIRST</code>: Apply color palette before scaling.</li><li><code>image.SCALE_ASPECT_KEEP</code>: Scale the image being drawn to fit inside the display.</li><li><code>image.SCALE_ASPECT_EXPAND</code>: Scale the image being drawn to fill the display (results in cropping)</li><li><code>image.SCALE_ASPECT_IGNORE</code>: Scale the image being drawn to fill the display (results in stretching).</li><li><code>image.ROTATE_90</code>: Rotate the image by 90 degrees (this is just VFLIP | TRANSPOSE).</li><li><code>image.ROTATE_180</code>: Rotate the image by 180 degrees (this is just HMIRROR | VFLIP).</li><li><code>image.ROTATE_270</code>: Rotate the image by 270 degrees (this is just HMIRROR | TRANSPOSE).</li></ul></div><p><code>copy</code> if True create a deep-copy on the heap of the image that’s been converted versus converting the original image in-place.</p><p><code>copy_to_fb</code> if True the image is loaded directly into the frame buffer. <code>copy_to_fb</code> has priority over <code>copy</code>. This has no special effect if the image is already in the frame buffer.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p>
		"""
		pass
	def to_evt_light(self, x_scale:float=1.0, y_scale:float=1.0, roi:Tuple[int,int,int,int]|None=None, rgb_channel:int=-1, alpha:int=256, color_palette=PALETTE_IRONBOW, alpha_palette=None, hint:int=0, copy:bool=False, copy_to_fb:bool=False) -> Image:
		"""
		<h3>image - Image.to_evt_light(x_scale: float = 1.0, y_scale: float = 1.0, roi: Tuple[int, int, int, int] | None = None, rgb_channel: int = -1, alpha: int = 256, color_palette=PALETTE_IRONBOW, alpha_palette=None, hint: int = 0, copy: bool = False, copy_to_fb: bool = False)</h3><p>Converts an image to an RGB565 Light Event Image (16-bits per pixel).</p><p><code>x_scale</code> controls how much the displayed image is scaled by in the x direction (float). If this value is negative the image will be flipped horizontally. Note that if <code>y_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>y_scale</code> controls how much the displayed image is scaled by in the y direction (float). If this value is negative the image will be flipped vertically. Note that if <code>x_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This allows you to extract just the pixels in the ROI to scale and draw on the destination image.</p><p><code>rgb_channel</code> is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed) and to render onto the destination image. For example, if you pass <code>rgb_channel=1</code> this will extract the green channel of the source RGB565 image and draw that in grayscale on the destination image.</p><p><code>alpha</code> controls how much of the source image to blend into the destination image. A value of 255 draws an opaque source image while a value lower than 255 produces a blend between the source and destination image. 0 results in no modification to the destination image.</p><p><code>color_palette</code> if not <code>None</code> can be an a color palette enum or a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of whatever the source image is. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>alpha_palette</code> if not <code>None</code> can be a 256 pixel in total GRAYSCALE image to use as a alpha palette which modulates the <code>alpha</code> value of the source image being drawn at a pixel pixel level allowing you to precisely control the alpha value of pixels based on their grayscale value. A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes more transparent until 0. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>hint</code> can be a logical OR of the flags:</p><div><ul><li><code>image.AREA</code>: Use area scaling when downscaling versus the default of nearest neighbor.</li><li><code>image.BILINEAR</code>: Use bilinear scaling versus the default of nearest neighbor scaling.</li><li><code>image.BICUBIC</code>: Use bicubic scaling versus the default of nearest neighbor scaling.</li><li><code>image.CENTER</code>: Center the image being drawn on the display. This is applied after scaling.</li><li><code>image.HMIRROR</code>: Horizontally mirror the image.</li><li><code>image.VFLIP</code>: Vertically flip the image.</li><li><code>image.TRANSPOSE</code>: Transpose the image (swap x/y).</li><li><code>image.EXTRACT_RGB_CHANNEL_FIRST</code>: Do rgb_channel extraction before scaling.</li><li><code>image.APPLY_COLOR_PALETTE_FIRST</code>: Apply color palette before scaling.</li><li><code>image.SCALE_ASPECT_KEEP</code>: Scale the image being drawn to fit inside the display.</li><li><code>image.SCALE_ASPECT_EXPAND</code>: Scale the image being drawn to fill the display (results in cropping)</li><li><code>image.SCALE_ASPECT_IGNORE</code>: Scale the image being drawn to fill the display (results in stretching).</li><li><code>image.ROTATE_90</code>: Rotate the image by 90 degrees (this is just VFLIP | TRANSPOSE).</li><li><code>image.ROTATE_180</code>: Rotate the image by 180 degrees (this is just HMIRROR | VFLIP).</li><li><code>image.ROTATE_270</code>: Rotate the image by 270 degrees (this is just HMIRROR | TRANSPOSE).</li></ul></div><p><code>copy</code> if True create a deep-copy on the heap of the image that’s been converted versus converting the original image in-place.</p><p><code>copy_to_fb</code> if True the image is loaded directly into the frame buffer. <code>copy_to_fb</code> has priority over <code>copy</code>. This has no special effect if the image is already in the frame buffer.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p>
		"""
		pass
	def to_jpeg(self, x_scale:float=1.0, y_scale:float=1.0, roi:Tuple[int,int,int,int]|None=None, rgb_channel:int=-1, alpha:int=256, color_palette=None, alpha_palette=None, hint:int=0, copy:bool=False, copy_to_fb:bool=False, quality:int=90, encode_for_ide:bool=False, subsampling:int=0) -> Image:
		"""
		<h3>image - Image.to_jpeg(x_scale: float = 1.0, y_scale: float = 1.0, roi: Tuple[int, int, int, int] | None = None, rgb_channel: int = -1, alpha: int = 256, color_palette=None, alpha_palette=None, hint: int = 0, copy: bool = False, copy_to_fb: bool = False, quality: int = 90, encode_for_ide: bool = False, subsampling: int = 0)</h3><p>Converts an image to a JPEG image.</p><p><code>x_scale</code> controls how much the displayed image is scaled by in the x direction (float). If this value is negative the image will be flipped horizontally. Note that if <code>y_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>y_scale</code> controls how much the displayed image is scaled by in the y direction (float). If this value is negative the image will be flipped vertically. Note that if <code>x_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This allows you to extract just the pixels in the ROI to scale and draw on the destination image.</p><p><code>rgb_channel</code> is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed) and to render onto the destination image. For example, if you pass <code>rgb_channel=1</code> this will extract the green channel of the source RGB565 image and draw that in grayscale on the destination image.</p><p><code>alpha</code> controls how much of the source image to blend into the destination image. A value of 255 draws an opaque source image while a value lower than 255 produces a blend between the source and destination image. 0 results in no modification to the destination image.</p><p><code>color_palette</code> if not <code>None</code> can be an a color palette enum or a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of whatever the source image is. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>alpha_palette</code> if not <code>None</code> can be a 256 pixel in total GRAYSCALE image to use as a alpha palette which modulates the <code>alpha</code> value of the source image being drawn at a pixel pixel level allowing you to precisely control the alpha value of pixels based on their grayscale value. A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes more transparent until 0. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>hint</code> can be a logical OR of the flags:</p><div><ul><li><code>image.AREA</code>: Use area scaling when downscaling versus the default of nearest neighbor.</li><li><code>image.BILINEAR</code>: Use bilinear scaling versus the default of nearest neighbor scaling.</li><li><code>image.BICUBIC</code>: Use bicubic scaling versus the default of nearest neighbor scaling.</li><li><code>image.CENTER</code>: Center the image being drawn on the display. This is applied after scaling.</li><li><code>image.HMIRROR</code>: Horizontally mirror the image.</li><li><code>image.VFLIP</code>: Vertically flip the image.</li><li><code>image.TRANSPOSE</code>: Transpose the image (swap x/y).</li><li><code>image.EXTRACT_RGB_CHANNEL_FIRST</code>: Do rgb_channel extraction before scaling.</li><li><code>image.APPLY_COLOR_PALETTE_FIRST</code>: Apply color palette before scaling.</li><li><code>image.SCALE_ASPECT_KEEP</code>: Scale the image being drawn to fit inside the display.</li><li><code>image.SCALE_ASPECT_EXPAND</code>: Scale the image being drawn to fill the display (results in cropping)</li><li><code>image.SCALE_ASPECT_IGNORE</code>: Scale the image being drawn to fill the display (results in stretching).</li><li><code>image.ROTATE_90</code>: Rotate the image by 90 degrees (this is just VFLIP | TRANSPOSE).</li><li><code>image.ROTATE_180</code>: Rotate the image by 180 degrees (this is just HMIRROR | VFLIP).</li><li><code>image.ROTATE_270</code>: Rotate the image by 270 degrees (this is just HMIRROR | TRANSPOSE).</li></ul></div><p><code>copy</code> if True create a deep-copy on the heap of the image that’s been converted versus converting the original image in-place.</p><p><code>copy_to_fb</code> if True the image is loaded directly into the frame buffer. <code>copy_to_fb</code> has priority over <code>copy</code>. This has no special effect if the image is already in the frame buffer.</p><p><code>quality</code> controls the jpeg image compression quality. The value can be between 0 and 100.</p><p><code>encode_for_ide</code> if True the image is encoded in a way that the IDE can display it if printed by doing <code>print(image)</code>. This is useful for debugging purposes over UARTs via Open Terminal in the IDE.</p><p><code>subsampling</code> can be:</p><div><ul><li><code>image.JPEG_SUBSAMPLING_AUTO</code>: Use the best subsampling for the image based on the quality.</li><li><code>image.JPEG_SUBSAMPLING_444</code>: Use 4:4:4 subsampling.</li><li><code>image.JPEG_SUBSAMPLING_422</code>: Use 4:2:2 subsampling.</li><li><code>image.JPEG_SUBSAMPLING_420</code>: Use 4:2:0 subsampling.</li></ul></div><p>Returns the image object so you can call another method using <code>.</code> notation.</p>
		"""
		pass
	def to_png(self, x_scale:float=1.0, y_scale:float=1.0, roi:Tuple[int,int,int,int]|None=None, rgb_channel:int=-1, alpha:int=256, color_palette=None, alpha_palette=None, hint:int=0, copy:bool=False, copy_to_fb:bool=False) -> Image:
		"""
		<h3>image - Image.to_png(x_scale: float = 1.0, y_scale: float = 1.0, roi: Tuple[int, int, int, int] | None = None, rgb_channel: int = -1, alpha: int = 256, color_palette=None, alpha_palette=None, hint: int = 0, copy: bool = False, copy_to_fb: bool = False)</h3><p>Converts an image to a PNG image.</p><p><code>x_scale</code> controls how much the displayed image is scaled by in the x direction (float). If this value is negative the image will be flipped horizontally. Note that if <code>y_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>y_scale</code> controls how much the displayed image is scaled by in the y direction (float). If this value is negative the image will be flipped vertically. Note that if <code>x_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This allows you to extract just the pixels in the ROI to scale and draw on the destination image.</p><p><code>rgb_channel</code> is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed) and to render onto the destination image. For example, if you pass <code>rgb_channel=1</code> this will extract the green channel of the source RGB565 image and draw that in grayscale on the destination image.</p><p><code>alpha</code> controls how much of the source image to blend into the destination image. A value of 255 draws an opaque source image while a value lower than 255 produces a blend between the source and destination image. 0 results in no modification to the destination image.</p><p><code>color_palette</code> if not <code>None</code> can be an a color palette enum or a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of whatever the source image is. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>alpha_palette</code> if not <code>None</code> can be a 256 pixel in total GRAYSCALE image to use as a alpha palette which modulates the <code>alpha</code> value of the source image being drawn at a pixel pixel level allowing you to precisely control the alpha value of pixels based on their grayscale value. A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes more transparent until 0. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>hint</code> can be a logical OR of the flags:</p><div><ul><li><code>image.AREA</code>: Use area scaling when downscaling versus the default of nearest neighbor.</li><li><code>image.BILINEAR</code>: Use bilinear scaling versus the default of nearest neighbor scaling.</li><li><code>image.BICUBIC</code>: Use bicubic scaling versus the default of nearest neighbor scaling.</li><li><code>image.CENTER</code>: Center the image being drawn on the display. This is applied after scaling.</li><li><code>image.HMIRROR</code>: Horizontally mirror the image.</li><li><code>image.VFLIP</code>: Vertically flip the image.</li><li><code>image.TRANSPOSE</code>: Transpose the image (swap x/y).</li><li><code>image.EXTRACT_RGB_CHANNEL_FIRST</code>: Do rgb_channel extraction before scaling.</li><li><code>image.APPLY_COLOR_PALETTE_FIRST</code>: Apply color palette before scaling.</li><li><code>image.SCALE_ASPECT_KEEP</code>: Scale the image being drawn to fit inside the display.</li><li><code>image.SCALE_ASPECT_EXPAND</code>: Scale the image being drawn to fill the display (results in cropping)</li><li><code>image.SCALE_ASPECT_IGNORE</code>: Scale the image being drawn to fill the display (results in stretching).</li><li><code>image.ROTATE_90</code>: Rotate the image by 90 degrees (this is just VFLIP | TRANSPOSE).</li><li><code>image.ROTATE_180</code>: Rotate the image by 180 degrees (this is just HMIRROR | VFLIP).</li><li><code>image.ROTATE_270</code>: Rotate the image by 270 degrees (this is just HMIRROR | TRANSPOSE).</li></ul></div><p><code>copy</code> if True create a deep-copy on the heap of the image that’s been converted versus converting the original image in-place.</p><p><code>copy_to_fb</code> if True the image is loaded directly into the frame buffer. <code>copy_to_fb</code> has priority over <code>copy</code>. This has no special effect if the image is already in the frame buffer.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p>
		"""
		pass
	def compress(self, x_scale:float=1.0, y_scale:float=1.0, roi:Tuple[int,int,int,int]|None=None, rgb_channel:int=-1, alpha:int=256, color_palette=None, alpha_palette=None, hint:int=0, copy:bool=False, copy_to_fb:bool=False, quality:int=90, encode_for_ide:bool=False, subsampling:int=0) -> Image:
		"""
		<h3>image - Image.compress(x_scale: float = 1.0, y_scale: float = 1.0, roi: Tuple[int, int, int, int] | None = None, rgb_channel: int = -1, alpha: int = 256, color_palette=None, alpha_palette=None, hint: int = 0, copy: bool = False, copy_to_fb: bool = False, quality: int = 90, encode_for_ide: bool = False, subsampling: int = 0)</h3><p>Converts an image to a JPEG image.</p><p><code>x_scale</code> controls how much the displayed image is scaled by in the x direction (float). If this value is negative the image will be flipped horizontally. Note that if <code>y_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>y_scale</code> controls how much the displayed image is scaled by in the y direction (float). If this value is negative the image will be flipped vertically. Note that if <code>x_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This allows you to extract just the pixels in the ROI to scale and draw on the destination image.</p><p><code>rgb_channel</code> is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed) and to render onto the destination image. For example, if you pass <code>rgb_channel=1</code> this will extract the green channel of the source RGB565 image and draw that in grayscale on the destination image.</p><p><code>alpha</code> controls how much of the source image to blend into the destination image. A value of 255 draws an opaque source image while a value lower than 255 produces a blend between the source and destination image. 0 results in no modification to the destination image.</p><p><code>color_palette</code> if not <code>None</code> can be an a color palette enum or a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of whatever the source image is. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>alpha_palette</code> if not <code>None</code> can be a 256 pixel in total GRAYSCALE image to use as a alpha palette which modulates the <code>alpha</code> value of the source image being drawn at a pixel pixel level allowing you to precisely control the alpha value of pixels based on their grayscale value. A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes more transparent until 0. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>hint</code> can be a logical OR of the flags:</p><div><ul><li><code>image.AREA</code>: Use area scaling when downscaling versus the default of nearest neighbor.</li><li><code>image.BILINEAR</code>: Use bilinear scaling versus the default of nearest neighbor scaling.</li><li><code>image.BICUBIC</code>: Use bicubic scaling versus the default of nearest neighbor scaling.</li><li><code>image.CENTER</code>: Center the image being drawn on the display. This is applied after scaling.</li><li><code>image.HMIRROR</code>: Horizontally mirror the image.</li><li><code>image.VFLIP</code>: Vertically flip the image.</li><li><code>image.TRANSPOSE</code>: Transpose the image (swap x/y).</li><li><code>image.EXTRACT_RGB_CHANNEL_FIRST</code>: Do rgb_channel extraction before scaling.</li><li><code>image.APPLY_COLOR_PALETTE_FIRST</code>: Apply color palette before scaling.</li><li><code>image.SCALE_ASPECT_KEEP</code>: Scale the image being drawn to fit inside the display.</li><li><code>image.SCALE_ASPECT_EXPAND</code>: Scale the image being drawn to fill the display (results in cropping)</li><li><code>image.SCALE_ASPECT_IGNORE</code>: Scale the image being drawn to fill the display (results in stretching).</li><li><code>image.ROTATE_90</code>: Rotate the image by 90 degrees (this is just VFLIP | TRANSPOSE).</li><li><code>image.ROTATE_180</code>: Rotate the image by 180 degrees (this is just HMIRROR | VFLIP).</li><li><code>image.ROTATE_270</code>: Rotate the image by 270 degrees (this is just HMIRROR | TRANSPOSE).</li></ul></div><p><code>copy</code> if True create a deep-copy on the heap of the image that’s been converted versus converting the original image in-place.</p><p><code>copy_to_fb</code> if True the image is loaded directly into the frame buffer. <code>copy_to_fb</code> has priority over <code>copy</code>. This has no special effect if the image is already in the frame buffer.</p><p><code>quality</code> controls the jpeg image compression quality. The value can be between 0 and 100.</p><p><code>encode_for_ide</code> if True the image is encoded in a way that the IDE can display it if printed by doing <code>print(image)</code>. This is useful for debugging purposes over UARTs via Open Terminal in the IDE.</p><p><code>subsampling</code> can be:</p><div><ul><li><code>image.JPEG_SUBSAMPLING_AUTO</code>: Use the best subsampling for the image based on the quality.</li><li><code>image.JPEG_SUBSAMPLING_444</code>: Use 4:4:4 subsampling.</li><li><code>image.JPEG_SUBSAMPLING_422</code>: Use 4:2:2 subsampling.</li><li><code>image.JPEG_SUBSAMPLING_420</code>: Use 4:2:0 subsampling.</li></ul></div><p>Returns the image object so you can call another method using <code>.</code> notation.</p><div><p>Note</p><p><code>Image.compress</code> is an alias for <code>Image.to_jpeg</code>.</p></div>
		"""
		pass
	def copy(self, x_scale:float=1.0, y_scale:float=1.0, roi:Tuple[int,int,int,int]|None=None, rgb_channel:int=-1, alpha:int=256, color_palette=None, alpha_palette=None, hint:int=0, copy_to_fb:float=False) -> Image:
		"""
		<h3>image - Image.copy(x_scale: float = 1.0, y_scale: float = 1.0, roi: Tuple[int, int, int, int] | None = None, rgb_channel: int = -1, alpha: int = 256, color_palette=None, alpha_palette=None, hint: int = 0, copy_to_fb: float = False)</h3><p>Creates a deep copy of the image object.</p><p><code>x_scale</code> controls how much the displayed image is scaled by in the x direction (float). If this value is negative the image will be flipped horizontally. Note that if <code>y_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>y_scale</code> controls how much the displayed image is scaled by in the y direction (float). If this value is negative the image will be flipped vertically. Note that if <code>x_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This allows you to extract just the pixels in the ROI to scale and draw on the destination image.</p><p><code>rgb_channel</code> is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed) and to render onto the destination image. For example, if you pass <code>rgb_channel=1</code> this will extract the green channel of the source RGB565 image and draw that in grayscale on the destination image.</p><p><code>alpha</code> controls how much of the source image to blend into the destination image. A value of 255 draws an opaque source image while a value lower than 255 produces a blend between the source and destination image. 0 results in no modification to the destination image.</p><p><code>color_palette</code> if not <code>None</code> can be an a color palette enum or a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of whatever the source image is. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>alpha_palette</code> if not <code>None</code> can be a 256 pixel in total GRAYSCALE image to use as a alpha palette which modulates the <code>alpha</code> value of the source image being drawn at a pixel pixel level allowing you to precisely control the alpha value of pixels based on their grayscale value. A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes more transparent until 0. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>hint</code> can be a logical OR of the flags:</p><div><ul><li><code>image.AREA</code>: Use area scaling when downscaling versus the default of nearest neighbor.</li><li><code>image.BILINEAR</code>: Use bilinear scaling versus the default of nearest neighbor scaling.</li><li><code>image.BICUBIC</code>: Use bicubic scaling versus the default of nearest neighbor scaling.</li><li><code>image.CENTER</code>: Center the image being drawn on the display. This is applied after scaling.</li><li><code>image.HMIRROR</code>: Horizontally mirror the image.</li><li><code>image.VFLIP</code>: Vertically flip the image.</li><li><code>image.TRANSPOSE</code>: Transpose the image (swap x/y).</li><li><code>image.EXTRACT_RGB_CHANNEL_FIRST</code>: Do rgb_channel extraction before scaling.</li><li><code>image.APPLY_COLOR_PALETTE_FIRST</code>: Apply color palette before scaling.</li><li><code>image.SCALE_ASPECT_KEEP</code>: Scale the image being drawn to fit inside the display.</li><li><code>image.SCALE_ASPECT_EXPAND</code>: Scale the image being drawn to fill the display (results in cropping)</li><li><code>image.SCALE_ASPECT_IGNORE</code>: Scale the image being drawn to fill the display (results in stretching).</li><li><code>image.ROTATE_90</code>: Rotate the image by 90 degrees (this is just VFLIP | TRANSPOSE).</li><li><code>image.ROTATE_180</code>: Rotate the image by 180 degrees (this is just HMIRROR | VFLIP).</li><li><code>image.ROTATE_270</code>: Rotate the image by 270 degrees (this is just HMIRROR | TRANSPOSE).</li></ul></div><p><code>copy_to_fb</code> if True the image is loaded directly into the frame buffer. This has no special effect if the image is already in the frame buffer.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p>
		"""
		pass
	def crop(self, x_scale:float=1.0, y_scale:float=1.0, roi:Tuple[int,int,int,int]|None=None, rgb_channel:int=-1, alpha:int=256, color_palette=None, alpha_palette=None, hint:int=0, copy:bool=False, copy_to_fb:bool=False) -> Image:
		"""
		<h3>image - Image.crop(x_scale: float = 1.0, y_scale: float = 1.0, roi: Tuple[int, int, int, int] | None = None, rgb_channel: int = -1, alpha: int = 256, color_palette=None, alpha_palette=None, hint: int = 0, copy: bool = False, copy_to_fb: bool = False)</h3><p>Modifies an image in-place without changing the underlying image type.</p><p><code>x_scale</code> controls how much the displayed image is scaled by in the x direction (float). If this value is negative the image will be flipped horizontally. Note that if <code>y_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>y_scale</code> controls how much the displayed image is scaled by in the y direction (float). If this value is negative the image will be flipped vertically. Note that if <code>x_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This allows you to extract just the pixels in the ROI to scale and draw on the destination image.</p><p><code>rgb_channel</code> is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed) and to render onto the destination image. For example, if you pass <code>rgb_channel=1</code> this will extract the green channel of the source RGB565 image and draw that in grayscale on the destination image.</p><p><code>alpha</code> controls how much of the source image to blend into the destination image. A value of 255 draws an opaque source image while a value lower than 255 produces a blend between the source and destination image. 0 results in no modification to the destination image.</p><p><code>color_palette</code> if not <code>None</code> can be an a color palette enum or a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of whatever the source image is. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>alpha_palette</code> if not <code>None</code> can be a 256 pixel in total GRAYSCALE image to use as a alpha palette which modulates the <code>alpha</code> value of the source image being drawn at a pixel pixel level allowing you to precisely control the alpha value of pixels based on their grayscale value. A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes more transparent until 0. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>hint</code> can be a logical OR of the flags:</p><div><ul><li><code>image.AREA</code>: Use area scaling when downscaling versus the default of nearest neighbor.</li><li><code>image.BILINEAR</code>: Use bilinear scaling versus the default of nearest neighbor scaling.</li><li><code>image.BICUBIC</code>: Use bicubic scaling versus the default of nearest neighbor scaling.</li><li><code>image.CENTER</code>: Center the image being drawn on the display. This is applied after scaling.</li><li><code>image.HMIRROR</code>: Horizontally mirror the image.</li><li><code>image.VFLIP</code>: Vertically flip the image.</li><li><code>image.TRANSPOSE</code>: Transpose the image (swap x/y).</li><li><code>image.EXTRACT_RGB_CHANNEL_FIRST</code>: Do rgb_channel extraction before scaling.</li><li><code>image.APPLY_COLOR_PALETTE_FIRST</code>: Apply color palette before scaling.</li><li><code>image.SCALE_ASPECT_KEEP</code>: Scale the image being drawn to fit inside the display.</li><li><code>image.SCALE_ASPECT_EXPAND</code>: Scale the image being drawn to fill the display (results in cropping)</li><li><code>image.SCALE_ASPECT_IGNORE</code>: Scale the image being drawn to fill the display (results in stretching).</li><li><code>image.ROTATE_90</code>: Rotate the image by 90 degrees (this is just VFLIP | TRANSPOSE).</li><li><code>image.ROTATE_180</code>: Rotate the image by 180 degrees (this is just HMIRROR | VFLIP).</li><li><code>image.ROTATE_270</code>: Rotate the image by 270 degrees (this is just HMIRROR | TRANSPOSE).</li></ul></div><p><code>copy</code> if True create a deep-copy on the heap of the image that’s been converted versus converting the original image in-place.</p><p><code>copy_to_fb</code> if True the image is loaded directly into the frame buffer. <code>copy_to_fb</code> has priority over <code>copy</code>. This has no special effect if the image is already in the frame buffer.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p>
		"""
		pass
	def scale(self, x_scale:float=1.0, y_scale:float=1.0, roi:Tuple[int,int,int,int]|None=None, rgb_channel:int=-1, alpha:int=256, color_palette=None, alpha_palette=None, hint:int=0, copy:bool=False, copy_to_fb:bool=False) -> Image:
		"""
		<h3>image - Image.scale(x_scale: float = 1.0, y_scale: float = 1.0, roi: Tuple[int, int, int, int] | None = None, rgb_channel: int = -1, alpha: int = 256, color_palette=None, alpha_palette=None, hint: int = 0, copy: bool = False, copy_to_fb: bool = False)</h3><p>Modifies an image in-place without changing the underlying image type.</p><p><code>x_scale</code> controls how much the displayed image is scaled by in the x direction (float). If this value is negative the image will be flipped horizontally. Note that if <code>y_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>y_scale</code> controls how much the displayed image is scaled by in the y direction (float). If this value is negative the image will be flipped vertically. Note that if <code>x_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This allows you to extract just the pixels in the ROI to scale and draw on the destination image.</p><p><code>rgb_channel</code> is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed) and to render onto the destination image. For example, if you pass <code>rgb_channel=1</code> this will extract the green channel of the source RGB565 image and draw that in grayscale on the destination image.</p><p><code>alpha</code> controls how much of the source image to blend into the destination image. A value of 255 draws an opaque source image while a value lower than 255 produces a blend between the source and destination image. 0 results in no modification to the destination image.</p><p><code>color_palette</code> if not <code>None</code> can be an a color palette enum or a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of whatever the source image is. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>alpha_palette</code> if not <code>None</code> can be a 256 pixel in total GRAYSCALE image to use as a alpha palette which modulates the <code>alpha</code> value of the source image being drawn at a pixel pixel level allowing you to precisely control the alpha value of pixels based on their grayscale value. A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes more transparent until 0. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>hint</code> can be a logical OR of the flags:</p><div><ul><li><code>image.AREA</code>: Use area scaling when downscaling versus the default of nearest neighbor.</li><li><code>image.BILINEAR</code>: Use bilinear scaling versus the default of nearest neighbor scaling.</li><li><code>image.BICUBIC</code>: Use bicubic scaling versus the default of nearest neighbor scaling.</li><li><code>image.CENTER</code>: Center the image being drawn on the display. This is applied after scaling.</li><li><code>image.HMIRROR</code>: Horizontally mirror the image.</li><li><code>image.VFLIP</code>: Vertically flip the image.</li><li><code>image.TRANSPOSE</code>: Transpose the image (swap x/y).</li><li><code>image.EXTRACT_RGB_CHANNEL_FIRST</code>: Do rgb_channel extraction before scaling.</li><li><code>image.APPLY_COLOR_PALETTE_FIRST</code>: Apply color palette before scaling.</li><li><code>image.SCALE_ASPECT_KEEP</code>: Scale the image being drawn to fit inside the display.</li><li><code>image.SCALE_ASPECT_EXPAND</code>: Scale the image being drawn to fill the display (results in cropping)</li><li><code>image.SCALE_ASPECT_IGNORE</code>: Scale the image being drawn to fill the display (results in stretching).</li><li><code>image.ROTATE_90</code>: Rotate the image by 90 degrees (this is just VFLIP | TRANSPOSE).</li><li><code>image.ROTATE_180</code>: Rotate the image by 180 degrees (this is just HMIRROR | VFLIP).</li><li><code>image.ROTATE_270</code>: Rotate the image by 270 degrees (this is just HMIRROR | TRANSPOSE).</li></ul></div><p><code>copy</code> if True create a deep-copy on the heap of the image that’s been converted versus converting the original image in-place.</p><p><code>copy_to_fb</code> if True the image is loaded directly into the frame buffer. <code>copy_to_fb</code> has priority over <code>copy</code>. This has no special effect if the image is already in the frame buffer.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><div><p>Note</p><p><code>Image.scale</code> is an alias for <code>Image.crop</code>.</p></div>
		"""
		pass
	def save(self, path:str, roi:Tuple[int,int,int,int]|None=None, quality=50) -> Image:
		"""
		<h3>image - Image.save(path: str, roi: Tuple[int, int, int, int] | None = None, quality=50)</h3><p>Saves a copy of the image to the filesystem at <code>path</code>.</p><p>Supports bmp/pgm/ppm/jpg/jpeg image files. Note that you cannot save jpeg compressed images to an uncompressed format.</p><p><code>roi</code> is the region-of-interest rectangle (x, y, w, h) to save from. If not specified, it is equal to the image rectangle which copies the entire image. This argument is not applicable for JPEG images.</p><p><code>quality</code> is the jpeg compression quality to use to save the image to jpeg format if the image is not already compressed (0-100) (int).</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p>
		"""
		pass
	def flush(self) -> None:
		"""
		<h3>image - Image.flush()</h3><p>Updates the frame buffer in the IDE with the image in the frame buffer on the camera.</p>
		"""
		pass
	def clear(self, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.clear(mask: Image | None = None)</h3><p>Sets all pixels in the image to zero (very fast).</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images.</p>
		"""
		pass
	def draw_line(self, x0:int, y0:int, x1:int, y1:int, color:int|Tuple[int,int,int]|None=None, thickness=1) -> Image:
		"""
		<h3>image - Image.draw_line(x0: int, y0: int, x1: int, y1: int, color: int | Tuple[int, int, int] | None = None, thickness=1)</h3><p>Draws a line from (x0, y0) to (x1, y1) on the image. You may either pass x0, y0, x1, y1 separately or as a tuple (x0, y0, x1, y1).</p><p><code>color</code> is an RGB888 tuple for Grayscale or RGB565 images. Defaults to white. However, you may also pass the underlying pixel value (0-255) for grayscale images or a RGB565 value for RGB565 images.</p><p><code>thickness</code> controls how thick the line is in pixels.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def draw_rectangle(self, x:int, y:int, w:int, h:int, color:int|Tuple[int,int,int]|None=None, thickness=1, fill=False) -> Image:
		"""
		<h3>image - Image.draw_rectangle(x: int, y: int, w: int, h: int, color: int | Tuple[int, int, int] | None = None, thickness=1, fill=False)</h3><p>Draws a rectangle on the image. You may either pass x, y, w, h separately or as a tuple (x, y, w, h).</p><p><code>color</code> is an RGB888 tuple for Grayscale or RGB565 images. Defaults to white. However, you may also pass the underlying pixel value (0-255) for grayscale images or a RGB565 value for RGB565 images.</p><p><code>thickness</code> controls how thick the lines are in pixels.</p><p>Pass <code>fill</code> set to True to fill the rectangle.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def draw_circle(self, x:int, y:int, radius:int, color:int|Tuple[int,int,int]|None=None, thickness=1, fill=False) -> Image:
		"""
		<h3>image - Image.draw_circle(x: int, y: int, radius: int, color: int | Tuple[int, int, int] | None = None, thickness=1, fill=False)</h3><p>Draws a circle on the image. You may either pass x, y, radius separately or as a tuple (x, y, radius).</p><p><code>color</code> is an RGB888 tuple for Grayscale or RGB565 images. Defaults to white. However, you may also pass the underlying pixel value (0-255) for grayscale images or a RGB565 value for RGB565 images.</p><p><code>thickness</code> controls how thick the edges are in pixels.</p><p>Pass <code>fill</code> set to True to fill the circle.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def draw_ellipse(self, cx:int, cy:int, rx:int, ry:int, rotation:int, color:int|Tuple[int,int,int]|None=None, thickness=1, fill=False) -> Image:
		"""
		<h3>image - Image.draw_ellipse(cx: int, cy: int, rx: int, ry: int, rotation: int, color: int | Tuple[int, int, int] | None = None, thickness=1, fill=False)</h3><p>Draws an ellipse on the image. You may either pass cx, cy, rx, ry, and the rotation (in degrees) separately or as a tuple (cx, yc, rx, ry, rotation).</p><p><code>color</code> is an RGB888 tuple for Grayscale or RGB565 images. Defaults to white. However, you may also pass the underlying pixel value (0-255) for grayscale images or a RGB565 value for RGB565 images.</p><p><code>thickness</code> controls how thick the edges are in pixels.</p><p>Pass <code>fill</code> set to True to fill the ellipse.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def draw_string(self, x:int, y:int, text:str, color:int|Tuple[int,int,int]|None=None, scale=1, x_spacing=0, y_spacing=0, mono_space=True, char_rotation=0, char_hmirror=False, char_vflip=False, string_rotation=0, string_hmirror=False, string_vflip=False) -> Image:
		"""
		<h3>image - Image.draw_string(x: int, y: int, text: str, color: int | Tuple[int, int, int] | None = None, scale=1, x_spacing=0, y_spacing=0, mono_space=True, char_rotation=0, char_hmirror=False, char_vflip=False, string_rotation=0, string_hmirror=False, string_vflip=False)</h3><p>Draws 8x10 text starting at location (x, y) in the image. You may either pass x, y separately or as a tuple (x, y).</p><p><code>text</code> is a string to write to the image. <code>\n</code>, <code>\r</code>, and <code>\r\n</code> line endings move the cursor to the next line.</p><p><code>color</code> is an RGB888 tuple for Grayscale or RGB565 images. Defaults to white. However, you may also pass the underlying pixel value (0-255) for grayscale images or a RGB565 value for RGB565 images.</p><p><code>scale</code> may be increased to increase/decrease the size of the text on the image. You can pass greater than 0 integer or floating point values.</p><p><code>x_spacing</code> allows you to add (if positive) or subtract (if negative) x pixels between cahracters.</p><p><code>y_spacing</code> allows you to add (if positive) or subtract (if negative) y pixels between cahracters (for multi-line text).</p><p><code>mono_space</code> defaults to True which forces text to be fixed spaced. For large text scales this looks terrible. Set the False to get non-fixed width character spacing which looks A LOT better.</p><p><code>char_rotation</code> may be 0, 90, 180, 270 to rotate each character in the string by this amount.</p><p><code>char_hmirror</code> if True horizontally mirrors all characters in the string.</p><p><code>char_vflip</code> if True vertically flips all characters in the string.</p><p><code>string_rotation</code> may be 0, 90, 180, 270 to rotate the string by this amount.</p><p><code>string_hmirror</code> if True horizontally mirrors the string.</p><p><code>string_vflip</code> if True vertically flips the string.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def draw_cross(self, x:int, y:int, color:int|Tuple[int,int,int]|None=None, size=5, thickness=1) -> Image:
		"""
		<h3>image - Image.draw_cross(x: int, y: int, color: int | Tuple[int, int, int] | None = None, size=5, thickness=1)</h3><p>Draws a cross at location x, y. You may either pass x, y separately or as a tuple (x, y).</p><p><code>color</code> is an RGB888 tuple for Grayscale or RGB565 images. Defaults to white. However, you may also pass the underlying pixel value (0-255) for grayscale images or a RGB565 value for RGB565 images.</p><p><code>size</code> controls how long the lines of the cross extend.</p><p><code>thickness</code> controls how thick the edges are in pixels.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def draw_arrow(self, x0:int, y0:int, x1:int, y1:int, color:int|Tuple[int,int,int]|None=None, thickness=1) -> Image:
		"""
		<h3>image - Image.draw_arrow(x0: int, y0: int, x1: int, y1: int, color: int | Tuple[int, int, int] | None = None, thickness=1)</h3><p>Draws an arrow from (x0, y0) to (x1, y1) on the image. You may either pass x0, y0, x1, y1 separately or as a tuple (x0, y0, x1, y1).</p><p><code>color</code> is an RGB888 tuple for Grayscale or RGB565 images. Defaults to white. However, you may also pass the underlying pixel value (0-255) for grayscale images or a RGB565 value for RGB565 images.</p><p><code>thickness</code> controls how thick the line is in pixels.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def draw_edges(self, image:Image, corners, color:int|Tuple[int,int,int]|None=None, size=0, thickness=1, fill=False) -> Image:
		"""
		<h3>image - Image.draw_edges(image: Image, corners, color: int | Tuple[int, int, int] | None = None, size=0, thickness=1, fill=False)</h3><p>Draws line edges between a corner list returned by methods like <code>blob.corners</code>. Coners is a four valued tuple of two valued x/y tuples. E.g. [(x1,y1),(x2,y2),(x3,y3),(x4,y4)].</p><p><code>color</code> is an RGB888 tuple for Grayscale or RGB565 images. Defaults to white. However, you may also pass the underlying pixel value (0-255) for grayscale images or a RGB565 value for RGB565 images.</p><p><code>size</code> if greater than 0 causes the corners to be drawn as circles of radius <code>size</code>.</p><p><code>thickness</code> controls how thick the line is in pixels.</p><p>Pass <code>fill</code> set to True to fill the corner circles if drawn.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def draw_image(self, image:Image, x:int, y:int, x_scale:float=1.0, y_scale:float=1.0, roi:Tuple[int,int,int,int]|None=None, rgb_channel:int=-1, alpha:int=256, color_palette=None, alpha_palette=None, hint:int=0) -> Image:
		"""
		<h3>image - Image.draw_image(image: Image, x: int, y: int, x_scale: float = 1.0, y_scale: float = 1.0, roi: Tuple[int, int, int, int] | None = None, rgb_channel: int = -1, alpha: int = 256, color_palette=None, alpha_palette=None, hint: int = 0)</h3><p>Draws an <code>image</code> whose top-left corner starts at location x, y. You may either pass x, y separately or as a tuple (x, y). This method automatically handles rendering the image passed into the correct pixel format for the destination image while also handling clipping seamlessly.</p><p>You may also pass a path instead of an image object for this method to automatically load the image from disk and use it in one step. E.g. <code>draw_image(&quot;test.jpg&quot;)</code>.</p><p><code>x_scale</code> controls how much the displayed image is scaled by in the x direction (float). If this value is negative the image will be flipped horizontally. Note that if <code>y_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>y_scale</code> controls how much the displayed image is scaled by in the y direction (float). If this value is negative the image will be flipped vertically. Note that if <code>x_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This allows you to extract just the pixels in the ROI to scale and draw on the destination image.</p><p><code>rgb_channel</code> is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed) and to render onto the destination image. For example, if you pass <code>rgb_channel=1</code> this will extract the green channel of the source RGB565 image and draw that in grayscale on the destination image.</p><p><code>alpha</code> controls how much of the source image to blend into the destination image. A value of 255 draws an opaque source image while a value lower than 255 produces a blend between the source and destination image. 0 results in no modification to the destination image.</p><p><code>color_palette</code> if not <code>None</code> can be an a color palette enum or a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of whatever the source image is. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>alpha_palette</code> if not <code>None</code> can be a 256 pixel in total GRAYSCALE image to use as a alpha palette which modulates the <code>alpha</code> value of the source image being drawn at a pixel pixel level allowing you to precisely control the alpha value of pixels based on their grayscale value. A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes more transparent until 0. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>hint</code> can be a logical OR of the flags:</p><div><ul><li><code>image.AREA</code>: Use area scaling when downscaling versus the default of nearest neighbor.</li><li><code>image.BILINEAR</code>: Use bilinear scaling versus the default of nearest neighbor scaling.</li><li><code>image.BICUBIC</code>: Use bicubic scaling versus the default of nearest neighbor scaling.</li><li><code>image.CENTER</code>: Center the image being drawn on the display. This is applied after scaling.</li><li><code>image.HMIRROR</code>: Horizontally mirror the image.</li><li><code>image.VFLIP</code>: Vertically flip the image.</li><li><code>image.TRANSPOSE</code>: Transpose the image (swap x/y).</li><li><code>image.EXTRACT_RGB_CHANNEL_FIRST</code>: Do rgb_channel extraction before scaling.</li><li><code>image.APPLY_COLOR_PALETTE_FIRST</code>: Apply color palette before scaling.</li><li><code>image.SCALE_ASPECT_KEEP</code>: Scale the image being drawn to fit inside the display.</li><li><code>image.SCALE_ASPECT_EXPAND</code>: Scale the image being drawn to fill the display (results in cropping)</li><li><code>image.SCALE_ASPECT_IGNORE</code>: Scale the image being drawn to fill the display (results in stretching).</li><li><code>image.ROTATE_90</code>: Rotate the image by 90 degrees (this is just VFLIP | TRANSPOSE).</li><li><code>image.ROTATE_180</code>: Rotate the image by 180 degrees (this is just HMIRROR | VFLIP).</li><li><code>image.ROTATE_270</code>: Rotate the image by 270 degrees (this is just HMIRROR | TRANSPOSE).</li><li><code>image.BLACK_BACKGROUND</code>: Assume the background image being drawn on is black speeding up blending.</li></ul></div><p>Returns the image object so you can call another method using <code>.</code> notation.</p>
		"""
		pass
	def draw_keypoints(self, keypoints, color:int|Tuple[int,int,int]|None=None, size=10, thickness=1, fill=False) -> Image:
		"""
		<h3>image - Image.draw_keypoints(keypoints, color: int | Tuple[int, int, int] | None = None, size=10, thickness=1, fill=False)</h3><p>Draws the keypoints of a keypoints object on the image. You may also pass a list of three value tuples containing the (x, y, rotation_angle_in_degrees) to re-use this method for drawing keypoint glyphs which are a cirle with a line pointing in a particular direction.</p><p><code>color</code> is an RGB888 tuple for Grayscale or RGB565 images. Defaults to white. However, you may also pass the underlying pixel value (0-255) for grayscale images or a RGB565 value for RGB565 images.</p><p><code>size</code> controls how large the keypoints are.</p><p><code>thickness</code> controls how thick the line is in pixels.</p><p>Pass <code>fill</code> set to True to fill the keypoints.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def flood_fill(self, x:int, y:int, seed_threshold=0.05, floating_threshold=0.05, color:int|Tuple[int,int,int]|None=None, invert=False, clear_background=False, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.flood_fill(x: int, y: int, seed_threshold=0.05, floating_threshold=0.05, color: int | Tuple[int, int, int] | None = None, invert=False, clear_background=False, mask: Image | None = None)</h3><p>Flood fills a region of the image starting from location x, y. You may either pass x, y separately or as a tuple (x, y).</p><p><code>seed_threshold</code> controls how different any pixel in the fill area may be from the original starting pixel.</p><p><code>floating_threshold</code> controls how different any pixel in the fill area may be from any neighbor pixels.</p><p><code>color</code> is an RGB888 tuple for Grayscale or RGB565 images. Defaults to white. However, you may also pass the underlying pixel value (0-255) for grayscale images or a RGB565 value for RGB565 images.</p><p>Pass <code>invert</code> as True to re-color everything outside of the flood-fill connected area.</p><p>Pass <code>clear_background</code> as True to zero the rest of the pixels that flood-fill did not re-color.</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are evaluated when flood filling.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p><p>This method is not available on the OpenMV Cam M4.</p>
		"""
		pass
	def mask_rectange(self, x:int, y:int, w:int, h:int) -> Image:
		"""
		<h3>image - Image.mask_rectange(x: int, y: int, w: int, h: int)</h3><p>Zeros a rectangular part of the image. If no arguments are supplied this method zeros the center of the image.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def mask_circle(self, x:int, y:int, radius:int) -> Image:
		"""
		<h3>image - Image.mask_circle(x: int, y: int, radius: int)</h3><p>Zeros a circular part of the image. If no arguments are supplied this method zeros the center of the image.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def mask_ellipse(self, x:int, y:int, radius_x:int, radius_y:int, rotation_angle_in_degrees:int) -> Image:
		"""
		<h3>image - Image.mask_ellipse(x: int, y: int, radius_x: int, radius_y: int, rotation_angle_in_degrees: int)</h3><p>Zeros an ellipsed shaped part of the image. If no arguments are supplied this method zeros the center of the image.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def binary(self, thresholds:List[Tuple[int,int]], invert=False, zero=False, mask:Image|None=None, to_bitmap=False, copy=False) -> Image:
		"""
		<h3>image - Image.binary(thresholds: List[Tuple[int, int]], invert=False, zero=False, mask: Image | None = None, to_bitmap=False, copy=False)</h3><p>Sets all pixels in the image to black or white depending on if the pixel is inside of a threshold in the threshold list <code>thresholds</code> or not.</p><p><code>thresholds</code> must be a list of tuples <code>[(lo, hi), (lo, hi), ..., (lo, hi)]</code> defining the ranges of color you want to track. For grayscale images each tuple needs to contain two values - a min grayscale value and a max grayscale value. Only pixel regions that fall between these thresholds will be considered. For RGB565 images each tuple needs to have six values (l_lo, l_hi, a_lo, a_hi, b_lo, b_hi) - which are minimums and maximums for the LAB L, A, and B channels respectively. For easy usage this function will automatically fix swapped min and max values. Additionally, if a tuple is larger than six values the rest are ignored. Conversely, if the tuple is too short the rest of the thresholds are assumed to be at maximum range.</p><div><p>Note</p><p>To get the thresholds for the object you want to track just select (click and drag) on the object you want to track in the IDE frame buffer. The histogram will then update to just be in that area. Then just write down where the color distribution starts and falls off in each histogram channel. These will be your low and high values for <code>thresholds</code>. It’s best to manually determine the thresholds versus using the upper and lower quartile statistics because they are too tight.</p><p>You may also determine color thresholds by going into <code>Tools-&gt;Machine Vision-&gt;Threshold Editor</code> in OpenMV IDE and selecting thresholds from the GUI slider window.</p></div><p><code>invert</code> inverts the thresholding operation such that instead of matching pixels inside of some known color bounds pixels are matched that are outside of the known color bounds.</p><p>Set <code>zero</code> to True to instead zero thresholded pixels and leave pixels not in the threshold list untouched.</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p><code>to_bitmap</code> turns the image data into a binary bitmap image where each pixel is stored in 1 bit. For very small images the new bitmap image may not fit inside of the original image requiring an out-of-place operation using <code>copy</code>.</p><p><code>copy</code> if True creates a copy of the binarized image on the heap versus modifying the source image.</p><div><p>Note</p><p>Bitmap images are like grayscale images with only two pixels values - 0 and 1. Additionally, bitmap images are packed such that they only store 1 bit per pixel making them very small. The OpenMV image library allows bitmap images to be used in all places <code>sensor.GRAYSCALE</code> and <code>sensor.RGB565</code> images can be used. However, many operations when applied on bitmap images don’t make any sense becuase bitmap images only have 2 values. OpenMV recommends using bitmap images for <code>mask</code> values in operations and such as they fit on the MicroPython heap quite easily. Finally, bitmap image pixel values 0 and 1 are interpreted as black and white when being applied to <code>sensor.GRAYSCALE</code> or <code>sensor.RGB565</code> images. The library automatically handles conversion.</p></div><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def invert(self) -> Image:
		"""
		<h3>image - Image.invert()</h3><p>Flips (binary inverts) all pixels values in the image. Note that binary inversion is the same as numerical inversion for images because:</p><p><code>(255 - pixel) % 256 == (255 + ~pixel + 1) % 256 == (~pixel + 256) % 256 == ~pixel</code> and this holds for any value that’s in a range of <code>(0-2^n-1)</code> which is true for all mutable image datatypes.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer/yuv images.</p>
		"""
		pass
	def b_and(self, image:Image, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.b_and(image: Image, mask: Image | None = None)</h3><p>Logically ANDs this image with another image.</p><p><code>image</code> can either be an image object, a path to an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale for grayscale images or a RGB565 value for RGB images).</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def b_nand(self, image:Image, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.b_nand(image: Image, mask: Image | None = None)</h3><p>Logically NANDs this image with another image.</p><p><code>image</code> can either be an image object, a path to an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale for grayscale images or a RGB565 value for RGB images).</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def b_or(self, image:Image, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.b_or(image: Image, mask: Image | None = None)</h3><p>Logically ORs this image with another image.</p><p><code>image</code> can either be an image object, a path to an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale for grayscale images or a RGB565 value for RGB images).</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def b_nor(self, image:Image, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.b_nor(image: Image, mask: Image | None = None)</h3><p>Logically NORs this image with another image.</p><p><code>image</code> can either be an image object, a path to an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale for grayscale images or a RGB565 value for RGB images).</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def b_xor(self, image:Image, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.b_xor(image: Image, mask: Image | None = None)</h3><p>Logically XORs this image with another image.</p><p><code>image</code> can either be an image object, a path to an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale for grayscale images or a RGB565 value for RGB images).</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def b_xnor(self, image:Image, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.b_xnor(image: Image, mask: Image | None = None)</h3><p>Logically XNORs this image with another image.</p><p><code>image</code> can either be an image object, a path to an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale for grayscale images or a RGB565 value for RGB images).</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def awb(self, max:bool=False) -> Image:
		"""
		<h3>image - Image.awb(max: bool = False)</h3><p>Performs automatic white balance on the image using the gray-world algorithm. This method operates on RAW Bayer Images so that you can improve image quality before converting to RGB565 or passing the RAW Bayer Image to an image processing funciton. You may also call this on a RGB565. This method has no affect on binary/grayscale images.</p><p><code>max</code> if True uses the white-patch algorithm instead.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed or yuv images.</p>
		"""
		pass
	def ccm(self, matrix) -> Image:
		"""
		<h3>image - Image.ccm(matrix)</h3><p>Multiples the passed floating-point color-correction-matrix with the image. Matrices may be in the form of:</p><div><div><pre>[[rr, rg, rb], [gr, gg, gb], [br, bg, bb]] [[rr, rg, rb], [gr, gg, gb], [br, bg, bb], [xx, xx, xx]] [[rr, rg, rb, ro], [gr, gg, gb, go], [br, bg, bb, bo]] [[rr, rg, rb, ro], [gr, gg, gb, go], [br, bg, bb, bo], [xx, xx, xx, xx]] [rr, rg, rb, ro, gr, gg, gb, go, br, bg, bb, bo] [rr, rg, rb, ro, gr, gg, gb, go, br, bg, bb, bo, xx, xx, xx, xx] </pre></div></div><p>The CCM Method does:</p><div><div><pre>|R&#39;| |R| |R&#39;| |R| |G&#39;| = 3x3 Matrix * |G| or |G&#39;| = 3x4 Matrix * |G| |B&#39;| |B| |B&#39;| |B| |1| </pre></div></div><p>Note that the sum of each row in the 3x3 matrix should generally be -1, +1, or 0. Weights may either be positive or negative.</p><p>You may want to use this method to eliminate systemic cross talk between color channels. Or alternatively, to do color correction on the whole image.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer/yuv images.</p>
		"""
		pass
	def gamma(self, gamma:float=1.0, contrast:float=1.0, brightness:float=0.0) -> Image:
		"""
		<h3>image - Image.gamma(gamma: float = 1.0, contrast: float = 1.0, brightness: float = 0.0)</h3><p>Quickly changes the image gamma, contrast, and brightness.</p><p><code>gamma</code> with values greater than 1.0 makes the image darker in a non-linear manner while less than 1.0 makes the image brighter. The gamma value is applied to the image by scaling all pixel color channels to be between [0:1) and then doing a remapping of <code>pow(pixel, 1/gamma)</code> on all pixels before scaling back.</p><p><code>contrast</code> with values greater than 1.0 makes the image brighter in a linear manner while less than 1.0 makes the image darker. The contrast value is applied to the image by scaling all pixel color channels to be between [0:1) and then doing a remapping of <code>pixel * contrast</code> on all pixels before scaling back.</p><p><code>brightness</code> with values greater than 0.0 makes the image brighter in a constant manner while less than 0.0 makes the image darker. The brightness value is applied to the image by scaling all pixel color channels to be between [0:1) and then doing a remapping of <code>pixel + brightness</code> on all pixels before scaling back.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed or bayer/yuv images.</p>
		"""
		pass
	def gamma_corr(self, gamma:float=1.0, contrast:float=1.0, brightness:float=0.0) -> Image:
		"""
		<h3>image - Image.gamma_corr(gamma: float = 1.0, contrast: float = 1.0, brightness: float = 0.0)</h3><p>Quickly changes the image gamma, contrast, and brightness.</p><p><code>gamma</code> with values greater than 1.0 makes the image darker in a non-linear manner while less than 1.0 makes the image brighter. The gamma value is applied to the image by scaling all pixel color channels to be between [0:1) and then doing a remapping of <code>pow(pixel, 1/gamma)</code> on all pixels before scaling back.</p><p><code>contrast</code> with values greater than 1.0 makes the image brighter in a linear manner while less than 1.0 makes the image darker. The contrast value is applied to the image by scaling all pixel color channels to be between [0:1) and then doing a remapping of <code>pixel * contrast</code> on all pixels before scaling back.</p><p><code>brightness</code> with values greater than 0.0 makes the image brighter in a constant manner while less than 0.0 makes the image darker. The brightness value is applied to the image by scaling all pixel color channels to be between [0:1) and then doing a remapping of <code>pixel + brightness</code> on all pixels before scaling back.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed or bayer/yuv images.</p><div><p>Note</p><p><code>Image.gamma_corr</code> is an alias for <code>Image.gamma</code>.</p></div>
		"""
		pass
	def negate(self) -> Image:
		"""
		<h3>image - Image.negate()</h3><p>Flips (binary inverts) all pixels values in the image. Note that binary inversion is the same as numerical inversion for images because:</p><p><code>(255 - pixel) % 256 == (255 + ~pixel + 1) % 256 == (~pixel + 256) % 256 == ~pixel</code> and this holds for any value that’s in a range of <code>(0-2^n-1)</code> which is true for all mutable image datatypes.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer/yuv images.</p><div><p>Note</p><p><code>Image.negate</code> is an alias for <code>Image.invert</code>.</p></div>
		"""
		pass
	def replace(self, image:Image, hmirror=False, vflip=False, transpose=False, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.replace(image: Image, hmirror=False, vflip=False, transpose=False, mask: Image | None = None)</h3><p>Replaces all pixels in the image object with a new image.</p><p><code>image</code> can either be another image object, a path to an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale for grayscale images or a RGB565 value for RGB images).</p><p>Set <code>hmirror</code> to True to horizontally mirror the replacing image.</p><p>Set <code>vflip</code> to True to vertically flip the replacing image.</p><p>Set <code>transpose</code> to True to flip the image along the diagonal (this changes the image image width/height if the image is non-square).</p><p>If you want to rotate an image by multiples of 90 degrees pass the following:</p><div><ul><li>vflip=False, hmirror=False, transpose=False -&gt; 0 degree rotation</li><li>vflip=True, hmirror=False, transpose=True -&gt; 90 degree rotation</li><li>vflip=True, hmirror=True, transpose=False -&gt; 180 degree rotation</li><li>vflip=False, hmirror=True, transpose=True -&gt; 270 degree rotation</li></ul></div><div><p>Note</p><p>If you don’t pass an <code>image</code> this method will operate on the underlying image that you were going to replace by applying the <code>hmirror</code>, <code>vflip</code>, and <code>transpose</code> options to rotate the image around. E.g. if you want to do <code>img.replace(img, etc...)</code> you just need to do <code>img.replace(etc..)</code>.</p></div><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified. Note that the mask is applied on the image before hmirror/vflip/transpose so the mask should be the same width/height of the initial unmodifed image.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def assign(self, image:Image, hmirror=False, vflip=False, transpose=False, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.assign(image: Image, hmirror=False, vflip=False, transpose=False, mask: Image | None = None)</h3><p>Alias for <code>Image.replace</code>.</p>
		"""
		pass
	def set(self, image:Image, hmirror=False, vflip=False, transpose=False, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.set(image: Image, hmirror=False, vflip=False, transpose=False, mask: Image | None = None)</h3><p>Alias for <code>Image.replace</code>.</p>
		"""
		pass
	def add(self, image:Image, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.add(image: Image, mask: Image | None = None)</h3><p>Adds an image pixel-wise to this one.</p><p><code>image</code> can either be an image object, a path to an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale for grayscale images or a RGB565 value for RGB images).</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def sub(self, image:Image, reverse=False, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.sub(image: Image, reverse=False, mask: Image | None = None)</h3><p>Subtracts an image pixel-wise to this one.</p><p><code>image</code> can either be an image object, a path to an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale for grayscale images or a RGB565 value for RGB images).</p><p>Set <code>reverse</code> to True to reverse the subtraction operation from <code>this_image-image</code> to <code>image-this_image</code>.</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def min(self, image:Image, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.min(image: Image, mask: Image | None = None)</h3><p>Returns the minimum image of two images pixel-wise.</p><p><code>image</code> can either be an image object, a path to an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale for grayscale images or a RGB565 value for RGB images).</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def max(self, image:Image, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.max(image: Image, mask: Image | None = None)</h3><p>Returns the maximum image of two images pixel-wise.</p><p><code>image</code> can either be an image object, a path to an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale for grayscale images or a RGB565 value for RGB images).</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def difference(self, image:Image, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.difference(image: Image, mask: Image | None = None)</h3><p>Returns the absolute difference image between two images (e.g. ||a-b||).</p><p><code>image</code> can either be an image object, a path to an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale for grayscale images or a RGB565 value for RGB images).</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def blend(self, image:Image, alpha=128, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.blend(image: Image, alpha=128, mask: Image | None = None)</h3><p>Alpha blends two images with each other.</p><p><code>image</code> can either be an image object, a path to an uncompressed image file (bmp/pgm/ppm), or a scalar value. If a scalar value the value can either be an RGB888 tuple or the underlying pixel value (e.g. an 8-bit grayscale for grayscale images or a RGB565 value for RGB images).</p><p><code>alpha</code> controls how much of the other image to blend into this image. <code>alpha</code> should be an integer value between 0 and 256. A value closer to zero blends more of the other image into this image and a value closer to 256 does the opposite.</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def histeq(self, adaptive=False, clip_limit=-1, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.histeq(adaptive=False, clip_limit=-1, mask: Image | None = None)</h3><p>Runs the histogram equalization algorithm on the image. Histogram equalization normalizes the contrast and brightness in the image.</p><p>If you pass <code>adaptive</code> as True then an adaptive histogram equalization method will be run on the image instead which as generally better results than non-adaptive histogram qualization but a longer run time.</p><p><code>clip_limit</code> provides a way to limit the contrast of the adaptive histogram qualization. Use a small value for this, like 10, to produce good histogram equalized contrast limited images.</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def erode(self, size:int, threshold:int|None=None, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.erode(size: int, threshold: int | None = None, mask: Image | None = None)</h3><p>Removes pixels from the edges of segmented areas.</p><p>This method works by convolving a kernel of <code>((size*2)+1)x((size*2)+1)</code> pixels across the image and zeroing the center pixel of the kernel if the sum of the neighbour pixels clear is greater than <code>threshold</code>.</p><p>This method works like the standard erode method if threshold is not set. If <code>threshold</code> is set then you can specify erode to only erode pixels that have, for example, more than 2 pixels clear in the kernel region with a threshold of 2.</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer/yuv images.</p>
		"""
		pass
	def dilate(self, size:int, threshold:int|None=None, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.dilate(size: int, threshold: int | None = None, mask: Image | None = None)</h3><p>Adds pixels to the edges of segmented areas.</p><p>This method works by convolving a kernel of <code>((size*2)+1)x((size*2)+1)</code> pixels across the image and setting the center pixel of the kernel if the sum of the neighbour pixels set is greater than <code>threshold</code>.</p><p>This method works like the standard dilate method if threshold is not set. If <code>threshold</code> is set then you can specify dilate to only dilate pixels that have, for example, more than 2 pixels set in the kernel region with a threshold of 2.</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer/yuv images.</p>
		"""
		pass
	def open(self, size:int, threshold:int|None=None, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.open(size: int, threshold: int | None = None, mask: Image | None = None)</h3><p>Performs erosion and dilation on an image in order. Please see <code>Image.erode()</code> and <code>Image.dilate()</code> for more information.</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer/yuv images.</p>
		"""
		pass
	def close(self, size:int, threshold:int|None=None, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.close(size: int, threshold: int | None = None, mask: Image | None = None)</h3><p>Performs dilation and erosion on an image in order. Please see <code>Image.dilate()</code> and <code>Image.erode()</code> for more information.</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer/yuv images.</p>
		"""
		pass
	def top_hat(self, size:int, threshold:int|None=None, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.top_hat(size: int, threshold: int | None = None, mask: Image | None = None)</h3><p>Returns the image difference of the image and <code>Image.open()</code>’ed image.</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Not supported on compressed images or bayer/yuv images.</p>
		"""
		pass
	def black_hat(self, size:int, threshold:int|None=None, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.black_hat(size: int, threshold: int | None = None, mask: Image | None = None)</h3><p>Returns the image difference of the image and <code>Image.close()</code>’ed image.</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Not supported on compressed images or bayer/yuv images.</p>
		"""
		pass
	def mean(self, size:int, threshold:bool|None=False, offset:int|None=0, invert:bool|None=False, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.mean(size: int, threshold: bool | None = False, offset: int | None = 0, invert: bool | None = False, mask: Image | None = None)</h3><p>Standard mean blurring filter using a box filter.</p><p><code>size</code> is the kernel size. Use 1 (3x3 kernel), 2 (5x5 kernel), etc.</p><p>If you’d like to adaptive threshold the image on the output of the filter you can pass <code>threshold=True</code> which will enable adaptive thresholding of the image which sets pixels to one or zero based on a pixel’s brightness in relation to the brightness of the kernel of pixels around them. A negative <code>offset</code> value sets more pixels to 1 as you make it more negative while a positive value only sets the sharpest contrast changes to 1. Set <code>invert</code> to invert the binary image resulting output.</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer/yuv images.</p>
		"""
		pass
	def median(self, size:int, percentile:float|None=0.5, threshold:bool|None=False, offset:int|None=0, invert:bool|None=False, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.median(size: int, percentile: float | None = 0.5, threshold: bool | None = False, offset: int | None = 0, invert: bool | None = False, mask: Image | None = None)</h3><p>Runs the median filter on the image. The median filter is the best filter for smoothing surfaces while preserving edges but it is very slow.</p><p><code>size</code> is the kernel size. Use 1 (3x3 kernel), 2 (5x5 kernel), etc.</p><p><code>percentile</code> controls the percentile of the value used in the kernel. By default each pixel is replaced with the 50th percentile (center) of its neighbors. You can set this to 0 for a min filter, 0.25 for a lower quartile filter, 0.75 for an upper quartile filter, and 1.0 for a max filter.</p><p>If you’d like to adaptive threshold the image on the output of the filter you can pass <code>threshold=True</code> which will enable adaptive thresholding of the image which sets pixels to one or zero based on a pixel’s brightness in relation to the brightness of the kernel of pixels around them. A negative <code>offset</code> value sets more pixels to 1 as you make it more negative while a positive value only sets the sharpest contrast changes to 1. Set <code>invert</code> to invert the binary image resulting output.</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer/yuv images.</p>
		"""
		pass
	def mode(self, size:int, threshold:bool|None=False, offset:int|None=0, invert:bool|None=False, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.mode(size: int, threshold: bool | None = False, offset: int | None = 0, invert: bool | None = False, mask: Image | None = None)</h3><p>Runs the mode filter on the image by replacing each pixel with the mode of their neighbors. This method works great on grayscale images. However, on RGB images it creates a lot of artifacts on edges because of the non-linear nature of the operation.</p><p><code>size</code> is the kernel size. Use 1 (3x3 kernel), 2 (5x5 kernel), etc.</p><p>If you’d like to adaptive threshold the image on the output of the filter you can pass <code>threshold=True</code> which will enable adaptive thresholding of the image which sets pixels to one or zero based on a pixel’s brightness in relation to the brightness of the kernel of pixels around them. A negative <code>offset</code> value sets more pixels to 1 as you make it more negative while a positive value only sets the sharpest contrast changes to 1. Set <code>invert</code> to invert the binary image resulting output.</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer/yuv images.</p>
		"""
		pass
	def midpoint(self, size:int, bias:float|None=0.5, threshold:bool|None=False, offset:int|None=0, invert:bool|None=False, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.midpoint(size: int, bias: float | None = 0.5, threshold: bool | None = False, offset: int | None = 0, invert: bool | None = False, mask: Image | None = None)</h3><p>Runs the midpoint filter on the image. This filter finds the midpoint ((max-min)/2) of each pixel neighborhood in the image.</p><p><code>size</code> is the kernel size. Use 1 (3x3 kernel), 2 (5x5 kernel), etc.</p><p><code>bias</code> controls the min/max mixing. 0 for min filtering only, 1.0 for max filtering only. By using the <code>bias</code> you can min/max filter the image.</p><p>If you’d like to adaptive threshold the image on the output of the filter you can pass <code>threshold=True</code> which will enable adaptive thresholding of the image which sets pixels to one or zero based on a pixel’s brightness in relation to the brightness of the kernel of pixels around them. A negative <code>offset</code> value sets more pixels to 1 as you make it more negative while a positive value only sets the sharpest contrast changes to 1. Set <code>invert</code> to invert the binary image resulting output.</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer/yuv images.</p>
		"""
		pass
	def morph(self, size:int, kernel:list, mul:float|None=1.0, add:float|None=0.0, threshold:bool|None=False, offset:int|None=0, invert:bool|None=False, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.morph(size: int, kernel: list, mul: float | None = 1.0, add: float | None = 0.0, threshold: bool | None = False, offset: int | None = 0, invert: bool | None = False, mask: Image | None = None)</h3><p>Convolves the image by a filter kernel. This allows you to do general purpose convolutions on an image.</p><p><code>size</code> controls the size of the kernel which must be <code>((size*2)+1)x((size*2)+1)</code> elements big.</p><p><code>kernel</code> is the kernel to convolve the image by. The kernel can either be a 1D tuple or list or a 2D tuple or list. For 1D kernels the tuple/list must be <code>((size*2)+1)x((size*2)+1)</code> elements big. For 2D tuples/lists each row must be <code>((size*2)+1)</code> elements big and there must be <code>((size*2)+1)</code> rows.</p><p><code>mul</code> allows you to do a global contrast adjustment. It’s value should be greater than 0.0. The default value is 1.0 which does nothing.</p><p><code>add</code> allows you to do a global brightness adjustment. It’s value should be between 0.0 and 1.0. The default value is 0.0 which does nothing.</p><p>If you’d like to adaptive threshold the image on the output of the filter you can pass <code>threshold=True</code> which will enable adaptive thresholding of the image which sets pixels to one or zero based on a pixel’s brightness in relation to the brightness of the kernel of pixels around them. A negative <code>offset</code> value sets more pixels to 1 as you make it more negative while a positive value only sets the sharpest contrast changes to 1. Set <code>invert</code> to invert the binary image resulting output.</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer/yuv images.</p>
		"""
		pass
	def gaussian(self, size:int, unsharp:bool|None=False, mul:float|None=1.0, add:float|None=0.0, threshold:bool|None=False, offset:int|None=0, invert:bool|None=False, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.gaussian(size: int, unsharp: bool | None = False, mul: float | None = 1.0, add: float | None = 0.0, threshold: bool | None = False, offset: int | None = 0, invert: bool | None = False, mask: Image | None = None)</h3><p>Convolves the image by a smoothing guassian kernel.</p><p><code>size</code> is the kernel size. Use 1 (3x3 kernel), 2 (5x5 kernel), etc.</p><p>If <code>unsharp</code> is set to the True then instead of doing just a guassian filtering operation this method will perform an unsharp mask operation which improves image sharpness on edges.</p><p><code>mul</code> allows you to do a global contrast adjustment. It’s value should be greater than 0.0. The default value is 1.0 which does nothing.</p><p><code>add</code> allows you to do a global brightness adjustment. It’s value should be between 0.0 and 1.0. The default value is 0.0 which does nothing.</p><p>If you’d like to adaptive threshold the image on the output of the filter you can pass <code>threshold=True</code> which will enable adaptive thresholding of the image which sets pixels to one or zero based on a pixel’s brightness in relation to the brightness of the kernel of pixels around them. A negative <code>offset</code> value sets more pixels to 1 as you make it more negative while a positive value only sets the sharpest contrast changes to 1. Set <code>invert</code> to invert the binary image resulting output.</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer/yuv images.</p>
		"""
		pass
	def laplacian(self, size:int, sharpen:bool|None=False, mul:float|None=1.0, add:float|None=0.0, threshold:bool|None=False, offset:int|None=0, invert:bool|None=False, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.laplacian(size: int, sharpen: bool | None = False, mul: float | None = 1.0, add: float | None = 0.0, threshold: bool | None = False, offset: int | None = 0, invert: bool | None = False, mask: Image | None = None)</h3><div><p>Convolves the image by a edge detecting laplacian kernel.</p><p><code>size</code> is the kernel size. Use 1 (3x3 kernel), 2 (5x5 kernel), etc.</p><p>If <code>sharpen</code> is set to the True then instead of just outputting an unthresholded edge detection image this method will instead sharpen the image. Increase the kernel size then to increase the image sharpness.</p><p><code>mul</code> allows you to do a global contrast adjustment. It’s value should be greater than 0.0. The default value is 1.0 which does nothing.</p><p><code>add</code> allows you to do a global brightness adjustment. It’s value should be between 0.0 and 1.0. The default value is 0.0 which does nothing.</p><p>If you’d like to adaptive threshold the image on the output of the filter you can pass <code>threshold=True</code> which will enable adaptive thresholding of the image which sets pixels to one or zero based on a pixel’s brightness in relation to the brightness of the kernel of pixels around them. A negative <code>offset</code> value sets more pixels to 1 as you make it more negative while a positive value only sets the sharpest contrast changes to 1. Set <code>invert</code> to invert the binary image resulting output.</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p></div><p>Not supported on compressed images or bayer/yuv images.</p>
		"""
		pass
	def bilateral(self, size:int, color_sigma:float|None=0.1, space_sigma:float|None=1.0, threshold:bool|None=False, offset:int|None=0, invert:bool|None=False, mask:Image|None=None) -> Image:
		"""
		<h3>image - Image.bilateral(size: int, color_sigma: float | None = 0.1, space_sigma: float | None = 1.0, threshold: bool | None = False, offset: int | None = 0, invert: bool | None = False, mask: Image | None = None)</h3><p>Convolves the image by a bilateral filter. The bilateral filter smooths the image while keeping edges in the image.</p><p><code>size</code> is the kernel size. Use 1 (3x3 kernel), 2 (5x5 kernel), etc.</p><p><code>color_sigma</code> controls how closely colors are matched using the bilateral filter. Increase this to increase color blurring.</p><p><code>space_sigma</code> controls how closely pixels space-wise are blurred with each other. Increase this to increase pixel blurring.</p><p>If you’d like to adaptive threshold the image on the output of the filter you can pass <code>threshold=True</code> which will enable adaptive thresholding of the image which sets pixels to one or zero based on a pixel’s brightness in relation to the brightness of the kernel of pixels around them. A negative <code>offset</code> value sets more pixels to 1 as you make it more negative while a positive value only sets the sharpest contrast changes to 1. Set <code>invert</code> to invert the binary image resulting output.</p><p><code>mask</code> is another image to use as a pixel level mask for the operation. The mask should be an image with just black or white pixels and should be the same size as the image being operated on. Only pixels set in the mask are modified.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer/yuv images.</p>
		"""
		pass
	def linpolar(self, reverse:bool=False) -> Image:
		"""
		<h3>image - Image.linpolar(reverse: bool = False)</h3><p>Re-project’s and image from cartessian coordinates to linear polar coordinates.</p><p>Set <code>reverse=True</code> to re-project in the opposite direction.</p><p>Linear polar re-projection turns rotation of an image into x-translation.</p><p>Not supported on compressed images or bayer images.</p><p>This method is not available on the OpenMV Cam M4.</p>
		"""
		pass
	def logpolar(self, reverse:bool=False) -> Image:
		"""
		<h3>image - Image.logpolar(reverse: bool = False)</h3><p>Re-project’s and image from cartessian coordinates to log polar coordinates.</p><p>Set <code>reverse=True</code> to re-project in the opposite direction.</p><p>Log polar re-projection turns rotation of an image into x-translation and scaling/zooming into y-translation.</p><p>Not supported on compressed images or bayer images.</p><p>This method is not available on the OpenMV Cam M4.</p>
		"""
		pass
	def lens_corr(self, strength:float=1.8, zoom:float=1.0, x_corr:float=0.0, y_corr:float=0.0) -> Image:
		"""
		<h3>image - Image.lens_corr(strength: float = 1.8, zoom: float = 1.0, x_corr: float = 0.0, y_corr: float = 0.0)</h3><p>Performs lens correction to un-fisheye the image due to the lens distortion.</p><p><code>strength</code> is a float defining how much to un-fisheye the image. Try 1.8 out by default and then increase or decrease from there until the image looks good.</p><p><code>zoom</code> is the amount to zoom in on the image by. 1.0 by default.</p><p><code>x_corr</code> floating point pixel offset from center. Can be negative or positive.</p><p><code>y_corr</code> floating point pixel offset from center. Can be negative or positive.</p><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def rotation_corr(self, x_rotation=0.0, y_rotation=0.0, z_rotation=0.0, x_translation=0.0, y_translation=0.0, zoom=1.0, fov=60.0, corners:List[Tuple[int,int]]|None=None) -> Image:
		"""
		<h3>image - Image.rotation_corr(x_rotation=0.0, y_rotation=0.0, z_rotation=0.0, x_translation=0.0, y_translation=0.0, zoom=1.0, fov=60.0, corners: List[Tuple[int, int]] | None = None)</h3><p>Corrects perspective issues in the image by doing a 3D rotation of the frame buffer.</p><p><code>x_rotation</code> is the number of degrees to rotation the image in the frame buffer around the x axis (i.e. this spins the image up and down).</p><p><code>y_rotation</code> is the number of degrees to rotation the image in the frame buffer around the y axis (i.e. this spins the image left and right).</p><p><code>z_rotation</code> is the number of degrees to rotation the image in the frame buffer around the z axis (i.e. this spins the image in place).</p><p><code>x_translation</code> is the number of units to move the image to the left or right after rotation. Because this translation is applied in 3D space the units aren’t pixels…</p><p><code>y_translation</code> is the number of units to move the image to the up or down after rotation. Because this translation is applied in 3D space the units aren’t pixels…</p><p><code>zoom</code> is the amount to zoom in on the image by. 1.0 by default.</p><p><code>fov</code> is the field-of-view to use internally when doing 2D-&gt;3D projection before rotating the image in 3D space. As this value approaches 0 the image is placed at infinity away from the viewport. As this value approaches 180 the image is placed within the viewport. Typically, you should not change this value but you can modify it to change the 2D-&gt;3D mapping effect.</p><p><code>corners</code> is a list of four (x,y) tuples representing four corners used to create a 4-point correspondence homography that will map the first corner to (0, 0), the second corner to (image_width-1, 0), the third corner to (image_width-1, image_height-1), and the fourth corner to (0, image_height-1). The 3D rotation is then applied after the image is re-mapped. This argument lets you use <code>rotation_corr</code> to do things like birds-eye-view transforms. E.g:</p><div><div><pre>top_tilt = 10 # if the difference between top/bottom_tilt become to large this method will stop working bottom_tilt = 0 points = [(tilt, 0), (img.width()-tilt, 0), (img.width()-1-bottom_tilt, img.height()-1), (bottom_tilt, img.height()-1)] img.rotation_corr(corners=points) </pre></div></div><p>Returns the image object so you can call another method using <code>.</code> notation.</p><p>Not supported on compressed images or bayer images.</p><p>This method is not available on the OpenMV Cam M4.</p>
		"""
		pass
	def get_similarity(self, image:Image, x:int|None=0, y:int|None=0, x_scale:float=1.0, y_scale:float=1.0, roi:Tuple[int,int,int,int]|None=None, rgb_channel:int=-1, alpha:int=256, color_palette=None, alpha_palette=None, hint:int=0, dssim:bool=False) -> Similarity:
		"""
		<h3>image - Image.get_similarity(image: Image, x: int | None = 0, y: int | None = 0, x_scale: float = 1.0, y_scale: float = 1.0, roi: Tuple[int, int, int, int] | None = None, rgb_channel: int = -1, alpha: int = 256, color_palette=None, alpha_palette=None, hint: int = 0, dssim: bool = False)</h3><p>Computes the similarity between two images. The similarity is computed by using the structural similiary index (SSIM). The SSIM is a metric that compares the structural similarity between two images. The SSIM is a value between -1 and 1. A value of 1 means the images are identical, a value of 0 means the images are not similar, and a value of -1 means the images are perfectly the opposite of each other. Typically, if you want to check if two images are different you should look to see how negative the SSIM value is.</p><p><code>image</code> is the image to compare to.</p><p>You may also pass a path instead of an image object for this method to automatically load the image from disk and use it in one step. E.g. <code>get_similarity(&quot;test.jpg&quot;)</code>.</p><p><code>x</code> is the x offset to start comparing the image at.</p><p><code>y</code> is the y offset to start comparing the image at.</p><p><code>x_scale</code> controls how much the displayed image is scaled by in the x direction (float). If this value is negative the image will be flipped horizontally. Note that if <code>y_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>y_scale</code> controls how much the displayed image is scaled by in the y direction (float). If this value is negative the image will be flipped vertically. Note that if <code>x_scale</code> is not specified then it will match <code>x_scale</code> to maintain the aspect ratio.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This allows you to extract just the pixels in the ROI to scale and draw on the destination image.</p><p><code>rgb_channel</code> is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed) and to render onto the destination image. For example, if you pass <code>rgb_channel=1</code> this will extract the green channel of the source RGB565 image and draw that in grayscale on the destination image.</p><p><code>alpha</code> controls how much of the source image to blend into the destination image. A value of 255 draws an opaque source image while a value lower than 255 produces a blend between the source and destination image. 0 results in no modification to the destination image.</p><p><code>color_palette</code> if not <code>None</code> can be an a color palette enum or a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of whatever the source image is. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>alpha_palette</code> if not <code>None</code> can be a 256 pixel in total GRAYSCALE image to use as a alpha palette which modulates the <code>alpha</code> value of the source image being drawn at a pixel pixel level allowing you to precisely control the alpha value of pixels based on their grayscale value. A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes more transparent until 0. This is applied after <code>rgb_channel</code> extraction if used.</p><p><code>hint</code> can be a logical OR of the flags:</p><div><ul><li><code>image.AREA</code>: Use area scaling when downscaling versus the default of nearest neighbor.</li><li><code>image.BILINEAR</code>: Use bilinear scaling versus the default of nearest neighbor scaling.</li><li><code>image.BICUBIC</code>: Use bicubic scaling versus the default of nearest neighbor scaling.</li><li><code>image.CENTER</code>: Center the image being drawn on the display. This is applied after scaling.</li><li><code>image.HMIRROR</code>: Horizontally mirror the image.</li><li><code>image.VFLIP</code>: Vertically flip the image.</li><li><code>image.TRANSPOSE</code>: Transpose the image (swap x/y).</li><li><code>image.EXTRACT_RGB_CHANNEL_FIRST</code>: Do rgb_channel extraction before scaling.</li><li><code>image.APPLY_COLOR_PALETTE_FIRST</code>: Apply color palette before scaling.</li><li><code>image.SCALE_ASPECT_KEEP</code>: Scale the image being drawn to fit inside the display.</li><li><code>image.SCALE_ASPECT_EXPAND</code>: Scale the image being drawn to fill the display (results in cropping)</li><li><code>image.SCALE_ASPECT_IGNORE</code>: Scale the image being drawn to fill the display (results in stretching).</li><li><code>image.ROTATE_90</code>: Rotate the image by 90 degrees (this is just VFLIP | TRANSPOSE).</li><li><code>image.ROTATE_180</code>: Rotate the image by 180 degrees (this is just HMIRROR | VFLIP).</li><li><code>image.ROTATE_270</code>: Rotate the image by 270 degrees (this is just HMIRROR | TRANSPOSE).</li><li><code>image.BLACK_BACKGROUND</code>: Assume the background image being drawn on is black speeding up blending.</li></ul></div><p><code>dssim</code> if true will compute the structual disimilarity index (DSSIM) instead of the SSIM. A value of 0 means the images are identical. A value of 1 means the images are completely different.</p><p>Returns a <code>image.Similarity</code> object.</p>
		"""
		pass
	def get_histogram(self, thresholds:List[Tuple[int,int]]|None=None, invert=False, roi:Tuple[int,int,int,int]|None=None, bins=256, l_bins=256, a_bins=256, b_bins=256, difference:Image|None=None) -> histogram:
		"""
		<h3>image - Image.get_histogram(thresholds: List[Tuple[int, int]] | None = None, invert=False, roi: Tuple[int, int, int, int] | None = None, bins=256, l_bins=256, a_bins=256, b_bins=256, difference: Image | None = None)</h3><p>Computes the normalized histogram on all color channels for an <code>roi</code> and returns a <code>image.histogram</code> object. Please see the <code>image.histogram</code> object for more information. You can also invoke this method by using <code>Image.get_hist()</code> or <code>Image.histogram()</code>. If you pass a list of <code>thresholds</code> then the histogram information will only be computed from pixels within the threshold list.</p><p><code>thresholds</code> must be a list of tuples <code>[(lo, hi), (lo, hi), ..., (lo, hi)]</code> defining the ranges of color you want to track. For grayscale images each tuple needs to contain two values - a min grayscale value and a max grayscale value. Only pixel regions that fall between these thresholds will be considered. For RGB565 images each tuple needs to have six values (l_lo, l_hi, a_lo, a_hi, b_lo, b_hi) - which are minimums and maximums for the LAB L, A, and B channels respectively. For easy usage this function will automatically fix swapped min and max values. Additionally, if a tuple is larger than six values the rest are ignored. Conversely, if the tuple is too short the rest of the thresholds are assumed to be at maximum range.</p><div><p>Note</p><p>To get the thresholds for the object you want to track just select (click and drag) on the object you want to track in the IDE frame buffer. The histogram will then update to just be in that area. Then just write down where the color distribution starts and falls off in each histogram channel. These will be your low and high values for <code>thresholds</code>. It’s best to manually determine the thresholds versus using the upper and lower quartile statistics because they are too tight.</p><p>You may also determine color thresholds by going into <code>Tools-&gt;Machine Vision-&gt;Threshold Editor</code> in OpenMV IDE and selecting thresholds from the GUI slider window.</p></div><p><code>invert</code> inverts the thresholding operation such that instead of matching pixels inside of some known color bounds pixels are matched that are outside of the known color bounds.</p><p>Unless you need to do something advanced with color statistics just use the <code>Image.get_statistics()</code> method instead of this method for looking at pixel areas in an image.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the <code>roi</code> are operated on.</p><p><code>bins</code> and others are the number of bins to use for the histogram channels. For grayscale images use <code>bins</code> and for RGB565 images use the others for each channel. The bin counts must be greater than 2 for each channel. Additionally, it makes no sense to set the bin count larger than the number of unique pixel values for each channel. By default, the historgram will have the maximum number of bins per channel.</p><p><code>difference</code> may be set to an image object to cause this method to operate on the difference image between the current image and the <code>difference</code> image object. This saves having to use a separate buffer.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def get_statistics(self, thresholds:List[Tuple[int,int]]|None=None, invert=False, roi:Tuple[int,int,int,int]|None=None, bins=256, l_bins=256, a_bins=256, b_bins=256, difference:Image|None=None) -> statistics:
		"""
		<h3>image - Image.get_statistics(thresholds: List[Tuple[int, int]] | None = None, invert=False, roi: Tuple[int, int, int, int] | None = None, bins=256, l_bins=256, a_bins=256, b_bins=256, difference: Image | None = None)</h3><p>Computes the mean, median, mode, standard deviation, min, max, lower quartile, and upper quartile for all color channels for an <code>roi</code> and returns a <code>image.statistics</code> object. Please see the <code>image.statistics</code> object for more information. You can also invoke this method by using <code>Image.get_stats()</code> or <code>Image.statistics()</code>. If you pass a list of <code>thresholds</code> then the histogram information will only be computed from pixels within the threshold list.</p><p><code>thresholds</code> must be a list of tuples <code>[(lo, hi), (lo, hi), ..., (lo, hi)]</code> defining the ranges of color you want to track. For grayscale images each tuple needs to contain two values - a min grayscale value and a max grayscale value. Only pixel regions that fall between these thresholds will be considered. For RGB565 images each tuple needs to have six values (l_lo, l_hi, a_lo, a_hi, b_lo, b_hi) - which are minimums and maximums for the LAB L, A, and B channels respectively. For easy usage this function will automatically fix swapped min and max values. Additionally, if a tuple is larger than six values the rest are ignored. Conversely, if the tuple is too short the rest of the thresholds are assumed to be at maximum range.</p><div><p>Note</p><p>To get the thresholds for the object you want to track just select (click and drag) on the object you want to track in the IDE frame buffer. The histogram will then update to just be in that area. Then just write down where the color distribution starts and falls off in each histogram channel. These will be your low and high values for <code>thresholds</code>. It’s best to manually determine the thresholds versus using the upper and lower quartile statistics because they are too tight.</p><p>You may also determine color thresholds by going into <code>Tools-&gt;Machine Vision-&gt;Threshold Editor</code> in OpenMV IDE and selecting thresholds from the GUI slider window.</p></div><p><code>invert</code> inverts the thresholding operation such that instead of matching pixels inside of some known color bounds pixels are matched that are outside of the known color bounds.</p><p>You’ll want to use this method any time you need to get information about the values of an area of pixels in an image. For example, after if you’re trying to detect motion using frame differencing you’ll want to use this method to determine a change in the color channels of the image to trigger your motion detection threshold.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the <code>roi</code> are operated on.</p><p><code>bins</code> and others are the number of bins to use for the histogram channels. For grayscale images use <code>bins</code> and for RGB565 images use the others for each channel. The bin counts must be greater than 2 for each channel. Additionally, it makes no sense to set the bin count larger than the number of unique pixel values for each channel. By default, the historgram will have the maximum number of bins per channel.</p><p><code>difference</code> may be set to an image object to cause this method to operate on the difference image between the current image and the <code>difference</code> image object. This saves having to use a separate buffer.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def get_regression(self, thresholds:List[Tuple[int,int]], invert=False, roi:Tuple[int,int,int,int]|None=None, x_stride=2, y_stride=1, area_threshold=10, pixels_threshold=10, robust=False) -> line:
		"""
		<h3>image - Image.get_regression(thresholds: List[Tuple[int, int]], invert=False, roi: Tuple[int, int, int, int] | None = None, x_stride=2, y_stride=1, area_threshold=10, pixels_threshold=10, robust=False)</h3><p>Computes a linear regression on all the thresholded pixels in the image. The linear regression is computed using least-squares normally which is fast but cannot handle any outliers. If <code>robust</code> is True then the Theil–Sen linear regression is used instead which computes the median of all slopes between all thresholded pixels in the image. This is an N^2 operation which may drops your FPS down to below 5 even on an 80x60 image if too many pixels are set after thresholding. However, as long as the number of pixels set after thresholding remains low the linear regression will be valid even in the case of up to 30% of the thresholded pixels being outliers (e.g. it’s robust).</p><p>This method returns a <code>image.line</code> object. See this blog post on how to use the line object easily: https://openmv.io/blogs/news/linear-regression-line-following</p><p><code>thresholds</code> must be a list of tuples <code>[(lo, hi), (lo, hi), ..., (lo, hi)]</code> defining the ranges of color you want to track. For grayscale images each tuple needs to contain two values - a min grayscale value and a max grayscale value. Only pixel regions that fall between these thresholds will be considered. For RGB565 images each tuple needs to have six values (l_lo, l_hi, a_lo, a_hi, b_lo, b_hi) - which are minimums and maximums for the LAB L, A, and B channels respectively. For easy usage this function will automatically fix swapped min and max values. Additionally, if a tuple is larger than six values the rest are ignored. Conversely, if the tuple is too short the rest of the thresholds are assumed to be at maximum range.</p><div><p>Note</p><p>To get the thresholds for the object you want to track just select (click and drag) on the object you want to track in the IDE frame buffer. The histogram will then update to just be in that area. Then just write down where the color distribution starts and falls off in each histogram channel. These will be your low and high values for <code>thresholds</code>. It’s best to manually determine the thresholds versus using the upper and lower quartile statistics because they are too tight.</p><p>You may also determine color thresholds by going into <code>Tools-&gt;Machine Vision-&gt;Threshold Editor</code> in OpenMV IDE and selecting thresholds from the GUI slider window.</p></div><p><code>invert</code> inverts the thresholding operation such that instead of matching pixels inside of some known color bounds pixels are matched that are outside of the known color bounds.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the <code>roi</code> are operated on.</p><p><code>x_stride</code> is the number of x pixels to skip over when evaluating the image.</p><p><code>y_stride</code> is the number of y pixels to skip over when evaluating the image.</p><p>If the regression’s bounding box area is less than <code>area_threshold</code> then None is returned.</p><p>If the regression’s pixel count is less than <code>pixels_threshold</code> then None is returned.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def find_blobs(self, thresholds:List[Tuple[int,int]], invert=False, roi:Tuple[int,int,int,int]|None=None, x_stride=2, y_stride=1, area_threshold=10, pixels_threshold=10, merge=False, margin=0, threshold_cb=None, merge_cb=None, x_hist_bins_max=0, y_hist_bins_max=0) -> List[blob]:
		"""
		<h3>image - Image.find_blobs(thresholds: List[Tuple[int, int]], invert=False, roi: Tuple[int, int, int, int] | None = None, x_stride=2, y_stride=1, area_threshold=10, pixels_threshold=10, merge=False, margin=0, threshold_cb=None, merge_cb=None, x_hist_bins_max=0, y_hist_bins_max=0)</h3><p>Finds all blobs (connected pixel regions that pass a threshold test) in the image and returns a list of <code>image.blob</code> objects which describe each blob. Please see the <code>image.blob</code> object more more information.</p><p><code>thresholds</code> must be a list of tuples <code>[(lo, hi), (lo, hi), ..., (lo, hi)]</code> defining the ranges of color you want to track. You may pass up to 32 threshold tuples in one call. For grayscale images each tuple needs to contain two values - a min grayscale value and a max grayscale value. Only pixel regions that fall between these thresholds will be considered. For RGB565 images each tuple needs to have six values (l_lo, l_hi, a_lo, a_hi, b_lo, b_hi) - which are minimums and maximums for the LAB L, A, and B channels respectively. For easy usage this function will automatically fix swapped min and max values. Additionally, if a tuple is larger than six values the rest are ignored. Conversely, if the tuple is too short the rest of the thresholds are assumed to be at maximum range.</p><div><p>Note</p><p>To get the thresholds for the object you want to track just select (click and drag) on the object you want to track in the IDE frame buffer. The histogram will then update to just be in that area. Then just write down where the color distribution starts and falls off in each histogram channel. These will be your low and high values for <code>thresholds</code>. It’s best to manually determine the thresholds versus using the upper and lower quartile statistics because they are too tight.</p><p>You may also determine color thresholds by going into <code>Tools-&gt;Machine Vision-&gt;Threshold Editor</code> in OpenMV IDE and selecting thresholds from the GUI slider window.</p></div><p><code>invert</code> inverts the thresholding operation such that instead of matching pixels inside of some known color bounds pixels are matched that are outside of the known color bounds.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the <code>roi</code> are operated on.</p><p><code>x_stride</code> is the number of x pixels to skip when searching for a blob. Once a blob is found the line fill algorithm will be pixel accurate. Increase <code>x_stride</code> to speed up finding blobs if blobs are known to be large.</p><p><code>y_stride</code> is the number of y pixels to skip when searching for a blob. Once a blob is found the line fill algorithm will be pixel accurate. Increase <code>y_stride</code> to speed up finding blobs if blobs are known to be large.</p><p>If a blob’s bounding box area is less than <code>area_threshold</code> it is filtered out.</p><p>If a blob’s pixel count is less than <code>pixels_threshold</code> it is filtered out.</p><p><code>merge</code> if True merges all not filtered out blobs whos bounding rectangles intersect each other. <code>margin</code> can be used to increase or decrease the size of the bounding rectangles for blobs during the intersection test. For example, with a margin of 1 blobs whos bounding rectangles are 1 pixel away from each other will be merged.</p><p>Merging blobs allows you to implement color code tracking. Each blob object has a <code>code</code> value which is a bit vector made up of 1s for each color threshold. For example, if you pass <code>Image.find_blobs</code> two color thresholds then the first threshold has a code of 1 and the second 2 (a third threshold would be 4 and a fourth would be 8 and so on). Merged blobs logically OR all their codes together so that you know what colors produced them. This allows you to then track two colors if you get a blob object back with two colors then you know it might be a color code.</p><p>You might also want to merge blobs if you are using tight color bounds which do not fully track all the pixels of an object you are trying to follow.</p><p>Finally, if you want to merge blobs, but, don’t want two color thresholds to be merged then just call <code>Image.find_blobs</code> twice with separate thresholds so that blobs aren’t merged.</p><p><code>threshold_cb</code> may be set to the function to call on every blob after its been thresholded to filter it from the list of blobs to be merged. The call back function will receive one argument - the blob object to be filtered. The call back then must return True to keep the blob and False to filter it.</p><p><code>merge_cb</code> may be set to the function to call on every two blobs about to be merged to prevent or allow the merge. The call back function will receive two arguments - the two blob objects to be merged. The call back then must return True to merge the blobs or False to prevent merging the blobs.</p><p><code>x_hist_bins_max</code> if set to non-zero populates a histogram buffer in each blob object with an x_histogram projection of all columns in the object. This value then sets the number of bins for that projection.</p><p><code>y_hist_bins_max</code> if set to non-zero populates a histogram buffer in each blob object with an y_histogram projection of all rows in the object. This value then sets the number of bins for that projection.</p><p>Not supported on compressed images or bayer images.</p>
		"""
		pass
	def find_lines(self, roi:Tuple[int,int,int,int]|None=None, x_stride=2, y_stride=1, threshold=1000, theta_margin=25, rho_margin=25) -> List[line]:
		"""
		<h3>image - Image.find_lines(roi: Tuple[int, int, int, int] | None = None, x_stride=2, y_stride=1, threshold=1000, theta_margin=25, rho_margin=25)</h3><p>Finds all infinite lines in the image using the hough transform. Returns a list of <code>image.line</code> objects.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the <code>roi</code> are operated on.</p><p><code>x_stride</code> is the number of x pixels to skip when doing the hough transform. Only increase this if lines you are searching for are large and bulky.</p><p><code>y_stride</code> is the number of y pixels to skip when doing the hough transform. Only increase this if lines you are searching for are large and bulky.</p><p><code>threshold</code> controls what lines are detected from the hough transform. Only lines with a magnitude greater than or equal to <code>threshold</code> are returned. The right value of <code>threshold</code> for your application is image dependent. Note that the magnitude of a line is the sum of all sobel filter magnitudes of pixels that make up that line.</p><p><code>theta_margin</code> controls the merging of detected lines. Lines which are <code>theta_margin</code> degrees apart and <code>rho_margin</code> rho apart are merged.</p><p><code>rho_margin</code> controls the merging of detected lines. Lines which are <code>theta_margin</code> degrees apart and <code>rho_margin</code> rho apart are merged.</p><p>This method working by running the sobel filter over the image and taking the magnitude and gradient responses from the sobel filter to feed a hough transform. It does not require any preprocessing on the image first. However, my cleaning up the image using filtering you may get more stable results.</p><p>Not supported on compressed images or bayer images.</p><p>This method is not available on the OpenMV Cam M4.</p>
		"""
		pass
	def find_line_segments(self, roi:Tuple[int,int,int,int]|None=None, merge_distance=0, max_theta_difference=15) -> List[line]:
		"""
		<h3>image - Image.find_line_segments(roi: Tuple[int, int, int, int] | None = None, merge_distance=0, max_theta_difference=15)</h3><p>Finds line segments in the image using the hough transform. Returns a list of <code>image.line</code> objects .</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the <code>roi</code> are operated on.</p><p><code>merge_distance</code> specifies the maximum number of pixels two line segements can be seperated by each other (at any point on one line) to be merged.</p><p><code>max_theta_difference</code> is the maximum theta difference in degrees two line segements that are <code>merge_distance</code> apart to be merged.</p><p>This method uses the LSD library (also used by OpenCV) to find line segements in the image. It’s somewhat slow but very accurate and lines don’t jump around.</p><p>This method is not available on the OpenMV Cam M4.</p>
		"""
		pass
	def find_circles(self, roi:Tuple[int,int,int,int]|None=None, x_stride=2, y_stride=1, threshold=2000, x_margin=10, y_margin=10, r_margin=10, r_min=2, r_max:int|None=None, r_step=2) -> List[circle]:
		"""
		<h3>image - Image.find_circles(roi: Tuple[int, int, int, int] | None = None, x_stride=2, y_stride=1, threshold=2000, x_margin=10, y_margin=10, r_margin=10, r_min=2, r_max: int | None = None, r_step=2)</h3><p>Finds circles in the image using the hough transform. Returns a list of <code>image.circle</code> objects.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the <code>roi</code> are operated on.</p><p><code>x_stride</code> is the number of x pixels to skip when doing the hough transform. Only increase this if circles you are searching for are large and bulky.</p><p><code>y_stride</code> is the number of y pixels to skip when doing the hough transform. Only increase this if circles you are searching for are large and bulky.</p><p><code>threshold</code> controls what circles are detected from the hough transform. Only circles with a magnitude greater than or equal to <code>threshold</code> are returned. The right value of <code>threshold</code> for your application is image dependent. Note that the magnitude of a circle is the sum of all sobel filter magnitudes of pixels that make up that circle.</p><p><code>x_margin</code> controls the merging of detected circles. Circles which are <code>x_margin</code>, <code>y_margin</code>, and <code>r_margin</code> pixels apart are merged.</p><p><code>y_margin</code> controls the merging of detected circles. Circles which are <code>x_margin</code>, <code>y_margin</code>, and <code>r_margin</code> pixels apart are merged.</p><p><code>r_margin</code> controls the merging of detected circles. Circles which are <code>x_margin</code>, <code>y_margin</code>, and <code>r_margin</code> pixels apart are merged.</p><p><code>r_min</code> controls the minimum circle radius detected. Increase this to speed up the algorithm. Defaults to 2.</p><p><code>r_max</code> controls the maximum circle radius detected. Decrease this to speed up the algorithm. Defaults to min(roi.w/2, roi.h/2).</p><p><code>r_step</code> controls how to step the radius detection by. Defaults to 2.</p><p>This method is not available on the OpenMV Cam M4.</p>
		"""
		pass
	def find_rects(self, roi:Tuple[int,int,int,int]|None=None, threshold=10000) -> List[rect]:
		"""
		<h3>image - Image.find_rects(roi: Tuple[int, int, int, int] | None = None, threshold=10000)</h3><p>Find rectangles in the image using the same quad detection algorithm used to find apriltags. Works best of rectangles that have good contrast against the background. The apriltag quad detection algorithm can handle any scale/rotation/shear on rectangles. Returns a list of <code>image.rect</code> objects.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the <code>roi</code> are operated on.</p><p>Rectangles which have an edge magnitude (which is computed by sliding the sobel operator across all pixels on the edges of the rectangle and summing their values) less than <code>threshold</code> are filtered out of the returned list. The correct value of <code>threshold</code> is depended on your application/scene.</p><p>This method is not available on the OpenMV Cam M4.</p>
		"""
		pass
	def find_qrcodes(self, roi:Tuple[int,int,int,int]|None=None) -> List[qrcode]:
		"""
		<h3>image - Image.find_qrcodes(roi: Tuple[int, int, int, int] | None = None)</h3><p>Finds all qrcodes within the <code>roi</code> and returns a list of <code>image.qrcode</code> objects. Please see the <code>image.qrcode</code> object for more information.</p><p>QR Codes need to be relatively flat in the image for this method to work. You can achieve a flatter image that is not effected by lens distortion by either using the <code>sensor.set_windowing()</code> function to zoom in the on the center of the lens, <code>Image.lens_corr()</code> to undo lens barrel distortion, or by just changing out the lens for something with a narrower fields of view. There are machine vision lenses available which do not cause barrel distortion but they are much more expensive to than the standard lenses supplied by OpenMV.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the <code>roi</code> are operated on.</p><p>This method is not available on the OpenMV Cam M4.</p>
		"""
		pass
	def find_apriltags(self, roi:Tuple[int,int,int,int]|None=None, families=TAG36H11, fx=0.0, fy=0.0, cx:int|None=None, cy:int|None=None) -> List[apriltag]:
		"""
		<h3>image - Image.find_apriltags(roi: Tuple[int, int, int, int] | None = None, families=TAG36H11, fx=0.0, fy=0.0, cx: int | None = None, cy: int | None = None)</h3><p>Finds all apriltags within the <code>roi</code> and returns a list of <code>image.apriltag</code> objects. Please see the <code>image.apriltag</code> object for more information.</p><p>Unlike QR Codes, AprilTags can be detected at much farther distances, worse lighting, in warped images, etc. AprilTags are robust too all kinds of image distortion issues that QR Codes are not to. That said, AprilTags can only encode a numeric ID as their payload.</p><p>AprilTags can also be used for localization purposes. Each <code>image.apriltag</code> object returns its translation and rotation from the camera. The units of the translation are determined by <code>fx</code>, <code>fy</code>, <code>cx</code>, and <code>cy</code> which are the focal lengths and center points of the image in the X and Y directions respectively.</p><div><p>Note</p><p>To create AprilTags use the tag generator tool built-in to OpenMV IDE. The tag generator can create printable 8.5”x11” AprilTags.</p></div><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the <code>roi</code> are operated on.</p><p><code>families</code> is bitmask of tag families to decode. It is the logical OR of:</p><div><ul><li><code>image.TAG16H5</code></li><li><code>image.TAG25H7</code></li><li><code>image.TAG25H9</code></li><li><code>image.TAG36H10</code></li><li><code>image.TAG36H11</code></li><li><code>image.ARTOOLKIT</code></li></ul></div><p>By default it is just <code>image.TAG36H11</code> which is the best tag family to use. Note that <code>Image.find_apriltags()</code> slows down per enabled tag family.</p><p><code>fx</code> is the camera X focal length in pixels. For the standard OpenMV Cam this is (2.8 / 3.984) * 656. Which is the lens focal length in mm, divided by the camera sensor length in the X direction multiplied by the number of camera sensor pixels in the X direction (for the OV7725 camera).</p><p><code>fx</code> is the camera Y focal length in pixels. For the standard OpenMV Cam this is (2.8 / 2.952) * 488. Which is the lens focal length in mm, divided by the camera sensor length in the Y direction multiplied by the number of camera sensor pixels in the Y direction (for the OV7725 camera).</p><p><code>cx</code> is the image center which is just <code>image.width()/2</code>. This is not <code>roi.w()/2</code>.</p><p><code>cy</code> is the image center which is just <code>image.height()/2</code>. This is not <code>roi.h()/2</code>.</p><p>Not supported on compressed images.</p><p>This method is not available on the OpenMV Cam M4.</p>
		"""
		pass
	def find_datamatrices(self, roi:Tuple[int,int,int,int]|None=None, effort=200) -> List[datamatrix]:
		"""
		<h3>image - Image.find_datamatrices(roi: Tuple[int, int, int, int] | None = None, effort=200)</h3><p>Finds all datamatrices within the <code>roi</code> and returns a list of <code>image.datamatrix</code> objects. Please see the <code>image.datamatrix</code> object for more information.</p><p>Data Matrices need to be relatively flat in the image for this method to work. You can achieve a flatter image that is not effected by lens distortion by either using the <code>sensor.set_windowing()</code> function to zoom in the on the center of the lens, <code>Image.lens_corr()</code> to undo lens barrel distortion, or by just changing out the lens for something with a narrower fields of view. There are machine vision lenses available which do not cause barrel distortion but they are much more expensive to than the standard lenses supplied by OpenMV.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the <code>roi</code> are operated on.</p><p><code>effort</code> controls how much time to spend trying to find data matrix matches. The default value of 200 should be good for all use-cases. However, you may increase the effort, at a cost of the frame rate, to increase detection. You may also lower the effort to increase the frame rate, but, at a cost of detections… note that when <code>effort</code> is set to below 160 or so you will not detect anything anymore. Also note that you can make <code>effort</code> as high as you like. But, any values above 240 or so do not result in much increase in the detection rate.</p><p>This method is not available on the OpenMV Cam M4.</p>
		"""
		pass
	def find_barcodes(self, roi:Tuple[int,int,int,int]|None=None) -> List[barcode]:
		"""
		<h3>image - Image.find_barcodes(roi: Tuple[int, int, int, int] | None = None)</h3><p>Finds all 1D barcodes within the <code>roi</code> and returns a list of <code>image.barcode</code> objects. Please see the <code>image.barcode</code> object for more information.</p><p>For best results use a 640 by 40/80/160 window. The lower the vertical res the faster everything will run. Since bar codes are linear 1D images you just need a lot of resolution in one direction and just a little resolution in the other direction. Note that this function scans both horizontally and vertically so you can use a 40/80/160 by 480 window if you want. Finally, make sure to adjust your lens so that the bar code is positioned where the focal length produces the sharpest image. Blurry bar codes can’t be decoded.</p><p>This function supports all these 1D barcodes (basically all barcodes):</p><div><ul><li><code>image.EAN2</code></li><li><code>image.EAN5</code></li><li><code>image.EAN8</code></li><li><code>image.UPCE</code></li><li><code>image.ISBN10</code></li><li><code>image.UPCA</code></li><li><code>image.EAN13</code></li><li><code>image.ISBN13</code></li><li><code>image.I25</code></li><li><code>image.DATABAR</code> (RSS-14)</li><li><code>image.DATABAR_EXP</code> (RSS-Expanded)</li><li><code>image.CODABAR</code></li><li><code>image.CODE39</code></li><li><code>image.PDF417</code></li><li><code>image.CODE93</code></li><li><code>image.CODE128</code></li></ul></div><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the <code>roi</code> are operated on.</p><p>This method is not available on the OpenMV Cam M4.</p>
		"""
		pass
	def find_displacement(self, template:Image, roi:Tuple[int,int,int,int]|None=None, template_roi:Tuple[int,int,int,int]|None=None, logpolar=False) -> List[displacement]:
		"""
		<h3>image - Image.find_displacement(template: Image, roi: Tuple[int, int, int, int] | None = None, template_roi: Tuple[int, int, int, int] | None = None, logpolar=False)</h3><p>Find the translation offset of the this image from the template. This method can be used to do optical flow. This method returns a <code>image.displacement</code> object with the results of the displacement calculation using phase correlation.</p><p><code>roi</code> is the region-of-interest rectangle (x, y, w, h) to work in. If not specified, it is equal to the image rectangle.</p><p><code>template_roi</code> is the region-of-interest rectangle (x, y, w, h) to work in. If not specified, it is equal to the image rectangle.</p><p><code>roi</code> and <code>template</code> roi must have the same w/h but may have any x/y location in the image. You may slide smaller rois arround a larger image to get an optical flow gradient image…</p><p><code>Image.find_displacement()</code> normally computes the x/y translation between two images. However, if you pass <code>logpolar=True</code> it will instead find rotation and scale changes between the two images. The same <code>image.displacement</code> object result encodes both possible repsonses.</p><p>Not supported on compressed images or bayer images.</p><div><p>Note</p><p>Please use this method on power-of-2 image sizes (e.g. <code>sensor.B64X64</code>).</p></div><p>Not supported on compressed images or bayer images.</p><p>This method is not available on the OpenMV Cam M4.</p>
		"""
		pass
	def find_template(self, template:Image, threshold:float, roi:Tuple[int,int,int,int]|None=None, step=2, search=SEARCH_EX) -> Tuple[int,int,int,int]:
		"""
		<h3>image - Image.find_template(template: Image, threshold: float, roi: Tuple[int, int, int, int] | None = None, step=2, search=SEARCH_EX)</h3><p>Tries to find the first location in the image where template matches using Normalized Cross Correlation. Returns a bounding box tuple (x, y, w, h) for the matching location otherwise None.</p><p><code>template</code> is a small image object that is matched against this image object. Note that both images must be grayscale.</p><p><code>threshold</code> is floating point number (0.0-1.0) where a higher threshold prevents false positives while lowering the detection rate while a lower threshold does the opposite.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the <code>roi</code> are operated on.</p><p><code>step</code> is the number of pixels to skip past while looking for the template. Skipping pixels considerably speeds the algorithm up. This only affects the algorithm in SERACH_EX mode.</p><p><code>search</code> can be either <code>image.SEARCH_DS</code> or <code>image.SEARCH_EX</code>. <code>image.SEARCH_DS</code> searches for the template using as faster algorithm than <code>image.SEARCH_EX</code> but may not find the template if it’s near the edges of the image. <code>image.SEARCH_EX</code> does an exhaustive search for the image but can be much slower than <code>image.SEARCH_DS</code>.</p><p>Only works on grayscale images.</p>
		"""
		pass
	def find_features(self, cascade, threshold=0.5, scale=1.5, roi:Tuple[int,int,int,int]|None=None) -> List[Tuple[int,int,int,int]]:
		"""
		<h3>image - Image.find_features(cascade, threshold=0.5, scale=1.5, roi: Tuple[int, int, int, int] | None = None)</h3><p>This method searches the image for all areas that match the passed in Haar Cascade and returns a list of bounding box rectangles tuples (x, y, w, h) around those features. Returns an empty list if no features are found.</p><p><code>cascade</code> is a Haar Cascade object. See <code>image.HaarCascade()</code> for more details.</p><p><code>threshold</code> is a threshold (0.0-1.0) where a smaller value increase the detection rate while raising the false positive rate. Conversely, a higher value decreases the detection rate while lowering the false positive rate.</p><p><code>scale</code> is a float that must be greater than 1.0. A higher scale factor will run faster but will have much poorer image matches. A good value is between 1.35 and 1.5.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the <code>roi</code> are operated on.</p>
		"""
		pass
	def find_eye(self, roi:Tuple[int,int,int,int]) -> Tuple[int,int]:
		"""
		<h3>image - Image.find_eye(roi: Tuple[int, int, int, int])</h3><p>Searches for the pupil in a region-of-interest (x, y, w, h) tuple around an eye. Returns a tuple with the (x, y) location of the pupil in the image. Returns (0,0) if no pupils are found.</p><p>To use this function first use <code>Image.find_features()</code> with the <code>frontalface</code> HaarCascade to find someone’s face. Then use <code>Image.find_features()</code> with the <code>eye</code> HaarCascade to find the eyes on the face. Finally, call this method on the eye ROI returned by <code>Image.find_features()</code> to get the pupil coordinates.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the <code>roi</code> are operated on.</p><p>Only works on grayscale images.</p>
		"""
		pass
	def find_lbp(self, roi:Tuple[int,int,int,int]):
		"""
		<h3>image - Image.find_lbp(roi: Tuple[int, int, int, int])</h3><p>Extracts LBP (local-binary-patterns) keypoints from the region-of-interest (x, y, w, h) tuple. You can then use then use the <code>image.match_descriptor()</code> function to compare two sets of keypoints to get the matching distance.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the <code>roi</code> are operated on.</p><p>Only works on grayscale images.</p>
		"""
		pass
	def find_keypoints(self, roi:Tuple[int,int,int,int]|None=None, threshold=20, normalized=False, scale_factor=1.5, max_keypoints=100, corner_detector=CORNER_AGAST):
		"""
		<h3>image - Image.find_keypoints(roi: Tuple[int, int, int, int] | None = None, threshold=20, normalized=False, scale_factor=1.5, max_keypoints=100, corner_detector=CORNER_AGAST)</h3><p>Extracts ORB keypoints from the region-of-interest (x, y, w, h) tuple. You can then use then use the <code>image.match_descriptor()</code> function to compare two sets of keypoints to get the matching areas. Returns None if no keypoints were found.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the <code>roi</code> are operated on.</p><p><code>threshold</code> is a number (between 0 - 255) which controls the number of extracted corners. For the default AGAST corner detector this should be around 20. FOr the FAST corner detector this should be around 60-80. The lower the threshold the more extracted corners you get.</p><p><code>normalized</code> is a boolean value that if True turns off extracting keypoints at multiple resolutions. Set this to true if you don’t care about dealing with scaling issues and want the algorithm to run faster.</p><p><code>scale_factor</code> is a float that must be greater than 1.0. A higher scale factor will run faster but will have much poorer image matches. A good value is between 1.35 and 1.5.</p><p><code>max_keypoints</code> is the maximum number of keypoints a keypoint object may hold. If keypoint objects are too big and causing out of RAM issues then decrease this value.</p><p><code>corner_detector</code> is the corner detector algorithm to use which extracts keypoints from the image. It can be either <code>image.CORNER_FAST</code> or <code>image.CORNER_AGAST</code>. The FAST corner detector is faster but much less accurate.</p><p>Only works on grayscale images.</p>
		"""
		pass
	def find_edges(self, edge_type, threshold=(100,200)):
		"""
		<h3>image - Image.find_edges(edge_type, threshold=(100, 200))</h3><p>Turns the image to black and white leaving only the edges as white pixels.</p><div><ul><li>image.EDGE_SIMPLE - Simple thresholded high pass filter algorithm.</li><li>image.EDGE_CANNY - Canny edge detection algorithm.</li></ul></div><p><code>threshold</code> is a two valued tuple containing a low threshold and high threshold. You can control the quality of edges by adjusting these values. It defaults to (100, 200).</p><p>Only works on grayscale images.</p>
		"""
		pass
	def find_hog(self, roi:Tuple[int,int,int,int]|None=None, size=8):
		"""
		<h3>image - Image.find_hog(roi: Tuple[int, int, int, int] | None = None, size=8)</h3><p>Replaces the pixels in the ROI with HOG (histogram of orientated graidients) lines.</p><p><code>roi</code> is the region-of-interest rectangle tuple (x, y, w, h). If not specified, it is equal to the image rectangle. Only pixels within the <code>roi</code> are operated on.</p><p>Only works on grayscale images.</p><p>This method is not available on the OpenMV Cam M4.</p>
		"""
		pass
	def stero_disparity(self, reversed:bool=False, max_disparity:int=64, threshold:int=64):
		"""
		<h3>image - Image.stero_disparity(reversed: bool = False, max_disparity: int = 64, threshold: int = 64)</h3><p>Takes a double wide grayscale image that contains the output of two camera sensors side-by-side and replaces one of the images in the double wide image with the stero-disparity image where each pixel reprsents depth. E.g. if you have two 320x240 cameras then this method takes a 640x240 image.</p><p><code>reversed</code> By default the left image is compared to the right image and the right image is then replaced. Pass true to compare the right image to the left image and replace the left image.</p><div><p>Note</p><p>The algorithm only works comparing left-&gt;right or right-&gt;left. If your camrea setup does not match this then you will get useless results.</p></div><p><code>max_disparity</code> is the maximum distance to search for a matching pixel block using the sum-of-absolute differences algorith. Larger values take exponentially longer to search with but result in higher quality images. Lower values make the algorithm run faster but may result in nonsense output.</p><p><code>threshold</code> if the sum-of-absolute differences between two blocks is less than or equal to this threshold they are considered to be matching.</p><p>This method is only available on the Arduino Portenta.</p><div><p>Note</p><p>Even with our best SIMD effort this algorithm is not real-time on the Cortex-M7 processor. This is just a toy example algorithm showing off stero-disparity.</p></div>
		"""
		pass

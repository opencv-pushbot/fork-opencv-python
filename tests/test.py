import unittest
import os

class OpenCVTest(unittest.TestCase):
    """ Simple functionality tests. """

    def test_import(self):
        """ Test that the cv2 module can be imported. """
        import cv2

    def test_video_capture(self):

        if os.name != 'posix':
            import cv2

            cap = cv2.VideoCapture("SampleVideo_1280x720_1mb.mp4")
            self.assertTrue(cap.isOpened())
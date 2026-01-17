from Products.Five import BrowserView
from zope.interface import implementer
from zope.publisher.interfaces import IPublishTraverse


@implementer(IPublishTraverse)
class ItemTraverser(BrowserView):

    default_size = 6  # Default size for SVG rendering
    default_stroke_width = 1  # Default stroke width for SVG rendering

    _size = None
    _stroke_width = None

    def publishTraverse(self, request, name):
        """Get name from URL traversing.

        Example: http://localhost:8080/Plone/@@svg/6
        """
        if not self._size:
            self._size = str(name)
        else:
            self._stroke_width = str(name)
        return self

    def __getitem__(self, name):
        """Get name from unrestrictedTraverse.

        Example: <tal:el replace="structure context/@@item/named-adapter-name" />
        """

        if not self._size:
            self._size = str(name)
        else:
            self._stroke_width = str(name)
        return self

    @property
    def size(self):
        return self._size or self.default_size

    @property
    def stroke_width(self):
        return self._stroke_width or self.default_stroke_width

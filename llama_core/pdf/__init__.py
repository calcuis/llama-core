
from ._crypt_providers import crypt_provider
from ._encryption import PasswordType
from ._merger import PdfMerger
from ._page import PageObject, Transformation, mult
from ._reader import DocumentInformation, PdfReader
from ._version import __version__
from ._writer import ObjectDeletionFlag, PdfWriter
from .constants import ImageType
from .pagerange import PageRange, parse_filename_page_ranges
from .papersizes import PaperSize

try:
    import PIL

    pil_version = PIL.__version__
except ImportError:
    pil_version = "none"

_debug_versions = (
    f"pypdf=={__version__}, crypt_provider={crypt_provider}, PIL={pil_version}"
)

__all__ = [
    "__version__",
    "_debug_versions",
    "ImageType",
    "mult",
    "PageRange",
    "PaperSize",
    "DocumentInformation",
    "ObjectDeletionFlag",
    "parse_filename_page_ranges",
    "PdfMerger",
    "PdfReader",
    "PdfWriter",
    "Transformation",
    "PageObject",
    "PasswordType",
]

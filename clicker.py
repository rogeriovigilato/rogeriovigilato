import argparse
import os
import time

# Default directory containing the five template images
DEFAULT_FOLDER = r"C:/xls/notas"

import pyautogui


def wait_and_click(image, timeout, interval):
    """Wait up to ``timeout`` seconds for ``image`` to appear and click it."""
    end_time = time.time() + timeout
    while time.time() < end_time:
        location = pyautogui.locateCenterOnScreen(image, confidence=0.8)
        if location:
            pyautogui.click(location)
            return True
        time.sleep(interval)
    return False


def find_and_click(images, interval, loops, timeout):
    if loops == 0:
        loops = float("inf")
    while loops:
        for image in images:
            wait_and_click(image, timeout, interval)
        if loops != float("inf"):
            loops -= 1


def gather_images(folder):
    """Return the first five images in *folder* sorted by name."""
    supported = {".png", ".jpg", ".jpeg", ".bmp", ".gif"}
    images = [
        os.path.join(folder, f)
        for f in sorted(os.listdir(folder))
        if os.path.splitext(f)[1].lower() in supported
    ]
    if len(images) < 5:
        raise FileNotFoundError("Folder must contain at least 5 images")
    return images[:5]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Click images found on screen using templates from a folder",
    )
    parser.add_argument(
        "--folder",
        default=DEFAULT_FOLDER,
        help=f"Folder containing template images (default: {DEFAULT_FOLDER})",
    )
    parser.add_argument("--interval", type=float, default=0.5,
                        help="Seconds to wait between clicks")
    parser.add_argument(
        "--loops",
        type=int,
        default=1,
        help="Number of times to loop over images (0 for infinite)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=5,
        help="Seconds to wait for each image to appear",
    )

    args = parser.parse_args()
    images = gather_images(args.folder)
    if not images:
        parser.error(f"No image files found in {args.folder}")
    find_and_click(images, args.interval, args.loops, args.timeout)

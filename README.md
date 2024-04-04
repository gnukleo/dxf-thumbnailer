# dxf-thumbnailer
Show thumbnails in GNU/Linux, dont work with Dolphin

# installation
1. clone this repository and go to the folder
    ```
   git clone https://github.com/gnukleo/dxf-thumbnailer.git
    ```
    ```
   cd dxf-thumbnailer
   ```
# automatic installation
2. set executable installer file
   ```
   chmod +x dxf_thumbnailer_installer.sh
   ```
3. execute intaller with:
   ```
   ./dxf_thumbnailer_installer.sh
   ```
4. done!

# manual installation
2. create directory for thumbnailers if not exist and copy the thumbnailer entry
   ```
   mkdir -p $HOME/.local/share/thumbnailers
   ```
   ```
   cp dxf_thumbnailer_installer
   ```
3. create virtualenv for python dependencies, whit sudo in that folder
   ```
   sudo python3 -m venv /usr/local/share/.dxf_thumbnailer_python_venv
   ```
4. and install all dependencies in the virtualenv
   ```
   sudo /usr/local/share/.dxf_thumbnailer_python_venv/bin/pip install ezdxf PyMuPdf pillow
   ```
5. copy the script for extract and create a thumbnail, and set executable
   ```
   sudo cp dxf-thumbnailer.py /usr/local/bin/
   ```
   ```
   sudo chmod +x /usr/local/bin/dxf-thumbnailer.py
   ```
6. now close all instances for nautilus
   ```
   nautilus -q
   ```
7. remove all the thumbnails from the cache, this so that they are all refreshed and we do not have errors from failed images
   ```
   rm -r $HOME/.cache/thumbnails
   ```
8. done, now open nautilus and navigate to any folder that has dxf files saved
